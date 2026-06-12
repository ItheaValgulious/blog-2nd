---
password: fuck
title: Math Analysis Homework - Sem 2 Week 13
tags:
  - homework
  - math-analysis
  - math
status: published
top: 0
date: '2026-06-08T13:36:01.578Z'
---

# Math Analysis Homework - Sem 2 Week 13

## Class 1

### T1

<div class="cbox">

**3.** 计算曲面积分
$$\iint_{\Sigma} (x^2+y^2) \mathrm{d}S,$$
其中 $\Sigma$ 为抛物面 $z = 2 - (x^2 + y^2)$ 在 $xOy$ 平面上方的部分。

</div>

<div class='pbox'>

$$
\begin{gathered}
x=r\sin \theta,y=r\cos \theta,z=2-r^2 \\
\left\|\begin{vmatrix} i&j&k \\
r\cos\theta&-r\sin\theta&0 \\
\sin\theta&\cos\theta&-2r \end{vmatrix}\right\|
=r\sqrt{4r^2+1} \\
\implies 
\iint_\Sigma (x^2+y^2)dS \\
=(\int_0^{2\pi} d\theta) \int_0^{\sqrt{2}}r^2(r\sqrt{4r^2+1})dr \\
=\dfrac{149}{30} \pi
\end{gathered}
$$

</div>

### T2

<div class="cbox">

**4.** 计算曲面积分
$$\iint_{\Sigma} (x^2 + y^2) \mathrm{d}S,$$
其中 $\Sigma$ 为锥面 $z = \sqrt{x^2+y^2}$ 与平面 $z=1$ 所围成的区域的所有边界。

</div>

<div class='pbox'>

锥面部分:

换元$x=z\cos \theta,y=z\sin \theta$,

$$
\begin{gathered}
\left\|\det \begin{bmatrix}
i&j&k \\
\cos\theta &\sin\theta&1 \\
-z\sin\theta&z\cos\theta&0
\end{bmatrix} \right\| \\
=\sqrt2 z
\end{gathered}
$$

$$
\begin{gathered}
I_1=\int_0^{2\pi} d\theta\int_0^1 \sqrt 2z^3dz \\
=\dfrac{\sqrt 2\pi}{2}  \\
\end{gathered}
$$

平面部分:

$$
\begin{gathered}
I_2=\int_0^{2\pi} d\theta \int_0^1 r^3dr \\
=\dfrac{\pi}{2} 
\end{gathered}
$$

故$I=I_1+I_2=\dfrac{(\sqrt 2+1)\pi}{2} $

</div>

### T3

<div class="cbox">

**5.** 计算曲面积分
$$\iint_{\Sigma} (x+y+z) \mathrm{d}S,$$
其中 $\Sigma$ 为球面 $x^2 + y^2 + z^2 = a^2$ 上 $z \ge h\ (0 < h < a)$ 的部分。

</div>

<div class='pbox'>

向XoY投影.

$$
\begin{gathered}
I=a\iint_{x^2+y^2\le a^2-h^2} (x+y+\sqrt{a^2-x^2-y^2})\dfrac{1}{\sqrt{a^2-x^2-y^2}} dS \\
=a\iint_{x^2+y^2\le a^2-h^2} (\dfrac{x+y}{\sqrt{a^2-x^2-y^2}} +1)dxdy \\
=a\int_0^{2\pi}\int_0^{\sqrt{a^2-h^2}}(\dfrac{r(\sin \theta+\cos\theta)}{\sqrt{a^2-r^2}}+1) rdrd\theta
\end{gathered}
$$

注意到第一部分先对$\theta$积分会直接变成$0$,所以

$$
\begin{gathered}
I=a\int_0^{2\pi}\int_0^{\sqrt{a^2-h^2}}rdrd\theta \\
=\pi a(a^2-h^2)
\end{gathered}
$$

</div>

### T4

<div class="cbox">

**6.** 计算
$$I = \iint_{\Sigma} xyz(y^2z^2 + z^2x^2 + x^2y^2) \mathrm{d}S,$$
其中 $\Sigma$ 是球面 $x^2 + y^2 + z^2 = a^2$ 在第一卦限中的部分。

</div>

<div class='pbox'>

$$
\begin{gathered}
I=\iint_{x^2+y^2\le a^2,x\ge 0,y\ge 0} xy\sqrt{a^2-x^2-y^2} (x^2y^2+(a^2-x^2-y^2)(x^2+y^2)) \dfrac{a}{\sqrt{a^2-x^2-y^2}}  dS\\
=a\iint_{x^2+y^2\le a^2,x\ge 0,y\ge 0} x^3y^3+xy(x^2+y^2)(a^2-x^2-y^2) dS \\
=a\int_0^{\frac\pi2}(\int_0^a r^6\sin^3 \theta\cos^3 \theta+r^4\sin\theta\cos\theta(a^2-r^2))rdrd\theta \\
=\dfrac{a^9}{8} (\int_0^{\frac\pi 2}\sin^3\theta\cos^3\theta d\theta)+\dfrac{a^9}{24} (\int_0^{\frac\pi2}\sin\theta\cos\theta d\theta) \\
=\dfrac{a^9}{32} 
\end{gathered}
$$

</div>

## Class 2

### T1

<div class="cbox">

**2.** 计算第二类曲面积分

$$I = \iint_{\Sigma} dy dz + dz dx + dx dy,$$

其中 $\Sigma$ 为上半单位球面 $z^2 = 1 - x^2 - y^2, z \ge 0$, 取内侧.

</div>

<div class="pbox">

由对称性,$\iint_{\Sigma} dydz=\iint_{\Sigma_{x^+}}dydz+\iint_{\Sigma_{x^-}}dydz=0$,其中$\Sigma_{x^+},\Sigma_{x^-}$分别表示$\Sigma$的$x$坐标为$+,-$的部分.

从而

$$
\begin{gathered}
I=\iint_{\Sigma} dxdy \\
=-\iint_{x^2+y^2\le 1} (0,0,1)\cdot (r_x\times r_y)  dxdy\\
=-\iint_{x^2+y^2\le 1} (0,0,1)\cdot ((1,0,f_x)\times (0,1,f_y))dxdy  \\
=-\iint_{x^2+y^2\le 1} (0,0,1)\cdot (-f_x,-f_y,1) dxdy\\
=-\iint_{x^2+y^2\le 1}1dxdy \\
=-\pi
\end{gathered}
$$

</div>

### T2

<div class="cbox">

**3.** 计算

$$I = \iint_{\Sigma} y(x-z) dy dz + x^2 dz dx + (y^2 + xz) dx dy,$$

其中 $\Sigma$ 为由 $x=y=z=0, x=y=z=a$ 六个平面所围成的立方体表面并取外侧为正向.

</div>

<div class="pbox">

$$
\begin{gathered}
f(x,y,z)=(yx-yz,x^2,y^2+xz) \\
\nabla\cdot f(x,y,z)=x+y \\
I=\iint_{\Sigma} f(x,y,z)\cdot d\vec S  \\
=\iint_{V} \nabla\cdot f(x,y,z)dV \\
=\int_0^a \int_0^a\int_0^a (x+y)dxdydz \\
=a^4
\end{gathered}
$$

</div>

### T3

<div class="cbox">

**4.** 计算

$$I = \iint_{\Sigma} (z+x) dy dz + (x+y) dz dx + (y+z) dx dy,$$

其中 $\Sigma$ 是由 $x^2 + y^2 = 1, z=1$ 以及三个坐标平面所围成的立体在第一卦限的部分的表面, 方向取外侧.

</div>

<div class="pbox">

$$
\begin{gathered}
I=\iint_V \nabla\cdot (z+x,x+y,y+z) dV \\
=\iint_V 3 dV \\
=3V \\
=\dfrac{3}{4} \pi
\end{gathered}
$$

</div>

### T4

<div class="cbox">

**5.** 计算第二类曲面积分

$$I = \iint_{\Sigma} (y-z) dy dz + (z-x) dz dx + (x-y) dx dy,$$

其中 $\Sigma$ 是球面 $x^2 + y^2 + z^2 = 2Rx$ 被柱面 $x^2 + y^2 = 2rx(0 < r < R)$ 截下的位于 $z \ge 0$ 的部分, 取外侧.

</div>

<div class="pbox">

向$xOy$投影,$z=\sqrt{R^2-(x-R)^2-y^2}$

$$
\begin{gathered}
I= \iint_{(x-r)^2+y^2\le r^2} (y-z,z-x,x-y)\cdot ((1,0,z_x)\times (0,1,z_y))dxdy \\
=\iint_{(x-r)^2+y^2\le r^2} (y-z,z-x,x-y)\cdot(-z_x,-z_y,1)dxdy \\
=\iint_{(x-r)^2+y^2\le r^2} (\dfrac{(x-R)}{z} (y-z)+\dfrac{y}{z} (z-x)+x-y)dxdy \\
=R\iint_{(x-r)^2+(y^2)\le r^2}(1-\dfrac{y}{z})dxdy
\end{gathered}
$$

注意到由于区域关于$x=0$对称,所以

$$
\begin{gathered}
=\iint_{(x-r)^2+(y^2)\le r^2}\dfrac{y}{z}dxdy \\
=\iint_{(x-r)^2+(y^2)\le r^2,x>0}\dfrac{y}{z}dxdy+\iint_{(x-r)^2+(y^2)\le r^2,x<0}\dfrac{y}{z}dxdy \\
=0
\end{gathered}
$$

于是

$$
\begin{gathered}
I=R\iint_{(x-r)^2+y^2\le r^2} 1dxdy \\
=\pi r^2R
\end{gathered}
$$

</div>
