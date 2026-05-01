---
title: Padic Homework
tags:
  - math
  - number
  - padic
  - homework
status: published
top: 0
date: '2026-04-24T12:08:12.079Z'
---

# Padic Homework

### T1

<div class="cbox">

1. 试证明, 若范数 $|\cdot|$ 满足对任意的整数 $n$ 都有 $|n| \le 1$, 则 $|\cdot|$ 一定是非阿的. (也就是说, 这个范数同构于某个 $p$-adic 范数.)

</div>

首先看起来这个范数同构于p-adic不对.比如$|x|=[x\ne 0]$不满足()

<div class="pbox">

$$
\begin{gathered}
(a+b)^n=\sum_{i=0}^n \binom nia^ib^{n-i} \\
|a+b|^n\le \sum_{i=0}^n |\binom ni| |a|^i|b|^{n-i} \\
\le (n+1)(\max(|a|,|b|))^n \\
\Rightarrow |a+b|\le \sqrt[n]{n+1}\max(|a|,|b|) \\
\Rightarrow |a+b| \\
= \lim_{n \to \infty} |a+b| \\
\le \lim_{n \to \infty} \sqrt[ n ]{ n+1 } \max(|a|,|b|) \\
=\max(|a|,|b|)
\end{gathered}
$$

</div>

### T2

<div class="cbox">

2. 记 $x \in \mathbb{Q}$, 且对任意的素数 $p$, 都有 $|x|_p \le 1$. 求证: $x \in \mathbb{Z}$.

</div>

<div class="pbox">

反证.设$x=\dfrac mn,|x|=\dfrac{|m|}{|n|},(m,n)=1,n\ne 1$.

只需证存在$p$使得$|m|_p>|n|_p$,即$\operatorname{ord}_p(m)<\operatorname{ord}_p(n)$,那么因为$m,n$互素且$n\ne 1$,一定存在一个质因子使得$m$的次数更低.于是一定存在$p$使得$|x|_p>1$,矛盾.得证.

</div>

### T3

<div class="cbox">

3. 请写出 $\frac{1}{3}$ 在 $\mathbb{Q}_5$ 中的 $p$-adic 展开以及 $-\frac{9}{16}$ 在 $\mathbb{Q}_{13}$ 中的 $p$-adic 展开.

</div>

<div class="pbox">

$$
\begin{gathered}
nx=1 \\
\Leftrightarrow |nx-1|_p=0 \\
\Leftrightarrow \forall i\ge 1,p^i|(\sum_{0\le j<i} 3x_ip^i-1)
\end{gathered}
$$

从而过程应该是

$$
\begin{gathered}
\begin{cases}
c_i=\dfrac{c_{i-1}-nx_{i-1}}{p} \\
nx_i=c_i \pmod p 
\end{cases}

\end{gathered}
$$

(1):

$$
\begin{gathered}
c_0=1,x_0=2 \\
c_1=-1=4,x_1=3 \\
c_2=-2,x_2=1 \\
c_3=-1,x_3=3
\end{gathered}
$$

从而$x=2\dot 3\dot 1$.

(2):

$$
\begin{gathered}
|16x+9|_{13}=0 \\
c_0=-9,x_0=10 \\
c_1=-13,x_1=0 \\
c_2=-1,x_2=4 \\
c_3=-5,x_3=7 \\
c_4=-9,x_4=10
\end{gathered}
$$

从而$x=\dot{(10)}04\dot7$.

</div>

### T4

<div class="cbox">

**进阶题**

4. 对任意的正整数 $n > 1$, 都可以将全体正整数写成 $n$ 进制. 那么, 为什么我们只考虑了素数 $p$ 的情形? 是否可以构造 6-adic? 9-adic 呢?

</div>

<div class="pbox">

第一题不是证过了,只能有至多一个质数$p$满足$p\ne 1$.或者说已经证明了所有构成度量的都是由质数$p$产生的.

</div>

### T5

<div class="cbox">

5. 证明: $p$-adic 整数环 $\mathbb{Z}_p$ 是列紧的. 也就是说, 任意的 $p$-adic 整数序列都总有收敛的子列.

</div>

<div class="pbox">

考虑把每个整数$z\in {\mathbb Z}_p$写成$\sum_i c_ip^i$.记$z^{(i)}=c_i$.

则任意一个数列$\{ z_n \}$,可以取子列$\{ z_{x_{1,n}} \} $满足$z_{x_{1,n}}^{(0)}$全部相等.(无限个元素分到有限个$z^{(0)}$取值必然有无限个落到同一类).

对子列$z_{x_{k,n}}$,可以取子列$z_{x_{k+1,n}}$满足$z_{x_{k,n}}^{(k)}$全部相等,且可额外限制$x_{k+1,n}>x_{k,n}$.

于是可以取子列$z_{x_{k,k}}$为收敛子列.

</div>

[think] 注意不能对$c$取模,否则会影响$\dfrac{c-nx}p$的值

### T6

<div class="cbox">

6. 证明: $p$-adic 数是有理数当且仅当它的 $p$ 进展开是最终周期的.

</div>

<div class="pbox">

$\Rightarrow$:考虑前面推过的p-adic的过程:

$$
\begin{gathered}
c_i=\dfrac{c_{i-1}-nx_{i-1}}{p} \\
nx_i=c_i \pmod p 
\end{gathered}
$$

那么对任意$\dfrac{c_0}n$展开成$x$的过程中,若存在$c_i=c_j$,则必有$x_i=x_j,c_{i+1}=c_{j+1}$,从而归纳得$c_{i+k}=c_{j+k}$,即$\forall n>i,c_n=c_{n+j-i}$,存在一个周期.

那么若$c_i\in [-n,n]$,则$c_{i+1}=\dfrac{c_{i-1}-nx_{i-1}}p\in [\dfrac{-n-n(p-1)}{p},\dfrac{n}{p}]\subset [-n,n]$.而可以通过拆带分数的方法让$c_i\in [-n,n]$.于是$c$有界,一定会重复.

$\Leftarrow$:

如果已知存在周期.设$x=\overline{a_1\ldots a_kb_1\ldots b_mb_1\ldots b_m\ldots}$.则$z=\overline{a_1\ldots a_k}\in Z,y=(x-z)p^{-k}=\overline{b_1\ldots b_mb_1\ldots b_m\ldots}$.所以只要证明纯循环数是有理数.

注意到

$$
\begin{gathered}
\dfrac{1}{1-p^k} =\dot 10\ldots \dot 0
\end{gathered}
$$

(考虑p-adic范数下收敛即可,不用考虑小数展开过程)

其中$0$的个数为$k-1$.

故$y=\dfrac{\overline{b_1\ldots b_m}}{1-p^m}$.得证.



</div>

### T7

<div class="cbox">

7. 对于前几个素数 $2, 3, 5, 7, 11, 13, 17, 19$, 在哪几个 $\mathbb{Q}_p$ 中, $-1$ 存在平方根?

</div>

<div class="pbox">

$$
\begin{gathered}
-1=\dfrac{p-1}{1-p}=\dot{(p-1)}
\end{gathered}
$$

否则求解$x^2=\dot{(p-1)}$即$\forall n,\sum_{i=0}^n x_ix_{n-i}=p-1$.

假设$x_0\ldots x_{k-1}$已经解出来了使得$\forall i<k,(x^2)_i=p-1$.则只要$x_k$满足:

$$
\begin{gathered}
2x_kx_0+\sum_{i=1}^{k-1} x_ix_{k-i}=(p-1) \pmod p
\end{gathered}
$$

当$p> 2$时这个方程一定有解.

而归纳边界时$\exists x_0^2=p-1 \pmod p$.这个成立要求$(-1)^{\dfrac{p-1}2}=1$得到$p=1\pmod 4$.

那么现在只剩下:
- $p=2$时,$x_0=1,x_1=\dfrac12$不存在于$F_2$,所以无平方根.
- $p>2$时只需$p=1\pmod 4$,$5,13,17$中$-1$有平方根.



</div>
