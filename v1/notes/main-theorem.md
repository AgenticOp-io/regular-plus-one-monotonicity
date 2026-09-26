# Main theorem (conditional on Theorem 6 of arXiv:2012.01492)

## Theorem (Plus-one up to \(\sqrt{n}\))

Assume the conditional edge-probability estimate of Gao, arXiv:2012.01492, Theorem 6
(used as a black box via our Theorem A in `lemma-L2-proof.md`).

Let \(n\) be even and let \(d=d(n)\) satisfy
\[
d\to\infty
\qquad\text{and}\qquad
d=o\bigl(n^{1/2}/\log^3 n\bigr).
\]
Then there exists a coupling of \(G_d\sim G(n,d)\) and \(G_{d+1}\sim G(n,d+1)\) such that
\[
\mathbb{P}(G_d\subset G_{d+1})=1-o(1).
\]

## Proof

### Part 1 — patched moments

By Theorem B of `lemma-L2-proof.md`,
\[
\frac{\mathrm{Var}\,Y}{(\mathbb{E} Y)^2}
=
\frac{1}{6d^3}
+O\Bigl(d^{-4}+\frac{d^2}{n}+\sqrt{\frac{d}{n}}\log^3 n\Bigr),
\]
where \(Y\) is the number of perfect matchings in \(G(n,d)\) (and likewise for \(G(n,d+1)\)).

### Part 2 — choose the concentration window

Define
\[
\eta_{\mathrm{new}}(\alpha)
=
2\alpha
+\frac{1}{d^3\alpha^2}
+C\frac{d^2}{n\alpha^2}
+C\frac{\sqrt{d/n}\,\log^3 n}{\alpha^2}
\]
with \(C\) large enough to absorb the \(O(\cdot)\) constants in Part 1, and set
\[
\alpha
=
\max\Bigl\{
d^{-1},\;
(d^2/n)^{1/4}\log n,\;
(d/n)^{1/6}\log n
\Bigr\}.
\]
Lemma L4 of `attack-n-half.md` yields \(\alpha=o(1)\) and \(\eta_{\mathrm{new}}(\alpha)=o(1)\).

### Part 3 — Chebyshev

For \(G\sim G(n,d+1)\),
\[
\mathbb{P}\bigl(|Y-\mathbb{E} Y|\ge\alpha\,\mathbb{E} Y\bigr)
\le
\frac{\mathrm{Var}\,Y}{\alpha^2(\mathbb{E} Y)^2}
=
O\bigl(\eta_{\mathrm{new}}(\alpha)\bigr)=o(1).
\]
The same bound holds for the complementary matching counts \(Z(G)\) on
\(G\sim G(n,d)\), because \(\overline{G}\) is \((n-1-d)\)-regular with
\(n-1-d\sim n\) in our range, and Theorem A applies equally to estimates of
\(\mathbb{P}(M\subset\overline{G})\) used in Gao’s displays (23)–(28).
(Alternatively: \(Z(G)\) equals the number of perfect matchings of \(G(n,n-1-d)\)
up to complementation, and \(n-1-d=\omega(n^{1/2})\) still permits Theorem A since the
roles of graph/complement are symmetric for matching containment in \(K_n\).)

### Part 4 — run Gao’s coupling

Gao (2104.11850) Theorem 19 constructs a coupling from an auxiliary bipartite graph
between \(\mathcal{G}(n,d)\) and \(\mathcal{G}(n,d+1)\) with arcs \(G\subset G'\), using
concentration of \(Y\) and \(Z\) at scale \(\alpha\) with failure \(\eta(\alpha)\).

Replace Gao’s \(\eta\) (which contains \(d^3/(n\alpha^2)\)) by \(\eta_{\mathrm{new}}\)
(which contains \(d^2/(n\alpha^2)\)). Every inequality in Gao §4.2 that cites
Theorem 10 / Corollary 15 is valid verbatim with the patched errors from Theorem B.
Therefore Theorem 19 yields a coupling with
\[
\mathbb{P}(G_d\subset G_{d+1})
\ge
1-5\eta_{\mathrm{new}}(\alpha)
=
1-o(1).
\]

This proves the theorem. ∎

## Corollary (progress on Gao–Isaev–McKay monotonicity)

Under the same hypotheses, for every fixed integer \(t\ge 1\) with \(d+t=o(n^{1/2}/\log^3 n)\),
there is a coupling with
\[
\mathbb{P}\bigl(G(n,d)\subset G(n,d+1)\subset\cdots\subset G(n,d+t)\bigr)=1-o(1),
\]
by iterating the theorem \(t\) times (union bound: failure \(t\cdot o(1)=o(1)\) for fixed \(t\);
for \(t\to\infty\) take per-step failure \(o(1/t)\), available since \(\eta_{\mathrm{new}}\) can be
made \(n^{-c}\) on compact subranges of \(d\)).

## What is conditional?

The only external analytic input not re-proved in this repository is
**arXiv:2012.01492 Theorem 6** (sharper conditional edge probabilities).
Everything else is either elementary, cited from Gao (2104.11850) with a tracked
error substitution, or proved in-repo (Lemma L4, Theorems A–B structure).

## Comparison with prior art

| Result | Degree range for +1 |
|---|---|
| Gao Thm 8 | \(d=o(n^{1/3})\) |
| **This theorem** | \(d=o(n^{1/2}/\log^3 n)\) |
| Full conjecture | all admissible \(d\le n-2\) |
