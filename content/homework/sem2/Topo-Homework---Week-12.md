---
title: Topo Homework - Week 12
tags:
  - math
  - homework
  - topo
status: published
top: 0
date: '2026-05-25T00:10:56.482Z'
---

# Topo Homework - Week 12

### T1

<div class="cbox">

**2.** (E) 设 $X$ 是一个拓扑空间, $S$ 是一个离散拓扑空间, $p: X \times S \to X, \forall (x,s) \in X \times S, p(x,s) = x$. 证明 $p$ 是一个覆盖映射.

</div>

<div class="pbox">

$$
\begin{gathered}
\forall x\in X,U \text{ is a neighborhood of } x,p^{-1}(U)=\bigsqcup_{s\in S} U\times \{s\}, \\
p \text{ is homeomorphism of } p^{-1}(U) \text{ and } U\times \{ s \}  \\
\implies p \text{ is a covering map} 
\end{gathered}
$$

</div>

### T2

<div class="cbox">

**3.** 证明下列映射是覆盖映射:
- (1) (ER) $f: \mathbb{R}^2 \to S^1 \times \mathbb{R}, (x,y) \mapsto (e^{2\pi i x}, y)$;
- (2) (M) $f: \mathbb{C} \to \mathbb{C} - \{0\}, z \mapsto e^z$;
- (3) (E) $f: \mathbb{R}^2 \to S^1 \times S^1, (x,y) \mapsto (e^{2\pi i x}, e^{2\pi i y})$.

</div>

<div class="pbox">

(1):对任意$(e^{2\pi ix},y)$的邻域$U=\{ (e^{2\pi ix'},y')| \max |x'-x|,|y'-y|<\dfrac15 \} $有$f^{-1}(U)=\bigsqcup_{k\in {\mathbb Z}} (x-\dfrac15+k,x+\dfrac15+k)\times (y-\dfrac15,y+\dfrac15)$.且容易验证限定到一个切片是同胚.

(2):对任意$x\in {\mathbb C}- \{ 0 \},f^{-1}(U)=\bigsqcup_{k\in {\mathbb Z}}\ln(U)+2k\pi i$.其中$U$为任意小邻域,$A+x=\{ a+x|a\in A \}$,$\ln$表示幅角主值.容易验证是同胚.

(3):因为$p:R^1\to S^1,x\mapsto e^{2\pi ix}$是覆盖映射,所以任取$p\times p:=(x,y)\mapsto (px,py)$是覆叠映射:$px,py$分别有小邻域$U,V$满足$p^{-1}(U),p^{-1}(V)$是若干不交且同胚于$U$的切片,则$p^{-1}(U\times V)=p^{-1}(U)\times p^{-1}(V)$是若干不交且同胚于$U\times V$的切片.

</div>

### T3

<div class="cbox">

**5.** (ER) 给出 $S^1 \times \mathbb{R}$ 到默比乌斯带的覆盖映射.

</div>

<div class="pbox">

$$
\begin{gathered}
f:S^1\times {\mathbb R}\to M \\
f(e^{2\pi i x},y)\to \begin{cases}
[(2x,\dfrac{2}{1+e^{-y}}-1)]  & x\in [0,\dfrac12) \\
[(2x-1,2-\dfrac{2}{1+e^{-y}} )] & x\in [\dfrac12,1)
\end{cases}

\end{gathered}
$$

</div>

### T4

<div class="cbox">

**6.** (ER) 给出默比乌斯到自身的一个非平凡的覆盖映射.

</div>

<div class="pbox">

莫比乌斯带定义为$I\times I/\sim$,其中$x\sim y \iff \exists t \ s.t.\ \{ x,y \} =\{ (0,t),(1,1-t) \}$,$[x]$表示原$x\in I\times I$商映射后的等价类.

则

$$
\begin{gathered}
p:I\times I/\sim\to I\times I/\sim , \\
[(x,y)]\mapsto \begin{cases}
[(3x,y)] & x\in [0,\dfrac13) \\
[((3x-1,1-y))]& x\in [\dfrac13,\dfrac23) \\
[(3x-2,y)]& x\in [\dfrac23,1)
\end{cases}
\end{gathered}
$$

容易验证这是一个3-sheet覆盖.

</div>

### T5

<div class="cbox">

**7.** (MRH) 证明环面是克莱因瓶上的覆盖空间.

</div>

<div class="pbox">

设${\mathbb T}^2=I\times I/\sim,{\mathbb K}^2=I\times I/\sim'$.

其中:

$$
\begin{gathered}
(x,y)\sim (a,b) \iff |x-a|=1\land b=y \lor |y-b|=1\land x=a \\
(x,y)\sim' (a,b) \iff |x-a|=1\land b+y=1 \lor |y-b|=1\land x=a
\end{gathered}
$$

则

$$
\begin{gathered}
p:I\times I/\sim\to I\times I/\sim', \\
[(x,y)]\mapsto \begin{cases}
[2x,y] &x\in [0,\dfrac12)\\
[2x-1,1-y] &x\in [\dfrac12,1)
\end{cases}
\end{gathered}
$$

容易验证是覆盖映射.

</div>

### T6

<div class="cbox">

**10.** (MRH) 设 $p : E \to B$ 为覆盖映射, 证明 $p$ 是开映射和商映射.

</div>

<div class="pbox">

设$U\subset E$为开集,考虑任意$x\in U,p(x)\in p(U)$,存在$p(x)$的邻域$N_x$满足$p^{-1}(N_x)=\bigsqcup_\lambda V_\lambda,x\in V_{\lambda_0},p|_{V_{\lambda_0}}=V_{\lambda_0}\cong U$.因为同胚,所以$p|_{V_{\lambda_0}}$是开映射,从而$p|_{V_{\lambda_0}}(V_{\lambda_0}\cap U)\subset f(U)$中的开集,从而$f(U)$是开集.

因为$p$是连续映射且满映射所以是商映射.

</div>

### T7

<div class="cbox">

**15.** (ER) 画出图形 $\infty$ (两个圆周的一点并) 的两个不同胚的 3 重覆盖.

</div>

<div class="pbox">

![pasted-image-1](@media/f1c33c3a779d8df3486f590aba009ca3d7d6c0b7bd56519d22a06f9ccf6dbc1b.png)

</div>

### T8

<div class="cbox">

**16.** (DRH) 证明对于每个正整数 $n$, 都存在一个从 $nT^2$ 到 $(n+1)\mathbb{P}^2$ 的 2 重覆盖.

</div>

<div class="pbox">

考虑$(n+1) {\mathbb P}^2$的基本群是$\langle a_1,\ldots a_{n+1}|\prod_i a_i^2=1 \rangle$.

那么构造一个映射把$\varphi:\pi_1((n+1){\mathbb P}^2)\to {\mathbb Z}/2 {\mathbb Z},\prod a_{p_i}^{c_i}\mapsto \prod_i (-1)^{c_i}$,容易验证其是满同态.从而其核作为子群会对应一个覆叠空间的基本群.又因为$\pi_1((n+1){\mathbb P}^2)/\ker \varphi\cong \operatorname{im} \varphi$所以这个覆叠空间是2-sheet.

注意到每个生成元都是改变定向的回路.所以走偶数个恰好是不改变定向的.则你这个子群里所有回路都是保持定向的,是个可定向空间.同时结合欧拉示性数是二倍$\chi=2(1-n)=2-2n$知道是$n {\mathbb T}^2$

</div>
