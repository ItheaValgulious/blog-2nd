---
title: Topo Homework - Week 10
tags:
  - topo
  - math
  - math-analysis
status: published
top: 0
date: '2026-05-17T09:53:57.615Z'
---

# Topo Homework - Week 10

### T1

<div class="cbox">

**1. (ERH)** 判断以下多边形表示的曲面实际上是闭曲面的拓扑分类定理中的哪一个？
- (1) $acda^{-1}bc^{-1}bd$;
- (2) $abcab^{-1}dcd$;
- (3) $ab^{-1}dc^{-1}a^{-1}bcd^{-1}$;
- (4) $abca^{-1}cdeb^{-1}de$.

</div>

<div class='pbox'>

我们已经知道公式是$\dfrac{n-2(k-1)}2$或再除$2$了.下面用数字代表多边形顶点.

(1): 
首先有同向边,是不可定向的.如果记为$1a2c3d4a^{-1}5b6c^{-1}7b8d$,则可知$1,5,4,7,2$是一类,$3,6,8$是一类,故是$3 {\mathbb P}^2$.

(2):
仍然不可定向.且$1a2b3c4a5b^{-1}6d7c8d$,于是$1,4,7,8,3,6,5,2$全都是一类,故是$4 {\mathbb P}^2$.

(3):
无同向边,可定向.且$1a2b^{-1}3d4c^{-1}5a^{-1}6b7c8d^{-1}$,于是$1,6,3$是一类,所以不止一类,又因为$4|8-2(k-1)$可以看出$k=3$,是${\mathbb T}^2$.

(4):
有同向边,不可定向.$1a2b3c4a^{-1}5c6d7e8b^{-1}9d10e$.可以看出$1,5,8,3$是一类,$2,4,9,6$是一类,$7,10$是一类,故为$3 {\mathbb P}^2$

</div>

### T2

<div class="cbox">

**3. (MR)** 分别列出 $\mathbb{P}^2$、克莱因瓶 $K$ 和环面 $T^2$ 的所有六边形表示.

</div>

<div class='pbox'>

${\mathbb P}^2$:有三个点类且含同向边.那么每个点类的两个点的所连边的情况必须一致.则包括:$abcabc$.

${\mathbb K}$:有两个点类且含同向边.$abcb^{-1}a^{-1}c$, $abcabc^{-1}$

${\mathbb T}^2$:有两个点类.$abca^{-1}b^{-1}c^{-1}$, $abcb^{-1}a^{-1}c^{-1}$ 

</div>

### T3

<div class="cbox">

**7. (MRH)** 在 $T^2$ 上挖去一个圆盘的内部, 然后将洞口 (同胚于一个圆周) 的对径点黏合, 得到的新的闭曲面 $X$. $X$ 实际上是闭曲面的拓扑分类定理中的哪一个？

</div>

<div class='pbox'>

$T^2$是$aba^{-1}b^{-1}$,挖去一个洞并对径点粘合就变成$abcca^{-1}b^{-1}$,只有一个点类,所以是$3 {\mathbb P}^2$.

</div>

### T4

<div class="cbox">

**12. (DRH)** 证明: 任何一个连通的不可定向闭曲面挖去一个小开圆盘后都可以嵌入 $\mathbb{R}^3$.

</div>

<div class='pbox'>
  
首先你可以把它三角剖分.因为当不上球的时候,每个三角形不可能三条边都是边界,所以可以每次把一个有至少一条边为边界的三角形收缩映射到边界上.则进行有限次后,可以把所有三角形都通过收缩映射收缩成1/2-simplex.

从而得到一张图.通过取若干仿射无关的点,可以把这张图嵌入$R^3$.

然后把图的每个顶点用一个小圆盘代替,对每条边,根据原曲面从两个顶点对应点的路劲上走是否会扭转,决定直接粘合对应小圆盘或扭转180°后粘合两个小圆盘.且边环绕小圆盘的顺序与原曲面环绕小圆盘这条路线收缩后的顺序相同,可以得到一个新曲面.它显然是已经被嵌入${\mathbb R}^3$了.

因为原曲面只挖掉了一个洞,所以它的边界同胚于$S^1$.而在形变收缩的图上你可以用相同的方式遍历所有的边界.那么你就可以把这个洞补上.

于是因为新曲面和原曲面收缩到相同的空间,所以他们同伦等价,补上洞后会有相同的欧拉示性数.而我们粘的方式保证了定向相同,所以他们对应相同的封闭曲面,互相同胚,那么挖掉洞也同胚.于是得证.

---

另一个做法是考虑${\mathbb P}^2\# {\mathbb T}^2=3 {\mathbb P}^2$,所以$n {\mathbb P}^2=m {\mathbb T}^2\#k {\mathbb P}^2,k\le 2$.

则可以证明$k{\mathbb P}^2$挖去一个洞一定可以嵌入${\mathbb R}^3$,然后可以容易的添加若干个把手${\mathbb T}^2$.

</div>

### T5

<div class="cbox">

**1. (E)** 设 $f, g: I \to \mathbb{C} \setminus \{0\}$, $f(t) = e^{2\pi i t}$, $g(t) = e^{-2\pi i t}$, $\forall t \in I$. 证明或反驳: $f$ 与 $g$ 同伦.

</div>

<div class='pbox'>

$$
\begin{gathered}
H(x,t)=e^{2\pi i x(1-2t)}
\end{gathered}
$$

即可.

</div>

### T6

<div class="cbox">

**3. (E)** 设 $f, g: X \to Y$ 为两个不同的常值映射, $Y$ 道路连通. 证明: $f \simeq g$; $Y$ 上的任意两条道路同伦.

</div>

<div class='pbox'>

任取一条$f(0)\rightsquigarrow g(0)$的道路$\alpha$,则$H(x,t)=\alpha(t)$是$f,g$的同伦.

任意$Y$上的道路$\alpha$同伦于到其起点的常值映射,只需令$H(x,t)=\alpha(x(1-t))$.

故$\forall \alpha,\beta,\alpha\simeq c_{\alpha(0)} \simeq c_{\beta(0)} \simeq \beta$.

</div>

### T7

<div class="cbox">

**5. (M)** 设 $f, g: X \to S^n$ 连续, 满足 $\forall x \in X, |f(x) - g(x)| < 2$. 证明 $f \simeq g$.

</div>

<div class='pbox'>

即不存在$f(x)=-g(x)$.

则直接令$H(x,t)=\dfrac{tf(x)+(1-t)g(x)}{\|tf(x)+(1-t)g(x)\|}$即可.

</div>

### T8

<div class="cbox">

**6. (M)** 设 $f, g: X \to \mathbb{C} \setminus \{0\}$ 连续, 满足 $\forall x \in X, |f(x) - g(x)| < |f(x)|$. 证明 $f \simeq g$.

</div>

<div class='pbox'>

即$\forall t,|(1-t)f(x)+tg(x)|\ge |t|g(x)-f(x)|-|f(x)|| >0$,故$(1-t)f(x)+g(x)\ne 0$,令$H(x,t)=tf(x)+(1-t)g(x)$即可.

</div>
