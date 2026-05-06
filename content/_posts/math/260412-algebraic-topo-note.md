---
title: Algebraic Topology Note
tags:
  - math
  - topo
  - self-study
date: '2026-04-12T12:00:00+08:00'
status: published
top: 0
---

# Algebraic Topology Note

看的是 https://dec41.user.srcf.net/notes/.

## 记号

$I$:$[0,1]$.

所有的映射不声明默认是连续的.

## Homotopy

<div class='dbox'>

同伦

有两个映射$f:X\to Y,g:X\to Y$,若存在$H:X\times I\to Y$,满足$H(x,0)=f(x),H(x,1)=g(x)$,则$f\simeq_H g$,$H$是$f,g$的同伦.我会写$H=f\simeq g$,这样能给下面那个相对集合的同伦的集合腾地方.

</div>

可以看出两个映射同伦是在说可以连续的变形过去.

<div class='dbox'>

同伦等价

若两个空间$X,Y$满足存在$f:X\to Y,g:Y\to X$满足 $f\circ g\simeq \mathrm{Id}_Y,g\circ f \simeq \mathrm{Id}_X$,则$X\simeq Y$.

</div>

如果把上面的$\simeq$变成$\cong$就变成了同胚的定义.所以相比同胚同伦更宽松一些.从几何上看你会说他允许把一一团东西压成一个点,但不允许改变洞.

脱离几何的话,它似乎应该仅是同伦的衍生概念:表面两个空间上的所有映射在只考虑同伦的情况下应该是完全相同的.但这个感觉不容易直接理解,可以考虑借助基本群吧.

<div class='dbox'>

相对于(respect to)集合的同伦

相对$f\simeq_A g$表示存在同伦$H$满足$\forall x\in A,\forall t\in I,f(x)=H(x,t)=g(x)$.

</div>

就是一部分点要求不变了

<div class='dbox'>

收缩映射:$X$到$A$的映射,满足$A$中的点映到自身.

形变收缩映射:如果有一个收缩映射,且它同伦于 $\mathrm{Id}_X$,那么这个同伦变换$H$是形变收缩映射

强形变收缩映射:如果有一个形变收缩映射,且要求那个$H$是相对于$A$的.

</div>

描述$X$如何变换到$A$.

<div class='dbox'>

可缩空间

一个空间是可缩的当且仅当它 **同伦等价** 于一个点

</div>

此时它一定可以形变收缩到一个点,但不一定强.比如AI说考虑$R^2$的一个子空间:它是x轴上$[0,1]$加上$\{(x,y)|y\in I,x\in [0,1]\cap Q\}$这样的.那么你发现他不能强形变收缩到锯齿上的点.好像还可以构造出不能强行收缩到任何点的情况.

## Fundamental Group

目的是赋予拓扑一个群结构,保证其在同伦变换下不变.群的对象是路径.

<div class='dbox'>

路径

- $a:I\to X$是$X$上的路径.$P=\{a(0),a(1)\}$是$a$的端点.

</div>

我们的讲义选择先定义$\pi_0$道路连通分支再到$\pi_1$基本群,使得你理解它们的相似性(都是空间上自然产生的一个结构,以及它们对映射的相似性)

<div class='dbox'>

道路连通分量

定义 $x\sim y \iff \exists p:I\to X,p(0)=x,p(1)=Y$.

定义 $\pi_0(X)=X/\sim,\forall x,[x]=\pi_0(x)$是$x$所在的等价类.

</div>

<div class='cbox'>

$\pi_0$诱导的映射:

对$f:X\to Y$,可以定义

$$
\begin{gathered}
\pi_0(f):\pi_0(X)\to \pi_0(Y) \\
\pi_0(f)([x])=[f(x)]
\end{gathered}
$$

**这里简写成$f^*$**

此时有性质:

- $f\simeq g \implies f^*=g^*$
- $f:A\to B,g:B\to C \implies (g\circ f)^*=g^*\circ f^*$
-  $\mathrm{Id}_X^*=\mathrm{Id}_{\pi_0(X)}$

</div>

<div class='pbox'>

首先先证明是良定义:

$$
\begin{gathered}
\forall [x]=[y], \\
\exists p:x\rightsquigarrow y \\
f\circ p \text{ is }  f(x)\rightsquigarrow f(y) \\
\implies [f(x)]=[f(y)]
\end{gathered}
$$

性质都比较显然:
- $f\simeq g \implies \forall x,p(t)=H(x,t)$是一条$Y$中的路径,于是$[f(x)]=[g(x)]$.
- 也是随便取个点$x\in A$两边都是$[g\circ f(x)]$.
- 更显然.

</div>

<div class='dbox'>

路径的更多

- $a,b$都是路径,且$a(1)=b(0)$,则 $ag=\begin{cases}a(2t),t\in [0,\frac12)\\b(2t-1),t\in [\frac12,1]\end{cases}$.
- $a^{-1}(x)=a(1-x)$.
- $a\simeq_P b$表示$a,b$相对于端点不变的同伦.可以叫路径同伦.
- $[a]$表示$a$所在的相对于端点不变的同伦的等价类.
- $c_x:I\to X,c_x(t)=x$是常路径.

</div>

你想要一个群,但大多数路径不能直接相连接(相乘),所以你直接要求它们起点和终点相同,这样相乘和逆都定义好了,则看起来就形成了个群?但这是废物群:太复杂了.你更希望它能把同伦的等价类作为元素,于是需要:

<div class='cbox'>

基本群

定义

$$
\begin{gathered}
[a][b]=[ab] \\
[a]^{-1}=[a^{-1}] \\
\end{gathered}
$$

则定义$\pi_1(X,x_0)$是由所有$x\rightsquigarrow x$的路径的同伦等价类构成的群,赋予刚才的乘法和逆.$x_0$称为基点.

</div>

<div class='pbox'>

<div class='cbox'>

$$
\begin{gathered}
[a]=[c],[b]=[d] \implies [ab]=[cd]
\end{gathered}
$$

</div>

<div class='pbox'>

存在$H_1,H_2:I\times I\to X,a\simeq_{H_1} c,b\simeq_{H_2} d$.

则

$$
\begin{gathered}
H(x,t)=\begin{cases}
H_1(x,2t),t\in [0,\dfrac12) \\
H_2(x,2t-1)\in [\dfrac12,1]
\end{cases} \\
\implies (ab)\simeq_H (cd)
\end{gathered}
$$

</div>

那么定义的第一条得证良定义.对第二条容易发现把同伦第一维也很简单反一下就完事了.

下面证是群,只需证:

- 结合律$([a][b])[c]=[a] ([b][c])$
- 单位元:$[c_x]$
- 逆元:$[a][a^{-1}]=[c_x]$

都很显然.

(实际上,**你发现单位元和逆元不光使用于群里的元素,也可以是端点不重合的**)

</div>

<div class='cbox'>

基本群诱导的映射

定义

$$
\begin{gathered}
\forall f:X\to Y \\
f^*=\pi_1(f):\pi_1(X,x_0)\to \pi_1(Y,f(x_0)) \\
\forall [p]\in \pi_1(X,x_0),f^* [p]=[f^*\circ p]
\end{gathered}
$$

类似$\pi_0$,有:
- $f,g:X\to Y,f\simeq y \implies f^*=g^*$
- $f:A\to B,g:B\to C \implies (g\circ f)^*=g^*\circ f^*$
- $\mathrm{Id}_X^*=\mathrm{Id}_{\pi_1(X,x_0)}$

</div>

三条性质的形式和$\pi_0$一模一样哦!

<div class='pbox'>

先证良定义:若$H(x,t)=p\simeq_P q$,则$f\circ H(x,t)=(f\circ p)\simeq_P (f\circ q)$.

如果$H=f\simeq g$,则$\forall p,H(p(x),t)=(f\circ p)\simeq_P (g\circ p)$,于是$f^*=g^*$.剩下两个更显然不写了.

</div>

我们定义基本群是因为我们希望它是一个同伦不变的性质.但问题是现在基本群都带着一个基点.所以我们想说明它其实是基点无关的.

<div class='cbox'>

若$X$是道路连通的,则$\pi_1(X,x_0)\cong \pi_1(X,x_1)$.

</div>

<div class='pbox'>

设存在 $u=x_0\rightsquigarrow x_1$,则设

$$
\begin{gathered}
\varphi:\pi_1(X,x_0)\to \pi_1(X,x_1) \\
\varphi(p)=[u^{-1}][p][u]
\end{gathered}
$$

若$[\varphi(p)]=[c_{x_1}]$,则$c_{x_1}=[u^{-1}][p][u]$,两边同左乘$[u]$,右乘$[u^{-1}]$即$[p]=[u] [c_{x_1}] [u^{-1}]=[c_{x_0}]$.所以是单的.

而任意$[p]\in \pi_1(X,x_1)$,显然有$\varphi([u] [p] [u^{-1}])=[p]$,于是又单又满是双射.

哦忘了同态:$\varphi(pq)=\varphi(p)\varphi(q)$,展开把$[u][u^{-1}]$显然.

</div>

所以换基点相当于把它作一个同构变换. **而且是被$[u]$共轭.**.

我们可以写$\pi_1(X)$来表示一个跟基点无关的群.

<div class='cbox'>

若$X\simeq Y$,则$\pi_1(X)\cong \pi_1(Y)$.

</div>

<div class='pbox'>

$X\simeq Y$所以 $\exists f:X\to Y,g:Y\to X,f\circ g\simeq \mathrm{Id}_Y,g\circ f\simeq \mathrm{Id}_X$.

任取$X$中的一个点$x_0$,得到

![1775982861270](@media/3a1fd9f935feaa9455acefdbb55c94fcd99df3da759854e8fe1945ff0382db79.png)

其中$u'=H(0,t),H(x,t)=\mathrm{Id}_X \simeq g\circ f$

则$\forall [p]\in \pi_1(X,x_0)$,考虑$g\circ f\circ p$和$p$的关系.

那么$H(p(x),t)=p\simeq g\circ f\circ p$,于是我们设$u_t=u'(x)|_{[0,t]}$截取前一部分,则任意$u_t H(p(x),t)) u_t^{-1}$是一条$\pi_1(X,x_0)$中的路径.于是你把它调整一下这三部分在$I$上的占比让他连续变化就有了一个同伦.一个形象的示意图:

![asdjflasdjklfjasdlfjasd.svg](@media/7f74ac1fc13314dadef9165a166272b18882ca2ecf60d6973066f6071570707f.svg)
(图中的$H$其实是$H(p(x),t)$,红线就是你构造的同伦).

于是回到基本群,你发现这证明了$[u'][p][u']^{-1}=g^*\circ f^*[p]$.那么这说明你$f^*$必须是单的,$g^*$必须是满的.

把$X,Y,f,g$颠倒一下,可以再证明$f^*$必须是满的$g^*$必须是单的,于是是双射.

同态的地方反而是显然的.于是同构.

</div>

## Covering Space

<div class='dbox'>

覆叠空间

若存在$p:\tilde X\to X$,满足 $\forall x\in X,\exists U\text{ is a neighborood of } x,p^{-1}(U)=\bigsqcup_\lambda V_\lambda$($\sqcup$表示不交并),且$\forall \lambda,p|_{V_\lambda}=(V_\lambda\cong U)$,则称$\tilde X$是$X$的覆叠空间

</div>

<div class='dbox'>

提升(Lift)

对任意$f:Y\to X$,若存在 $\tilde f:Y\to \tilde X \ s.t.\ f=p\circ \tilde f$,则$\tilde f$是$f$的一个提升.

</div>

<div class='cbox'>

对$f$的两个提升$\tilde f,\tilde f'$,集合 $S=\{ x | \tilde f(x)=\tilde f'(x) \}$是既开又闭的.

</div>

<div class='pbox'>

若$\tilde f(x)=\tilde f'(x)$,考虑$f(x)$存在邻域$U$,有$p^{-1}(U)=\bigsqcup V_\lambda$,且$\exists ! \lambda,\tilde f(x)=\tilde f'(x)\in V_\lambda$.所以$B=\tilde f^{-1}(V_\lambda)\cap \tilde f'^{-1}(V_\lambda)$中是$x$的邻域满足$\forall x'\in B,\tilde f(x')\in V_\lambda,\tilde f'(x')\in V_\lambda$.即它俩在同一片空间.但这个空间是同胚,只能$\tilde f'(x')=\tilde f(x')=p|_{V_\lambda}^{-1}f(x')$.

所以 $x\in S \implies f^{-1}(U) \subset S$,是开集.

同理,如果$x$处不相等,那么两个提升的值一定在不同的切片里,于是它的邻域也在不同的切片里,从而$Y-S$是开集,从而$S$既开又闭.

</div>

从而,如果空间是连通的,那么$S$一定是全集或空集,于是只要确定提升在一个点上的取值就能知道整个空间的取值.ai叫他提升的唯一性之类的名字.

<div class='cbox'>

路径的提升一定存在

对任意路径$f:I\to X$,存在$\tilde f:I\to \tilde X$使得$f=p\circ \tilde f$

</div>

<div class='pbox'>

考虑一个路径$f:I\to X$,若$f|_S,S\subset I$存在一个提升$\tilde f$.

考虑若$t\in S$,那么和上面提升的唯一性一样的方法:$f(t)$存在邻域$U$,$p^{-1}(U)=\bigsqcup_\lambda V_\lambda$,设$\tilde f(t)\in V_i$,则我们对$\forall t'\in f^{-1}(U)$,令$\tilde f(t')=(p|_{V_i})^{-1}(f(t'))$.然后它在每个小邻域上都是连续的可以说明$\tilde f$是连续的复合条件.

而若$t\notin S$,那么$t$也有一个小邻域$U$,使得如果$\exists t'\in U,t'\in S$,那么你可以把$t$映射到$t'$所在的那片覆盖上,所以如果$t\notin S$则$\exists t\in U,U\cap S=\varnothing$,$S$是闭集.

又因为你随便把$0$映到一个$p^{-1}(f(0))$中的东西就有$0\in S,S\ne \varnothing$,所以$S=I$,提升$\tilde f$存在.

</div>

由上面的唯一性定理,只要确定了路径的起点,那么这个提升是唯一的.

<div class='cbox'>

同伦的提升一定存在

对任意同伦$H:Y\times I\to X,H=f_0\simeq f_1,\exists \tilde f_0$,则$\exists \tilde H:Y\times I\to \tilde X \ s.t.\ H=p\circ \tilde H$.

</div>

<div class='pbox'>

上面路径的情况相当于$Y$是一个单点空间.

那么对每个点$y\in Y$,都可以定义$g_y(t)=H(y,t)$,存在$\tilde g_y$.我们希望证明$\tilde H(y,t)=\tilde g_y(t)$.

先考虑对一个$y$和$g_y$,那么对任意一个$t$,存在$g_y(t)$的邻域$U$满足$p^{-1}(U)=\bigsqcup_\lambda V_\lambda$且$\exists \lambda,\tilde g_y(t)\in V_\lambda$.则$H^{-1}(U)$是$(y,t)$的一个邻域,在这个邻域内可以定义$\tilde H_y(y,t)=(p|_{V_\lambda})^{-1}H(y,t)$.由于$y$的紧性,可以用有限个这样定义的邻域覆盖住$t$的范围$I$,使得对任意$y$,可以定义$\tilde H_y(y,t),y\in U_y$.

然后由于提升的唯一性,所以对两个$H_{y_1},H_{y_2},\forall y\in U_{y_1}\cap U_{y_2},H_{y_1}(y,0)=H_{y_2}(y,0)=f_0(y)$,所以它们在交集处一定都是相等的.可以定义整个$\tilde H(y,t)=\tilde H_{y_i}(y,t),y\in U_{y_i}$.

最后焊接引理可以说明它是连续函数.

</div>

我们定义覆叠空间是为了给基本群一个作用的对象.

<div class='dbox'>

考虑基本群$\pi_1(X,x_0)$,如果$x_0$有一个覆叠空间$\tilde X$,设$S=p^{-1}(x_0)$,那么对任意一个基本群中的元素$[p]$,定义$p$起点为$x$的提升为$\tilde p_x$(即$\tilde p_x(0)=x$),$\varphi:S\to S,\varphi=x\mapsto \tilde p_x(1)$

</div>

要验证它是良定义,我们需要证明同伦的$p,p'$导出的变换是相同的,那么这时候我们直到这个同伦也可以提升:$\tilde H=\tilde p\simeq_P \tilde p'$,这足以说明$\tilde p$和$\tilde p'$在有相同的起点的时候也有相同的终点.

我们并没有否认,可能存在不同的路径等价类对应了相同的变换.

那么我们想仔细理解这个群的结构,考虑轨道稳定子定理:

$$
\begin{gathered}
\operatorname{Orb}(x)\cong G/\operatorname{Stab}(x)
\end{gathered}
$$

那么现在$G=\pi_1(X,x_0)$,而$\operatorname{Stab}(x)$是其中作用了没用的,那么容易发现这个群是$p(\pi_1(\tilde X,\tilde x_0))$,而$\operatorname{Orb}(x)$就是$x$走一条路能去的地方.当$X$路径联通时:

<div class='bbox'>

$$
\begin{gathered}
p^{-1}(x_0)\cong \pi_1(X,x_0)/(\pi_1(p)\pi_1(\tilde X,\tilde x_0))
\end{gathered}
$$

这里不是商群而是集合意义上的等价类.因为右边不保证除的是正规子群,导致得到的不是群.

</div>

<div class='def'>

Simply Connected

$\pi_1(X)=\{1\}$则它单连通.

</div>

<div class='dbox'>

Universal Covering Space

单连通的覆叠空间.

</div>

则此时$p^{-1}(x_0)\cong \pi_1(X,x_0)$.因为固定了起点后每个$p^{-1}(x_0)$都是一个不同的同伦类走出来的.

<div class='cbox'>

在有Universal Covering Space时,$\pi_1(X,x_0)$的子群与覆叠空间一一对应.

</div>

<div class='pbox'>

首先,对任意$\tilde X$,定义$\varphi:\pi_1(\tilde X,\tilde x_0)\to \pi_1(X,x_0),\varphi=a\mapsto p\circ a$,它是同态是显然的,是单的也是显然的.于是令子群 $H=\operatorname{im} \varphi$.

那么反过来,对任意子群,如何生成其覆叠空间呢?

考虑先拿过来普遍覆叠空间$\tilde X$,$\pi_1(X,x_0)$同构于$p^{-1}(x_0)$的变换群.这个空间的$\pi_1$是只有一个元素的平凡群:因为它把所有$X$里的大量闭环都拆开的不闭环了.

现在你希望你的空间的基本群长的像$H$,那我们只要要求$H$中这些路径是闭环的,于是你通过粘合上面的覆叠空间,就把原本不是闭环的粘贴成了闭环.所以你想到定义$\tilde X/\sim_H$为你想要的空间,其中$x\sim_H y \iff \exists [h]\in H,\tilde h(0)=x,\tilde h(1)=y$.

容易验证它的基本群投影到$X$后就是子群$H$.

</div>

刚才都是在有基点的情况讨论.因为变换基点相当于把子群变成他的一个共轭子群,所以你会的得到共轭子群类与覆叠空间一一对应.

我们想知道什么时候Universal Covering Space存在.

<div class='dbox'>

locally connected: 存在一个邻域是单连通的.

semi-locally simply connected: 邻域内的一条回路在整个空间内可以同伦到常路径.

</div>

这是因为如果$X$有普遍覆叠空间$\tilde X$,那么存在一个$p:\tilde X\to X$,则对任意一点$x$,存在一个邻域$U$是和任意$V_\lambda,\lambda\in A$同胚的,而这些$V_\lambda$是$X$的子空间啊.所以这里面的路径一定可以在整个空间$\tilde X$中同伦到常路径,再把这个同伦用$p$映射下来就成了semi-locally simply connected.

所以反过来,我们会这样希望

<div class='cbox'>

Universal Covering Space存在性

semi-locally simply connected,locally path connected,path connected 则 $X$有Universal Covering Space

</div>

<div class='pbox'>

考虑Universal Covering Space表明任意一个其中的点$\tilde x$可以被唯一一个$\tilde x_0$开始的路径(不是回路)同伦等价类确定.而因为确定了起点,那么这样的路径还双射到$X$中$x_0$开始的一条路径.所以我们直接定义$\tilde X=\{[p]|p \text{ is a path in }X \}$.

然后需要给他赋予一个靠谱的拓扑.什么是开集?

不会了,AI帮忙:开集的结构太复杂,考虑拓扑基.

于是$\forall p=x_0\rightsquigarrow y,U_y \text{ is a neighborood of } y$,由条件,我们可以让$U$是semi-locally simply connected和path connected.则定义$V_p=\{[p(y\rightsquigarrow z)]|z\in U_y\}$.而拓扑基自然就是$\{ V_p \} _{[p]\in \tilde X}$.

然后你可以验证,$U$在$\tilde X$中就会被复制$\pi_1$份,实际上是$x_0\to U$的同伦类数量.且$U$对应的任意两个切片不交:否则就存在一个路径$\gamma=\alpha\beta=\omega\theta$,其中$[\alpha]\ne [\omega]$,但由刚才保证$U$ semi-locally simply connected你知道$[\beta]=[\theta]$,就矛盾了.

</div>

<div class='cbox'>

Lifting criterion

给定空间$X,Y$,映射$f:Y\to X$.$\tilde X$是$X$的覆叠空间.

$Y$路径连通,局部路径连通.

则给定起点$\tilde f(y_0)=\tilde x_0$后存在唯一$\tilde f:Y\to \tilde X$满足$f=p\circ \tilde f$当且仅当

$$
\begin{gathered}
f_*(\pi_1(Y,y_0))\subset p_* \pi_1(\tilde X,\tilde x_0)
\end{gathered}
$$

</div>

<div class='cbox'>

首先,假设$\tilde f$存在,则$f_*(\pi_1(Y,y_0))=p_*\circ {\tilde f}_*(\pi_1(Y, y_0))\subset p_*(\pi_1(\tilde X,\tilde x_0))$.是显然的.

反过来,如果已知$f_*\pi_1(Y,y_0)\subset p_*\pi_1(\tilde X,\tilde x_0)$,需要证明存在性.

则对任意一条$Y$中的路径$\alpha=y_0\rightsquigarrow y$,$f(\alpha)$有唯一的提升$\widetilde {f(\alpha)}$,那么我们定义$\tilde f(y_0)=\widetilde {f(\alpha)}(1)$.

首先证明其良定义.

我们知道不同的$X$中的路径可以被提升成终点不同的路径,具体地说$\pi_1(X,x_0)/\pi_1(\tilde X,\tilde x_0)$中的每个等价类对应了一个路径终点.

那么你要保证两条路被提升到同一终点:若又有$\beta=y_0\rightsquigarrow y$,则因为$f_*([\alpha\beta^{-1}])\in f_*(\pi_1(Y,y_0))\subset p_*\pi_1(\tilde X,\tilde x_0)$,所以这条路径被提升后的$\widetilde {(f_*(\alpha\beta^{-1}))}$在$\pi_1(\tilde X,\tilde x_0)$里相当于说回到自身,即:$\widetilde {f_*(\alpha)}(1)=\widetilde {f_*(\beta^{-1})}(0)$,反过来就是$\widetilde {f_*(\alpha)}(1)=\widetilde {f_*(\beta^{-1})}^{-1}(1)$.然后把它投影回去,你可以确信$\widetilde {f_*(\beta^{-1})}^{-1}=\widetilde {f_*(\beta)}$.于是确实到同一个终点.

</div>

<div class='cbox'>

两个覆叠空间同胚的证明

$(X,x_0)$有覆叠空间$(\tilde X_i,\tilde x_i)$,对应映射$p_i$.则

$$
\begin{gathered}
p_1\pi_1(\tilde X_1,\tilde x_1)\cong p_2\pi_1(\tilde X_2,\tilde x_2) \\
\iff \exists! h:\tilde X_1\to \tilde X_2 \text{ is homeomorphism}  \ s.t.\ 
p_1=p_2\circ h
\end{gathered}
$$

</div>

<div class='pbox'>

首先如果存在同胚那么基本群肯定相同.只要证另一边了.

反过来,假设群是同构的.最直接的证法是用刚才的提升准则:把$\tilde X_1$看成$Y$,对$p_1$使用提升准则会存在唯一$\tilde f:\tilde X_1\to \tilde X_2$满足$p_1=p_2\circ f$.然后对$\tilde X_2$和$p_2$用一次会得到$\exists !g:\tilde X_2\to \tilde X_1$满足$p_2=p_1\circ g$.

于是$p_1=p_1\circ g\circ f$,因为我们对$p_1$用提升引理提升到$X_1$得到存在唯一$\varphi$使得$p_1\circ \varphi=p_1$,而$\varphi$可以取$\mathrm{Id}$,故$g\circ f=\mathrm{Id}$.反过来$f\circ g=\mathrm{Id}$一样.于是这两个空间同胚.

</div>

最后是学完这个章节后你可以会的一个应用

<div class='cbox'>

Brouwer’s fixed point theorem(2d)

$$
\begin{gathered}
f:D^2\to D^2
\end{gathered}
$$

一定有不动点$x_0\in D^2$满足$f(x_0)=x_0$.

</div>

<div class='pbox'>

反证法.考虑如果不存在这样的$x_0$,那么对任意$x\in D^2$,可以定义$f:D^2\to S^1$把$x$映到$x,f(x)$所在直线与圆盘边界$S^1$的交点.且满足$f(S^1)=S^1$.

则设$i$为$S^1\to D^2$的含入映射,就有$f\circ i=\mathrm{Id}$.

但同时取其基本群上诱导的映射,就成了$i^*:{\mathbb Z}\to \{ 0 \},f^*:\{ 0 \} \to {\mathbb Z},f^*\circ i^*=\mathrm{Id}$,然而这是不可能的.所以矛盾.所以一定存在不动点.

</div>

## SVK

## Simplicial Complex

感觉这一节就是一些语言定义.

<div class='dbox'>

Affine Independnece

对$n$个点$\{ v_i \}$,若$\sum_i c_iv_i=0,\sum_i c_i=0$当且仅当$\forall i,c_i=0$则称这些点仿射无关.

</div>

<div class='dbox'>

n-Simplex

对$n+1$个仿射无关的点$\{ v_i \}$,$\sigma=\{ \sum_{i=0}^n c_iv_i | \sum_{i=0}^n c_i\le 1,c_i\ge 0 \} $是一个simplex.

</div>

<div class='dbox'>

Face,Boundry,Interior

若simplex $\sigma$由仿射无关点集$S$仿射张成,则任意$T\subset S$仿射张成的simplex$\sigma'$是$\sigma$的一个face.记作$\sigma'\le \sigma$.若$T\ne S$则$\sigma'<\sigma$

所有的face的并是Boundry$\partial \sigma$.Boundry的补是Interior $\operatorname{Int} \sigma$

</div>

<div class='dbox'>

Simplicial Complex

一个Simplex的集合$K=\{ \sigma_i \}_i$,要求
- 其中任意$\sigma_i,\sigma_j$满足$\sigma_i\cap \sigma_j$只能是空集或一个公共face
- $\forall \sigma_i\in K,\forall \sigma'\le \sigma_i,\sigma'\in K$.

</div>

<div class='dbox'>

Vertices,Polyhedron

一个simplicial complex$K$的polyhedron$|K|=\bigcup_{\sigma \in K}\sigma$.

一个simplicial complex$K$的所有simplex的所有顶点构成点集$V_K$.

</div>

<div class='dbox'>

Simplicial map

$f:V_K\to V_L$ 是$K$到$L$的simplicial map如果 $f$ 把simplex映到simplex.即若$S$在$K$中张成一个simplex,则$f(S)$在$L$中张成simplex.

</div>

容易注意到Simplicial map唯一确定了一个连续映射$|f|:|K|\to |L|$

$$
\begin{gathered}
\forall x\in |K|,x=\sum_{v\in V_K} c_v v \ s.t.\ 
\sum_{v\in V_K} c_v=1 \\
\text{then } |f|=x\mapsto \sum_{v\in V_K} c_v f(v)
\end{gathered}
$$

<div class='dbox'>

Star,Link

对一个$|K|$中的点$x$:

- $\operatorname{St} x=\bigcup_{\sigma\in K,x\in \sigma}\operatorname{Int}\sigma $.即所有包含这个点的simplex的内部.
- $\operatorname{Lk} x=\bigcup_{\sigma\in K,x\in \sigma,\alpha\le \sigma,x\notin \alpha} \alpha$.即所有在一个包含这个点的simplex上的面,但这个面本身不包含这个点.

</div>

感觉需要注意到$|K|$中的一个点最多在一个simplex的interior里.可以更好的理解为什么Star/Link是这样的.

<div class='dbox'>

Simplicial Approximation

$g:|K|\to |L|$是$f:|K|\to |L|$的一个simplicial approximation若$f(\operatorname{St} x)\subset St(g(x))$.

</div>

第一次见这个定义的时候感觉定义的很奇怪,但仔细看发现它长得很像连续的定义.如果你定义simplicial complex的拓扑是拓扑基是所有Star,那么这正是连续的定义.

<div class='dbox'>

Barycentric subdivision 

定义一个n-simplex $\sigma$的barycenter是$\dfrac1{n+1} \sum_{i=0}^n v_i$,记为$\overline \sigma$.

则一个simplicial complex的barycentric subdivision $K^{(1)}=\{ <\overline \sigma_1,\ldots,\overline \sigma_n> | \sigma_i< \sigma_{i+1}\} $.

定义$K^{(k)}=(K^{(k-1)})^{(1)}$.

</div>

<div class='cbox'>

$|K|=|K^{(k)}|$.

</div>

<div class='pbox'>

显然只需要证$k=1$.

你发现显然$|K^{(1)}|\le |K|$,因为$|K^{(1)}|$中的每个simplex的点集都:一定是原来一个simplex下的一串点,这些点都可以被原来那个simplex张成,所以他们张成的也可以.

反过来,考虑任意一个$|K|$中的点,要证明可以被细分后的包含.只需找到那个具体的simplex:那

</div>

<div class='pbox'>

todo

</div>



<div class='cbox'>

任何映射都有 simplicial approximation

且如果$f$在某个子集上是implicial map,则这个approximation在这个子集上等于$f$.

</div>

<div class='pbox'>

todo

</div>



## Homology

### Definitions and Related Algebra

<div class='dbox'>

Oriented simplex

对一个simplex $<v_1,\ldots v_n>$,规定其符号,且要求任意交换两个点的位置符号相反(即其符号为$(-1)^{\sigma(p)}$)

</div>



<div class='dbox'>

链群

对simplicial complex$K$,设其中所有$n$-simplex构成集合$S$并任意定向,则$C_n(K)=\{\sum_i c_s s|s\in S\}$.

</div>

<div class='dbox'>

求导映射

定义$d_n:C_n\to C_{n-1},d_n(<v_1,\ldots v_n>)=\sum_i (-1)^i <v_1,\ldots,v_{i-1},v_{i+1},\ldots v_n>$

</div>

我们发现这个求导是把一个图形映射到他的边界.





### Mayer

<div class='dbox'>

正和列

</div>

<div class='dbox'>

短正和列

正和列

```commutative
WzAsNSxbMCwwLCJidWxsZXQiXSxbMiwwLCJBX24iXSxbNCwwLCJCX24iXSxbNiwwLCJDX24iXSxbOCwwLCJidWxsZXQiXSxbMCwxXSxbMSwyLCJpIl0sWzIsMywiaiJdLFszLDRdXQ==
```

称为短正和列.

</div>

由于正和性质,$i$一定是单射,$j$是满射,且$\ker j=\operatorname{im} i$.所以从群角度我们可以写$C_n\cong B_n/A_n$.

而从空间角度,你会发现

<div class='cbox'>

$$
\begin{gathered}
C_n\cong \dfrac{(B/A)_n}{*_n} 
\end{gathered}
$$

</div>

<div class='pbox'>

直觉上,这是因为在链复形上作商就是把一些路径类压成0,而空间作商是压到一点$*$,所以你要把一个单点$*_n$的链复形除掉变成$0$.

todo

</div>

<div class='cbox'>

Snake Lemma

若链复形$A_\bullet,B_\bullet,C_\bullet$在每一层构成短正和列:

```commutative
WzAsNSxbMCwwLCJidWxsZXQiXSxbMiwwLCJBX24iXSxbNCwwLCJCX24iXSxbNiwwLCJDX24iXSxbOCwwLCJidWxsZXQiXSxbMCwxXSxbMSwyLCJpIl0sWzIsMywiaiJdLFszLDRdXQ==
```

则其同调群构成长正和列:

```commutative
WzAsOCxbMCwyLCJIX24oQSkiXSxbMiwyLCJIX24oQikiXSxbNCwyLCJIX24oQykiXSxbMCw0LCJIX3tuLTF9IChBKSJdLFsyLDQsIkhfe24tMX0gKEIpIl0sWzQsNCwiSF97bi0xfSAoQykiXSxbMCw2LCJcXGNkb3RzIl0sWzQsMCwiXFxjZG90cyJdLFswLDEsImlfKiIsMV0sWzEsMiwic18qIiwxXSxbMyw0LCJpXyoiLDFdLFs0LDUsInNfKiIsMV0sWzIsMywiXFxkZWx0YSJdLFs1LDYsIlxcZGVsdGEiXSxbNywwLCJcXGRlbHRhIl1d
```

</div>

其实我们不想要长正和列,我们希望他们的同调群也构成短正和列就太好了.然后我们发现这做不到:同调群关注的是洞,但除的时候可能产生新洞.

<div class='pbox'>

那么首要任务是构造这个$\delta$.

考虑对$H_n(C)$中一个等价类$[c]$的代表元$c$,有$c\in \ker d_n$.那么因为$s$是满射一定$\exists b,s(b)=c$.且由交换图我们知道$s_{n-1}(d_n(b))=d_n(s_n(b))=d_n(c)=0$.

所以$d_n(b)\in \ker s_{n-1}=\operatorname{im} i_{n-1}$,$\exists !a\in A_{n-1} \ s.t.\ i_{n-1}(a)=d_n(b)$.那么因为$i_{n-2}(d_{n-1}(a))=d_{n-1}(i_{n-1}(a))=d_{n-1}(d_n(b))=0$,而$i$是单射可以推出$d_{n-1}(a)=0$.于是$a$是闭链,$[a]\in H_{n-1}(A)$.

则我们令$\delta([c])=[a]$.下面首先要证明它良定义.需要证明它与选取的$b,c$无关.

假设选取了两个不一样的$b,b'$,那么由$s_n(b-b')=c-c=0$,所以$b-b'\in \ker s_n=\operatorname{im} i_n,\exists \alpha\in A_n,i_n(\alpha)=b-b'$,从而求导得$i_{n-1}(d_n(\alpha))=d(i_n(\alpha))=d(b)-d(b')=i_{n-1}(a)-i_{n-1}(a')$,$i$是单射,所以$d_n(\alpha)=a-a'$,故$a-a'\in \operatorname{im} d_{n}$,差一个高维边界,从而$[a]=[a']$.

假设选取了两个不一样的$c,c'$,那么$[c]=[c']$得$\exists d_{n+1}(\gamma)=c-c'$,则$\exists \beta\in B_{n+1},s_{n+1}(\beta)=\gamma$.于是$c'=c+d_{n+1}(\gamma)=c+d_{n+1}(s_{n+1}\beta)=c+s_n(d_{n+1}\beta)$,那么可以得到$s_n(b+d_{n+1}\beta)=c'$,从而如果选$b'=b+d_{n+1}\beta$,则有$d(b')=d(b)+d(d_{n+1}(\beta))=d(b)$,于是必然得到相同的$a$.

所以$\delta$是良定义的.接下来要证明这个长正和列确实是正和的.

在$H_n(A)$处:即证$\operatorname{im} \delta=\ker i_*$.因为$\delta$的像满足$\delta([c])=[a],i(a)=d(b)$所以容易看出$\operatorname{im} \delta\subset \ker i_*$.又因为每个$\ker i_*$中的$[a]$一定有$i_*(a)=d(b)$,于是$\delta([s(b)])=[a]$,所以$\ker i_*\subset \operatorname{im} \delta$.于是得证.

在$H_n(B)$处:即证$\operatorname{im} i_*=\ker s_*$.因为$s_*\circ i_*=(s\circ i)_*=0_*=0$,所以$\operatorname{im} i_*\subset \ker s_*$.反过来对任意$s_*(b)=0$,这代表$\exists \gamma,s(b)=d(\gamma)$,从而$\exists \beta,s(\beta)=\gamma$.这意味着$s(d(\beta))=d(s(\beta))=s(b)$,从而$s(b-d(\beta))=0$,从而$\exists i(a)=b-d(\beta)$.且因为$i(d(a))=d(i(a))=d(b-d(\beta))=d(b)-d(d(\beta))=0$,所以$[a]\in H_n(A)$.于是$i([a])=[b-d(\beta)]=[b]$,这就说明$\ker s_*\subset \operatorname{im} i_*$.

在$H_n(C)$处:即证$\operatorname{im} s_*=\ker \delta$.因为$\operatorname{im} s_*$中的$[c]$在找$\delta [c]$的过程中先拉回到$[b]\in H_n(B)$,这代表$d(b)=0$,从而找到的$i^{-1}(d(b))=0$.这说明$\operatorname{im} s_*\subset \ker \delta$.而如果$\delta [c]=[a]=0$,则我们先把$\delta$的定义写清楚:$c=s(b),i(a)=d(b)$,则$\exists \alpha,a=d(\alpha)$,于是$d(i(\alpha))=i(d(\alpha))=d(b)$,从而$d(b-i(\alpha))=0$,所以$[b-i(\alpha)]\in H_n(B)$.同时我们有$s(b-i(\alpha))=s(b)-s(i(\alpha))=s(b)=c$.从而得证$\ker \delta\subset \operatorname{im} s_*$.

于是真的是正和的.

</div>

### Homotopy invariance


### Applications

#### Sphere

#### Surfaces

### Rational Homology

#### Euler number

#### Lefschetz number
