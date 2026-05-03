from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date as date_type
from pathlib import Path


DATE_PREFIX_RE = re.compile(r"^(?P<yy>\d{2})(?P<mm>\d{2})(?P<dd>\d{2})-")
FRONTMATTER_RE = re.compile(r"\A---\r?\n(?P<body>.*?)(?P<closing>\r?\n---(?:\r?\n|$))", re.DOTALL)
DATE_LINE_RE = re.compile(r"(?m)^(?P<indent>[ \t]*)date:[^\r\n]*(?P<newline>\r?\n|$)")


@dataclass
class ProcessResult:
    path: Path
    status: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Restore frontmatter dates from YYMMDD filename prefixes under content/_posts."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("content") / "_posts",
        help="Root directory to scan. Defaults to content/_posts.",
    )
    parser.add_argument(
        "--time",
        default="12:00:00",
        help="Time portion to use for restored dates. Defaults to 12:00:00.",
    )
    parser.add_argument(
        "--tz",
        default="+08:00",
        help="Timezone suffix appended to restored dates. Defaults to +08:00.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write changes to disk. Without this flag, the script only prints planned changes.",
    )
    return parser.parse_args()


def build_restored_value(filename: str, time_part: str, tz_suffix: str) -> str | None:
    match = DATE_PREFIX_RE.match(filename)
    if not match:
        return None

    year = 2000 + int(match.group("yy"))
    month = int(match.group("mm"))
    day = int(match.group("dd"))

    try:
        parsed = date_type(year, month, day)
    except ValueError:
        return None

    return f"{parsed.isoformat()}T{time_part}{tz_suffix}"


def split_text_and_encoding(raw: bytes) -> tuple[str, str]:
    has_bom = raw.startswith(b"\xef\xbb\xbf")
    encoding = "utf-8-sig" if has_bom else "utf-8"
    return raw.decode(encoding), encoding


def update_frontmatter(text: str, restored_value: str) -> tuple[str | None, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, "no-frontmatter"

    body = match.group("body")
    closing = match.group("closing")
    restored_line = f"date: '{restored_value}'"

    if DATE_LINE_RE.search(body):
        updated_body = DATE_LINE_RE.sub(lambda m: f"{m.group('indent')}{restored_line}{m.group('newline')}", body, count=1)
        action = "replace-date"
    else:
        newline = "\r\n" if "\r\n" in match.group(0) else "\n"
        updated_body = f"{body}{newline}{restored_line}"
        action = "add-date"

    updated_text = f"---{match.group(0)[3:match.start('body')]}{updated_body}{closing}{text[match.end():]}"
    return updated_text, action


def process_file(path: Path, time_part: str, tz_suffix: str, write: bool) -> ProcessResult:
    restored_value = build_restored_value(path.name, time_part, tz_suffix)
    if restored_value is None:
        return ProcessResult(path, "skipped", "no-date-prefix")

    raw = path.read_bytes()
    text, encoding = split_text_and_encoding(raw)
    updated_text, action = update_frontmatter(text, restored_value)

    if updated_text is None:
        return ProcessResult(path, "skipped", action)

    if updated_text == text:
        return ProcessResult(path, "unchanged", restored_value)

    if write:
        path.write_bytes(updated_text.encode(encoding))

    return ProcessResult(path, "updated" if write else "would-update", f"{action} -> {restored_value}")


def main() -> int:
    args = parse_args()
    root = args.root.resolve()

    if not root.exists():
        print(f"Root directory does not exist: {root}", file=sys.stderr)
        return 1

    results: list[ProcessResult] = []
    for path in sorted(root.rglob("*")):
        if path.is_file():
            results.append(process_file(path, args.time, args.tz, args.write))

    changed_statuses = {"updated", "would-update"}
    changed = [result for result in results if result.status in changed_statuses]
    skipped = [result for result in results if result.status == "skipped"]
    unchanged = [result for result in results if result.status == "unchanged"]

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"[{mode}] scanned {len(results)} files under {root}")
    print(f"[{mode}] {len(changed)} files {'updated' if args.write else 'would be updated'}")
    print(f"[{mode}] {len(unchanged)} files already matched the restored date")
    print(f"[{mode}] {len(skipped)} files skipped")

    for result in changed:
        rel_path = result.path.relative_to(root.parent)
        print(f"{result.status}: {rel_path} ({result.detail})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
