---
password: fuckhomework
title: Topo Homework - Week 14
tags:
  - topo
  - homework
  - math
status: published
top: 0
date: '2026-06-05T10:06:44.041Z'
---

# Topo Homework - Week 14

### T1

<div class="cbox">

**16.** (M) 证明 $X \times Y$ 是可缩的当且仅当 $X$ 和 $Y$ 是可缩的.

</div>

<div class='pbox'>

是可缩的意味着$c_a\simeq \mathrm{id}$,则若$X\times Y$可缩,$c_{(x_0,y_0)}\simeq \mathrm{id}_{X\times Y}$令$p_1:X\times Y\to X,(x,y)\mapsto x,p_2:X\times Y\to Y,(x,y)\mapsto y$,则显然$\forall i\in \{ 1,2 \}, p_i c_{(x_0,y_0)}\simeq p_i\mathrm{id}_{X\times Y} \iff c_{x_0}\simeq \mathrm{id}_X,c_{y_0}\simeq \mathrm{id}_Y$,所以$X,Y$自身也是可缩的.

反之,$X,Y$可缩,$c_{x_0}\simeq \mathrm{id}_X,c_{y_0}\simeq \mathrm{id}_Y$,则$c_{x_0}\times c_{y_0}\simeq \mathrm{id}_X\times \mathrm{id}_Y$,于是成立.(令同伦$H(x,y,t)=(H_1(x,t),H_2(y,t))$即可).

</div>

### T2

<div class="cbox">

**17.** (H) 构造以下形变收缩:

(1) (ER) $\mathbb{R}^3 - \mathbb{R}^1 \to S^1$;

(2) (E) $\mathbb{R}^n - \mathbb{R}^m \to S^{n-m-1}, m < n$;

(3) (ER) $S^3 - S^1 \to S^1$;

(4) (E) $S^n - S^m \to S^{n-m-1}, m < n$;

(5) (E) $\mathbb{P}^n - \mathbb{P}^m \to \mathbb{P}^{n-m-1}, m < n$.

$\mathbb{P}^n$ 的定义参看例 6.1.3.

</div>

<div class='pbox'>

(1):不妨设$R^1$是$x=y=0$,则

$$
\begin{gathered}
H(x,y,z,t)=(t\dfrac{x}{\|(x,y)\|}+(1-t)x,t\dfrac{y}{\|(x,y)\|}+(1-t)y  ,(1-t)z)
\end{gathered}
$$

(2):

记$(x,y)\in R^n,x\in R^{n-m},y\in R^m$,挖掉的$R^m$是$(0,y)$,则

$$
\begin{gathered}
H(x,y,t)=(t\dfrac{x}{\|x\|}+(1-t)x,(1-t)y)\in S^{n-m-1}
\end{gathered}
$$

(3),(4):

$$
\begin{gathered}
S^n\cong \{ (x,y)|\|x\|^2+\|y\|^2=1,x\in R^{m+1},y\in R^{n-m}\} \\
S^m\cong \{ (x,0)|\|x\|^2=1,x\in R^{m+1},y\in R^{n-m}\}\subset S^n \\
H(x,y,t)=((1-t)x,y\sqrt{\dfrac{\|x\|^2(2t-t^2)}{1-\|x\|^2} +1})
\end{gathered}
$$

(5):

对$S^n$中两点$x,-x$,有$H(x,t)=-H(-x,t)$,故因为$P^n\cong S^n/\sim,x\sim y\iff x=-y$,故由$S^n-S^m\simeq S^{n-m-1}$知$P^n-P^m\cong (S^n-S^m)/\sim \simeq S^{n-m-1}\cong P^{n-m-1}$


</div>

### T3

<div class="cbox">

**19.** (DH) 证明具有不同根的二次复多项式的空间 $\{(p,q) \in \mathbb{C}^2 \mid z^2 + pz + q \text{ 有两个不同的根}\}$ 与圆周是同伦等价的.

</div>

<div class='pbox'>

$X=\{ (p,q)\in {\mathbb C}^2|p^2-4q\ne 0 \}\cong \{ (p,p^2-4q)|p^2-4q\ne 0 \} = \{ (a,b)|b\ne 0 \}$.

于是空间$X=C^2-C\times \{0\}$可以收缩到$S^1$:$H(x,y,t)=((1-t)x,(1-t)y+t\dfrac{y}{\|y\|} )$.故同伦等价.

</div>

### T4

<div class="cbox">

**21.** (MRH) 证明可缩空间的收缩核是可缩的.

</div>

<div class='pbox'>

$X$是可缩空间故$X$道路连通且$\forall x_0\in X,c_{x_0}\simeq \mathrm{id}_X$,设这个同伦为$H(x,t) \ s.t.\ H(x,0)=x_0,H(x,1)=x$

对$X$的任意收缩核$A$,存在连续映射$r:X\to A,r|_A=\mathrm{id}_A$和$i$是包含映射.

则取$x_0\in A\subset X$,$c_{x_0}\simeq \mathrm{id}_X$由$H'(a,t)=r(H(i(a),t))$得到.

</div>

### T5

<div class="cbox">

**23.** (ER) 证明下列结论:

(1) 连通空间的收缩核仍然是连通的;

(2) 紧空间的收缩核仍然是紧的;

(3) 单连通空间的收缩核仍然是单连通的.

</div>

<div class='pbox'>

(1):

连通集的$r$的像是连通的.

(2):

$i\circ r$是$X\to X$上的连续映射,把紧集映到紧集,$X$紧故$i(A)$紧故$A$紧.

(3):

设有含入映射$i:A\to X$和收缩映射$r:X\to A$.

对$\pi_1(X)$,由$r\circ i=\mathrm{id}_A$知则$i_*:\pi_1(A)\to \pi_1(X),r_*:\pi_1(X)\to \pi_1(A)$满足$r_*\circ i_*=\mathrm{id}_A$,故$i_*$是单的$r_*$是满的,故$\pi_1(A)=\operatorname{im} r_*\cong \pi_1(X)/\ker r_*\le \pi_1(X)$

从而若$X$单连通对应$\pi_1(X)$平凡从而$\pi_1(A)$对应平凡.

</div>

### T6

<div class="cbox">

**35.** (DRH) 设 $T = S^1 \times S^1, a \in S^1, A = S^1 \times a \subset T$. 证明商空间 $T/A$ 与一点并空间 $S^1 \vee S^2$ 同伦等价.

</div>

<div class='pbox'>

$T/A$同胚于$S^2$粘合掉一对对径点.

考虑课上的结论:$f,g:S^0\to S^2,f\simeq g \implies S^2\cup_f D^1\simeq S^2 \cup_g D^1$.

故设球面$S^2$是$\{ (x,y,z)\in R^3|x^2+y^2+z^2=1 \},S^0=\{-1,1\}$,定义:$f(-1)=f(1)=(0,0,1)$,$g(x)=(0,0,x)$,则$S^2\cup_f D^1\cong S^2\vee S^1$,而接下来只需证$S^2\cup_g D^1\simeq T/A$.

你发现只需证空间$D^1\cup_h (S^1\times I)$当$h=h_i,h_1\simeq h_2$时同伦,这里$h:(S^1\times S^0)\to D^1$,则$D^1\cup_h (S^1\times I)=D^1\sqcup (S^1\times I)/(x\sim h(x))$.也就是粘贴两个底面的方式和原空间连接.如果这个成立的话,则取$h_1=0$,$h_2$为把一个地面映到$0$,另一个地面映到$1$,则$S^2\cup_g D^1$是$D^1\cup_{h_2} (S^1\times I)$,而$D^1\cup_{h_1}(S^1\times I)$可形变收缩到$T/A$.

最后这个证明和原来的结论方法是类似的:考虑$h_1,h_2$的同伦$H:S^1\times I\times I\to D^1$,设空间$X=D^1\sqcup (S^1\times I\times I)/(x\sim H(x))$,则其中$S^1\times I\times I$的部分可以形变收缩到边界$S^1\times I\times \{0\}$就对应了$h_1$,另一边对应$h_2$,于是两个空间都同伦等价这个大空间,故他们两个小的也同伦等价.

于是就证明完了.


</div>
