---
title: Math Analysis Homework - Sem 2 Week 11
tags:
  - math
  - homework
  - math-analysis
status: published
top: 0
date: '2026-05-27T04:45:50.476Z'
---

# Math Analysis Homework - Sem 2 Week 11

## Class 1

### T1

<div class="cbox">

**7.** 求曲线 $\left(\frac{x^2}{a^2} + \frac{y^2}{b^2}\right)^2 = \frac{x^2}{a^2} - \frac{y^2}{b^2}$ 所围区域的面积.

</div>

<div class='pbox'>

$x=ra\cos \theta,y=rb\sin \theta$,则曲线变为$r^2=(\cos^2\theta-\sin^2\theta)=\cos 2\theta$.设$D'=\{ (r,\theta)|r\le \sqrt{\cos 2\theta} \}$.

$$
\begin{gathered}
\iint_D 1dxdy \\
=\iint_{D'} rab drd\theta \\
=4ab\int_0^{\frac\pi 4} \int_0^{\sqrt{\cos 2\theta}} rdrd\theta \\
=4ab\int_0^{\frac\pi 4}\dfrac{\cos2\theta}{2}d\theta  \\
=ab
\end{gathered}
$$


</div>

### T2

<div class="cbox">

**8.** 计算圆柱面 $x^2 + y^2 = R^2$ 与 $x^2 + z^2 = R^2$ 所围立体的体积.

</div>

<div class='pbox'>

$$
\begin{gathered}
V=\iint_{\{ (y,z)|y<R,z<R \} } 2\sqrt{R^2-\max(y^2,z^2)}dydz \\
=16\int_0^R\int_{0}^{y} \sqrt{ R^2-y^2 } dzdy \\
=16\int_0^R y\sqrt{R^2-y^2}dy \\
=\dfrac{16}{3} R^3
\end{gathered}
$$

</div>

### T3

<div class="cbox">

**9.** 计算积分 $I = \iint_D |x| \mathrm{d}x\mathrm{d}y$, 其中 $D$ 为 $2x^2 - 2xy + y^2 \le 1$.

</div>

<div class='pbox'>

$$
\begin{gathered}
\iint_D |x|dxdy \\
=\iint_{\{ (x,t)|x^2+t^2\le 1 \} } |x| dxdt \\
=2\int _0^1 \int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}}xdtdx \\
=4\int_0^1 x\sqrt{1-x^2} dx \\
=\dfrac{4}{3} 
\end{gathered}
$$

</div>

### T4

<div class="cbox">

**10.** 设 $D = \{(x,y) \mid x^2 + y^2 \le 1\}$, 证明: $\frac{61\pi}{165} \le \iint_D \sin \sqrt{(x^2 + y^2)^3} \mathrm{d}x\mathrm{d}y \le \frac{2\pi}{5}$.

</div>

<div class='pbox'>

$$
\begin{gathered}
I=\iint_D \sin\sqrt{(x^2+y^2)^3}dxdy \\
=\int_0^{2\pi}\int_0^1 r\sin r^{3}drd\theta \\
=2\pi \int_0^1 r\sin r^3dr \\
\le 2\pi\int_0^1 r^4dr \\
=\dfrac{2\pi}{5}  \\
I=2\pi \int_0^1 r\sin r^3dr \\
\ge 2\pi \int_0^1 r (r^3-\dfrac{r^9}{6} ) \\
=\dfrac{61\pi}{165} 
\end{gathered}
$$

</div>

### T5

<div class="cbox">

**11.** 求 $\lim_{R \to +\infty} \iint\limits_{|x| \le R, |y| \le R} (x^2 + y^2) e^{-(x^2 + y^2)} \mathrm{d}x\mathrm{d}y$.

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } G(t)=\iint\limits_{|x| \le R, |y| \le R} (x^2 + y^2) e^{-(x^2 + y^2)} \mathrm{d}x\mathrm{d}y, \\
F(t)=\iint\limits_{\{ (x,y)|x^2+y^2<t^2 \} } (x^2 + y^2) e^{-(x^2 + y^2)} \mathrm{d}x\mathrm{d}y \\
=8\int_0^\frac\pi4 \int_0^t r^3e^{-r^2}drd\theta \\
=\pi (1-(t^2+1)e^{-t^2})
\end{gathered}
$$

因为$G(t)\in (F(t),F(\sqrt 2t))$,故由夹逼定理:

$$
\begin{gathered}
\lim_{R \to +\infty} G(R)\in [\lim_{R\to +\infty} F(t),\lim_{R\to +\infty} F(\sqrt 2t)]  \\
\implies \lim_{R \to +\infty} G(R)=\pi
\end{gathered}
$$

</div>

### T6

<div class="cbox">

**12.** 设 $f(t)$ 在区间 $[1, 2]$ 上可积, $D$ 是由曲线 $xy=1, xy=2$ 和直线 $y=x, y=4x$ 所围成的区域在第一象限中的部分, 证明: 
$$\iint_D f(\sqrt{xy}) \mathrm{d}x\mathrm{d}y = \ln 2 \cdot \int_1^2 f(\sqrt{t}) \mathrm{d}t.$$

</div>

<div class='pbox'>

设$t=xy,s=\dfrac yx$,则雅可比矩阵行列式为:

$$
\begin{gathered}
\left|\dfrac{1}{2\sqrt{st}} \det\begin{bmatrix} 1&-\dfrac{t}{s} \\s&t
\end{bmatrix} \right| \\
=\dfrac{1}{2s} 
\end{gathered}
$$

于是

$$
\begin{gathered}
\iint_D f(\sqrt{xy}) \mathrm{d}x\mathrm{d}y  \\
=\int_1^4 \int_1^2 f(\sqrt t) \dfrac{1}{2s} dtds \\
=(\int_1^4 \dfrac{1}{2s}ds )(\int_1^1 f(\sqrt t)dt) \\
=\ln 2\int_1^2 f(\sqrt {t})dt
\end{gathered}
$$

</div>

## Class 2

### T1

<div class="cbox">

2. 计算三重积分 $I = \iiint_{\Omega} (x+y)^2 \mathrm{d}V$, 其中 $\Omega$ 是由曲线 $\begin{cases} y^2 = 2z, \\ x = 0 \end{cases}$ 绕 $z$ 轴旋转得到的曲面与平面 $z = 2, z = 8$ 所围成的区域.

</div>

<div class="pbox">

$$
\begin{gathered}
I=\int_2^8 \iint_{\{ (x,y)|(x^2+y^2\le 2z) \} } (x+y)^2dxdydz \\
=\int_2^8 \int_0^{2\pi} \int_0^{\sqrt{2z}}(r\cos\theta+r\sin\theta)^2rdrd\theta dz \\
=\int_2^8 \int_0^{2\pi} 2\sin^2(\theta+\dfrac\pi4) z^2d\theta dz \\
=\int_2^8 2\pi z^2 dz \\
=336\pi
\end{gathered}
$$

</div>

### T2

<div class="cbox">

3. 计算三重积分 $\iiint_{\Omega} z^2 \mathrm{d}x\mathrm{d}y\mathrm{d}z$, 其中 $\Omega$ 为:

(1) 两个球 $x^2 + y^2 + z^2 \leqslant R^2, x^2 + y^2 + z^2 \leqslant 2Rz$ 的公共部分;

(2) 锥面 $z^2 = \frac{h^2}{R^2}(x^2 + y^2)$ 与平面 $z = h$ 所围成的区域.

</div>

<div class="pbox">

(1):

为$B((0,0,0),R)\cap B((0,0,R),R)$.

$$
\begin{gathered}
I=\int_0^{\frac R2} z^2 \pi(R^2-(R-z)^2)dz \\
+\int_{\frac R2}^R z^2 \pi(R^2-z^2)dz \\
=\dfrac{\pi}{40} R^5+\dfrac{47\pi}{480} R^5 \\
=\dfrac{59\pi}{480} R^5
\end{gathered}
$$

(2):

$$
\begin{gathered}
\int_0^h z^2 \pi(\dfrac{z^2R^2}{h^2} ) dz \\
=\dfrac{\pi}{5} h^3R^2
\end{gathered}
$$

</div>
