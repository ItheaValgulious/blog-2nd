---
title: Padic-Discussion
tags:
  - math
  - padic
  - discuss
  - class-note
status: draft
top: 0
---

# Padic-Discussion

<div class='dbox'>

非阿

</div>



<div class='cbox'>

有限域上绝对值一定平凡

</div>

<div class='cbox'>

特征为$p$的域上的绝对值一定是非阿的

</div>

<div class='cbox'>

为什么p-adic选这个常数

</div>

<div class='cbox'>

度量空间完备化原空间是稠密子集.

比如$Q$在$\hat Q_p$

</div>

<div class='cbox'>

若有$K\to  \hat K_v$是包含映射,$K\to L$是拓扑域嵌入,其中$L$是完备的,则存在唯一$\varphi$使得$\hat K_v\to L$也是拓扑域嵌入.

</div>

<div class='dbox'>

偏序集中$I$中,有一组元素$\{ x_i \} _{i\in I}$,有一组态射$\{ f_{i,j}:x_i\leftarrow x_j,i\le j \} $,$f_{ik}=f_{ij}\circ f_{jk},f_{ii}=\mathrm{Id}$.

如果有$X$下另一组$\{ \varphi_i:x\to x_i \}$,满足 $\varphi_i=f_{ij}\varphi_j$.且任意满足这个的一族$\phi$满足存在唯一$T$使得$\phi=\varphi(T)$.

则$\varprojlim X_i=\{ (x_i)\in \prod X_i:x_i=f_{ij}(x_j) \} $.

</div>

注意$\prod X_i$的拓扑是有限项取开集剩下的取全空间作为拓扑基.

<div class='cbox'>

$$
\begin{gathered}
X_n={\mathbb Z}/p^n {\mathbb Z},f_{ij}:X_i\leftarrow X_j
\end{gathered}
$$

然后定义极限是${\mathbb Z}_p=\varprojlim X_i$

</div>

<div class='cbox'>

定义

$$
\begin{gathered}
\hat {\mathbb Z}_p=\{ x\in \hat {\mathbb Q}_p:|x|_p\le 1 \} 
\end{gathered}
$$

则${\mathbb Z}_p\cong \hat{\mathbb Z}_p$.且这个是拓扑同构.

</div>

<div class='pbox'>

首先尝试构造$\hat {\mathbb Z}_p\to {\mathbb Z}/p^i {\mathbb Z}$

对一个柯西列$\{ x_n \} _n$,可以把他每项都商掉$p^i {\mathbb Z}$,因为商映射是连续的所有原来收敛商完了也收敛.但商完了是连续拓扑所以最后一定是常值,取这个常值$c$作为这个映射$\phi_i(\{ x_n \} _n)=c$.

泛性质说明一定存在$T:\hat {\mathbb Z}_p\to {\mathbb Z}_p$.然后验证其是单是满的.

然后考虑两边开集是什么样的说明其拓扑同构.

</div>

<div class='cbox'>

$$
\begin{gathered}
{\mathbb Z}_{(p)}=\{ \dfrac{a}{b} \in Q,p\not|b \} 
\end{gathered}
$$

然后发现$({\mathbb Z}_{(p)})_p={\mathbb Z}_p$

</div>

<div class='dbox'>

可以对$F^p(t)$定义类似的绝对值.可以取不可约多项式然后定义 $|x|_\pi=q^{-v_{\pi}(x)}$.

并把刚才的例子再做一遍.

</div>

<div class='dbox'>

用幂级数定义指数,对数映射

</div>

<div class='cbox'>

指数函数在

$$
\begin{gathered}
x\in p {\mathbb Z}_p,p\ne 2, \\
x\in 4 {\mathbb Z}_2,p=2
\end{gathered}
$$

收敛.

对数映射是

$$
\begin{gathered}
x\in 1+p {\mathbb Z}_p
\end{gathered}
$$

时收敛.

</div>

<div class='pbox'>

考虑单项的$v_p$,再构造一个能取满的.

</div>

<div class='cbox'>

$$
\begin{gathered}
p^m {\mathbb Z}_p \cong 1+p^m {\mathbb Z}_p
\end{gathered}
$$

</div>

<div class='cbox'>


$$
\begin{gathered}
{\mathbb Q}_p^\times = {\mathbb Z}\oplus {\mathbb Z}_p^\times
\end{gathered}
$$


</div>

<div class='cbox'>


$$
\begin{gathered}
{\mathbb Z}_p/p {\mathbb Z}_p\cong {\mathbb F}_p
\end{gathered}
$$

</div>

<div class='pbox'>



</div>
