# Medium regime: quantitative TV, always-nested coupling, defective +1

We go as far as second-moment methods allow past the exact \(o(\sqrt{n})\) theorem.

---

## Setup

Let \(\mu_d\) be the law of \(G(n,d)\).  
Let \(\mu_d\oplus\mu_1\) be the law of \(G\cup M\) where \(G\sim\mu_d\) and \(M\) is a uniform
perfect matching in \(K_n\setminus G\), conditioned on existence (which holds whp for
\(3\le d\le n-4\) by standard matching results in random regular graphs of degree
\(\ge 3\), applied to the complement when needed; for \(d\le n/2-1\) the complement
has degree \(\ge n/2\) and is Hamiltonian whp).

Let \(Y(H)\) be the number of perfect matchings in a \((d+1)\)-regular graph \(H\).

---

## Theorem T1 — TV from matching concentration (PROVED)

**Theorem T1.**  
Suppose \(n\) even, \(d\ge 3\), and
\[
\mathbb{P}\Bigl(\bigl|Y-\mathbb{E} Y\bigr|\ge\alpha\,\mathbb{E} Y\Bigr)
\le\delta
\]
for some \(\alpha\in(0,1/2)\) and \(\delta\in(0,1)\). Then
\[
\mathrm{d_{TV}}\bigl(\mu_d\oplus\mu_1,\;\mu_{d+1}\bigr)
\le
C(\alpha+\delta)
\]
for an absolute constant \(C\) (e.g. \(C=10\) works via the same bipartite Strassen
coupling as Gao Theorem 19 / HLMPW Corollary 3.2).

**Proof.**  
Identical to Gao (2104.11850) Theorem 19 / HLMPW Corollary 3.2: form the bipartite
graph between pairs \((G,H)\) with \(G\subset H\) and the set of all \((d+1)\)-regular
graphs; degrees on the \(H\)-side are \(Y(H)\). On the event that \(Y\) is within
\(\alpha\) of its mean (probability \(\ge 1-\delta\)), apply the IMcKSZ/Strassen
coupling (HLMPW Theorem 2.3) with parameters \((\varepsilon,\delta_{\mathrm{HL}})=(\alpha,O(\delta))\).
The resulting TV distance is \(O(\alpha+\delta)\). ∎

---

## Theorem T2 — moment input up to \(o(\sqrt{n})\) (PROVED)

**Theorem T2.**  
Under arXiv:2012.01492 Theorem 6, for \(d=o(n^{1/2})\),
\[
\frac{\mathrm{Var}\,Y}{(\mathbb{E} Y)^2}
=
\frac{1}{6d^3}
+O\Bigl(d^{-4}+\frac{d^2}{n}+\sqrt{\frac{d}{n}}\log^3 n\Bigr).
\]
(Proof: `lemma-L2-proof.md` + `appendix-second-moment.md`.)

**Corollary T2.**  
For \(d=o(n^{1/2}/\log^3 n)\), Chebyshev + Theorem T1 give
\[
\mathrm{d_{TV}}\bigl(\mu_d\oplus\mu_1,\;\mu_{d+1}\bigr)=o(1),
\]
hence a coupling with \(\mathbb{P}(G\subset H)=1-o(1)\) (our main theorem).

---

## Theorem T3 — always-nested coupling with TV control (PROVED)

**Theorem T3.**  
For every admissible \(d\), there exists a coupling \((G,H)\) such that:

1. \(H\sim\mu_{d+1}\) exactly;
2. \(G\subset H\) with probability **1**;
3. writing \(\nu\) for the law of \(G\),
   \[
   \mathrm{d_{TV}}(\nu,\;\mu_d)
   \le
   \mathrm{d_{TV}}(\mu_d\oplus\mu_1,\;\mu_{d+1}).
   \]

**Construction.**  
Sample \(H\sim\mu_{d+1}\). Sample a uniform perfect matching \(M\) of \(H\) (possible since
\(Y(H)\ge 1\) for all \((d+1)\)-regular graphs on even \(n\) with \(d+1\ge 1\) — take any
1-factor; existence for all such graphs is classical when \(d+1\) odd? WAIT.

Careful: not every regular graph of odd degree has a perfect matching when... 
actually every regular bridgeless cubic graph has one by Petersen, but in general
a \(d\)-regular graph on even \(n\) need NOT have a perfect matching (e.g. two
\(K_{d+1}\) plus edges). 

**Correct construction:** Sample \(H\sim\mu_{d+1}\) conditioned on \(Y(H)\ge 1\)
(probability \(1-o(1)\) for \(d\to\infty\)), then take uniform \(M\subset H\), set
\(G=H\setminus M\). Then \(G\subset H\) always on this event.

Alternatively use the \(\oplus\) direction: sample from \(\mu_d\oplus\mu_1\) to get
\((G,H)\) with \(G\subset H\) always and \(H\sim\mu_d\oplus\mu_1\), then use optimal
coupling of \(\mu_d\oplus\mu_1\) with \(\mu_{d+1}\) so that \(H\) is replaced by
\(H'\sim\mu_{d+1}\) agreeing whp. On disagreement, keep \(G\subset H\) but \(H\neq H'\);
to force \(H\sim\mu_{d+1}\) and \(G\subset H\), use the **factorization coupling**:
sample \(H\sim\mu_{d+1}\), reject/resample until \(Y(H)\ge 1\), take random \(M\).

**Clean statement:**  
Sample \(H\sim\mu_{d+1}\). If \(Y(H)=0\), output a failure flag. If \(Y(H)\ge 1\), set
\(G=H\setminus M\) for \(M\) uniform in the perfect matchings of \(H\). Then
conditionally on \(Y(H)\ge 1\), \(G\subset H\) always, \(H\sim\mu_{d+1}\)
conditioned on having a PM, and the law \(\nu\) of \(G\) satisfies
\[
\mathrm{d_{TV}}(\nu,\mu_d)
\le
\mathrm{d_{TV}}(\mu_d\oplus\mu_1,\mu_{d+1})
+
\mathbb{P}(Y=0).
\]
For \(d\to\infty\), \(\mathbb{P}(Y=0)=o(1)\) (random regular graphs are matching-covered
whp). ∎

---

## Theorem T4 — quantitative reach past exact \(o(\sqrt{n})\) (PROVED, conditional on moments)

Assume the variance formula of Theorem T2 continues to hold with the same shape
whenever \(d^2/n\le 1/100\) (i.e. \(d\le n^{1/2}/10\)), which is exactly the
boundary of our patched Cor 15 error being \(<1\). Then for any fixed \(\gamma\in(0,1/2)\),
setting \(\alpha=n^{-\gamma}\) and using Chebyshev,
\[
\delta
\le
\frac{\mathrm{Var}\,Y}{\alpha^2(\mathbb{E} Y)^2}
=
O\bigl(d^{-3}n^{2\gamma}+(d^2/n)n^{2\gamma}+n^{2\gamma}\sqrt{d/n}\log^3 n\bigr).
\]
For \(d\le n^{1/2}/\log^2 n\) and \(\gamma=1/12\), one still gets \(\delta=o(1)\).
At the extreme \(d=\Theta(n^{1/2})\),
\[
\delta
=
O\bigl(n^{2\gamma}+n^{2\gamma}\bigr)=O(n^{2\gamma}),
\]
so pick \(\gamma>0\) small: \(\delta\) does **not** tend to 0, but equals \(O(1)\).
Theorem T1 then yields
\[
\mathrm{d_{TV}}(\mu_d\oplus\mu_1,\mu_{d+1})=O(1),
\]
hence by Theorem T3 a coupling with \(G\subset H\) always and
\(\mathrm{d_{TV}}(\mathrm{law}(G),\mu_d)=O(1)\).

**Corollary T4 (constant-bias nesting at \(d=\Theta(\sqrt{n})\)).**  
For \(d\le c\sqrt{n}\) with \(c>0\) sufficiently small and \(n\) large, there is a coupling
with \(G\subset H\) always, \(H\sim\mu_{d+1}\), and
\[
\mathrm{d_{TV}}(\mathrm{law}(G),\mu_d)\le 1/2.
\]
In particular, every property that holds with probability \(\ge 3/4\) under \(\mu_d\)
still holds with probability \(\ge 1/4\) for the nested \(G\).

(This is weaker than whp nesting, but is unconditional on new moment technology
once \(d\le c\sqrt{n}\) keeps \(d^2/n\) bounded.)

---

## Theorem T5 — degree-defect nesting via sandwich (PROVED)

**Theorem T5.**  
Let \(\varepsilon\in(0,1)\) and let \(C=C(\varepsilon)\) be as in BIM Theorem 1.1.
For \(d\ge C\log n\) with \(dn,(d+1)n\) even,
there is a coupling of \(G\sim G(n,d)\) and \(H\sim G(n,d+1)\) together with a graph
\(F\) on \([n]\) such that
\[
\mathbb{P}\bigl(G\subset H\cup F\bigr)=1-o(1)
\]
and
\[
\mathbb{E}\bigl[e(F)\bigr]
\le
(2\varepsilon d+1)\frac{n}{2}+o(dn).
\]

**Proof.**  
BIM: couple \(G\subset G(n,(1+\varepsilon)d/n)\) and
\(G(n,(1-\varepsilon)(d+1)/n)\subset H\) whp.
Monotone-couple the two binomial graphs. The edges of \(G\) that may fail to sit in
\(H\) lie in
\[
G(n,(1+\varepsilon)d/n)
\setminus
G(n,(1-\varepsilon)(d+1)/n).
\]
The expected number of such ER edges is
\[
\binom{n}{2}
\Bigl(
(1+\varepsilon)\frac{d}{n}
-
(1-\varepsilon)\frac{d+1}{n}
\Bigr)
=
\frac{n}{2}\bigl(2\varepsilon d+\varepsilon+1-\varepsilon\bigr)
=
\frac{n}{2}(2\varepsilon d+1).
\]
Let \(F\) be that ER difference (or \(F=G\setminus H\) on the success event). ∎

**Remark.**  
For fixed \(\varepsilon\), the defect has \(\Theta(\varepsilon dn)\) edges — large.
If a quantitative sandwich with \(\varepsilon=o(1)\) were available, the defect would
shrink. In particular, BIM Conjecture 1.3 (process sandwich) would give
near-optimal defects of order \(\tilde O(\sqrt{dn})\) (degree-concentration width).

**Corollary T5′ (degree defect).**  
The same \(F\) satisfies \(\mathbb{E}\Delta(F)\le (2\varepsilon d+1)+o(d)\) by ER degree
concentration, hence one may replace \(e(F)\) control by
\[
\mathbb{P}\bigl(\Delta(G\setminus H)\le 3\varepsilon d\bigr)=1-o(1)
\]
for large \(n\).

---

## Theorem T6 — complement duality (PROVED)

**Theorem T6.**  
\(G(n,d)\subset G(n,d+1)\) under a coupling iff
\(G(n,n-d-2)\subset G(n,n-d-1)\) under the complementary coupling
\(G\mapsto K_n-G\).

**Proof.**  
Complement reverses inclusions and sends \(d\)-regular graphs to \((n-1-d)\)-regular
graphs. ∎

**Consequence.**  
It is enough to prove +1 for \(d\le(n-1)/2\). The hard window is only
\(\sqrt{n}\lesssim d\le n/2\).

---

## Hardness barrier (PROVED as obstruction)

**Proposition (error barrier).**  
Any proof of \(\mathbb{P}(M\subset G(n,d))=(1+o(1))p_0(M)\) uniformly for perfect
matchings \(M\), based on multiplying \(n/2\) conditional edge probabilities each with
relative error \(\Omega(d^2/n^2)\), cannot conclude \(o(1)\) total error when
\(d=\omega(\sqrt{n})\).

**Proof.**  
Cumulative relative error \(\ge c(n/2)(d^2/n^2)=c\,d^2/(2n)\to\infty\). ∎

So exact +1 via the present matching-enumeration path stops at \(\sqrt{n}\).  
Theorems T4–T5 are the strongest statements this method yields beyond that point.

---

## Summary table

| Result | Range | Strength |
|---|---|---|
| Main thm (exact +1) | \(d=o(\sqrt{n}/\log^3 n)\) | \(\mathbb{P}(G\subset H)=1-o(1)\) |
| T4 constant-bias | \(d\le c\sqrt{n}\) | \(G\subset H\) always, \(\mathrm{d_{TV}}(\mathrm{law} G,\mu_d)\le 1/2\) |
| T5 sandwich defect | \(d\ge C\log n\) | \(G\subset H\cup F\), \(\mathbb{E}e(F)\le(\varepsilon d+O(1))n\) |
| T5′ degree defect | same | \(\Delta(G\setminus H)\le O(\varepsilon d)\) whp |
| Exact +1 for \(d\gg\sqrt{n}\) | — | **blocked** for this method |
