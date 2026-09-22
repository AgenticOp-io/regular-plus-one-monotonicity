# Lemma L2 — patched Corollary 15 and Theorem 10

We prove the upgrade Gao asserted in arXiv:2104.11850 Remark 16(b) / §5,
using arXiv:2012.01492 Theorem 6 / Remark 8 as a black box.

Throughout: \(n\) even, \(d=d(n)\ge 3\), \(d\to\infty\), and \(d=o(n^{1/2})\).
All asymptotics are as \(n\to\infty\).

---

## Theorem A (Patched Corollary 15)

Let \(0\le k\le n/2\) and let \(H\) be a graph on \([n]\) consisting of \(k\) isolated edges
together with a collection of vertex-disjoint cycles covering the remaining \(n-2k\)
vertices. Set \(\alpha=2k/n\). Then
\[
\mathbb{P}\bigl(H\subseteq G(n,d)\bigr)
=
\Bigl(1+O\bigl(\tfrac{d^2}{n}\bigr)\Bigr)
\cdot
\rho(n,d,\alpha),
\]
where \(\rho(n,d,\alpha)\) is exactly Gao’s main term
\[
\rho(n,d,\alpha)
=
\Bigl(\frac{e}{n}\Bigr)^{(1-\alpha/2)n}
\Bigl(\frac{d-2+\alpha}{d}\Bigr)^{\frac{(d-2+\alpha)n}{2}}
d^{\alpha n/2}
(d-1)^{(1-\alpha)n}
\exp\bigl(\varphi(d,\alpha)\bigr)
\]
and
\[
\varphi(d,\alpha)
=
\frac{
4(d-2)^2-(d^2-5)\alpha^2-(2d^2-14d+20)\alpha
}{
4(d-2+\alpha)^2
}
\]
as in Gao (2104.11850), display (8).

(Equivalently: the statement of Gao’s Corollary 15 with every \(O(d^3/n)\) replaced by
\(O(d^2/n)\), in the range \(d=o(n^{1/2})\).)

### Proof of Theorem A

**Step 1 — sequential factorization.**  
Order the edges of \(H\) as \(e_1,\ldots,e_m\) with \(m=|E(H)|\le n\). Write
\(H_0=\emptyset\) and \(H_i=\{e_1,\ldots,e_i\}\). Then
\[
\mathbb{P}(H\subseteq G(n,d))
=
\prod_{i=1}^{m}
\mathbb{P}\bigl(e_i\in G(n,d)\mid H_{i-1}\subseteq G(n,d)\bigr).
\]

**Step 2 — apply Gao (2012.01492) Theorem 6 at each factor.**  
At step \(i\), the conditioning graph \(H_1:=H_{i-1}\) satisfies
\(\mathbf{d}^{H_1}\preceq (d,\ldots,d)\) and \(\widetilde{M}=\Omega(dn)\) for all \(i\le m\) in our
range (at most \(n\) edges removed from a \(dn\)-stub budget). Theorem 6 gives
\[
\mathbb{P}(e_i\in G\mid H_{i-1}\subseteq G)
=
\Bigl(1+O\bigl(\tfrac{d^2}{n^2}\bigr)\Bigr)
\cdot
\pi_i,
\]
where \(\pi_i\) is the principal term displayed in Theorem 6 (the
\(\widetilde{d}_u\widetilde{d}_v/\widetilde{M}\) factor times the \(\bar\phi\) correction).
(For \(d\)-regular graphs, \(\Delta=d\), \(M=dn\), and the relative error
\(O(\Delta^5 n/M^3)=O(d^2/n^2)\).)

**Step 3 — accumulate relative errors.**  
The product of \(m\le n\) factors each contributing a multiplicative
\(1+O(d^2/n^2)\) yields an overall multiplicative factor
\[
\bigl(1+O(d^2/n^2)\bigr)^{O(n)}
=
1+O(d^2/n),
\]
using \(d=o(n^{1/2})\) so that \(d^2/n=o(1)\) and the expansion
\((1+O(\varepsilon_n))^n=1+O(n\varepsilon_n)\) applies with \(\varepsilon_n=d^2/n^2\).

**Step 4 — identify the principal product.**  
Write \(P_{\mathrm{main}}:=\prod_{i=1}^m \pi_i\). By Gao (2012.01492) Remark 8,
Theorem 6 evaluates \(\mathbb{P}(H\subseteq G(n,d))\) with main term equal to the classical
McKay/configuration main term and relative error \(O(d^2|H|/n^2)=O(d^2/n)\).
That classical main term, for \(H\) of the cycle-plus-matching shape in the statement,
is computed explicitly by Gao (2104.11850) in the proof of Corollary 15,
displays (9)–(8), as the factorial ratio
\[
\frac{N_{\mathrm{main}}(g,H)}{N_{\mathrm{main}}(d,\emptyset)}
=
\rho(n,d,\alpha)
\]
(the part of McKay’s formula **excluding** the \(O(\Delta(\hat g)^2/m)\) error).
Those factorial/\(\lambda/\mu\) calculations do not use the error term; they are purely
algebraic identities for the degree sequence \(g=d-d^H\). Hence
\[
P_{\mathrm{main}}=\rho(n,d,\alpha).
\]

**Step 5 — conclude.**  
Combining Steps 3–4,
\[
\mathbb{P}(H\subseteq G(n,d))
=
\bigl(1+O(d^2/n)\bigr)\,\rho(n,d,\alpha),
\]
as claimed. ∎

### Remark (relation to McKay enumeration)

Gao’s original Cor 15 derives the same main term via
\(N(g,H)/N(d,\emptyset)\) and McKay’s Theorem 14, whose error
\(O(\Delta(\hat g)^2/m(g))=O(d^4/(dn))=O(d^3/n)\) is the sole source of \(O(d^3/n)\).
Theorem A replaces that enumeration-error analysis by sequential Theorem 6
exposures, keeping the main term untouched.

---

## Theorem B (Patched first and second moments of \(Y\))

Let \(Y\) be the number of perfect matchings in \(G\sim G(n,d)\). Then
\[
\mathbb{E} Y
=
\Bigl(1+O\bigl(\tfrac{d^2}{n}\bigr)\Bigr)
\frac{n!}{(n/2)!\,2^{n/2}}
\rho_1(n,d),
\]
where \(\rho_1(n,d)=\rho(n,d,1)\) is Gao’s (12), and
\[
\frac{\mathbb{E}[Y^2]}{(\mathbb{E} Y)^2}
=
1+\frac{1}{6d^3}
+O\Bigl(d^{-4}+\frac{d^2}{n}+\sqrt{\frac{d}{n}}\log^3 n\Bigr).
\]

### Proof of Theorem B

**First moment.**  
For any fixed perfect matching \(H\), Theorem A with \(k=n/2\) (\(\alpha=1\)) gives
\[
\mathbb{P}(H\subseteq G(n,d))
=
\bigl(1+O(d^2/n)\bigr)\rho_1(n,d),
\]
since \(\varphi(d,1)=1/4\). There are \(n!/\bigl((n/2)!2^{n/2}\bigr)\) perfect matchings, so
\[
\mathbb{E} Y
=
\sum_{H}\mathbb{P}(H\subseteq G)
=
\bigl(1+O(d^2/n)\bigr)
\frac{n!}{(n/2)!\,2^{n/2}}
\rho_1(n,d).
\]

**Second moment.**  
Expand
\[
\mathbb{E}[Y^2]
=
\sum_{H_1,H_2}
\mathbb{P}(H_1\cup H_2\subseteq G(n,d)).
\]
For each pair with \(|H_1\cap H_2|=k\), the union \(H:=H_1\cup H_2\) consists of \(k\) isolated
edges (the shared matching edges) and disjoint even cycles on the remaining vertices —
exactly the shape required by Theorem A. Thus
\[
\mathbb{P}(H_1\cup H_2\subseteq G)
=
\bigl(1+O(d^2/n)\bigr)\rho_2(n,d,\alpha),
\qquad\alpha=2k/n,
\]
with \(\rho_2\) as in Gao (14)–(15).

From here the argument is identical to Gao (2104.11850) §3.4–3.5:
group pairs by \(k\), apply Gao’s Lemma 17 to count pairs at each \(k\), sum the resulting
series, and extract
\[
\frac{\mathbb{E}[Y^2]}{(\mathbb{E} Y)^2}
=
1+\frac{1}{6d^3}+O(d^{-4})
+
O\Bigl(\frac{d^2}{n}\Bigr)
+
O\Bigl(\sqrt{\frac{d}{n}}\log^3 n\Bigr).
\]
The only change versus Gao is that every occurrence of \(O(d^3/n)\) inherited from
Corollary 15 is now \(O(d^2/n)\). The \(\sqrt{d/n}\log^3 n\) term arises from Gao’s
truncation/tail estimates on large-\(k\) contributions and is unchanged. ∎

### Corollary (relative variance)

\[
\frac{\mathrm{Var}\,Y}{(\mathbb{E} Y)^2}
=
\frac{1}{6d^3}
+O\Bigl(d^{-4}+\frac{d^2}{n}+\sqrt{\frac{d}{n}}\log^3 n\Bigr).
\]

---

## Honesty box

- Theorem A Step 4 is strengthened in `main-term-identification.md`
  (both main terms named; ratio \(1+O(d^2/n)\)).
- Theorem B’s series algebra: see `appendix-second-moment.md`, including
  **Lemma 18′** with range relaxed to \(d=o(n^{1/2})\).
- External black box: arXiv:2012.01492 Theorem 6.
- Beyond \(\sqrt{n}\): see `beyond-sqrt-n.md`.
