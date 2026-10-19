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

## Attack

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
