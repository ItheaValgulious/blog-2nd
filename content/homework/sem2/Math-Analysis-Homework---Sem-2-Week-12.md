---
password: fuckhomework
title: Math Analysis Homework - Sem 2 Week 12
tags:
  - homework
  - math
  - math-analysis
status: published
top: 0
date: '2026-06-01T13:03:53.099Z'
---

# Math Analysis Homework - Sem 2 Week 12

## Class 1

### T1

<div class="cbox">

**2.** 求曲线 $\Gamma$: 
$$
\begin{cases} (x - y)^2 = a(x + y), \\ x^2 - y^2 = \frac{9}{8}z^2 \end{cases}
$$
从点 $O(0,0,0)$ 到 $A(x_0, y_0, z_0)$ 的弧长, 其中 $a > 0, x_0 > 0$.

</div>

<div class="pbox">

$$
\begin{gathered}
\begin{cases}
t=x-y \\
x+y=\dfrac{t^2}{a}  \\
x=\dfrac{1}{2} (\dfrac{t^2}{a} +t) \\
y=\dfrac{1}{2} (\dfrac{t^2}{a} -t) \\ \\
z=\sqrt{\dfrac{t^3}{a}\dfrac{8}{9}  } \\
\end{cases} \\
\implies \begin{cases}
dx=(\dfrac{t}{a} +\dfrac{1}{2})dt  \\
dy=(\dfrac{t}{a} -\dfrac{1}{2})dt  \\
dz=(\dfrac{\sqrt{2t}}{\sqrt a})dt 
\end{cases} \\
\implies \int_L ds \\
=\int_0^{x_0-y_0} \sqrt{\dfrac{2t}{a} +\dfrac{2t^2}{a^2} +\dfrac{1}{2} }dt \\
=\int_0^{x_0-y_0} \sqrt{2(\dfrac{t}{a} +\dfrac{1}{2} )^2}dt \\
=\sqrt 2\int_0^{x_0-y_0} (\dfrac ta+\dfrac{1}{2} )dt \\
=\sqrt 2(\dfrac{x_0-y_0}{2} +\dfrac{(x_0-y_0)^2}{2a} ) \\
=\sqrt 2 x_0


\end{gathered}
$$

</div>

### T2

<div class="cbox">

**3.** 计算 
$$
I = \int_L |y| ds,
$$
$L$ 为双纽线 $(x^2 + y^2)^2 = a^2(x^2 - y^2)$.

</div>

<div class="pbox">

$$
\begin{gathered}
\begin{cases}
x=r\cos\theta \\
y=r\sin \theta
\end{cases} \\
\implies r^4=a^2 r^2\cos(2\theta) \\
\implies r^2=a^2\cos(2\theta) \\
\implies I=2(\int_{0}^{\frac\pi 4}+\int^{\pi}_{\frac34\pi})| r\sin\theta  \sqrt{dr^2+r^2d\theta^2}| \\
=4\int_{0}^{\frac\pi 4}(a^2|\sin \theta| d\theta) \\
=4a^2(1-\dfrac{\sqrt 2}{2} )

\end{gathered}
$$

</div>

### T3

<div class="cbox">

**1.** 计算积分 
$$
I = \int_C (x^2 + 2xy) dy,
$$
其中 $C$ 表示逆时针方向的上半椭圆 $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($y \geqslant 0$).

</div>

<div class="pbox">

有左右对称性,$\int_C x^2dy=0$.

$$
\begin{gathered}
I=\int_C 2xydy \\
=2\int_0^{\pi} ab\cos\theta\sin\theta b\cos\theta d\theta \\
=2ab^2\int_0^\pi \sin\theta\cos^2\theta d\theta \\
\text{let } J=\int_0^\pi \sin \theta \cos^2\theta d\theta \\
=-\cos^3 \theta|_0^\pi-\int_0^\pi -\cos\theta \cdot (2\cos\theta \cdot -\sin\theta)d\theta \\
=-\cos^3 \theta|_0^\pi-2J \\
\implies 3J=2,J=\dfrac{2}{3}  \\
\implies I=\dfrac{4}{3} ab^2
\end{gathered}
$$

</div>

### T4

<div class="cbox">

**2.** 求积分 
$$
\int_{\Gamma} y^2 dx + z^2 dy + x^2 dz,
$$
其中曲线 $\Gamma$ 表示球面 $x^2 + y^2 + z^2 = a^2$ 与柱面 $x^2 + y^2 = ax$ 相交的部分, 这里 $a > 0$, 且从 $x$ 轴正向看 $\Gamma$ 是逆时针方向.

</div>

<div class="pbox">

柱面是$(x-\dfrac{a}{2} )^2+y^2=\dfrac{a^2}{4}$.

由于关于$y=0$对称,有$\int_\Gamma y^2dx=\int_\Gamma x^2dz=0$,

由关于$z=0$的对称性,得知$\int z^2dy$在上下部分抵消,$\int_\Gamma z^2dy=0$.

故积分值为$0$.

</div>

## Class 2

### T1

<div class="cbox">

**1.** 计算第二类曲线积分
$$\int_C (2xy^3 - y^2 \cos x) dx + (1 - 2y \sin x + 3x^2y^2) dy,$$
其中 $C$ 是抛物线 $2x = \pi y^2$ 自 $(0,0)$ 到 $\left(\frac{\pi}{2}, 1\right)$ 的弧段.

</div>

<div class="pbox">

$$
\begin{gathered}
P(x,y)=2xy^3-y^2\cos x,Q(x,y)=1-2y\sin x+3x^2y^2 \\
P_y=6xy^2-2y\cos x=Q_x \\
\text{let } H(x,y)=x^2y^3-y^2\sin x+y \\
\text{then } \int_C Pdx+Qdy \\
=\int_C \nabla H \cdot d\vec s \\
=H(\dfrac\pi 2,1)-H(0,0) \\
=\dfrac{\pi^2}{4}
\end{gathered}
$$

</div>

### T2

<div class="cbox">

**2.** 计算第一类曲线积分
$$\oint_C \frac{\cos(\boldsymbol{r}, \boldsymbol{n})}{r} ds,$$
其中 $C$ 为分段光滑的简单闭曲线, $\boldsymbol{r} = (x,y)$, $r = \|\boldsymbol{r}\| = \sqrt{x^2+y^2}$, $\boldsymbol{n}$ 是 $C$ 上的单位外法向量.

</div>

<div class="pbox">

不妨设$C$逆时针.

$$
\begin{gathered}
I=\oint_C \dfrac{\vec r\times d\vec s}{r^2 ds} ds \\
= \oint_C \dfrac{\vec r}{r^2}\times d\vec s \\
=\oint_C \dfrac{xdy-ydx}{x^2+y^2}  \\
=\oint_C Qdy+Pdx \text{ where } Q(x,y)=\dfrac{x}{x^2+y^2} ,P(x,y)=\dfrac{-y}{x^2+y^2}
\end{gathered}
$$

因为

$$
\begin{gathered}
P_y=\dfrac{-x^2+y^2}{(x^2+y^2)^2} ,Q_x=\dfrac{x^2+y^2-2x^2}{(x^2+y^2)^2} \\
P_y=Q_x
\end{gathered}
$$

设$C$围成的区域为$D$,若该区域不包含原点,则

$$
\begin{gathered}
I=\iint_D (Q_x-P_y)dxdy=0
\end{gathered}
$$

否则取$\Gamma:x^2+y^2=\epsilon^2$,顺时针:

$$
\begin{gathered}
I+\oint_{\Gamma} \dfrac{xdy-ydx}{x^2+y^2} =\iint_{D-\{(x,y)|x^2+y^2<\epsilon^2\}} (Q_x-P_y)dxdy=0 \\
\implies I=-\oint_{\Gamma} \dfrac{xdy-ydx}{x^2+y^2}  \\
=-\dfrac{1}{\epsilon^2} \oint_\Gamma (xdy-ydx) \\
=\dfrac{1}{\epsilon^2} \iint_{\{(x,y)|x^2+y^2<\epsilon^2\}} 2 \\
=2\pi
\end{gathered}
$$

</div>

### T3

<div class="cbox">

**3.** 计算
$$I = \oint_C \frac{e^y}{x^2+y^2} [(x \sin x + y \cos x) dx + (y \sin x - x \cos x) dy],$$
其中 $C : x^2 + y^2 = 1$, 取逆时针方向.

</div>

<div class="pbox">

$$
\begin{gathered}
I=\oint_C \dfrac{e^y}{x^2+y^2} [(x\sin x+y\cos x)dx+(y\sin x-x\cos x)dy] \\
=\oint_C \dfrac{e^y\sin x}{x^2+y^2} (xdx+ydy)-\oint_C \dfrac{e^y\cos x}{x^2+y^2} (xdy-ydx) \\
x^2+y^2=1 \implies xdx+ydy=0 \\
-I=\oint_C e^y\cos x (xdy-ydx) \\
=\int_0^{2\pi} e^{\sin t}\cos (\cos t)dt \\
\end{gathered}
$$

$z=\cos t+i\sin t=e^{it},\Re(e^{-iz})=\Re(e^{\sin t}-e^{i\cos t})=e^{\sin t}\cos(\cos t),dz=de^{it}=izdt$,故:

$$
\begin{gathered}
I=-\Re[\oint_{|z|=1}\dfrac{e^{-iz}}{iz} ] \\
=-2\pi i \dfrac{1}{i}  \\
=-2\pi
\end{gathered}
$$

</div>
