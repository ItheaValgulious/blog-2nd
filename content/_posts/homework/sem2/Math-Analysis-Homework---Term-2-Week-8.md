---
title: Math Analysis Homework - Sem 2 Week 8
tags:
  - math
  - math-analysis
  - homework
status: draft
top: 0
---

# Math Analysis Homework - Term 2 Week 8

### T1

<div class="cbox">

**6.** 设函数 $z = z(x,y)$ 由方程 $F(x+zy^{-1}, y+zx^{-1}) = 0$ 所确定. 证明
$$x \frac{\partial z}{\partial x} + y \frac{\partial z}{\partial y} = z - xy.$$

</div>

<div class="pbox">

$$
\begin{gathered}

dF=F_xdx+F_ydy+F_zdz
 \\ 
\implies (F_1-\dfrac{z}{x^2} F_2)dx+(F_2-\dfrac{z}{y^2} F_1)dy+(F_1\dfrac{1}{y} +F_2\dfrac{1}{x})dz=0 \\
dx=0 \implies z_y=-\dfrac{F_2-\dfrac{zF_1}{y^2} }{\dfrac{F_1}{y} +\dfrac{F_2}{x} }  \\
dy=0 \implies z_x=-\dfrac{F_1-\dfrac{zF_2}{x^2} }{\dfrac{F_2}{x} +\dfrac{F_1}{y} }
\end{gathered}
$$

代入化简得$z-xy=xz_x+yz_y$.

</div>

### T2

<div class="cbox">

**7.** 设函数 $z = z(x,y)$ 由方程 $\frac{x}{z} = \varphi\left(\frac{y}{z}\right)$ 所确定, 其中 $\varphi$ 具有连续的二阶导数. 证明
$$\frac{\partial^2 z}{\partial x^2} \frac{\partial^2 z}{\partial y^2} = \left(\frac{\partial^2 z}{\partial x \partial y}\right)^2.$$

</div>

<div class="pbox">

$$
\begin{gathered}
F(x,y,z)=\varphi(\dfrac{y}{z} )-\dfrac{x}{z} =0 \\
F_z=-\varphi'(\dfrac{y}{z} )\dfrac{y}{z^2}+\dfrac{x}{z^2}  \\
z_x=-\dfrac{F_x}{F_z} = \dfrac{1}{zF_z},z_y=\dfrac{-F_y}{F_z} =\dfrac{-\varphi'(\dfrac yz)}{zF_z} \\
\implies xz_x+yz_y=\dfrac{x-y\varphi'(\dfrac{y}{z})}{zF_z} =z \\
\implies \begin{cases}
z_x+xz_{xx}+yz_{yx}=z_x \\
xz_{xy}+z_y+yz_{yy}=z_y
\end{cases} \\
\implies \begin{cases}
xz_{xx}=-yz_{xy} \\
yz_{yy}=-xz_{xy}
\end{cases} \\
\begin{bmatrix} z_{xx} &z_{xy}\\z_{xy}&z_{yy} \end{bmatrix} \begin{bmatrix} x\\y \end{bmatrix} =0 \\
\implies \det \begin{bmatrix} z_{xx} &z_{xy}\\z_{xy}&z_{yy} \end{bmatrix} \\
=z_{xx}z_{yy}-z_{xy}^2=0
\end{gathered}
$$

</div>

### T3

<div class="cbox">

**8.** 设方程 $F(x+y+z, x^2+y^2+z^2) = 0$ 确定函数 $z = z(x,y)$, 其中 $F$ 具有二阶连续的偏导数, 求 $\frac{\partial^2 z}{\partial x \partial y}$.

</div>

<div class="pbox">

$$
\begin{gathered}
F(x+y+z,x^2+y^2+z^2)=0 \\
z_x=-\dfrac{-F_x}{F_z} =-\dfrac{F_1+2xF_2}{F_1+2zF_2}  \\
z_y=-\dfrac{F_1+2yF_2}{F_1+2zF_2}  \\
(F_1+2zF_2)^2z_{xy}=-(F_1+2zF_2)(F_{11}(1+z_y)+F_{12}(2y+2zz_y)+ \\
2xF_{21}(1+z_y)+2xF_{22}(2y+2zz_y)) \\ 
+(F_1+2xF_2)(F_{11}(1+z_y)+F_{12}(2y+2zz_y)+ \\
2z_yF_2+2zF_{21}(1+z_y)+2zF_{22}(2y+2zz_y))
\end{gathered}
$$
经过漫长的展开化简

$$
\begin{gathered}
z_{xy} = -\frac{4(z-x)(z-y)(F_{11}F_2^2 - 2F_{12}F_1F_2 + F_{22}F_1^2) + 2F_2(F_1+2xF_2)(F_1+2yF_2)}{(F_1+2zF_2)^3}
\end{gathered}
$$

</div>

### T4

<div class="cbox">

**10.** 求下列方程组所确定隐函数的导数或偏导数:
(1) $\begin{cases} z = x^2 + y^2, \\ x^2 + 2y^2 + 3z^2 = 20, \end{cases}$ 求 $\frac{dy}{dx}, \frac{dz}{dx}$;

</div>

<div class="pbox">

$$
\begin{gathered}
\begin{cases}
z_x=2x+2yy_x \\
2x+4yy_x+6zz_x=20
\end{cases}
\implies \begin{cases}
z_x=\dfrac{x}{1+3z}  \\
y_x=-\dfrac{x(1+6z)}{2y(1+3z)} 
\end{cases}
\end{gathered}
$$

</div>

### T5

<div class="cbox">

**10.** 求下列方程组所确定隐函数的导数或偏导数:
(2) $\begin{cases} u = f(ux, v+y), \\ v = g(u-x, v^2y), \end{cases}$ 其中 $f,g$ 具有一阶连续偏导数, 求 $\frac{\partial u}{\partial x}, \frac{\partial v}{\partial x}$;

</div>

<div class="pbox">

$$
\begin{gathered}
\begin{cases}
u_x= (xu_x+u)f_1+v_xf_2 \\
v_x=(u_x-1)g_1+(2yvv_x)g_2
\end{cases} \\
\implies \begin{cases}
u_x=-\dfrac{f_2g_1+2yvg_2f_1u-f_1u}{2xyvf_1g_2-xf_1-2yvg_2+1-f_2g_1}  \\
v_x=\dfrac{xf_1g_1-g_1+f_1g_1u}{2xyvf_1g_2-xf_1-2yvg_2+1-f_2g_1} 
\end{cases}
\end{gathered}
$$

</div>

### T6

<div class="cbox">

**11.** 设 $y = f(x,t)$, 而 $t$ 是由方程 $F(x,y,t) = 0$ 所确定关于 $x,y$ 的函数, 其中 $f,F$ 均有一阶连续的偏导数, 求 $\frac{dy}{dx}$.

</div>

<div class="pbox">

$$
\begin{gathered}
\begin{cases}
y=f(x,t) \\
F(x,y,t)=0
\end{cases} \\
\implies \begin{cases}
y_x=f_1+f_2t_x \\
F_1+F_2y_x+F_3t_x=0
\end{cases} \\
\implies y_x=\dfrac{F_3f_1-F_1f_2}{F_3+F_2f_2} 
\end{gathered}
$$

</div>

### T7

<div class="cbox">

**12.** 设 $u = f(x,y,z), \varphi(x^2, e^y, z) = 0, y = \sin x$, 其中 $f,\varphi$ 具有一阶连续的偏导数, 且 $\frac{\partial \varphi}{\partial z} \neq 0$, 求 $\frac{du}{dx}$.

</div>

<div class="pbox">

$$
\begin{gathered}
\begin{cases}
u=f(x,y,z) \\
\varphi(x^2,e^y,z)=0 \\
y=\sin x
\end{cases} \\
\implies \begin{cases}
u_x=f_1+f_2y_x+f_3z_x \\
2x\varphi_1+e^yy_x\varphi_2+z_x\varphi_3=0 \\
y_x=\cos x
\end{cases} \\
\implies u_x=f_1+f_2\cos x-\dfrac{2x\varphi_1+e^y\cos x\varphi_2}{\varphi_3}f_3 


\end{gathered}
$$

</div>

### T8

<div class="cbox">

**13.** 设函数 $z = f(x,y)$ 具有二阶连续偏导数, 且 $\frac{\partial z}{\partial y} \neq 0$. 证明对函数的值域内任意给定的值 $C, f(x,y) = C$ 为直线的充分必要条件是
$$(z_y)^2 z_{xx} - 2z_x z_y z_{xy} + (z_x)^2 z_{yy} = 0.$$

</div>

<div class="pbox">

因为$z_y=f_y\ne 0$,故设$F(x,y,C)=f(x,y)-C=0,F_2=f_2\ne 0$,可看作$F(x,y,C)$确定了$y$是关于$x,C$的隐函数$y(C,z)$.

题目原式实际为:

$$
\begin{gathered}
(f_2)^2 f_{11} - 2f_1 f_2 f_{12} + (f_1)^2 f_{22} = 0
\end{gathered}
$$

考虑

$$
\begin{gathered}
y_x=-\dfrac{F_2}{F_1}  \\
=-\dfrac{f_1}{f_2}  \\
y_{xx}=-\dfrac{(f_{11}+f_{12}y_x)f_2-f_1(f_{21}+f_{22}y_x)}{f_2^2}  \\
=-\dfrac{1}{f_2^2} (f_{11}f_2-f_1f_{12}-f_1f_{21}+\dfrac{f_22f_1}{f_2} ) \\
=-\dfrac{1}{f_2^3} (f_{11}f_2^2-2f_1f_2f_{12}+f_1^2f_{22})
\end{gathered}
$$

故原式为$0$等价于$y_{xx}=0$等价于是直线.

</div>

### T9

<div class="cbox">

**4.** 在曲线 $x=t, y=t^2, z=t^3$ 上求一点, 使曲线在此点的切线平行于平面 $x+2y+z=4$.

</div>

<div class="pbox">

平面法向量为$[1,2,1]$,切线向量$[1,2t,3t^2]$,则平行即:

$$
\begin{gathered}
[1,2,1]\cdot [1,2t,3t^2]=0 \\
\implies t=-1,-\dfrac13
\end{gathered}
$$

故点为$[-1,1,-1]$或$[-\dfrac13,\dfrac19,-\dfrac1{27}]$.

</div>

### T10

<div class="cbox">

**5.** 求函数 $u = \frac{x}{\sqrt{x^2+y^2+z^2}}$ 在点 $M(1,2,-2)$ 沿曲线 $x=t, y=2t^2, z=-2t^4$ 在此点的切线方向上的方向导数.

</div>

<div class="pbox">

切线方向向量$v=[1,4t,-8t^3]|_{t=1}=[1,4,-8]$,方向导数即:

$$
\begin{gathered}
\dfrac{1}{\|v\|} u(1+t,2+4t,-2-8t)'|_{t=0} \\
=\dfrac{1}{\|v\|} (u_x+4u_y-8u_z)|_{t=0} \\
=-\dfrac{16}{27} \cdot \|v\| \\
=-\dfrac{16}{243} 
\end{gathered}
$$

</div>

### T11

<div class="cbox">

**7.** 设 $f(u,v)$ 可微, 证明曲面 $f(ax-bz, ay-cz) = 0$ 上任一点的切平面都与某一定直线平行, 其中 $a,b,c$ 是不同时为零的常数.

</div>

<div class="pbox">

设$F(x,y,z)=f(ax-bz,ay-cz)$,则曲面法向量即:

$$
\begin{gathered}
\vec n=\nabla F=[f_1a,f_2a,-bf_1-cf_2]
\end{gathered}
$$

故
$$
\begin{gathered}
\vec n\cdot [b,c,a]=0
\end{gathered}
$$

故切面与直线$\{ t(b,c,a)|t\in R \}$平行.

</div>

### T12

<div class="cbox">

**8.** 设函数 $f(u,v)$ 可微, 证明曲面 $f\left(\frac{y-b}{x-a}, \frac{z-c}{x-a}\right) = 0$ 上任一点的切平面都过一定点.

</div>

<div class="pbox">

$$
\begin{gathered}
\text{let } F(x,y,z)=f(\dfrac{y-b}{x-a} ,\dfrac{z-c}{x-a} ) \\
\vec n=\nabla F=[-\dfrac{f_1(y-b)+f_2(z-c)}{(x-a)^2},\dfrac{f_1}{x-a} ,\dfrac{f_2}{x-a} ] \\
\vec n\cdot ((a,b,c)-(x,y,z)) \\
=-\dfrac{f_1(y-b)+f_2(z-c)}{(x-a)^2} (a-x)+\dfrac{f_1}{x-a} (b-y)+\dfrac{f_2}{x-a} (c-z) \\
=0
\end{gathered}
$$

故横过$(a,b,c)$

</div>

### T13

<div class="cbox">

**9.** 求曲面 $x^2 + 2y^2 + 3z^2 = 21$ 的平行于平面 $x+4y+6z=0$ 的所有切平面.

</div>

<div class="pbox">

平面$x+4y+6z=0$法向量为$[1,4,6]$,曲面的切平面法向量即$[2x,4y,6z]$.

$$
\begin{gathered}
\begin{cases}
2x=k \\
4y=4k \\
6z=6k \\
x^2+2y^2+3z^2=21
\end{cases} \\
\implies \begin{cases}
k=2 \\
x=1 \\
y=2 \\
z=2
\end{cases}
,\begin{cases}
k=-2 \\
x=-1 \\
y=-2 \\
z=-2
\end{cases}
\end{gathered}
$$

代入得两个平面分别为$2x+8y+12z=62,-2x-8y-12z=-62$.

</div>

### T14

<div class="cbox">

**10.** 证明: 曲面 $xyz = a^3 (a>0)$ 上任意一点的切平面与三个坐标面围成的四面体的体积是 $\frac{9}{2} a^3$.

</div>

<div class="pbox">

任取一点其切平面显然是

$$
\begin{gathered}
(\vec p-[x,y,z])\cdot [yz,xz,xy]=0 \\
\iff \vec p\cdot [yz,xz,xy]=3xyz=3a^3
\end{gathered}
$$

显然该平面上存在点$(3x,0,0),(0,3y,0),(0,0,3z)$,为这个四面体的三个顶点.最后一个顶点是$(0,0,0)$.

故体积为

$$
\begin{gathered}
\dfrac{1}{3} (\dfrac{1}{2} 3x\cdot 3z) 3z \\
=\dfrac{29}{2} xyz \\
=\dfrac{29}{2} a^3
\end{gathered}
$$

</div>
