---
title: Math Analysis Homework - Sem 2 Week 9
tags:
  - math-analysis
  - math
  - homework
status: published
top: 0
date: '2026-05-17T09:53:46.264Z'
---

# Math Analysis Homework - Sem 2 Week 9

### T1

<div class="cbox">

**2.** 求函数 $f(x, y) = 2x^2 - xy - y^2 - 6x - 3y + 5$ 在点 $(1, -2)$ 的泰勒展开式.

</div>

<div class='pbox'>

$$
\begin{gathered}
f(1,-2)=5 \\
f_x(1,-2)=0 \\
f_y(1,-2)=0 \\
f_{xx}(1,-2)=4 \\
f_{yy}(1,-2)=-2 \\
f_{xy}(1,-2)=-1 \\
f(x,y)=5+\dfrac{1}{2} (4(x-1)^2-2(x-1)(y+2)-2(y+2)^2)
\end{gathered}
$$

</div>

### T2

<div class="cbox">

**3.** 求下列函数的泰勒展开式:
(1) $f(x, y) = \sin(x^2 + y^2)$ 在点 $(0, 0)$, 直到二阶为止;

</div>

<div class='pbox'>

$$
\begin{gathered}
\sin(x)=x+o(x)  \\
f(x,y)=x^2+y^2+o(x^2+y^2 )
\end{gathered}
$$

</div>

### T3

<div class="cbox">

**3.** 求下列函数的泰勒展开式:
(3) $f(x, y) = \ln(1 + x + y)$ 在点 $(0, 0)$, 直到 $n$ 阶为止.

</div>

<div class='pbox'>

$$
\begin{gathered}
\ln(1+(x+y))=\sum _{i = 1} ^{n} (-1)^{i-1}\dfrac{(x+y)^i}{i}  \\
=\sum _{i = 1} ^{n} \dfrac{(-1)^{i-1}}{i}  \sum _{j = 0} ^{i}  \binom ijx^jy^{i-j}+o((x^2+y^2)^\frac n2)
\end{gathered}
$$

</div>

### T4

<div class="cbox">

**5.** 设 $f(x, y) = 3x^2y - x^4 - 2y^2$. 证明: $(0, 0)$ 不是它的极值点, 但沿过 $(0, 0)$ 点的每条直线, $(0, 0)$ 都是它的极大值点.

</div>

<div class='pbox'>

对过$(0,0)$的直线$x=at,y=bt$,有

$$
\begin{gathered}
f(x,y)=3a^2bt^3-a^4t^4-2b^2t^2 \\
\dfrac{df}{dt} =9a^2bt^2-4a^4t^3-4b^2t \\
=t(-4a^4t^2+9a^2bt-4b^2)
\end{gathered}
$$

故$\dfrac{df}{dt}(0,0)=0$,且在原点小邻域内$\operatorname{sgn}(t(-4a^4t^2+9a^2bt-4b^2))=\operatorname{sgn}(-t)$,故为极大值点.

但当$y=\dfrac{3}{4}x^2$时,$f(x,y)=\dfrac{1}{8} x^4$,$(0,0)$是该条抛物线上的极小值.故$(0,0)$的小邻域内同时有比$(0,0)$大/小的,不为极值.

</div>

### T5

<div class="cbox">

**6.** 证明函数 $z = f(x, y) = (1 + e^y) \cos x - ye^y$ 有无穷多个极大值, 但无极小值.

</div>

<div class='pbox'>

$$
\begin{gathered}
f_x(x,y)=-\sin(x)(1+e^y) \\
f_y(x,y)=(\cos x-y-1)e^y \\
f_{xx}=-\cos(x)(1+e^y) \\
f_{xy}=-e^y\sin(x) \\
f_{yy}=e^y(\cos x-y-2) \\
\begin{vmatrix} -\cos x(1+e^y)&-e^y\sin x\\-e^y\sin x&e^y(\cos x-y-2) \end{vmatrix}  \\
=e^y(-e^{y}-\cos^2 x+(y+2)\cos x+(y+2)e^{y}\cos x) \\
\end{gathered}
$$

对驻点处,$f_x=f_y=0$,故$\sin x=0,\cos x=y+1$,于是驻点为$(2k\pi,0),((2k+1)\pi,-2)$,分别代入判别式得:
$$
\begin{gathered}
\text{for } (2k\pi,0),-1-1+2+2=2>0 \\
\text{for } ((2k+1)\pi,-2),(-e^y-1)e^y<0
\end{gathered}
$$

故所有$(2k\pi,0)$为极值,因为$f_{xx}<0$所以是极大值,有无穷个;所有$((2k+1)\pi,-2)$为鞍点.无极小值.

</div>

### T6

<div class="cbox">

**8.** 求函数 $f(x, y) = x^3 - 3x^2 + 2xy - y^2$ 在 $D = [-3, 3] \times [-1, 1]$ 上的最大值.

</div>

<div class='pbox'>

对$D$的内部:

$$
\begin{gathered}
\begin{cases}
f_x=3x^2-6x+2y=0 \\
f_y=2x-2y=0
\end{cases}
\implies \begin{cases}
x=0 \\
y=0
\end{cases},\begin{cases}
x=\dfrac{4}{3}  \\
y=\dfrac{4}{3} 
\end{cases}
\end{gathered}
$$

则$f(0,0)=0$,$(\dfrac{4}{3} ,\dfrac{4}{3} )$在区域外舍去.

对$D$的边缘:

$x=3$得$f(3,y)=6y-y^2$,最大为$f(3,1)=5$.

$x=-3$得$f(-3,y)=-54-6y-y^2<0$.

$y=1$得$f(x,1)=x^3-3x^2+2x-1$,求导得$3x^2-6x+2$,有极大值$f(1-\dfrac{\sqrt3}3,1)<5$

$y=-1$得$f(x,-1)=x^3-3x^2-2x-1$,$x>0$时小于$f(x,1)$,$x<0$时$x^3-3x^2-2x-1<-2x-1<5$

故最大值为$5$.

</div>

### T7

<div class="cbox">

**11.** 曲面 $z = \frac{1}{2}x^2 - 4xy + 9y^2 + 3x - 14y + \frac{1}{2}$ 在何处有最高点或最低点?

</div>

<div class='pbox'>

$$
\begin{gathered}
\begin{cases}
f_x=x-4y+3=0 \\
f_y=18y-4x-14=0
\end{cases} \\
\implies \begin{cases}
x=1 \\
y=1
\end{cases}
\end{gathered} \\
f_{xx}=1,f_{yy}=18,f_{xy}=-4 \\
\begin{vmatrix} 1 &-4\\-4&18 \end{vmatrix}=2>0
$$

则唯一的驻点是$z(1,1)=-5$是极小值.

显然$x=y$时,$\lim_{x \to \infty} z(x,y)=+\infty$,无极大值.

注意到

$$
\begin{gathered}
z=8(\dfrac x4-y)^2+(y-7)^2+3x+C  \\
\ge 7(\dfrac{x}{4} -y)^2+2(\dfrac{x}{8} -\dfrac{7}{2} )^2+3x+C 
\end{gathered}
$$

由下式知存在$M$使得$\max(x,y)>M$时$z>0$,故$-5$是最小值.

</div>
