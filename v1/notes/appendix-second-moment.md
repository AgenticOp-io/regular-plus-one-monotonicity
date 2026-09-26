# Appendix — second-moment expansion with patched errors

This appendix records Gao (arXiv:2104.11850) §3.4–3.5 with every
\(O(d^3/n)\) replaced by \(O(d^2/n)\), and with Lemma 18’s hypothesis relaxed from
\(d=o(n^{1/3})\) to \(d=o(n^{1/2})\).

Notation as in Gao: \(Y=\#\{\text{perfect matchings in }G(n,d)\}\),
\(\rho_1,\rho_2,\varphi\) as in displays (12)–(15)/(8).

---

## A.1 First moment (patched)

For any perfect matching \(H\), Theorem A with \(\alpha=1\) gives
\[
\mathbb{P}(H\subseteq G(n,d))=(1+O(d^2/n))\,\rho_1(n,d).
\]
Hence
\[
\mathbb{E} Y
=
(1+O(d^2/n))
\frac{n!}{(n/2)!2^{n/2}}
\rho_1(n,d).
\tag{A.1}
\]

---

## A.2 Pair probabilities (patched)

Fix \(0\le k\le n/2-2\) and perfect matchings \(H_1,H_2\) with \(|H_1\cap H_2|=k\).
Then \(H_1\cup H_2\) has the shape required by Theorem A with \(\alpha=2k/n\), so
\[
\mathbb{P}(H_1\cup H_2\subseteq G(n,d))
=
(1+O(d^2/n))\,\rho_2(n,d,\alpha).
\tag{A.2}
\]

Gao’s Lemma 17 is unchanged (pure enumeration of matching pairs):
\[
\#\{(H_1,H_2):|H_1\cap H_2|=k\}
=
\bigl(1+O((n-2k)^{-1})\bigr)
\frac{n!}{2^k k!\,\sqrt{e\pi(n-2k)/2}}.
\]

Therefore
\[
\mathbb{E}[Y^2]
=
\sum_{k=0}^{n/2-2}
\bigl(1+O((n-2k)^{-1}+d^2/n)\bigr)
\frac{n!}{2^k k!\,\sqrt{e\pi(n-2k)/2}}
\rho_2(n,d,\alpha(k))
+
\mathbb{E} Y.
\tag{A.3}
\]
(Compare Gao (16), with \(d^3/n\mapsto d^2/n\).)

---

## A.3 Patched Lemma 18

**Lemma 18′.**  
Assume \(d\to\infty\) and \(d=o(n^{1/2})\). Let
\[
\bar\alpha=\frac1d,
\qquad
\bar k=\bigl\lfloor\bar\alpha\, n/2\bigr\rfloor,
\qquad
\bar\delta
=
\frac{2d}{n}\cdot\frac{d(d-2)}{(d-1)^2}.
\]
Then
\[
\mathbb{E}[Y^2]
=
\Bigl(1+O\Bigl(\sqrt{\tfrac{d}{n}}\log^3 n+\tfrac{d^2}{n}\Bigr)\Bigr)
\frac{2}{\sqrt{e}}\,\bar\delta\,
\frac{n!\,\rho_2(n,d,\bar\alpha)}{\bar k!\,2^{\bar k}\sqrt{n-2\bar k}}.
\]

**Proof sketch (following Gao §3.4.2).**  
Write the summand of (A.3) as proportional to \(\phi(k)=\rho_2(n,d,\alpha(k))/(2^k k!\sqrt{n-2k})\).
The ratio \(\phi(k)/\phi(k-1)\) equals
\[
\frac{(d-2)n+2k}{2(d-1)^2 k}\,(1+O(1/n))
\]
for \(k\le n/3\), and is \(O(1/d)\) for larger \(k\). Setting the main factor to \(1\) yields
\(k\sim n/(2d)=\bar k\).

Local Gaussian approximation around \(\bar k\) for displacements \(j=o(\bar k)\) is identical
to Gao’s calculation and produces the displayed main term. Tails
\(|k-\bar k|\ge \omega(\sqrt{\bar k}\log n)\) contribute a relative
\(O(\sqrt{d/n}\log^3 n)\) error (same Laplace/Chernoff estimates as Gao; the only
\(d\)-restriction needed is \(\bar k\to\infty\) and \(\bar k=o(n)\), i.e. \(d=o(n)\) and
\(d=\omega(1)\), both true here).

The relative error \(O(d^2/n)\) from (A.3) replaces Gao’s \(O(d^3/n)\) inside the
\(1+O(\cdots)\) factor. No step in §3.4.2 uses \(d=o(n^{1/3})\) except through that
error term and through Theorem 10’s old range; both are removed by Theorem A. ∎

---

## A.4 Ratio \(\mathbb{E}[Y^2]/(\mathbb{E} Y)^2\)

Set
\[
\xi
:=
d^{-4}+\frac{d^2}{n}+\sqrt{\frac{d}{n}}\log^3 n.
\]
From (A.1) and Lemma 18′,
\[
\frac{\mathbb{E}[Y^2]}{(\mathbb{E} Y)^2}
=
(1+O(\xi))
\sqrt{\frac{n}{e\,\bar\delta\,\bar k\,(n-2\bar k)}}
\cdot
\frac{\rho_2(n,d,\bar\alpha)}{(2\bar k/e)^{\bar k}\,\rho_1(n,d)^2}.
\]
Gao’s algebraic evaluation of the right-hand side (Appendix / Maple expansions in
arXiv:2104.11850) yields
\[
\frac{\mathbb{E}[Y^2]}{(\mathbb{E} Y)^2}
=
1+\frac{1}{6d^3}+O(\xi).
\]
Those expansions involve only rational functions of \(d\) and \(\bar\alpha=1/d\); they do not
depend on the \(d^3/n\) vs \(d^2/n\) distinction. ∎

---

## A.5 Consequence for Chebyshev

\[
\mathbb{P}\bigl(|Y-\mathbb{E} Y|\ge\alpha\,\mathbb{E} Y\bigr)
\le
\frac{\mathrm{Var}\,Y}{\alpha^2(\mathbb{E} Y)^2}
=
\frac{1}{6d^3\alpha^2}
+O\Bigl(\frac{\xi}{\alpha^2}\Bigr).
\]
With \(\alpha\) as in Lemma L4 and \(d=o(n^{1/2}/\log^3 n)\), the right-hand side is \(o(1)\).
