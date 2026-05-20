---
title: Math Analysis Homework - Sem 2 Week 10
tags:
  - homework
  - math
  - math-analysis
status: published
password: sdfsdkfjaljasdjlfjskdajflasdjf.kasdjfldasfdasdf
top: 0
date: '2026-05-18T15:53:23.627Z'
---

# Math Analysis Homework - Sem 2 Week 10

## Class 1

### T1

<div class="cbox">

15. (1) 求表面积固定而体积最大的长方体; (2) 求体积固定而表面积最小的长方体.

</div>

<div class="pbox">

(1):

设边长分别为$a,b,c$,即求:

$$
\begin{gathered}
\max abc \\
\ s.t.\ 
2ab+2bc+2ac=S
\end{gathered}
$$

从而设$F(a,b,c,\lambda)=abc-\lambda(ab+bc+ac)$,根据拉格朗日条件:

$$
\begin{gathered}
\begin{cases}
F_x=bc-\lambda(b+c)=0 \\
F_y=ab-\lambda(a+b)=0 \\
F_z=ac-\lambda(a+c)=0 \\
2ab+2bc+2ac=S
\end{cases} \\
\implies \begin{cases}
a=b=c=\sqrt{\dfrac{S}{6} } \\
\lambda=\dfrac{\sqrt{6S}}{12} 
\end{cases}
\end{gathered}
$$

故表面积恒定时,正方体体积最大为$\dfrac{\sqrt 6 S^{\frac32}}{36}$.

由上面我们知道:

$$
\begin{gathered}
V\le \dfrac{\sqrt 6 S^\frac32}{36} 
\end{gathered}
$$

从而解的

$$
\begin{gathered}
S\ge 6V^\frac23
\end{gathered}
$$

也当正方体取等.

</div>

### T2

<div class="cbox">

16. 求椭圆 $x^2 + 3y^2 = 12$ 的内接等腰三角形, 使其底边平行于椭圆的长轴, 且面积最大.

</div>

<div class="pbox">

由对称性,设底边为$(x,y),(-x,y)$,不妨设$y<0,x>0$,则顶点为$(0,2)$,即求:

$$
\begin{gathered}
\max \dfrac{1}{2} 2x \cdot (2-y) \\
\ s.t.\ 
x^2+3y^2=12
\end{gathered}
$$

从而设$F(x,y,\lambda)=x(2-y)-\lambda (x^2+3y^2)$,即求:

$$
\begin{gathered}
\begin{cases}
F_x=2-y-2\lambda x=0 \\
F_y=-x-6\lambda y=0 \\
x^2+3y^2=12
\end{cases}
\end{gathered}
$$

(舍去不合法解)解得:

$$
\begin{gathered}
\begin{cases}
y=-1 \\
x=3 \\
\lambda=\dfrac12
\end{cases}
\end{gathered}
$$

从而该三角形为$(3,-1),(-3,-1),(0,2)$,面积为$9$.

</div>

### T3

<div class="cbox">

17. 在抛物线 $y^2 = 4x$ 上求一点, 使该点与直线 $x - y + 4 = 0$ 的距离最近.

</div>

<div class="pbox">

这个实在没必要拉格朗日了()

即求:

$$
\begin{gathered}
\min \dfrac{|\dfrac {y^2}4-y+4|}{\sqrt{1^2+1^2}} 
\end{gathered}
$$

因为$\dfrac{y^2}4-y+4\ge 3$,当$y=2$时取等.

故距离最近的点为$(1,2)$,距离为$\dfrac{3\sqrt 2}{2}$.

</div>

### T4

<div class="cbox">

18. 求函数 $f(x, y, z) = x^3 + y^3 + z^3 - 2xyz$ 在 $x^2 + y^2 + z^2 \leqslant 1$ 上的最大值和最小值.

</div>

<div class="pbox">

设$F(x, y, z) = x^3 + y^3 + z^3 - 2xyz - \lambda(x^2 + y^2 + z^2 - 1)$:

$$
\begin{gathered}
\begin{cases}
F_x = 3x^2 - 2yz - 2\lambda x = 0 \\
F_y = 3y^2 - 2xz - 2\lambda y = 0 \\
F_z = 3z^2 - 2xy - 2\lambda z = 0 \\
x^2 + y^2 + z^2 = 1 \\
\end{cases} \\
\end{gathered}
$$

解得

$$
\begin{gathered}
(x,y,z) \in \left\{ (\pm 1, 0, 0), \pm\left(\frac{\sqrt{3}}{3}, \frac{\sqrt{3}}{3}, \frac{\sqrt{3}}{3}\right), \pm\left(\frac{5}{3\sqrt{6}}, \frac{5}{3\sqrt{6}}, -\frac{2}{3\sqrt{6}}\right) \right\} \text{and other permutations}
\end{gathered}
$$

从而最大值和最小值分别为

$$
\begin{gathered}
1, -1
\end{gathered}
$$

</div>

### T5

<div class="cbox">

19. 设 $a_1, a_2, \cdots, a_n$ 为已知的 $n$ 个正数, 求函数 
$$f(x_1, x_2, \cdots, x_n) = \sum_{k=1}^n a_k x_k$$ 
在 $x_1^2 + x_2^2 + \cdots + x_n^2 \leqslant 1$ 上的最大值.

</div>

<div class="pbox">


显然令$x_i=[i=1]$即知最大值为正数.那么显然$x_i'=1/\|x\| x_i,f(x_i')\ge f(x_i)$即知取最大值时限制不等式一定取等.

设$F(x_1,\ldots,x_n)=f(x_1,\ldots,x_n)+\sum _{i = 1} ^{n}  \lambda x_i^2$:

$$
\begin{gathered}
\begin{cases}
F_{x_i}=a_i+2\lambda x_i=0 \\
\sum _{i = 1} ^{n}  x_i^2= 1 \\
\end{cases} \\
\end{gathered}
$$

解得

$$
\begin{gathered}
x_i=\dfrac{a_i}{\sqrt{\sum_i a_i^2}} 
\end{gathered}
$$

从而最大为

$$
\begin{gathered}
\sqrt{\sum _{i = 1} ^{n}  a_i^2}
\end{gathered}
$$

</div>

### T6

<div class="cbox">

20. 求函数 
$$f(x_1, x_2, \cdots, x_n) = x_1^2 + x_2^2 + \cdots + x_n^2$$ 
在约束条件 $\sum_{k=1}^n a_k x_k = 1$ ($a_k > 0, k = 1, 2, \cdots, n$) 下的最小值.

</div>

<div class="pbox">

由第19题,我们可以知道,$\sum_i a_ix_i\le \sqrt{\sum _{i = 1} ^{n}  x_i^2}\sqrt{\sum _{i = 1} ^{n}  a_i^2}$.

从而有

$$
\begin{gathered}
\sqrt{\sum _{i = 1} ^{n}  x_i^2} \ge \dfrac{\sqrt{\sum _{i = 1} ^{n}  a_i^2}}{ (\sum_i a_ix_i) }\\
=\sqrt{\sum _{i = 1} ^{n}  a_i^2}
\end{gathered}
$$

仍然是当$x_i=\dfrac{a_i}{\sqrt{\sum _{i = 1} ^{n}  a_i^2}} $时取等


</div>

### T7

<div class="cbox">

2. 设 $D$ 为 $\mathbb{R}^2$ 上可求面积的有界区域, 函数 $f(x, y)$ 在 $D$ 上可积. 证明: $f(x, y)$ 在 $D$ 上有界.

</div>

<div class="pbox">

反证,假设无界.

因为可积等价于任意划分网格后,对任意$\epsilon$,存在$\delta$使得若任意网格直径$|\Delta_{i,j}|<\delta$,则

$$
\begin{gathered}
S=\sum _{i = 1} ^{n}  \sum _{j = 1} ^{m}  |w(\Delta_{i,j})|\operatorname{Area}(\Delta_{i,j})<\epsilon
\end{gathered}
$$

但因为$f$无界,则至少存在一个格子内是无界的,则该格子内存在$|f(x_0)|>\dfrac{\epsilon}{\operatorname{Area}(\Delta_{i,j})}+|f(\xi)|$,其中$\xi$任取,则$w(\Delta_{i,j})=\sup_{x,y\in \Delta_{i,j}}|f(x)-f(y)| >\dfrac{\epsilon}{\operatorname{Area}(\Delta_{i,j})}$,$S>\epsilon$.矛盾,故$f(x,y)$有界.

</div>

### T8

<div class="cbox">

4. 设有界非负函数 $f$ 在区域 $D$ 上可积, 证明: $\iint_D f(x, y) \mathrm{d}x \mathrm{d}y = 0$ 的充分必要条件是 $f$ 在其连续点处函数值均为零.

</div>

<div class="pbox">

$\implies$:假设存在一点$x_0$满足$f$在$x_0$连续且$|f(x_0)|>0$,则存在$x_0$的邻域开球$U=B(x_0,r)$满足$\forall x\in U,f(x)>\dfrac{f(x_0)}2$,从而$\iint_D f(x,y)dxdy\ge \iint_U f(x,y)dxdy>\pi r^2 \dfrac{f(x_0)}{2}>0$,矛盾,故不存在函数值不为$0$的连续点.

$\impliedby$:假设任意连续点处函数值均为$0$,因为可积保证它的不连续点集勒贝格测度为$0$,所以对任意$n\times m$的网格划分上求和

$$
\begin{gathered}
\sum _{i = 1} ^{n}  \sum _{j = 1} ^{m} f(\xi_{i,j})\operatorname{Area}(\Delta_{i,j})
\end{gathered}
$$

中的任意$i,j$,存在$\xi_{i,j}$是$f$的连续点,则该和式为$0$.且可以找一列网格直径趋近于$0$的网格列,每个和式都为$0$,故积分值为$0$.

</div>

## Class 2

### T1

<div class="cbox">

**1.** 设函数 $f$ 定义在 $A = [0, 1] \times [0, 1]$ 上且
$$f(x, y) = \begin{cases} 1, & x \notin \mathbb{Q}, \\ 2y, & x \in \mathbb{Q}, \end{cases}$$
证明: 
- (1) $f$ 在 $A$ 上不可积; 
- (2) $\int_0^1 dx \int_0^1 f(x, y)dy$ 存在, $\int_0^1 dy \int_0^1 f(x, y)dx$ 不存在.

</div>

<div class='pbox'>

(1):

对任意$n\times m$网格划分中的任一网格$\Delta_{i,j}$,若可积,因为显然任意格子中同时存在$f(x,y)=1$的点与$f(x,y)=2y$的点,有

$$
\begin{gathered}
\lim_{\max |\Delta_{i,j}| \to 0} \sum _{i = 1} ^{n}  \sum _{i = 1} ^{m} |2y-1| \operatorname{Area}(\Delta_{i,j}) \\
=0
\end{gathered}
$$

而直接平均划分就有:

$$
\begin{gathered}
=\lim_{n \to \infty}\sum_{i=1}^n\sum_{j=1}^n |\dfrac{2i}{n} -1| \dfrac{1}{n^2}  \\
> \lim_{n \to \infty}\sum_{i=\lceil\dfrac {3n}4\rceil}^n\sum_{j=1}^n \dfrac{1}{2n^2} \\
=\dfrac{1}{8} \\
>0
\end{gathered}
$$

于是不可积.

(2):

$$
\begin{gathered}
\int_0^1 dx\int_0^1 f(x,y)dy \\
=\int_0^1 ([x\in Q] +[x\notin Q]) dx \\
=\int_0^1 1 dx \\
=1
\end{gathered}
$$

积分存在.

$$
\begin{gathered}
\int_0^1 dy \int_0^1 f(x,y)dx \\
=\int_0^1 dy 1+(2y-1)\int_0^1 [x\in Q]dx
\end{gathered}
$$

内层是迪利克雷函数,不可积.

</div>

### T2

<div class="cbox">

**2.** 计算二重积分 $\iint_D e^{\max\{x^2, y^2\}} dxdy$, 其中 $D = \{(x, y) \mid 0 \le x \le 1, 0 \le y \le 1\}$.

</div>

<div class='pbox'>

由对称性,可以只计算$y<x$的部分.则原式等于:

$$
\begin{gathered}
2\int_0^1 \int_0^x e^{x^2}dydx \\
=2\int_0^1 xe^{x^2}dx \\
=e^{x^2}|_0^1 \\
=e-1
\end{gathered}
$$

</div>

### T3

<div class="cbox">

**3.** 设函数 $f(x) \in C([0, 1])$, 且设 $\int_0^1 f(x)dx = A$, 计算 $\int_0^1 dx \int_x^1 f(x)f(y)dy$.

</div>

<div class='pbox'>

$$
\begin{gathered}
2\int_0^1 dx \int_x^1 f(x)f(y)dy \\
=\int_0^1 dx\int_x^1 f(x)f(y)dy +\int_0^1 dy \int_y^1 f(y)f(x) dx \\
=\int_0^1 dx\int_x^1 f(x)f(y)dy +\int_0^1 dx \int_0^x f(y)f(x) dy \\
=\int_0^1 f(x)dx\int_0^1 f(y)dy \\
=A^2 \\
\implies \text{Ans} =\dfrac{1}{2} A^2
\end{gathered}
$$

</div>

### T4

<div class="cbox">

**4.** 计算 $\iint_D \left( \sqrt{\frac{x-c}{a}} + \sqrt{\frac{y-c}{b}} \right) dxdy$, 其中 $D$ 由曲线 $\sqrt{\frac{x-c}{a}} + \sqrt{\frac{y-c}{b}} = 1$ 和直线 $x=c, y=c$ 所围成 $(a, b, c > 0)$.

</div>

<div class='pbox'>

设$s=\sqrt{\dfrac{x-c}{a} },t=\sqrt{ \dfrac{y-c}{b}  }$.

则$ds=\dfrac{dx}{2as},dy=\dfrac{dy}{2bt} $.$x=c$即$s=0$,$y=c$即$t=0$.

原式即:

$$
\begin{gathered}
\iint_D \left( \sqrt{\frac{x-c}{a}} + \sqrt{\frac{y-c}{b}} \right) dxdy \\
=\iint_{s\ge 0,t\ge 0,s+t\le 1} (s+t)(2asds)(2btdt) \\
=4ab \int_0^1 sds(\int_0^{1-s} (t^2+st) dt) \\
=4ab \int_0^1 s(\dfrac{(1-s)^3}{3} +\dfrac{s(1-s)^2}{2} )ds \\
=4ab \int_0^1 (\dfrac{s^4}{6} -\dfrac{s^2}{2} +\dfrac{s}{3} )ds \\
=\dfrac{2}{15} ab
\end{gathered}
$$

</div>

### T5

<div class="cbox">

**5.** 计算 $\iint_{[0, 1] \times [0, e]} f(x, y)dxdy$, 其中 $f(x, y) = \begin{cases} 1, & y \le e^x, \\ 0, & y > e^x. \end{cases}$

</div>

<div class='pbox'>

$$
\begin{gathered}
\int_0^1 \int_0^e [y\le e^x]dydx \\
=\int_0^1 \int_0^{e^x}1dydx \\
=\int_0^1 e^x dx \\
=e-1
\end{gathered}
$$

</div>

### T6

<div class="cbox">

**6.** 计算 $\iint_D (x+y)dxdy$, 其中 $D$ 是由曲线 $y^2 = 2x$ 和直线 $x+y = 4, x+y = 12$ 所围成的区域.

</div>

<div class='pbox'>

$D=\{ (x,y)|x+y\ge 4,x+y\le 12,2x\ge y^2 \}$.

设$z=x+y$,则$dz\wedge dy=dx\wedge dy$,再设$F=\{(z,y),z\in [4,12],2z+1\ge (y+1)^2\}$

$$
\begin{gathered}
\iint_D (x+y)dxdy \\
=\iint_F z dzdy \\
=\int_4^{12} zdz \int_{-\sqrt{2z+1}-1}^{\sqrt{2z+1}-1} 1 dy \\
=\int_4^{12} 2z(\sqrt{2z+1})dz \\
=\int_3^5 (t^2-1) t^2dt \\
=\int_3^5 (t^4-t^2)dt \\
=\dfrac{8156}{15} 
\end{gathered}
$$

</div>
