# Sharp unconstrained m-factor rate

Target: Conjecture residual-factor-sharp.
\[
\frac{\Var Z}{(\EE Z)^2}
=
O\Bigl(\frac{m^2}{\delta^3}+\frac{\delta^2 m}{n}\Bigr)
\quad\text{for}\quad
m=o(\delta^{3/2}),\ \delta=o(n^{2/5}).
\]
Proposition residual-sharp-bim: at BIM scales this is \(\Theta(1/d)\to0\).

## Fixed degree: closed (Theorem fixed-degree-factor)

In the pairing model the second moment is exactly
\(\sum_A \PP(S=A)\,M(A)M(mn-A)^2M((\delta-2m)n+A)M(\delta n)/[M(mn)M((\delta-m)n)]^2\),
where \(S\) is a sum of \(n\) iid Hypergeometric\((\delta,m,m)\)
(Lemma factor-one-dim; checked against exhaustive pairings).
Global max: Hoeffding \(I_{hyp}\ge I_{bin}\), and \(I_{bin}\ge\psi\) by
\(G'\propto x(1-2p)\) after \(m\le\delta/2\) (Lemma factor-rate).
Laplace: \(\psi''\sigma^2=\delta/(2(\delta-1))\), giving
\(\sqrt{(\delta-1)/(\delta-2)}\) for every \(m\) (Lemma factor-config).
Cycle effects \((-1/(\delta-1))^k\) for every \(m\), so small subgraph
conditioning gives relvar \(\to\exp(\sum_{k\ge3}x^k/2k)-1\approx1/(6\delta^3)\).
**The \(m^2\) in the conjecture is not sharp**; the true shape is \(m\)-free
and symmetric under \(m\leftrightarrow\delta-m\).
Scripts: `v2/scripts/fixed_degree_factor/`.

Open for \(\delta\to\infty\): \(\PP(\text{simple}\mid F)\) and
\(\PP(\text{simple}\mid F_1,F_2)\) relative to \(\PP(\text{simple})\), to
relative error \(o(\delta^{-3})\). These are McKay enumerations for the
four-class degree sequences \((a_v),(m-a_v),(m-a_v),(\delta-2m+a_v)\).
That is the Gao21 step, at a general \(m\).

## Attack (superseded route)

Apply McKay enumeration ([McK85, Thm 4.6] = Gao21 Thm 14) to
\[
\PP(U\subseteq G)=\frac{N(\boldsymbol g,U)}{N(\delta\mathbf 1,\emptyset)},
\qquad
g_v=\delta-d_U(v).
\]
For \(F_1,F_2\) \(m\)-regular with \(K=|E(F_1)\cap E(F_2)|\) and
\(a_v=\) number of shared edges at \(v\) (\(\sum a_v=2K\)):
\[
d_U(v)=2m-a_v,
\qquad
g_v=\delta-2m+a_v.
\]
Expand \(\lambda(\boldsymbol g)+\lambda(\boldsymbol g)^2+\mu(\boldsymbol g,U)\) in
\(1/\delta\) about the \(a\equiv0\) point, average against the pair measure of
\((a_v)\) under \(\mu_m\otimes\mu_m\), and extract the coefficient of
\(1/\delta^3\). At \(m=1\) this must recover \(1/(6\delta^3)\).

Matching special case uses Corollary 15 of Gao21 (union is isolated edges +
cycles). For \(m\ge2\) the degree sequence is not of that shape; use the full
McKay parameters.

## Numerics

| n | δ | m | relvar (sample) | m²/δ³ | 1/(6δ³) |
|---|---|---|-----------------|-------|---------|
| 8 | 3 | 1 | 0.033 | 0.037 | 0.006 |
| 8 | 3 | 2 | 0.159 | 0.148 | 0.006 |
| 8 | 5 | 1 | 0.00054 | 0.008 | 0.0013 |
| 8 | 5 | 2 | 0.0020 | 0.032 | 0.0013 |

Ratio relvar(m=2)/relvar(m=1) ≈ 4 at δ=5, matching m².

## Screen

`config-second-moment --degree o(sqrt(n))` is CLEAR.
That screen does not prove the rate.

## Blocked substitute

Gao (RSA 2013) pair ratio \(m^2/(2\ell)\,(1+O(\ell/(mn)+m/n))\), summed to the
mode \(K=nm^2/(2\delta)\), has error budget
\(\exp(O(nm^3/\delta^2+m^3/\delta))\).
For fixed \(m\ge 2\) and \(\delta=o(n^{1/2})\) the budget tends to infinity
(Proposition switching-sparse-mode). Identities:
\((nm^2/(2\delta))^2/(2mn)=nm^3/(8\delta^2)\) and
\((nm^2/(2\delta))m/n=m^3/(2\delta)\). At \(\delta=n^{2/5}\) the first term is
\(\Theta(m^3 n^{1/5})\to\infty\).

A McKay probability with configuration-model \(\mu\), averaged on a
Poisson(\(m^2/2\)) overlap, produces a logarithm of size \(\Theta(n/\delta^2)\)
for \(m=2\). That is the same order as the budget, and it disagrees with
exact small graphs (relative variance about \(0.004\) on \(30\) simple
\(4\)-regular graphs on \(10\) vertices, against \(m^2/\delta^3=1/16\);
Remark eight-factors already has relative variance about \(5\cdot 10^{-4}\)
for \(2\)-factors of \(6\)-regular graphs on \(12\) vertices). Do not quote
that average as an asymptotic.

## Simple-graph transfer: what Gao21 Thm 14 does and does not give (2026-11-10)

McKay Thm 14 (= [McK85, Thm 4.6], quoted in Gao21 §3) counts simple graphs
with degrees g avoiding a fixed simple graph X, with relative error
O(hatDelta^2/m(g)), hatDelta = Delta(g)^2 + Delta(g)Delta(x), under
hatDelta = o(m(g)). It is stated for arbitrary X, not only matchings.

Applied to X = F1 u F2, g_v = delta - 2m + a_v: Delta(g) <= delta,
Delta(x) <= 2m <= 2 delta, so hatDelta <= 3 delta^2 and m(g) = Theta(delta n).
Hypothesis holds iff delta = o(n); error is O(delta^3/n), the same as Gao's
O(d^3/n) in Cor 15. So the probability P(F1 u F2 in G) is available for every
m <= delta with no loss relative to m = 1. (Gao Cor 15 is the special case where
the union is isolated edges + cycles, which gives a closed form; for m >= 2 the
exponent -lambda(g) - lambda(g)^2 - mu(g,X) must be kept as a function of (a_v)
and the edge sums sum_{ij in X} g_i g_j.)

**The real obstacle is not this probability.** E[Z^2] = sum over pairs of
m-regular graphs (F1,F2) of P(F1 u F2 in G). For m = 1, Gao Lemma 17 counts
pairs of perfect matchings by overlap k exactly (alternating cycles, EGF
exp(F)). For m >= 2 one needs the number of pairs of m-regular graphs with a
given overlap, and the exponent above depends on the joint law of (a_v) and
sum_{ij in X} g_i g_j, not only on k. At fixed m this is a pairing-model
computation; for growing m it is an enumeration of pairs of m-regular graphs
at the same level of difficulty as the original problem.

Still unproved: the delta -> infinity m-factor variance. Not attempted: whether
the 1-D pairing sum (Lemma factor-one-dim) can be coupled to the exponent
averaged over the pair measure; that coupling would replace the missing pair
count.
