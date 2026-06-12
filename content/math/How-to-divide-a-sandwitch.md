---
title: How to divide a sandwitch
tags:
  - homework
  - topo
  - math
status: draft
top: 0
---

# How To Divide a Sandwitch

### Theorem

<div class='cbox'>

$$
\begin{gathered}
\forall g:S^n\to R^n \\
\exists x_0\in S^n \ s.t.\ g(x_0)=g(-x_0)
\end{gathered}
$$

</div>

### Lemma 1

<div class='cbox'>

The theorem is equivlant to:

$$
\begin{gathered}
\not\exists f:S^n \to S^{n-1} \\
\ s.t.\ f(-x)=-f(x)
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{If } \exists g \ s.t.\ \forall x,g(x)\ne g(-x), \\
\text{then let } f=\dfrac{g(x)-g(-x)}{\|g(x)-g(-x)\|} ,f(x)=f(-x) \\
\text{Contrarily, if }\exists f:S^n\to S^{n-1},f(-x)=-f(x) \\
\text{then } g=l\circ f \ s.t.\ g(x)=-g(-x)\ne g(-x) \\
\text{where } l:S^{n-1}\to R^n \text{ maps } s\in S^{n-1} \text{ to its coordinate representation in } \{x\in R^n,\|x\|=1\} \subset R^n
\end{gathered}
$$

So they are indeed equivlent. We'll prove the lemma's form.

</div>

### Homology

We'll use simplicial homology to prove the theorem. And we'll use homology on ${\mathbb Z}_2$ rather than ${\mathbb Z}$, since the homology of ${\mathbb RP}^n$ will be more simple.

Limited by the length of the article, some basic conclusions about homology in this section won't be proved. 

<div class='dbox'>

Simplicial complex

</div>



<div class='dbox'>

Chain Groups

</div>

<div class='dbox'>

Boundry Operator

</div>

<div class='dbox'>

Homology Groups

</div>

<div class='dbox'>

Simplicial map

</div>



<div class='cbox'>

$$
\begin{gathered}
X\simeq Y \implies H(X)\cong H(Y) \\
f:X\to Y \text{ induces a homomorphism }  \\
f^*:H(X)\to H(Y) \\
f^* \sum_{i=1}^k c_i<v_1\ldots v_n> =\sum_{i=1}^k c_i<f(v_1)\ldots f(v_n)>
\end{gathered}
$$

</div>

<div class='dbox'>

Degree of a map(for ${\mathbb Z}_2$)

$$
\begin{gathered}
\text{for map } f:S^n\to S^n, f \text{ induces a homomorphism } f^*:H_n(S^n)\to H_n(S^n) \\
\text{Since } H(S^n)\cong {\mathbb Z}_2, f^* \text{ is a homomorphism} \\
\text{so take } 1 \text{ as the unit in } H(S^n) \\
f^*(1)=m \implies f^*(n\cdot 1)=n\cdot f^*(1) \\
\text{thus define } \deg f=f^*(1)
\end{gathered}
$$

</div>

I just replaced all ${\mathbb Z}$ to ${\mathbb Z}_2$,so $\deg f \in \{ 0,1 \} $.

<div class='cbox'>

$$
\begin{gathered}
H_n(S^k)=\begin{cases}
{\mathbb Z}_2&k\in \{ 0,n \}  \\
0& \text{otherwise}
\end{cases}
\end{gathered}
$$

</div>

<div class='cbox'>

$$
\begin{gathered}
H_n({\mathbb RP}^k)=\begin{cases}
{\mathbb Z}_2&k\in [ 0,n ]  \\
0& \text{otherwise}
\end{cases}
\end{gathered}
$$

</div>

### Lemma 2

<div class='cbox'>

$$
\begin{gathered}
\forall f:S^n\to S^n \\
f \text{ can be extended to } D^n \implies \deg f=0
\end{gathered}
$$

</div>

<div class='pbox'>

$f$ can be extended indicates that $\exists F:D^n\to S^n \ s.t.\ F|_{\partial D^n}=f$, making the following graph commute:

```commutative
WzAsMyxbMSwxLCJEXm4iXSxbMCwwLCJTXm4iXSxbMiwwLCJTXm4iXSxbMSwyLCJmIl0sWzEsMCwiaSIsMix7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn19fV0sWzAsMiwiRiIsMl1d
```

Consider the map it induces on homology, we have:

```commutative
WzAsMyxbMCwwLCJIX24oU15uKSJdLFsyLDAsIkhfbihTXm4pIl0sWzEsMSwiSF9uKERebikiXSxbMCwyLCJpIiwwLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifX19XSxbMiwxLCJGXioiXSxbMCwxLCJmXioiLDJdXQ==
```

But $H_n(D^n)=0$, so if $i=0$, then $f^*=F^*\circ i=F^*\circ 0=0$,thus $\deg f^*=0$

</div>

### Homology

### Lemma 3

<div class='cbox'>

$$
\begin{gathered}
\forall f:S^n\to S^n,f(-x)=-f(x) \\
\deg f \equiv 1 \pmod 2
\end{gathered}
$$

</div>

<div class='pbox'>

#### Backbone


Since $f(-x)=-f(x)$, so for ${\mathbb {RP}}^n=S^n/_{x\sim -x}$, we can descend f to $\overline{f}:{\mathbb {RP}}^n\to {\mathbb {RP}}^n, [x]\mapsto [f(x)]$. Apparently, since $[x]=[y]\land x\ne y \iff x=-y \implies f(x)=-f(y) \iff [f(x)]=[f(y)]$, we know it's well defined.2 

So we'll have this graph:

```commutative
WzAsNSxbMSwwLCJDX2koXFxtYXRoYmJ7UlB9Xm4pIl0sWzMsMCwiQ19pKFxcbWF0aGJie1JQfV5uKSJdLFsyLDAsIkNfaShTXm4pIl0sWzQsMCwiMCJdLFswLDAsIjAiXSxbMCwyLCJUIl0sWzIsMSwicCJdLFsxLDNdLFs0LDBdXQ==
```


If we believe that $T,p$ are commutable with the boundry operator $\partial$. By snake lemma,we'll have:

```commutative
WzAsNyxbMCwxLCJIX2koXFxtYXRoYmJ7UlB9Xm4pIl0sWzEsMSwiSF9pKFNebikiXSxbMiwxLCJIX2koXFxtYXRoYmJ7UlB9Xm4pIl0sWzAsMiwiSF97aS0xfShcXG1hdGhiYntSUH1ebikiXSxbMiwwLCJIX3tpKzF9KFxcbWF0aGJie1JQfV5uKSJdLFsxLDAsIlxcY2RvdHMiXSxbMSwyLCJcXGNkb3RzIl0sWzAsMSwiVF4qIl0sWzEsMiwicF4qIl0sWzIsMywiXFxkZWx0YSJdLFs0LDAsIlxcZGVsdGEiXSxbNSw0XSxbMyw2XV0=
```



For $f$, it'll induce endomorphism on homology as well. And agin if we have validated that $f_*,\overline f_*$ is commutable with $T^*,p^*,\delta$, we are able to write this graph:

```commutative
WzAsMTIsWzEsMSwiSF9pKFxcbWF0aGJie1JQfV5uKSJdLFsyLDEsIkhfaShTXm4pIl0sWzMsMSwiSF9pKFxcbWF0aGJie1JQfV5uKSJdLFs0LDEsIkhfe2ktMX0oXFxtYXRoYmJ7UlB9Xm4pIl0sWzAsMSwiXFxjZG90cyJdLFs1LDEsIlxcY2RvdHMiXSxbMSwwLCJIX2koXFxtYXRoYmJ7UlB9Xm4pIl0sWzIsMCwiSF9pKFNebikiXSxbMywwLCJIX2koXFxtYXRoYmJ7UlB9Xm4pIl0sWzQsMCwiSF97aS0xfShcXG1hdGhiYntSUH1ebikiXSxbMCwwLCJcXGNkb3RzIl0sWzUsMCwiXFxjZG90cyJdLFs0LDBdLFszLDVdLFswLDEsIlReKiJdLFsxLDIsInBeKiJdLFsyLDMsIlxcZGVsdGEiXSxbMTAsNl0sWzksMTFdLFs2LDcsIlReKiJdLFs3LDgsInBeKiJdLFs4LDksIlxcZGVsdGEiXSxbNiwwLCJcXG92ZXJsaW5lIGZeKiIsMV0sWzcsMSwiZiIsMV0sWzgsMiwiXFxvdmVybGluZSBmXioiLDFdLFs5LDMsIlxcb3ZlcmxpbmUgZl4qIiwxXV0=
```

To prove the degree is 1, we must prove that $f^*_n$ is a isomorphisim. And $\overline f^*$ plays a role as bridge.

We'll do it by induction: for $i=0$,$H_0$ represents the connected component. ${\mathbb RP}^n$ is connected. so of course $\overline f^*= \mathrm{id}$ is an isomorphism. 

Now consider $i\in [1,n-1]$.,assume we have proved $\forall k\lt i,\overline{f}^*_k$ is an isomorphism.

Notice that $H_i(S^n)=0,\forall i\in [1,n-1]$. So by exactness, we find $\forall i\in [1,n-1],\delta_i$ is an injection, so a isomorphism. As for $i=n$,$\delta_i$ is a surjection, so a isomorphism as well. Thus in this part of the commute graph we see:

```commutative
WzAsNCxbMCwwLCJIX2koXFxtYXRoYmJ7Un1QXm4pIl0sWzEsMCwiSF9pKFxcbWF0aGJie1J9UF5uKSJdLFswLDEsIkhfaShcXG1hdGhiYntSfVBebikiXSxbMSwxLCJIX2koXFxtYXRoYmJ7Un1QXm4pIl0sWzAsMSwiXFxkZWx0YSJdLFswLDIsIlxcb3ZlcmxpbmUgZl9pIiwxXSxbMSwzLCJcXG92ZXJsaW5lIGZfe2ktMX0iLDFdLFsyLDMsIlxcZGVsdGEiXV0=
```


the up,bottom,right edges are all isomorphisms, so the left is alose a isomorphism.

Finally, look at this part:

```commutative
WzAsMTIsWzEsMSwiSF9uKFxcbWF0aGJie1J9UF5uKSJdLFsyLDEsIkhfbihTXm4pIl0sWzMsMSwiSF9uKFxcbWF0aGJie1J9UF5uKSJdLFs0LDEsIkhfe24tMX0oXFxtYXRoYmJ7Un1QXm4pIl0sWzAsMSwiSF97bisxfShcXG1hdGhiYntSfVBebikiXSxbNSwxLCJcXGNkb3RzIl0sWzEsMCwiSF9uKFxcbWF0aGJie1J9UF5uKSJdLFsyLDAsIkhfbihTXm4pIl0sWzMsMCwiSF9uKFxcbWF0aGJie1J9UF5uKSJdLFs0LDAsIkhfe24tMX0oXFxtYXRoYmJ7Un1QXm4pIl0sWzAsMCwiSF97bisxfShcXG1hdGhiYntSfVBebikiXSxbNSwwLCJcXGNkb3RzIl0sWzQsMF0sWzMsNV0sWzAsMSwiVF4qIl0sWzEsMiwicF4qIl0sWzIsMywiXFxkZWx0YSJdLFsxMCw2XSxbOSwxMV0sWzYsNywiVF4qIl0sWzcsOCwicF4qIl0sWzgsOSwiXFxkZWx0YSJdLFs2LDAsIlxcb3ZlcmxpbmUgZl4qIiwxXSxbNywxLCJmXioiLDFdLFs4LDIsIlxcb3ZlcmxpbmUgZl4qIiwxXSxbOSwzLCJcXG92ZXJsaW5lIGZeKiIsMV0sWzEwLDQsIlxcb3ZlcmxpbmUgZl4qIiwxXV0=
```



$H_{n+1}(RP^n)=0$. so the five map between two long exact sequence is all isomorphisms except the middle one. Then by five lemma, the middle one is an isomorphism.

So $f^*=\mathrm{id},\deg f=1$.

#### Trifles

So now we only have to validate that those graphs are indeed commutable:



</div>



### Final Proof

### Summary
