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

## Class 1

<div class='dbox'>

非阿

</div>

<div class='cbox'>

有限域上绝对值一定平凡

</div>

<div class='pbox'>

元素一定有阶,所以乘着乘着会变成$1$.

</div>

<div class='cbox'>

特征为$p$的域上的绝对值一定是非阿的

</div>

<div class='pbox'>

把其中的整数拿出来形成一个有限群.然后用上面有限群的说法.

</div>

等下,什么是整数?

<div class='cbox'>

为什么p-adic选这个常数

</div>

<div class='pbox'>

todo.

</div>

<div class='cbox'>

度量空间完备化原空间是稠密子集.

比如$Q$在$\hat Q_p$

</div>

<div class='cbox'>

若有$K\to  \hat K_v$是包含映射,$K\to L$是拓扑域嵌入,其中$L$是完备的,则存在唯一$\varphi$使得$\hat K_v\to L$也是拓扑域嵌入.

</div>

<div class='dbox'>

极限

偏序集中$I$中,有一组元素$\{ x_i \} _{i\in I}$,有一组态射$\{ f_{i,j}:x_i\leftarrow x_j,i\le j \} $,$f_{ik}=f_{ij}\circ f_{jk},f_{ii}=\mathrm{Id}$.

如果有$X$下另一组$\{ \varphi_i:x\to x_i \}$,满足 $\varphi_i=f_{ij}\varphi_j$.且任意满足这个的一族$\phi$满足存在唯一$T$使得$\phi=\varphi(T)$.

则$\varprojlim X_i=\{ (x_i)\in \prod X_i:x_i=f_6{ij}(x_j) \} $.

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

todo

</div>

## Class 2

<div class='cbox'>

任意三角形等腰

</div>

<div class='pbox'>

取三角形最长的一条边,对他用超距不等式.则最长边$a\le \max(b,c)$,又因为他最长所以不能小于所以取等就完事了.

</div>

<div class='cbox'>

$$
\begin{gathered}
\forall x\in B(a,r),B(a,r)=B(x,r) \\
B(a,r)\cap B(b,s)\ne \varnothing,r\le s \implies B(a,r)\subset B(b,s) \\
B(a,r),\overline B(a,r) \text{ is open and close}  \\
\{ x\in K,|x|=1 \} \text{ is open} 
\end{gathered}
$$

</div>

<div class='pbox'>

从上面的等腰三角形考虑.前两条比较显然.

第三条:证明开球是闭的:考虑任意球外面的点,以他为球心做一个半径相同的开球,那么如果他们有交则由前两条这就是同一个球,矛盾,所以这个新球和原来的开球没有交.然后证明闭球是开的也是类似的todo.

</div>
<div class='cbox'>

对${\mathbb Q}_p$:

$$
\begin{gathered}
{\mathbb Z}_p\subset {\mathbb Q}_p \text{ is clopen}  \\
{\mathbb Z}_p \text{ is compact}  \\
{\mathbb Q}_p \text{ is not compact}  \\
{\mathbb Z}\subset {\mathbb Z}_p \text{ is dense} 
\end{gathered}
$$

</div>

<div class='pbox'>

(1):${\mathbb Z}_p$是开球所以他既开又闭.

(2):证明${\mathbb Z}_p$是完备且完全有界的然后推到他是紧的.todo.${\mathbb Q}_p$无界所以当然不是紧的.

(3):最后一个是用${\mathbb Z}_p$是${\mathbb Z}$的完备化.

</div>

<div class='cbox'>

${\mathbb Z}$到$R$的嵌入

</div>

<div class='pbox'>

todo

</div>

---

<div class='cbox'>

$$
\begin{gathered}
\text{let } \{ a_i \} _{i=1}^n \subset K,\sum_{i=1}^n a_i=0
\end{gathered}
$$

则$|a_i|$的最大值的$i$取到至少两次

</div>

<div class='cbox'>

Hensel in Q_p

$$
\begin{gathered}
f(x)=\sum _{i = 0} ^{n}  a_ix^i\in {\mathbb Z}_p[X] \\
\text{if } \exists x_1\in {\mathbb Z}_p,|f(x_1)|<1,|f'(x_1)|=1 \\
\text{then } \exists! x\in {\mathbb Z}_p \ s.t.\ 
f(x)=0,|x-x_1|<1
\end{gathered}
$$

</div>

<div class='pbox'>

考虑递归,逐位做

todo

考虑干脆直接套牛顿迭代的式子

</div>

<div class='cbox'>

$$
\begin{gathered}
\exists x,y,z\in {\mathbb Z}_7 \\
x^7+y^7=z^7
\end{gathered}
$$

</div>



<div class='cbox'>

Hensel 2nd

$$
\begin{gathered}
f,g,h \in {\mathbb Z}_p [x] \\
\begin{cases}
\overline f=\overline g\overline h \in {\mathbb F}_p[x] \\
\gcd(\overline g,\overline h)=\overline 1\in {\mathbb F}_p[x] \\
g(x) \text{ is monic} 
\end{cases} \\
\Rightarrow \begin{cases}
\exists g(x),h(x)\in {\mathbb Z}_p[x] \ s.t.\ 
f(x)=g(x)h(x) \\
g \text{ is monic}  \\

\end{cases}


\end{gathered}
$$

</div>

---

幂集数

<div class='cbox'>

幂集数的性质

- 乘法的收敛性
- 平移的收敛性
- 交换求和号的收敛性
- 复合(要求无常数项)收敛性

</div>

<div class='cbox'>

Strassman Theorem

</div>
