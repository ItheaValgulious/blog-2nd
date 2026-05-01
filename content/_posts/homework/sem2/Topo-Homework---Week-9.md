---
title: Topo Homework - Week 9
tags:
  - topo
  - homework
  - math
status: published
top: 0
date: '2026-04-30T14:54:10.719Z'
---

# Topo Homework - Week 9
### T1

<div class="cbox">

8. (ER) 找到一个不是商映射的连续满射 $p: X \to Y$.

</div>

<div class="pbox">

$$
\begin{gathered}
X=\{a,b,c,d\} \\
\mathcal{T}_1 \text{ is discrete topology on } X \\
\mathcal{T}_2 = \{ \varnothing,X \}  \\
\mathrm{Id}:(X,\mathcal{T}_1)\to (X,\mathcal{T}_2) \text{ is continuous and surjective ,but not quotient map}. 
\end{gathered}
$$

</div>

### T2

<div class="cbox">

2. (ERH) 设 $S = S^1 \times I, \beta$ 是一个定角. 在 $S$ 上定义等价关系 “$\sim$” 如下: 当 $x \in \text{Int}(S)$ 时, $x \sim x; \forall \theta \in [0, 2\pi], e^{\theta i} \times \{0\} \sim e^{(\theta+\beta)i} \times \{1\}$. 证明: 商空间 $S / \sim$ 与环面同胚.

</div>

<div class="pbox">

定义映射

$$
\begin{gathered}
T(s)=\begin{cases}
(e^{\theta i-h\beta i},e^{2\pi hi}),s=\{(e^{\theta i},h)\},h\in (0,1) \\
(e^{\theta i},1),s=\{ (e^{\theta i},0),(e^{(\theta +\beta )i},1) \} 
\end{cases} \\
\end{gathered}
$$

容易直接验证$T$是双射.且$T$对每个分量连续,$T$为紧空间到T2空间的映射.故$T$为同胚.

</div>

### T3

<div class="cbox">

4. (ERH) 回答下列问题:
- (1) 如果把矩形左端固定, 右端扭转 $n\pi$ 角度, $n \in \mathbb{N}_+$, 再把左右两侧边黏合, 可以得到什么曲面?
- (2) 把 “长条形” 的矩形在三维空间中 “打结”, 然后再把左右两侧边黏合, 可以得到什么曲面?
- (3) “长条形” 矩形的左右两端还有没有其他方式的同胚黏合? 可以得到多少种不同胚的曲面?

</div>

<div class="pbox">

(1):$2|n$时为平环$S^1\times I$,$2\not |I$时为莫比乌斯带.

(2):打结不改变其同胚性.还是圆环面或莫比乌斯带.

长条形左右两端都是$I=[0,1]$,不同胚的曲面数,即本质不同的粘合方式数量,即$I$的自同胚数量.

设$f:I\to I$是同胚.$g:I\to I,g=(x\mapsto x)$是$I$上一条不自交的路径,于是$f\circ g$也是一条不自交的路径,且覆盖整个$I$.而$I$上的覆盖$I$的不自交的路径只有$g$和$g^{-1}$两种.所以粘合后得到的商空间只有$I\times I/((0,x)\sim (1,x))$和$I\times I/((0,x)\sim (0,1-x))$两种.

</div>

### T4

<div class="cbox">

8. (ERH) 证明沿默比乌斯带的二等分腰线割开它, 所得的曲面同胚于平环.

</div>

<div class="pbox">

考虑莫比乌斯带同胚于$I\times I/\sim$,其中$x \sim y \Leftrightarrow x=y\lor (\exists t \ s.t.\ \{ x,y \} =\{ (0,t),(1,1-t) \} )$.

那么莫比乌斯带的二等分腰线是一条$(0,\dfrac12)\rightsquigarrow (1,\dfrac12)$的路径.不妨设为$\alpha(t)=(t,\dfrac12)$.

于是剪开后的莫比乌斯带即:

$$
\begin{gathered}
([0,\dfrac12)\cup (\dfrac12,1])\times I/\sim
\end{gathered}
$$

于是可构造同胚:

$$
\begin{gathered}
h:([0,\dfrac12)\cup (\dfrac12,1])\times I/\sim\to S^1\times I \\
h(S)=\begin{cases}
(e^{\pi x i},2y) ,\text{ if } S=\{(x,y)\},x\in (0,1)\land y<\dfrac12 \\
(-e^{\pi x i},2-2y) ,\text{ if } S=\{(x,y)\},x\in (0,1)\land y>\dfrac12 \\
(1,2y) ,\text{ if } S=\{(0,y),(1,1-y)\},y<\dfrac12 \\
(-1,2-2y) ,\text{ if } S=\{(0,y),(1,1-y)\},y>\dfrac12
\end{cases}
\end{gathered}
$$

容易验证它随每个分量连续,且是双射,且逆映射连续.

</div>

### T5

<div class="cbox">

9. (EH) 回答下列问题:
(1) 沿默比乌斯带的三等分腰线割开它, 得到什么曲面?
(2) 沿默比乌斯带四等分腰线、五等分腰线分别割开它, 各得到什么曲面?

</div>

<div class="pbox">

(1):![pasted-image-1](@media/1eb682076e6894db1e98144a0d26a3170b5ae364dbcb7ffad8347e36db1fc7d9.png)得到一个莫比乌斯环和一个平环.

(2):四等分,五等分线图和结果都同三等分线.

</div>

### T6

<div class="cbox">

11. (MH) 在射影平面 $\mathbb{P}^2$ 上分别找出两条简单闭曲线 $\alpha$ 和 $\beta$, 使得 $\mathbb{P}^2$ 沿 $\alpha$ 切开得到默比乌斯带和一个圆盘, 而沿 $\beta$ 切开只得到一个圆盘.

</div>

<div class="pbox">

![pasted-image-1](@media/6aa73a23645850d994167b0cd4288cde19dbce1cf34fb254fc471170861bbeec.png)

如图.考虑$D^1$粘合对径点的模型,则

取$\alpha$为一小圆圈路径得到一个圆盘和一个莫比乌斯带.

取$\beta$为一条直径,则得到一个圆盘.

</div>

### T7

<div class="cbox">

13. (MRH) 定义映射 $f: I^2 \to \mathbb{R}^5$ 如下: 
$$f(x, y) = (\cos(2\pi x), \cos(2\pi y), \sin(2\pi y), \sin(2\pi x) \cos(\pi y), \sin(2\pi x) \sin(\pi y)).$$
证明: $f$ 的像同胚于克莱因瓶.

</div>

<div class="pbox">

克莱因瓶即$I\times I/\sim,x\sim y \Leftrightarrow \exists t,\{ x,y \} =\{ (0,t),(1,t) \} \lor \{ x,y \} =\{ (t,0),(1-t,1) \}$.

那么直接定义映射$T:I\times I/\sim \Rightarrow \operatorname{Im} f,T(S)=f(s),s\in S$.

证明$T$良定义:因为$f(0,t)=(1,\cos(2\pi t),\sin(2\pi t),0,0)=f(1,t)$,$f(t,0)=(\cos(2\pi t),1,0,\sin(2\pi t),0)=f(1-t,1)$.

仍然观察到$T$对每一维分量连续,$T$连续.

$T$是满射:$\forall f(x,y)\in \operatorname{Im} f,T\pi(x,y)=f(x,y)$.

$T$是单射:$T(a,b)=T(x,y)$解第二,三维可知$b=y$,解第一,四维可知$x=a$.故事单射.

$T$是紧空间到T2空间的连续双射.故$T$是同胚.

</div>
