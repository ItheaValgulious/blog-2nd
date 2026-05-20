---
title: Topo Homework - Week 8
tags:
  - topo
  - homework
  - math
status: published
top: 0
date: '2026-04-24T15:25:49.351Z'
---

# Topo Homework - Week 8

### T1

<div class="cbox">

**11.** (MRH) 用极坐标 $(r, \theta)$ 表示平面上的点 $P$, 其中 $r$ 表示点 $P$ 到原点的距离, $\theta$ 表示从原点出发过点 $P$ 的射线与 $x$ 轴正向的夹角. 设
$$A = \left\{ \left( \frac{\theta}{\theta+1}, \theta \right) \bigg| \theta \in (0, \infty) \right\} \subset \mathbb{R}^2, \quad W = A \cup S^1,$$
称 $W$ 是欧氏平面 $\mathbb{R}^2$ 的拓扑涡流线. 证明 $W$ 是连通的, 但不是道路连通的.

</div>

<div class="pbox">

$W$连通:任意$S^1$上一点$(1,\theta)$都是$A$中点列$\{ (\dfrac{\theta+2\pi n}{\theta+2\pi n+1} ,\theta+2\pi n) \}_n$的极限,从而$S^1\subset A'$.同时考虑:$S^1$以内,$S^1$以外的任意点都可以简单验证存在开球邻域与$A$不交,从而不在闭包里.于是$\operatorname{Cl}A=A\cup A'=A\cup S^1=W$连通.

不道路连通:反证,存在道路$f:I\to W,f(0)\in S^1,f(1)\in A$.设$t=\sup f^{-1}(S^1)$.因为$S^1$闭从而$f(t)\in S^1$.因为$f\in C$,故 $\lim_{x \to t^+} f(x)=f(t)$.那么$R=(r,\theta)\mapsto r$连续得到$\lim_{x \to t^+} R(f(x))=R(f(t))=1$.但如果设$X=(r,\theta)\mapsto r\cos\theta$是$R^2$上连续函数,则理应有$\lim_{x \to t^+} X(f(x))=X(f(t))$.可是因为对$W$上的点有$X=R\cos\dfrac{R}{1-R}$,而$R\to 1$的时候$X$的极限不存在,就出现了矛盾.从而不道路连通.

</div>

### T2

<div class="cbox">

**16.** (MRH) 设 $X$ 为一个拓扑空间, $A$ 和 $B$ 都是 $X$ 的闭子集 (或开子集), 且 $A \cup B$ 和 $A \cap B$ 都是道路连通的.
- (1) 证明 $A$ 和 $B$ 也是道路连通的;
- (2) $\forall a \in A, b \in B$, 以及 $A \cup B$ 中任何一条连接 $a$ 和 $b$ 的道路 $\alpha$, 证明 $\alpha$ 必经过 $A \cap B$ 中的点.

</div>

<div class="pbox">

为什么感觉两问顺序反了.

(2):

假设存在一条$\alpha=a\rightsquigarrow b$,则$\alpha:I\to A\cup B$连续.那么$\alpha^{-1}(A),\alpha^{-1}(B)$都是闭集(或开集).且因$\operatorname{im}\alpha\cap A\cap B=\varnothing$,故$\alpha^{-1}(A)\cap \alpha^{-1}(B)=\varnothing$.同时$\alpha^{-1}(A)\cup \alpha^{-1}(B)=I$且都不为空,则$I$不连通.但我们知道$I$连通.矛盾.故$\alpha$一定经过$A\cap B$的点.

(1):

下证$A$道路连通.

那么因为$A\cap B$道路连通.故$\forall a,b\in A,\exists \alpha:I\to A\cup B \ s.t.\ \alpha(0)=a,\alpha(1)=b$.如果$\operatorname{im} \alpha\subset A$就之间结束了.

否则$\operatorname{im} \alpha\cap B\ne \varnothing$.那么在$A,B$都为闭集的时候,设$t_a=\inf \{ t|\alpha(t)\in A\cap B \},t_b=\sup \{ t|\alpha(t)\in A\cap B \}$.因为$A\cap B$也为闭集,所以$\alpha(t_a),\alpha(t_b)\in A\cap B$

则$\forall t_0,\alpha(t_0)\notin A$一定有$t_0\in [t_a,t_b]$,否则如果$t_0<t_a$,$a\rightsquigarrow \alpha(t_0)$这段路径不经过$A\cap B$与(1)矛盾.$t_0>t_b$同理.所以说$\beta_1=a\rightsquigarrow \alpha(t_a),\beta_2=\alpha(t_b)\rightsquigarrow b$满足$\operatorname{im} \beta_i\subset A$.最后因为$A\cap B$路径连通,存在$\beta_3:I\to A\cap B,\beta_3(0)=t_a,\beta_3(1)=t_b$.于是令$\beta=\beta_1\beta_3\beta_2$,则它是$A$中的$a\rightsquigarrow b$的路径.所以$A$道路连通.$B$道路连通同理.

当$A,B$为开集的时候,你不能直接用上下确界.考虑因为是开集,所以$A$的补集是闭集,存在一个$t_a=\min\{t|\alpha(t)\notin A\}$和$t_b=\max\{t|\alpha(t)\in A\}$.则$<t_a$处一定存在一个$A\cap B$中的点,然后你就可以一样取点了.

</div>

### T3

<div class="cbox">

**28.** (E) 证明两条相交直线的并集与一条直线不同胚.

</div>

<div class="pbox">

设存在同胚$f:R\wedge R\to R$,则$f|_{R\wedge R-\{p\}}:R\wedge R-\{p\}\to R-\{f(p)\}$也是同胚.其中$p$为两直线交点.但是$R-\{f(p)\}$有两个连通分量,而$R-\{f(p)\}$有四个.而连通分量个数是拓扑性质.矛盾.故不同胚.

</div>

### T4

<div class="cbox">

**1.** (ER) 令 $X = \{a, b, c, d, e\}$, 定义 $p: \mathbb{R} \to X$ 如下:
$$p(x) = \begin{cases} a, & x > 2, \\ b, & x = 2, \\ c, & 0 \le x < 2, \\ d, & -1 < x < 0, \\ e, & x \le -1. \end{cases}$$
- (1) 在欧氏直线 $\mathbb{R}$ 上, 列出 $X$ 上的商拓扑;
- (2) 在下极限拓扑空间 $\mathbb{R}_l$ 上, 列出 $X$ 上的商拓扑.

</div>

<div class="pbox">

(1):

$\mathcal{T}=\{ \varnothing, X, \{ a \}, \{ d \}, \{ a,d \}, \{ c,d \}, \{ a,c,d \}, \{ d,e \}, \{ a,d,e \}, \{ c,d,e \}, \{ a,c,d,e \}, \{ a,b,c,d \} \}$

(2):

$\mathcal{T}=\{ \varnothing, X, \{ a \}, \{ c \}, \{ d \}, \{ a,c \}, \{ a,d \}, \{ c,d \}, \{ a,c,d \}, \{ a,b \}, \{ a,b,c \}, \{ a,b,d \}, \{ a,b,c,d \}, \{ d,e \}, \{ a,d,e \}, \{ c,d,e \}, \{ a,c,d,e \}, \{ a,b,d,e \} \}$

</div>

### T5

<div class="cbox">

**6.** (ER) 证明 $I^2 / [(0, t) \sim (1, t), t \in I]$ 同胚于 $S^1 \times I$.

</div>

<div class="pbox">

考虑$f:S^1\times I\to I^2/\sim,f=(\theta,x)\mapsto (\dfrac{\theta}{2\pi},x)$.是连续的双射且$f^{-1}$连续.故$f$是同胚.

</div>

### T6

<div class="cbox">

**9.** (ER) 在标准 $\mathbb{R}$ 中, 对任意 $x, y \in \mathbb{R}$, 令 $x \sim y \iff x - y \in \mathbb{Q}$. 记商空间 $X = \mathbb{R} / \sim$. 证明 $X$ 中仅有的开集是空集和集合 $X$ 本身. (所以 $X$ 具有非离散拓扑.)

</div>

<div class="pbox">

设商映射:$\pi=x\mapsto [x]$,其中$[x]=\{y|y-x\in {\mathbb Q}\}$.$X$同胚于$\operatorname{im}\pi$,不妨就令$X=\operatorname{im}\pi$

那么任意开集$S\subset X$,一定有$\pi^{-1}(S)=\bigcup_{x\in T}[x]$.设$S$非平凡,则$\exists r\notin \pi^{-1}(S),[r]\cap \pi^{-1}(S)=\varnothing$.则$\forall x\in \pi^{-1}(S)$,对任意小邻域$U$,存在邻域基元素$N=(x-\epsilon,x+\epsilon)\subset U\subset \pi^{-1}(S)$.但由于$Q$的稠密性,一定存在$q\in {\mathbb Q},q\in (x-\epsilon-t,x+\epsilon-t)$,从而$\exists t+q\in [t],t+q\in N\notin \pi^{-1}(S)$,与上面$N\subset S$矛盾.

</div>

### T7

<div class="cbox">

**10.** (ER) 设 $\mathbb{R}$ 为标准直线, $X = \mathbb{R} / \mathbb{Q}$, 即 $X$ 为将 $\mathbb{R}$ 中所有有理数都捏为一个单点得到的商空间. 证明 $X$ 的单点子集 $\{\mathbb{Q}\}$ 在 $X$ 中是稠密的.

</div>

<div class="pbox">

设商映射$\pi:{\mathbb R}\to X$.

$\{{\mathbb Q}\}$稠密等价于$\operatorname{Cl}\{ {\mathbb Q} \} =X$,等价于$\operatorname{Cl}\pi({\mathbb Q})=\pi({\mathbb R})$.而其中因为${\mathbb Q}$在${\mathbb R}$稠密,故$\operatorname{Cl}(\pi(Q))=\pi(\operatorname{Cl}Q)=\pi({\mathbb R})$.所以等价回去$\{ {\mathbb Q} \}$稠密.

</div>

### T8

<div class="cbox">

**12.** (E) 设 $X$ 和 $Y$ 为拓扑空间, $\tilde{X} = X / \sim$ 和 $\tilde{Y} = Y / \approx$ 为商空间, $p: X \to \tilde{X}$ 和 $q: Y \to \tilde{Y}$ 为商映射. $f: X \to Y$ 是一个映射. 证明存在映射 $\tilde{f}: \tilde{X} \to \tilde{Y}$ 使得 $\tilde{f} \circ p = q \circ f$ 当且仅当 $\forall x_1, x_2 \in X, q(f(x_1)) = q(f(x_2)) \iff x_1 \sim x_2$.

</div>

<div class="pbox">

如果$q(f(x_1))=q(f(x_2))\iff x_1\sim x_2$:

那么直接定义$\tilde f=p(x)\mapsto q(f(x))$.由条件,$\forall p(x_1)=p(x_2) \implies  x_1\sim x_2 \implies q(f(x_1))=q(f(x_2))$,故良定义.此时显然$\tilde f\circ p=q\circ f$.因为$q,f$连续由商空间泛性质知道$\tilde f$还是连续的.

反过来,如果存在这样的$\tilde f$,那么任意$x_1\sim x_2$,有$p(x_1)=p(x_2)\implies q(f(x_1))=\tilde f(p(x_1))=\tilde f(p(x_2))=q(f(x_2))$.

</div>

### T9

<div class="cbox">

**13.** (ERH) 设 $X = I \times I$ 是欧氏平面的子空间. 定义

$$f: X \to \mathbb{R}^2, \quad (x, y) \mapsto (\cos(x+y), \sin(x+y));$$

$$p: I \times I \to S^1 \times S^1 = T^2, \quad (x, y) \mapsto (e^{2\pi x i}, e^{2\pi y i})$$

(把 $S^1$ 看成复平面 $\mathbb{C}$ 的子空间). 证明:
- (1) $p$ 是商映射;
- (2) 存在一个映射 $g: T^2 \to S^1$, 使得 $g \circ p = f$;
- (3) $g$ 连续 (利用微分几何还可以证明 $g$ 可微).
提示: 应用第 10, 11 题, 以及定理 2.3.2.

</div>

<div class="pbox">

(1):

分量连续所以$p$连续.满射显然.然后他是紧空间到T2空间的映射所以是闭映射.从而是商映射.

(2):

这是个错题啊

$p(0,0)=p(1,0)=(1,1)$.但$f(0,0)=(1,0)\ne f(1,0)=(\cos(1),\sin(1))$.那你让我证啥呢.那(3)也不对啊.

我猜是$f=(\cos(2\pi(x+y)),\sin(2\pi(x+y)))$.

则直接令$g(x,y)=(\Re xy,\Im xy)$即可.

(3):

$f$显然连续.只需要看他分量坐标在$R^2\to R^2$意义下都连续.

因为$f$是连续,所以由商空间泛性质知道$g$连续.


</div>
