---
title: Topo Homework - Week 13
tags:
  - topo
  - homework
  - math
status: published
top: 0
date: '2026-05-29T12:44:23.540Z'
---

# Topo Homework - Week 13

### T1

<div class="cbox">

**6.** (ER) 证明圆柱筒 $S^1 \times I$ 与默比乌斯带的基本群都同构于自由循环群, 从而它们与单位圆盘 $D^2$ 都不同胚.

</div>

<div class='pbox'>

$$
\begin{gathered}
\pi_1(S^1\times I)\cong \pi_1(S^1)\oplus \pi_1(I)={\mathbb Z}\times \{1\}={\mathbb Z}
\end{gathered}
$$

对莫比乌斯带$M$,考虑其是一个三角形其中两条边同向粘合.设三角形为$T$,被粘合的两条边是$T'$,那么存在同伦等价$r:T\to T'$和商映射$p:T\to M$:
```commutative
WzAsNCxbMCwxLCJUIl0sWzAsMCwiVCciXSxbMiwxLCJNIl0sWzIsMCwiTSciXSxbMCwyLCJwIiwyXSxbMSwzLCJwJyJdLFsyLDNdLFswLDEsInIiXSxbMSwwLCJpIiwxLHsib2Zmc2V0IjotMywic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifX19XV0=
```

商空间自然的诱导了上$M$和$M'$上的$r_*,i_*$:$r_*:=[x]\mapsto [rx],i_*:=[x]\mapsto [ix]$.可以验证是良定义的.而左侧是同伦等价的,发现左侧这个收缩可以是respect to T'的,所以对一个$H:=T\times I\to T,H:=(r\circ i \simeq_{T'} \mathrm{id})$来说,它也有一个$H':I\times M,H':=[x]\mapsto [H(x,t)]$.

从而,我们把$T$同伦等价到其被粘合的那两条边组成的$T'$后粘合得到的与莫比乌斯带同伦等价.而这样粘出来的是$S^1$,于是 $\pi_1(M)={\mathbb Z}$.

而$\pi_1(D^2)\cong \{0\}\ne {\mathbb Z}$,故不同胚.

</div>


### T2

<div class="cbox">

**10.** (MRH) 设 $X$ 是默比乌斯带, $A = \partial X, a \in A, i : A \to X$ 为含入映射. 证明:

(1) $i_* : \pi_1(A, a) \to \pi_1(X, a)$ 不是同构;

(2) 默比乌斯带不能收缩到它的边界上.

</div>

<div class='pbox'>

(1):

设$X\cong I\times I/\sim,(x\sim y \iff \exists t,\{ x,y \} =\{ (0,t),(1,1-t) \} )$.

$X$有Universal Covering Space$\tilde X\cong I\times R$,故$\pi_1(X,x_0)$唯一的对应到$I\times R$中的变换.取定$R$中$I\times [0,1]$是第$0$个sheet,则可以设把第$i$个sheet映射到第$i+c$个sheet的等价类对应$c,c\in {\mathbb Z}$.设这个映射是$T:\pi_1(X,x_0)\to {\mathbb Z}$

同理可以把 $A$中的映射到${\mathbb Z}$上,记为$S:\pi_1(A,a_0)\to {\mathbb Z}$

取$S\alpha=1$的一条路,它在$X$中的像可能是

$$
\begin{gathered}
\alpha':=t\mapsto \begin{cases}
[0,2t],t<\dfrac12 \\
[1,2t-1],t\ge \dfrac12
\end{cases}
\end{gathered}
$$

而把它原样提升到$I\times R$发现$T\alpha'=2$.从而实际上$i_*$到$\pi_1(X)$的子群$2 {\mathbb Z}$的同构,从而显然不是到$\pi_1(X)$的同构.

(2):

若可以收缩到边界上,则存在映射$r$是收缩映射,满足$r\circ i= \mathrm{id}$,则有$r_*\circ i_*= \mathrm{id}_*$,那么$r_*(i_*(1))=r_*(2)=2r_*(1)=1$,无界,从而矛盾,得证.


</div>


### T3

<div class="cbox">

**11.** (MRH) 设 $f : S^1 \to S^1$ 连续, 且 $f$ 不与恒等映射 $\text{id} : S^1 \to S^1$ 同伦. 证明存在 $x \in S^1$, 使得 $f(x) = -x$.

</div>

<div class='pbox'>

只需考虑若不存在不动点则有$f$到$\mathrm{id}$的同伦:

$$
\begin{gathered}
H(x,t)=\dfrac{tf(x)+(1-t)x}{|tf(x)+(1-t)x|} 
\end{gathered}
$$

</div>


### T4

<div class="cbox">

**12.** (MRH) 设 $D^2$ 为 2 维闭圆盘, $f : D^2 \to D^2$ 连续, 且它在 $S^1$ 上的限制是 $S^1$ 上的恒等映射. 证明 $f$ 是满射.

</div>

<div class='pbox'>

假设$f$不是满射,存在一点$x_0\notin f(D^2)$,显然$x_0\notin S^1$.$f$可以看成$f:D^2\to D^2-\{x_0\}$的映射.

则存在$r:D^2-\{x_0\}\to S^1$为收缩映射,下图交换:

```commutative
WzAsNCxbMCwwLCJEXjIiXSxbMCwyLCJTXjEiXSxbMiwyLCJTXjEiXSxbMiwwLCJEXjItXFx7eF8wXFx9Il0sWzEsMiwiXFxtYXRocm17aWR9Il0sWzEsMCwiaSIsMix7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoiYm90dG9tIn19fV0sWzAsMywiZiIsMl0sWzMsMiwiciIsMl1d
```


从而$r\circ f\circ i=\mathrm{id} \implies r_*\circ f_*\circ i_*=\mathrm{id}$,这代表$r_*\circ f_*$是满的.

但是$\pi_1(D^2)=\{1\},\pi_1(S^1)={\mathbb Z}$所以$r_*\circ f_*$一定不是满的.矛盾.得证.

</div>


### T5

<div class="cbox">

**13.** (E) 设 $r : S^1 \to S^1$ 为对径映射, 即对任意 $x \in S^1, r(x) = -x$. 证明 $r$ 同伦于恒等映射 $\text{id} : S^1 \to S^1$.

</div>

<div class='pbox'>

只需考虑

$$
\begin{gathered}
H(x,t)=e^{\pi it}x
\end{gathered}
$$

</div>


### T6

<div class="cbox">

**15.** (DRH*) 特殊线性群定义为 $SL(n, \mathbb{R}) = \{A \in \mathbb{R}^{n \times n} \mid \det A = 1\} \subset \mathbb{R}^{n \times n}$. $SL(n, \mathbb{R})$ 上采用欧氏空间 $\mathbb{R}^{n \times n}$ 的子空间拓扑. 证明它的基本群是交换群.

</div>

<div class='pbox'>

考虑任意实矩阵有$A=S\sqrt{A^TA}$,其中$S$是正交矩阵,$\sqrt{A^TA}$是对称正定矩阵.所以存在$L^TL=\sqrt{A^TA}$且$L$是下三角矩阵.(Cholesky分解).

于是令$r:A\mapsto S$,$i:S\mapsto S$,那么$r\circ i=\mathrm{id},i\circ r\simeq \mathrm{id}$(这个同伦考虑只要把$L^TL$连续的把非对角线元素都变换到$0$).所以这个空间同伦等价于$SO(n)=\{ A\in SL(n,R)|A^TA=I \} $.

这种正交矩阵对应了$S^{n-1}$上的旋转变换.那么其中的一条回路应该是连续的把$S^{n-1}$进行旋转然后转回来.我们要说明两条旋转路径的交换是同伦的.

考虑我们要说明两条路径$\alpha,\beta:I\to SO(n),\alpha(0)=\alpha(1)=\beta(0)=\beta(1)=I$,满足$\alpha\beta\simeq \beta\alpha$.

考虑我们证明其都同伦于$\gamma:I\to SO(n),\gamma:=x\mapsto \alpha(x)\beta(x)$.注意到只需要构造如下同伦:

$$
\begin{gathered}
H(x,t)=\begin{cases}
\alpha((3-3t)x)&x\in [0,\dfrac13) \\
\alpha(3tx-2t+1)\beta(3tx-t)&x\in [\dfrac13,\dfrac23) \\
\beta(-3tx+3x+3t-2)&x\in [\dfrac23,1]
\end{cases} \\ s.t.\\ 
H(\bullet,0)\simeq\alpha\beta,H(\bullet,1)\simeq \gamma
\end{gathered}
$$

同理,对$\beta\alpha$只需要交换$\alpha,\beta$再交换中间那一项的乘法顺序.也可以构造同伦.

于是得证.

</div>
