# Next-order constant for factor-rate below \(n^{4/5}\)

Status: workshop. Not a theorem.

## Setup

Theorem mllt-sparse gives
\[
\log\frac{N_3N_1}{N_2^2}=O(n^{-1}a^{-2})
\]
after the exact cancellation \(c_3+c_1-2c_2=0\). Factor-rate needs
\(o(a^3)\). The bound \(O(1/(na^2))\) is \(o(a^3)\) iff \(a\gg n^{-1/5}\),
i.e. \(L\gg n^{4/5}\) (Corollary factor-rate-sparse).

## Sources of the \(1/(na^2)\) term

Under the rescaled Gaussian of Lemma edge-cumulants, every even joint
cumulant of total degree \(\ge8\) in the edge variables is
\(O(n(na)^{-2})=O(n^{-1}a^{-2})\). Contributors include:

- \(\kappa_1(\Phi_6)\), \(\kappa_1(\Phi_8),\ldots\) (even homogeneous means)
- \(\operatorname{Var}W=\kappa_2(\Phi_4)\)
- \(\kappa_4(X)\) and \(\kappa(X,X,W)\), \(\kappa(X,W,W)\), \ldots
- cross terms in \(\operatorname{Re}(\sum\kappa_r/r!)\)

Odd cumulants affect only the phase and drop from the modulus.

## Attack

Compute the coefficient \(d_m(a,\lambda)\) of \(n^{-1}\) in
\(\operatorname{Re}\sum_{r\le s}\kappa_r^{(m)}/r!\) as a rational function of
\((a,\lambda)\), for \(m\in\{1,2,3\}\), through the Wick pairings of total
degree 8 (leading sparse order). Then test
\[
D:=d_3+d_1-2d_2
\]
on a rational grid. If \(D\equiv0\), factor-rate extends to the next
threshold (likely \(a\gg n^{-1/4}\) or better, depending on the following
term). If \(D\not\equiv0\), the true rate is \(\Theta(1/(na^2))\) and
factor-rate fails below \(n^{4/5}\).

Screen: no blocked approach. Do not confuse with the blocked
config-second-moment or binomial-PGF attacks.
