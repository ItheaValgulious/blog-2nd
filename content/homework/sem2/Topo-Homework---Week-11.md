---
title: Topo Homework - Week 11
tags:
  - topo
  - homework
  - math
status: published
top: 0
date: '2026-05-17T09:53:50.398Z'
---

# Topo Homework - Week 11

### T1

<div class="cbox">

**1.** (ER) 设 $X$ 为单连通空间, $\alpha, \beta$ 是 $X$ 中有相同起点和终点的道路. 证明 $\alpha \simeq_p \beta$.

</div>

<div class='pbox'>

$X$为单连通空间,故$\pi_1(X,\alpha(0))=\{[\alpha]\}$,$\alpha,\beta\in [\alpha]$这一个回路等价类.故$\alpha \simeq_p \beta$.

</div>

### T2

<div class="cbox">

**3.** (ER) 设 $X$ 为平凡或离散拓扑空间, $x_0 \in X$, 证明 $\pi_1(X, x_0)$ 是平凡群.

</div>

<div class='pbox'>

对平凡拓扑空间,对任意两条回路$\alpha,\beta$,$H(x,t)=\begin{cases}\alpha(x),t<1\\\beta(x),t=1\end{cases}$是合法的路径同伦.故基本群平凡.

对离散拓扑空间,$\alpha:I\to X$连续要求$\alpha$为常路径.故基本群只有常路径一个元素,平凡.

</div>

### T3

<div class="cbox">

**4.** (ERH) 设 $A \subset X$, $r: X \to A$ 和 $i: A \to X$ 分别为收缩映射与含入映射, $a \in A$. 证明 $r_* : \pi_1(X, a) \to \pi_1(A, a)$ 是满同态, $i_* : \pi_1(A, a) \to \pi_1(X, a)$ 是单同态.

</div>

<div class='pbox'>

$r$是满射,故存在$s$满足$rs=\mathrm{Id}_A$,从而$r_*s_*=\mathrm{Id}_*$,从而$r_*$是满射.

$i$是单射,故存在$j$满足$ji=\mathrm{Id}_A$,从而$j_*i_*=\mathrm{Id}_*$从而$i_*$是单射.

</div>

### T4

<div class="cbox">

**5.** (ERH) 设 $X$ 道路连通, 证明下列说法等价:

(1) $X$ 单连通;

(2) 任意的连续映射 $f: S^1 \to X$ 可以扩张到 $D^2$ (扩张是指: $S^1 = \partial D^2$, 存在连续映射 $\widetilde{f}: D^2 \to X$, 使得 $\widetilde{f}|_{\partial D^2=S^1} = f$).

</div>

<div class='pbox'>

若$X$单连通,考虑$f$是确定了$X$上的一个环,任取其上一点$x_0$,把这个环变成$x_0$为基点的回路$\alpha$,则$H=c_{x_0} \simeq_p \alpha$,于是可以构造映射:对$D^2$上任意一点$d$,与$x_0$连线交$S$于令一点$s$,则将其映为$H(s,(d-x_0)/(s-x_0))$,就得到一个$D^2$上的扩张.

反过来,先取定一个基点$x_0\in S^1$,那么任何一个回路$\alpha$都可以扩张到一个$D^2\to X$的映射,从而可以构造$H(s,t)$就是$S^1$上的$s$与$x_0$连线的$t$分点.从而构造了一个$\alpha\simeq_p c_{x_0}$的同伦.于是单连通.

</div>

### T5

<div class="cbox">

**6.** (ER) 设 $X$ 道路连通, $x_1, x_2 \in X$. 证明 $\pi_1(X, x_1)$ 是交换群当且仅当对任意两条连接 $x_1, x_2$ 的道路 $\alpha, \beta$, 有 $\alpha_\# = \beta_\#$. (参看定理 5.2.2 上面的定义.)

</div>

<div class='pbox'>

考虑两条不同的$x_1\rightsquigarrow x_2$的$\alpha,\beta$,则$\alpha_\#=\beta_\# \iff \forall a,\alpha^{-1} a\alpha\simeq_p\beta^{-1} a\beta \iff a\alpha\beta^{-1}\simeq_p \alpha\beta^{-1}a$.

从而如果$\pi_1$是交换群,一定有$\alpha\#=\beta\#$.

而如果$\alpha\#=\beta\#$,对任意$\pi_1(X,x_1)$中的元素$a,b$,因为$b\simeq \alpha \alpha^{-1} b$,从而可以拆成$b=\alpha\beta^{-1},\beta=b^{-1}\alpha$的形式.,从而$ab=ba$,$\pi_1(X,x_1)$是交换群.

</div>

### T6

<div class="cbox">

**7.** (MR) 设 $f: X \to Y$ 连续, $x_i \in X, y_i \in Y, i=0, 1$. 设 $\gamma$ 是 $X$ 中一个从 $x_0$ 到 $x_1$ 的道路. 证明下面的同态图表可交换:

$$
\begin{matrix}
\pi_1(X, x_0) & \xrightarrow{f_*} & \pi_1(Y, y_0) \\
\gamma_\# \Big\downarrow \quad & & \quad \Big\downarrow (f \circ \gamma)_\# \\
\pi_1(X, x_1) & \xrightarrow{f_*} & \pi_1(Y, y_1)
\end{matrix}
$$

</div>

<div class='pbox'>

对$\pi_1(X,x_0)$中的任意一条道路类$[\alpha]$.

走左侧是$f_*(\gamma_\# [\alpha])=[f(\gamma^{-1} \alpha\gamma)]$,走右侧是$(f\circ \gamma)_\#(f_*([\alpha]))=(f\circ \gamma)^{-1} ([f\circ \alpha]) (f\circ \gamma)=[f(\gamma^{-1}\alpha\gamma)]$,从而得证.

</div>

### T7

<div class="cbox">

**8.** (ERH) 基本群的等价定义:

满足 $f: S^1 \to X$, 使得 $f((1, 0)) = x_0$ 的所有 $f$ 组成集合 $A$. 在 $A$ 上定义等价关系: 对于 $f_1, f_2 \in A$, 如果存在同伦 $H: S^1 \times [0, 1] \to X$, 使得 $H(x, 0) = f_1(x)$, $H(x, 1) = f_2(x)$, $H((1, 0), t) = x_0, \forall t \in [0, 1]$, 则称 $f_1, f_2$ 等价, 记为 $f_1 \sim f_2$. 令 $\pi_1'(X, x_0) = A/\sim$. 在 $A$ 上定义乘法如下:

$$
f_1f_2((\cos\theta, \sin\theta)) = \begin{cases} 
f_1((\cos 2\theta, \sin 2\theta)), & \theta \in [0, \pi], \\ 
f_2((\cos 2\theta, \sin 2\theta)), & \theta \in [\pi, 2\pi]. 
\end{cases}
$$

证明 $\pi_1'(X, x_0)$ 同构于本节定义的基本群 $\pi_1(X, x_0)$.

</div>

<div class='pbox'>

对任意一条$\pi_1'(X,x_0)$的回路$\alpha:S^1\to X$,定义$\varphi(\alpha):I\to X,\varphi(\alpha)(t)=\alpha(\cos 2\pi t,\sin 2\pi t)$.

直接代入展开即得$\varphi(\alpha\beta)(t)=\begin{cases}\alpha(\cos2\pi t,\sin 2\pi t),t<\dfrac12\\\beta(\cos2\pi t,\sin 2\pi t),t\ge \dfrac12\end{cases}=\varphi(\alpha)\varphi(\beta)$,是同态.

同时因为只有$\varphi(s\mapsto x_0)=c_{x_0}$,故是单射.因为对任意$p:I\to X,p(0)=p(1)$,令$\pi$为$I/\{0,1\}$的商映射,令$\alpha(\pi x)=p(x)$.若$\pi(x_1)=\pi(x_2),x_1\ne x_2$,则一定是$\{ x_1,x_2 \} =\{ 0,1 \}$,从而$p(x_1)=p(x_2)$,而我们知道商映射是满的且像空间的开集一定有开集原像,所以是良定义且连续.而$\varphi(\alpha)=p$所以是满的,所以是同构.

</div>
