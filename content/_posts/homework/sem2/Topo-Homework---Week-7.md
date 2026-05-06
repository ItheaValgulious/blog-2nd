---
title: Topo Homework - Week 7
tags:
  - topo
  - homework
  - math
status: published
top: 0
date: '2026-04-16T14:35:37.718Z'
---

# Topo Homework - Week 7

### T1

<div class="cbox">

14. (ER) 设映射 $f: X \to Y$, 如果 $X$ 的每个点都有一个邻域 $U$, 使得 $f$ 限制在 $U$ 上为常数, 则称 $f$ 是局部常值映射. 证明:
- (1) 任何局部常值映射都是连续的;
- (2) 连通空间上的局部常值映射是常值映射.

</div>

<div class='pbox'>

(1):

$$
\begin{gathered}
\forall V \text{ is open}  \\
\forall x\in V,\exists x\in U_x ,U_x\text{ is open},f|_{U_x}(x')=f(x) \\
\implies f^{-1}(V) \\
=\bigcup_{v\in V} f^{-1}(v) \\
=\bigcup_{v\in V} \bigcup_{ x\in f^{-1}(v) } U_x \text{ is open}  \\
\implies f(x) \text{ is continuous} 
\end{gathered}
$$

(2):

任取$x\in X$,$X$是连通空间.设$S=\{ y|f(y)=f(x) \}$.

则若$y\in S$,$\exists U_y \text{ is }y\text{'s neighborhood} \ s.t.\ \forall z\in U_y,f(z)=f(y)=f(x),z\in S,U_y\subset S$,故$S$是开集.

若$y\notin S$,同理$\exists y\in U_y\in \mathcal{T},f(U_y)=f(y)=f(x),U_y\subset S$,故$X-S$是开集.

又因为$x\in S,S\ne \varnothing$,且$X$连通,故$S=X$,$\forall y,f(y)=f(x)$

</div>

### T2

<div class="cbox">

18. (MRH) 证明:
- (1) $X$ 中任一既开又闭的连通子集都是 $X$ 的连通分支;
- (2) 如果 $X$ 只有有限个连通分支, 那么 $X$ 的每个连通分支都是既开又闭的. 举例说明如果 $X$ 有无限个连通分支, 结论未必成立.

</div>

<div class='pbox'>

(1):

若$A$即开又闭,$C$是$X$的一个连通分支,若$C\cap A\ne \varnothing$,则自然有$A\subset C$.

若$A\ne C,\exists x\in C-A$,则 $A,X-A$为交集为空,覆盖$C$的两个开集,与$C$连通矛盾.故$A=C$.则既开又闭的任意连通子集是一个连通分支.

(2):

连通分支一定是闭的:若$A$为连通集,则$\operatorname{Cl}A$也为连通集且$\operatorname{Cl}A\supset A$.

若只有有限个连通分支,因为连通分支是点的等价类,故互不相交,则$C_i=X-\bigcup_{j\ne i} C_j$,其中$\bigcup_{j\ne i} C_j$为闭集的有限并,仍为闭集,故$C_i$为开集.故任意$C_i$又开又闭.

无限反例:$Q$赋予$R$的子空间拓扑,每个点是一个连通分支,不是开的.

</div>

### T3

<div class="cbox">

22. (E) 举例说明拓扑空间的连通分支不必是开集.

</div>

<div class='pbox'>

这不和上一题的反例一样吗?$Q$上的标准拓扑.

</div>

### T4

<div class="cbox">

25. (EH) 证明康托尔三分集 (见习题 1.3 第 39 题) 是完全不连通的.

</div>

<div class='pbox'>

康托尔集等价于三进制表示下不含$1$的所有$[0,1]$之间的实数,设为$C$.

对任意非单点集$S$,设$l=\inf S,r=\sup S$,显然有$r\ne l$.

那么必然存在$i$使得$l,r$的前$i-1$位相同,第$i$位不同.则必然有$l_i=0,r_i=2$($x_i$表示$x$的三进制下第$i$位小数).

那么取$m=l+3^{-i}\in (l,r)$,则$C\cap [0,m),C\cap (m,1]$是不交且覆盖$S$的开集,$S$不连通.

故任意非单点集不连通,完全不连通.

</div>

### T5

<div class="cbox">

1. (ER) 判断 $\mathbb{R}^2$ 的下列子集是否道路连通:
- (1) $A = \{(x, y) \mid x, y \text{ 中至少有一个为有理数}\}$;
- (2) $B = \{(x, y) \mid x = 0 \text{ 或 } y \in \mathbb{Q}\}$.

</div>

<div class='pbox'>

(1):

是道路连通.

对$(x_1,y_1),(x_2,y_2)$,若$x_i\in Q,i\in \{1,2\}$或$y_i\in Q,i\in \{1,2\}$,构造路径$p(t)=(1-t)(x_1,y_1)+t(x_2,y_2)$即为$(x_1,y_1)\rightsquigarrow (x_2,y_2)$的路径.

否则若$x_i\in Q,y_{3-i}\in Q,i\in \{1,2\}$,则由上述构造,其分别有路径连通于$(x_i,y_{3-i})$.

故任意两点有路径连通,是道路连通.

(2):

是道路连通.显然$(x_1,y_1)\sim (0,y_1)\sim (0,y_2)\sim (x_2,y_2)$,其中$\sim$表示使用上述$p(t)$构造即可将两点道路连通.

</div>

### T6

<div class="cbox">

2. (ER) 设 $X$ 表示 $\mathbb{R}^3$ 中至少有一个坐标是有理数的点的集合, 证明 $X$ 是道路连通的.

</div>

<div class='pbox'>

和上面一样.仍然设$p_{a,b}(t)=tb+(1-t)a$.

不妨设$x_i^{1}\in Q$.则$p=p_{x_1,(x_1^{(1)},x_2^{(2)},x_2^{(3)})}p_{(x_1^{(1)},x_2^{(2)},x_2^{(3)}),x_2}$是$x_1\rightsquigarrow x_2$的路径.

</div>

### T7

<div class="cbox">

6. (MH) 设 $X \subset \mathbb{R}^2$ 是一个可数集, 证明 $\mathbb{R}^2 - X$ 是折线连通的.

</div>

<div class='pbox'>

考虑任意$R^2-X$中的两个点,不妨设为$(0,0),(x,0)$,假设他们折线不连通.

那么考虑折线$(0,0)\rightsquigarrow (\dfrac x2,a)\rightsquigarrow (x,0)$,则这条折线上至少有一个$X$中的点.设这个折线上除了$(0,0),(x,0)$外的点集为$S_a$.

于是每个$S_a$中至少有一个$X$中的点$p$,且$S_a$两两不交.故$S_a\mapsto p,p\in S_a$建立了$R$到$X$的单射.但$R$不可数,所以$X$不可数,矛盾.

</div>

### T8

<div class="cbox">

9. (M) 设 $X$ 为可数无限集, $\mathcal{T}_{fc}$ 为 $X$ 上的有限补拓扑, 证明 $(X, \mathcal{T}_{fc})$ 连通而非道路连通.

</div>

<div class='pbox'>

$X$连通等价于$X$不存在非平凡的即开又闭的集合.

而非平凡的开集的补有限,闭集是有限集,若其既开又闭则$X$为有限集,与$X$可数无限矛盾.故不存在.$X$连通.

设存在一条$x\rightsquigarrow y$的道路$p$,设其在$S_i\subset [0,1]$这个集合取值$c_i$,$i\in Z$.

那么问题等价成了是否存在可数个闭集$f^{-1}(c_i)$可以不交的覆盖$[0,1]$.因为可数,设闭集序列为$F_i$.

我们直到,$[0,1]$上的开集都可以被唯一的写成开区间的不交并(取连通分支即可),那么$U_i=[0,1]-\bigcup_{1\le i\le n} F_i=\bigsqcup_j (l_{i,j},r_{i,j})=\bigsqcup_j I_{i,j}$.

那么若$I_{i,j}\supset I_{i+1,k}$,就在这两个区间连一条边,可以得到一棵树.

我们注意到,如果这棵树的区间并非只有一个和他自己相同的儿子,那么必然出现了分叉:考虑若树上有开区间$(l,r)$,因为他是等价类切出来的,所以$l,r$一定已经被某个闭集覆盖.为了不交,新的这个闭集必须不包含$l,r$,也就不包含它们俩的小邻域.而闭集只要不为空,$l,r$就不再连通,于是它必须有至少两个儿子.

那么现在:

如果树上存在一个从根无限延伸的路径满足从某处开始后面都不再分叉只有一个儿子,设最后一个分叉后的区间是$(l,r)$,则最终$(l,r)$就不会被覆盖.

否则,这棵树的每个开区间必然都不断分叉,那么对一个开区间$(l_i,r_i)$,必然可以找到其子树中的某个深度存在至少$3$个区间.不妨设其中最靠左的区间是$I_{l,i}$,最靠右的区间是$I_{r,i}$,则任取$l'_i\in I_{l,i},r'_i\in I_{r,i}$,必然有$[l'_i,r'_i]\subset (l_i,r_i)$,且$[l_i,r_i]$内至少还有一个树上的开区间,可以设为$(l_{i+1},r_{i+1})$递归下去.

于是得到闭区间套$[l_i',r_i']$,其中含有至少一个点,违背覆盖.

故得证$[0,1]$不可能被可数个闭区间覆盖,于是不存在一个路径$p$,不道路连通.

</div>

### T9

<div class="cbox">

28. (MRH) 设 $GL^+(n; \mathbb{R})$ 是由所有行列式大于零的矩阵组成的 $Mat(n \times n, \mathbb{R})$ 的子空间, 它可以看成 $\mathbb{R}^{n^2}$ 的子空间. 证明 $GL^+(n, \mathbb{R})$ 是道路连通的.

</div>

<div class='pbox'>

考虑对任意矩阵$M_1,M_2$,我们分解$M_i=L_iD_iU_i$,其中$L_i$为对角线全为$1$的下三角矩阵,$D$为对角矩阵,$U_i$为对角线全为$1$的上三角矩阵.

则构造$p(t)=(tL_2+(1-t)L_1)(tD_2+(1-t)D_1)(tU_2+(1-t)U_1)$,显然满足连续,$p(0)=M_1,p(1)=M_2$,且$\forall t,|p(t)| >0$.

故任意两元素道路连通.空间道路连通.

</div>
