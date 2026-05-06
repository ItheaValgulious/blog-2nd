---
title: Math Analysis Homework - Sem2 Week 7
tags:
  - math
  - math-analysis
  - homework
status: published
top: 0
date: '2026-04-22T05:27:17.490Z'
---

# Math Analysis Homework - Sem2 Week 7

## Class 1

### T1

<div class="cbox">

**2.** 设 $f(x, y) = x + (y - 1) \arcsin \sqrt{\frac{x}{y}}$, 求 $f_x(x, 1)$.

</div>

<div class='pbox'>

$$
\begin{gathered}
f_x(x,1)=1+(1-1)(\arcsin\sqrt\dfrac{x}{y} )^{-1} \\
=1
\end{gathered}
$$

</div>

### T2

<div class="cbox">

**3.** 设 $f(x, y) = \begin{cases} y \sin \frac{1}{x^2 + y^2}, & x^2 + y^2 \neq 0, \\ 0, & x^2 + y^2 = 0, \end{cases}$ 考察函数 $f(x, y)$ 在点 $(0, 0)$ 处的可偏导性.

</div>

<div class='pbox'>

$$
\begin{gathered}
f_x(0,0)=\lim_{x \to 0} \dfrac{f(x,0)}{x} =\lim_{x \to 0} \dfrac{0\sin \dfrac{1}{x^2+0^2}}{0}=0 \\
f_y(0,0)=\\lim_{y \to 0} \dfrac{f(0,y)}{y} = \lim_{y \to 0} \dfrac{y\sin \dfrac{1}{0^2+y^2} }{y} =\lim_{y \to 0}\sin \dfrac{1}{y^2}  ,\\
\text{ which does not exist}  
\end{gathered}
$$

</div>

### T3

<div class="cbox">

**4.** 证明函数 $z = \sqrt{x^2 + y^2}$ 在点 $(0, 0)$ 处连续但偏导数不存在.

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{(x,y) \to (0,0)} z(x,y) \\
=\lim_{(x,y) \to (0,0)} \sqrt{x^2+y^2} \\
=0=z(0,0)
\end{gathered}
$$

故$(0,0)处$连续.

$z$关于$x,y$对称,只考虑$x$的偏导数:

$$
\begin{gathered}
z_x(0,0)=\lim_{x \to 0} \dfrac{z(x,0)-z(0,0)}{x}  \\
=(\dfrac{|x|}x)' \text{ which does not exist} 
\end{gathered}
$$

</div>

### T4

<div class="cbox">

**6.** 证明：若函数 $f(x, y)$ 在点 $P(x_0, y_0)$ 的某邻域 $U(P)$ 内的偏导数 $f_x$ 与 $f_y$ 有界, 则 $f(x, y)$ 在 $U(P)$ 内连续.

</div>

<div class='pbox'>

设$\max (|f_x(x,y)|,|f_y(x,y)|)<M$

$$
\begin{gathered}
\forall (x_1,y_1),(x_2,y_2)\in U(P) \\
|f(x_1,y_1)-f(x_2,y_2)|  \\
\le |f(x_1,y_1)-f(x_2,y_1)|+|f(x_2,y_1)-f(x_2,y_2)| \\
= |f_x(\xi_1,y_1)(x_2-x_1)|+|f_y(x_2,\xi_2)(y_1-y_2)| \\
\le M(|x_2-x_1|+|y_2-y_1|)\le 2M\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
\end{gathered}
$$

因为邻域,所以对任意$(x_1,y_1)$,存在一个小开球$B((x_1,y_1),r)\subset U(P)$.那么$\forall \epsilon,\exists \delta=\min (\dfrac \epsilon{2M},\dfrac{\sqrt 2}2r)$就使得两点距离小于$\delta$时,上面证明中用到的点$(x_1,y_1),(x_2,y_1),(x_2,y_2)$都在开球故都在$U(P)$里,且$|f(x_1,y_1)-f(x_2,y_2)|<\epsilon$.于是得证.


</div>

### T5

<div class="cbox">

**7.** 求下列函数在给定点的全微分:
(2) $z = \frac{x}{\sqrt{x^2 + y^2}}$ 在点 $(1, 0)$.

</div>

<div class='pbox'>

先验证:

$$
\begin{gathered}
f_x=(\dfrac1{x^2+y^2})(\sqrt{x^2+y^2}-\dfrac{x^2}{\sqrt{x^2+y^2}}) \\
f_y=-\dfrac{2xy}{2(x^2+y^2)^{\frac32}} 
\end{gathered}
$$

均连续.故可微,代入得

$$
\begin{gathered}
f_x(1,0)=(\dfrac{x}{|x|})' |_{x=1}=0 \\
f_y(1,0)=0 \\
f(x,y)=o(\sqrt{(x-1)^2+y^2}), (x,y)\in U(1,0)
\end{gathered}
$$

</div>

### T6

<div class="cbox">

**8.** 求下列函数的全微分:
(2) $u = x e^{y^z} + e^{-z} + y$.

</div>

<div class='pbox'>

$$
\begin{gathered}
f_x=e^{y^z} \\
f_y=1+zxe^{y^z}y^{z-1} \\
f_z=-e^{-z}+xe^{y^z}y^z\ln y
\end{gathered}
$$

当在定义域$y>0$时,三个都连续.故可微.且全微分即

$$
\begin{gathered}
f(x,y,z) \\
=f_x(x_0,y_0,z_0)dx \\
+f_y(x_0,y_0,z_0)dy \\
+f_z(x_0,y_0,z_0)dz
\end{gathered}
$$

</div>

### T7

<div class="cbox">

**9.** 证明函数 
$$f(x, y) = \begin{cases} \frac{x^2 y}{x^2 + y^2}, & x^2 + y^2 \neq 0, \\ 0, & x^2 + y^2 = 0 \end{cases}$$ 
在点 $(0, 0)$ 连续且偏导数存在，但在此点不可微.

</div>

<div class='pbox'>

连续:

$$
\begin{gathered}
0\le \lim_{(x,y) \to (0,0)} |\dfrac{x^2y}{x^2+y^2}| \\
=\lim_{r \to 0} |\dfrac{r^3\cos^2(\theta)\sin(\theta)}{r^2}|  \\
=\lim_{r \to 0} |r\cos^2(\theta)\sin(\theta)| \\
=0=f(0,0)
\end{gathered}
$$

$$
\begin{gathered}
f_x(0,0)=\lim_{x \to 0} \dfrac{f(x,0)-f(0,0)}{x}=0 \\
f_y(0,0)=\lim_{y \to 0} \dfrac{f(0,y)-f(0,0)}{y} =0
\end{gathered}
$$

则若微分存在,一定有$f(x,y)=o(\sqrt{x^2+y^2})$.但沿$y=x$得

$$
\begin{gathered}
\lim_{(x,x) \to (0,0)} \dfrac{f(x,x)}{\sqrt{x^2+x^2}}=\dfrac1{2\sqrt 2}\ne 0
\end{gathered}
$$

于是不存在.

</div>

### T8

<div class="cbox">

**10.** 证明函数 
$$f(x, y) = \begin{cases} (x^2 + y^2) \sin \frac{1}{\sqrt{x^2 + y^2}}, & x^2 + y^2 \neq 0, \\ 0, & x^2 + y^2 = 0 \end{cases}$$ 
在点 $(0, 0)$ 连续且偏导数存在，但偏导数在点 $(0, 0)$ 不连续，而 $f$ 在点 $(0, 0)$ 处可微.

</div>

<div class='pbox'>

连续:

$$
\begin{gathered}
0\le \lim_{(x,y) \to (0,0)} |f(x,y)| \\
=\lim_{r \to 0} |r^2\sin \dfrac1{r}| \\
\le \lim_{r \to 0} |r^2| \\
=0 \\
\implies \lim_{(x,y) \to (0,0)} f(x,y)=0=f(0,0)
\end{gathered}
$$

偏导数:

$$
\begin{gathered}
\forall(x,y)\ne (0,0): \\
f_x(x,y)=2x\sin(\dfrac{1}{\sqrt{x^2+y^2}} )-x\dfrac1{\sqrt{x^2+y^2}}\cos(\dfrac{1}{\sqrt{x^2+y^2}}) \\
=2r\cos(\theta)\sin(\dfrac{1}{r} )-\cos(\theta)\cos(\dfrac{1}{r}) \\
\lim_{(x,y) \to (0,0)} f_x(x,y) \\
=\lim_{r \to 0} f_x(x,y) \\
=\cos\theta \cos(\dfrac1r) \\
\text{which does not exist} \\ 
\text{while } 
\forall (0,0): \\
f_x(0,0)=\lim_{x \to 0} \dfrac{f(x,0)-f(0,0)}{x} =\lim_{x \to 0} x\sin\dfrac{1}{x} =0
\end{gathered}
$$

故不连续.

但令$r=\sqrt{r^2+y^2}$,$\lim_{r \to 0} \dfrac{r^2\sin(\dfrac1r)}{r} =0$,故$f(x,y)=f(0,0)+o(\sqrt{x^2+y^2})$,可微.


</div>

### T9

<div class="cbox">

**11.** 若函数 $f(x, y)$ 对每一个固定的 $y$ 是 $x$ 的连续函数，又 $f$ 存在对 $y$ 的有界偏导数. 证明：$f$ 为连续函数.

</div>

<div class='pbox'>

对任意$(x_0,y_0)$,设$|f_y|\le M$:

$$
\begin{gathered}
\lim_{(x,y) \to (x_0,y_0)} |f(x,y)-f(x_0,y_0)| \\
\le \lim_{(x,y) \to (x_0,y_0)} |f(x,y)-f(x,y_0)|+|f(x,y_0)-f(x_0,y_0)| \\
=\lim_{(x,y) \to (x_0,y_0)} |(y-y_0)f_y(x,\xi)|+0 \\
\le \lim_{(x,y) \to (x_0,y_0)} |y-y_0|M \\
=0
\end{gathered}
$$

故任意点连续.函数连续.

</div>

### T10

<div class="cbox">

**12.** 试证在点 $(0, 0)$ 的充分小邻域内, 有 
$$\arctan \frac{x + y}{1 + xy} \approx x + y.$$

</div>

<div class='pbox'>

什么叫约等于啊!@@E#!@我们假装约等于是同阶无穷小.

注意到
$$
\begin{gathered}
\begin{cases}
\lim_{x \to 0} \dfrac{f(x)}{g(x)} =0 \\
|g(x)|<M,h(x)\in C[R]
\end{cases} \\
\implies \lim_{x \to 0} \dfrac{h(f(x))}{h(g(x))} =0
\end{gathered}
$$

那么只需证

$$
\begin{gathered}
\dfrac{x+y}{1+xy} \approx \tan(x+y)
\end{gathered}
$$

那么我们知道

$\tan(x+y)\approx x+y\approx \dfrac{x+y}{1+xy}$.

于是就结束了.

</div>

### T11

<div class="cbox">

**18.** 求 $u(x, y) = x^2 - xy + y^2$ 在 $(1, 1)$ 处沿方向 $l = (\cos \alpha, \sin \alpha)$ 的方向导数, 并进一步求:
- (1) 在哪个方向上其导数有最大值?
- (2) 在哪个方向上其导数有最小值?
- (3) 在哪个方向上其导数为零?
- (4) $u$ 的梯度.

</div>

<div class='pbox'>

当$u$偏导数存在且一维连续时

$$
\begin{gathered}
\lim_{t \to 0} \dfrac{u(x+t\cos\alpha,y+t\sin\alpha)-u(x,y)}{t}  \\
=\lim_{t \to 0} (\dfrac{u(x+t\cos\alpha,y)-u(x,y)}{t\cos\alpha}\cos\alpha+ \\
\dfrac{u(x+t\cos\alpha,y+t\sin\alpha)-u(x+t\cos\alpha)}{t\sin\alpha})\sin\alpha  \\
=\lim_{t \to 0} u_x(x,y)\cos\alpha+u_y(x+t\cos\alpha,y)\sin\alpha \\
=u_x(x,y)\cos\alpha+u_y(x,y)\sin\alpha
\end{gathered}
$$

于是

$$
\begin{gathered}
u_x(1,1)=1,u_y(1,1)=1
\end{gathered}
$$

则方向导数$u_l=(\cos\alpha+\sin\alpha)$当$\alpha=\dfrac\pi4$时取最大值$\sqrt 2$.$\alpha=-\dfrac\pi4$时取最小值$\sqrt 2$,$\alpha=\dfrac34\pi,-\dfrac14\pi$时为$0$.


$$
\begin{gathered}
(\nabla u)(x,y)=(2x-y,2y-x)
\end{gathered}
$$

</div>

### T12

<div class="cbox">

**20.** 求常数 $a, b, c$, 使 $f(x, y, z) = a x y^2 + b y z + c z^2 x^3$ 在点 $(1, 2, -1)$ 沿平行于 $z$ 轴正向的方向有最大的方向导数 64.

</div>

<div class='pbox'>

方向导数沿梯度最大.$(1,2,-1)$处梯度为

$$
\begin{gathered}
(\nabla f)(x,y,z)=(4a+3c,4a-b,2b-2c)=\vec v
\end{gathered}
$$

平行于$z$轴知:$4a+3c=0,4a-b=0$.方向导数大小即$64=2b-2c$.

解得:

$$
\begin{gathered}
\begin{cases}
a= 6\\
b= 24\\
c= -8\\
\end{cases}
\end{gathered}
$$

</div>

### T13

<div class="cbox">

**21.** 求 $u(x, y, z) = x^2 + 2y^2 + 3z^2 + xy - 4x + 2y - 4z$:
- (1):在点 $(0, 0, 0)$ 处的梯度及其模的大小.
- (2):在点 $(5, -3, \frac{2}{3})$ 处的梯度及其模的大小.

</div>

<div class='pbox'>

$$
\begin{gathered}
\nabla u=(2x+y-4,4y+x+2,6z-4) \\
\vec v_1=(\nabla u)|_{(0,0,0)}=(-4,2,-4),\|\vec v_1\|=6 \\
\vec v_2=(\nabla u)|_{(5,-3,\frac23)}=(3,-5,0),\|\vec v_2\|=\sqrt{34} \\
\end{gathered}
$$

</div>


### T14

<div class="cbox">

**22.** 设函数 $u = \ln \left( \frac{1}{r} \right)$, 其中 $r = \sqrt{(x-a)^2 + (y-b)^2 + (z-c)^2}$, 求 $u$ 的梯度；并指出在空间哪些点上成立等式 $\|\text{grad } u\| = 1$.

</div>

<div class='pbox'>

$$
\begin{gathered} \\
u_x=r\cdot (-\dfrac1{r^2})\dfrac{dr}{dx} \\
=-\dfrac1r \dfrac{x-a}{r} \\
u_y=-\dfrac1r \dfrac{y-b}{r} \\
u_z=-\dfrac1r \dfrac{y-z}{r} \\
\implies \nabla u=-r^{-2}(x-a,y-b,z-c) \\
\|\nabla u\|=1 \implies r^{-2} \|(x-a,y-b,z-c)\|=r^{-1}=1 \\
\end{gathered}
$$

故在到$(a,b,c)$距离为$1$的点上成立.

</div>

### T15

<div class="cbox">

**25.** 设二元函数 
$$f(x, y) = \begin{cases} xy \frac{x^2 - y^2}{x^2 + y^2}, & x^2 + y^2 \neq 0, \\ 0, & x^2 + y^2 = 0. \end{cases}$$ 
求 $f_{xy}(0, 0)$ 与 $f_{yx}(0, 0)$.

</div>

<div class='pbox'>

$$
\begin{gathered}
f_{xy}(0,0)=\lim_{y \to 0}\dfrac1y(\lim_{x \to 0} \dfrac{f(x,y)}{x}-\lim_{x \to 0} \dfrac{f(x,0)}{x}) \\
\lim_{y \to 0} \dfrac{1}{y} (-y-0)=-1 \\
f_{yx}(0,0)=\lim_{x \to 0} \dfrac{1}{x} (\lim_{y \to 0} \dfrac{f(x,y)}{y} - \lim_{y \to 0} \dfrac{f(0,y)}{y} ) \\
=\lim_{x \to 0} \dfrac{1}{x} (x-0)=1
\end{gathered}
$$

</div>

### T16

<div class="cbox">

**28.** 设 $f_x, f_y$ 在点 $(x_0, y_0)$ 的某邻域内存在且在点 $(x_0, y_0)$ 处可微, 则有 $f_{xy}(x_0, y_0) = f_{yx}(x_0, y_0)$.

</div>

<div class='pbox'>

设$W(\Delta x,\Delta y)=f(x_0+\Delta x,y_0+\Delta y)-f(x_0,y_0+\Delta y)-f(x_0+\Delta x,y_0)+f(x_0,y_0)$.

然后为了一致,对$\varphi(t)=f(t,y_0+\Delta y)-f(t,y_0)$,则

$$
\begin{gathered}
W(\Delta x,\Delta y)=\phi'(x_0+\xi_1)\Delta x=\Delta x f_x(x_0+\xi_1,y_0+\Delta y)-\Delta x f_x(x_0+\xi_1,y_0) \\
=f_{xy}(x_0,y_0) \Delta x \Delta y+o(\Delta x\sqrt{\Delta x^2+\Delta y^2})
\end{gathered}
$$

同理还可以得到

$$
\begin{gathered}
W(\Delta x,\Delta y)=f_{yx}(x_0,y_0) \Delta x \Delta y+o(\Delta y\sqrt{\Delta x^2+\Delta y^2})
\end{gathered}
$$

那么极限

$$
\begin{gathered}
\lim_{\Delta x \to 0} \dfrac{W(\Delta x,\Delta x)}{\Delta x^2} =f_{xy}(x_0,y_0)=f_{yx}(x_0,y_0)
\end{gathered}
$$

得证.

</div>

## Class 2

### T1

<div class="cbox">

**3.** 设 $f(x, y)$ 可微, $f(1, 1) = 1, f_x(1, 1) = a, f_y(1, 1) = b$. 令 $\varphi(x) = f(x, f(x, x))$, 求 $\varphi'(1)$.

</div>

<div class='pbox'>

$$
\begin{gathered}
\varphi'(1)=\dfrac{\partial f}{\partial x} +\dfrac{\partial f}{\partial y} (\dfrac{\partial f}{\partial x} +\dfrac{\partial f}{\partial y} ) \\
=a+ab+b^2
\end{gathered}
$$

</div>

### T2

<div class="cbox">

**4.** 已知 $z = u^2 \ln v, u = \frac{x}{y}, v = 3x - 2y$, 求 $\frac{\partial z}{\partial x}, \frac{\partial z}{\partial y}$.

</div>

<div class='pbox'>

$$
\begin{gathered}
z_x=z_uu_x+z_vv_x \\
=2u\ln v\dfrac{1}{y} +\dfrac{u^2}{v} 3 \\
=\dfrac{2x\ln(3x-2y)}{y^2} +\dfrac{3x^2}{y^2(3x-2y)} 
\end{gathered} \\
z_y=z_uu_y+z_vv_y \\
=2u\ln v \cdot (-\dfrac{x}{y^2} )-2\dfrac{u^2}{v}  \\
=-\dfrac{2x^2\ln(3x-2y)}{y^3} -\dfrac{2x^2}{y^2(3x-2y)} 
$$

</div>

### T3

<div class="cbox">

**6.** 设 $z = \sin y + f(\sin x - \sin y)$, 其中 $f$ 为可微函数, 证明: 
$$\frac{\partial z}{\partial x} \sec x + \frac{\partial z}{\partial y} \sec y = 1.$$

</div>

<div class='pbox'>

$$
\begin{gathered}
z_x\sec x+z_y\sec y \\
=f'(\sin x-\sin y)\cos x\sec x \\
+(\cos y-f'(\sin x-\sin y)\cos y)\sec y \\
=1
\end{gathered}
$$

</div>

### T4

<div class="cbox">

**7.** 在方程 $x \frac{\partial z}{\partial x} + y \frac{\partial z}{\partial y} = z^2$ 中作变换 $u = x, v = \frac{1}{y} - \frac{1}{x}, w = \frac{1}{z} - \frac{1}{x}$, 求变换后的方程.

</div>

<div class='pbox'>

$$
\begin{gathered}
w_x=-\dfrac{z_x}{z^2} +\dfrac{1}{x^2}=w_uu_x+w_vv_x=w_u+\dfrac{1}{u^2} w_v  \\
w_y=-\dfrac{z_y}{z^2} =w_vv_y+w_uu_y=-\dfrac{w_v}{y^2}  \\
z_x=\dfrac{z^2}{x^2} -w_uz^2-\dfrac{z^2}{u^2} w_v \\
z_y=\dfrac{z^2}{y^2} w_v \\
\end{gathered}
$$

原式变成

$$
\begin{gathered}
1=\dfrac{1}{u} -uw_u-\dfrac{w_v}{x} +\dfrac{w_v}{y}  \\
\iff \dfrac{1}{u} -uw_u+w_vv=1
\end{gathered}
$$

</div>

### T5

<div class="cbox">

**11.** 设 $u = u(x, y), x = r \cos \theta, y = r \sin \theta$. 证明: 
$$\frac{\partial^2 u}{\partial r^2} + \frac{1}{r} \frac{\partial u}{\partial r} + \frac{1}{r^2} \frac{\partial^2 u}{\partial \theta^2} = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}.$$

</div>

<div class='pbox'>

$$
\begin{gathered}
u_r=u_x\cos\theta+u_y\sin\theta \\
u_\theta=-u_xr\sin\theta+u_yr\cos\theta \\
u_{rr}=\cos\theta(u_{xx}\cos\theta+u_{xy}\sin\theta)+\sin\theta(u_{yx}\cos\theta+u_{yy}\sin\theta) \\
u_{\theta\theta}=-r\cos\theta u_x-r\sin\theta(-u_{xx}r\sin\theta+u_{xy}r\cos\theta) \\
-r\sin\theta u_y+r\cos\theta(-u_{yx}r\sin\theta+u_{yy}r\cos\theta) \\
u_{rr}+\dfrac{1}{r} u_r+\dfrac{1}{r^2} u_{\theta\theta} \\
=u_{xx}(\cos^2\theta+\dfrac{r^2}{r^2} \sin^2\theta) \\
+u_{yy}(\sin^2\theta+\dfrac{r^2}{r^2} \cos^2\theta) \\
+u_{xy}(\sin\theta\cos\theta-\sin\theta\cos\theta) \\
+u_{yx}(\sin\theta\cos\theta-\sin\theta\cos\theta) \\
+\dfrac{u_x\cos\theta+u_y\sin\theta}{r} -\dfrac{r}{r^2} (u_x\cos\theta+u_y\sin\theta) \\
=u_{xx}+u_{yy}
\end{gathered}
$$

</div>

### T6

<div class="cbox">

**12.** 证明函数 $u = \frac{1}{2a\sqrt{\pi t}} e^{-\frac{(x-b)^2}{4a^2t}}$ ($a, b$ 为常数) 满足热传导方程: 
$$\frac{\partial u}{\partial t} = a^2 \frac{\partial^2 u}{\partial x^2}.$$

</div>

<div class='pbox'>

$$
\begin{gathered}
u_t=\dfrac{1}{2a\sqrt\pi}((-\dfrac12t^{-\frac32} )e^{-\frac{(x-b)^2}{4a^2t}}+t^{-\frac12}e^{-\frac{(x-b)^2}{4a^2t}}(\dfrac{1}{t^2}\dfrac{(x-b)^2}{4a^2} )) \\
=u(-\dfrac{1}{2t} + \dfrac{(x-b)^2}{4a^2t^2} ) \\
u_{x}=-\dfrac{(x-b)}{2a^2t} u \\
u_{xx}=-\dfrac{1}{2a^2t} u+\dfrac{(x-b)}{2a^2t}\dfrac{(x-b)}{2a^2t} u \\
\text{so } 
a^2u_{xx}=u(-\dfrac{1}{2t} +\dfrac{(x-b)^2}{4a^2t^2})=u_t
\end{gathered}
$$

</div>

### T7

<div class="cbox">

**13.** 证明函数 $u = \ln \sqrt{(x-a)^2 + (y-b)^2}$ ($a, b$ 为常数) 满足拉普拉斯方程: 
$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0.$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } r=(x-a)^2+(y-b)^2 \\
u_x=\dfrac{1}{2} \dfrac{1}{r} 2(x-a)=\dfrac{x-a}{r}  \\
u_{xx}=\dfrac{r-2(x-a)(x-a)}{r^2} =\dfrac{(y-b)^2-(x-a)^2}{r^2}  \\
u_y=\dfrac{1}{2} \dfrac{1}{r} 2(y-b)=\dfrac{y-b}{r}  \\
u_{yy}=\dfrac{r-2(y-b)(y-b)}{r^2} =\dfrac{(x-a)^2-(y-b)^2}{r^2}  \\
\text{so } u_{xx}+u_{yy}=0
\end{gathered}
$$

</div>

### T8

<div class="cbox">

**16.** 设 $u = f(r), r = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2}$, 证明: 
$$\frac{\partial^2 u}{\partial x_1^2} + \frac{\partial^2 u}{\partial x_2^2} + \dots + \frac{\partial^2 u}{\partial x_n^2} = \frac{d^2 u}{d r^2} + \frac{n-1}{r} \frac{d u}{d r}.$$

</div>

<div class='pbox'>

$$
\begin{gathered}
u_{x_i}=u_r r_{x_i}=u_r \dfrac{x_i}{r}  \\
u_{x_ix_i}=(u_{rr}r_{x_i})\dfrac{x_i}{r} +u_r(\dfrac{x_i}{r} )_{x_i} \\
=u_{rr}\dfrac{x_i^2}{r^2} +u_r\dfrac{r-x_i \dfrac{x_i}{r} }{r^2}  \\
=u_{rr}\dfrac{x_i^2}{r^2} +u_r (\dfrac{1}{r} -\dfrac{x_i^2}{r^3} ) \\
\text{so } \sum_{i=1}^n u_{x_ix_i} \\
=u_{rr} \dfrac{\sum_{i=1}^n x_i^2}{r^2} +\dfrac{nu_r}{r} -u_r\dfrac{\sum_{i=1}^n x_i^2}{r^3}  \\
=u_{rr}+\dfrac{n-1}{r} u_r
\end{gathered}
$$

</div>

### T9

<div class="cbox">

**17.** 设 $z = f[x + \varphi(y)]$, 其中 $\varphi$ 可微, $f$ 有二阶连续导数. 证明: 
$$\frac{\partial z}{\partial x} \frac{\partial^2 z}{\partial x \partial y} = \frac{\partial z}{\partial y} \frac{\partial^2 z}{\partial x^2}.$$

</div>

<div class='pbox'>

$$
\begin{gathered}
z_x=f'(x+\varphi(y)) \\
z_y=f'(x+\varphi(y))\varphi'(y) \\
z_{xx}=f''(x+\varphi(y)) \\
z_{xy}=f''(x+\varphi(y))\varphi'(y) \\
\text{so } z_xz_{xy}=f'f''\varphi'=z_yz_{xx}
\end{gathered}
$$

</div>

### T10

<div class="cbox">

**18.** 证明: 若函数 $u = f(x, y)$ 满足拉普拉斯方程 $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$, 则函数 $v = f\left(\frac{x}{x^2 + y^2}, \frac{y}{x^2 + y^2}\right)$ 也满足拉普拉斯方程.

</div>

<div class='pbox'>

$$
\begin{gathered} \\
\text{let } r=x^2+y^2,a=\dfrac{x}{r} ,b=\dfrac{y}{r}  \\
v_x=v_aa_x+v_bb_x \\
v_{xx}=(v_{aa}a_x+v_{ab}b_x)a_x+v_a(a_{xx})+(v_{ba}a_x+v_{bb}b_x)b_x+v_b(b_{xx}) \\
=v_{aa}(a_x^2-b_x^2)+a_xb_x(v_{ab}+v_{ba})+v_aa_{xx}+v_bb_{xx} \\
\text{Similarily, } \\
v_{yy}=v_{bb}(b_y^2-a_y^2)+a_yb_y(v_{ab}+v_{ba})+v_bb_{yy}+v_aa_{yy}
\end{gathered}
$$

因为

$$
\begin{gathered}
a_x^2-b_x^2-b_y^2+a_y^2 \\
=(\dfrac{y^2-x^2}{r^2})^2-(\dfrac{-2xy}{r^2} )^2-(\dfrac{x^2-y^2}{r^2} )^2+(\dfrac{-2xy}{r^2} )^2=0 \\
a_xb_x+a_yb_y=\dfrac{-2xy(y^2-x^2)}{r^4} +\dfrac{-2xy(x^2-y^2)}{r^4} =0 \\
a_{xx}+a_{yy} \\
=\dfrac{-2xr^2-(y^2-x^2)2r2x}{r^4} +\dfrac{-2xr^2+2xy2r2y}{r^4}  \\
=2\dfrac{-2x(x^2+y^2)-2x(y^2-x^2)+4xy^2}{r^3}  \\
=0 \\
\text{Similarily} b_xx+b_yy=0 \\
\end{gathered}
$$

则有

$$
\begin{gathered}
v_{xx}+v_{yy} \\
=v_{aa}(a_x^2-b_x^2-b_y^2+a_y^2) \\
+(v_{ab}+v_{ba})(a_xb_x+a_yb_y) \\
+v_a(a_{xx}+a_{yy})+v_b(b_{xx}+b_{yy}) \\
=0
\end{gathered}
$$

</div>
