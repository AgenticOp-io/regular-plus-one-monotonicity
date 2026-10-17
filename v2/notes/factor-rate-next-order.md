# Next-order constant for factor-rate below \(n^{4/5}\)

Status: workshop. Not a theorem.

## Current theorem

Corollary factor-rate-sparse: if \(n^{4/5}=o(L)\) with linear co-length and
complement, then \(\Var Z_L/(\EE Z_L)^2=o(L^3/n^3)\).
Proof: Theorem factor-moment-sparse gives error \(O(n^{-1}a^{-2})\), and
\(1/(na^5)\to0\) iff \(a=\omega(n^{-1/5})\).

## Sources of the \(1/(na^2)\) term

Under the rescaled Gaussian of Lemma edge-cumulants, every even joint
cumulant of total degree \(\ge8\) in the edge variables is
\(O(n(na)^{-2})=O(n^{-1}a^{-2})\). Contributors include:

- \(\kappa_1(\Phi_6)\), \(\kappa_1(\Phi_8),\ldots\) (even homogeneous means)
- \(\operatorname{Var}W=\kappa_2(\Phi_4)\)
- \(\kappa_4(X)\) and mixed \(\kappa(X,X,W)\), \(\kappa(X,W,W)\), \ldots
- For \(m=1\) (no factor coordinate) the same graphs give only \(O(1/n)\),
  since \(\Sigma=\varLambda\) is bounded away from zero.

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
threshold. If \(D\not\equiv0\), the true rate is \(\Theta(1/(na^2))\) on
that range and Conjecture factor-rate fails below \(n^{4/5}\).

Screen: no blocked approach. Do not confuse with the blocked
config-second-moment or binomial-PGF attacks.
