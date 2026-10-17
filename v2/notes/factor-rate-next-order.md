# Next-order constant for factor-rate below \(n^{3/4}\)

Status: the \(a^{-2}\) second difference is settled
(Lemma sparse-second-diff in the paper). Workshop below is for the
remaining \(1/(na)\) term.

## Current theorem

Corollary factor-rate-sparse: if \(n^{3/4}=o(L)\) with linear co-length and
complement, then \(\Var Z_L/(\EE Z_L)^2=o(L^3/n^3)\).
Proof: Lemma sparse-second-diff gives error \(O(n^{-1}a^{-1})\) in the
ratio, and \(1/(na^4)\to0\) iff \(a=\omega(n^{-1/4})\).

## What cancelled

Precision \(\Sigma_m^{-1}=a^{-1}J_m+O(1)\) with \(J_m\) an orthogonal sum of
\(m-1\) factor projectors and \((\Sigma_3^{-1})_{F_1F_2}=0\)
(Lemma precision-lead). Weight-\(a^{-2}\) Wick diagrams are additive over
factor colours, so \(\alpha_m=(m-1)\alpha_2\) and
\(\alpha_3+\alpha_1-2\alpha_2=0\).

Checked explicitly (scripts/next_order_sparse.py): for \(\EE\Phi_6\) and
\(\tfrac12\operatorname{Var}W\) at \(\lambda\in\{1/2,2/5,3/4\}\),
\[
[a^{-2}]\,d_3=2\,[a^{-2}]\,d_2,\qquad [a^{-2}]\,d_1=0,
\]
and the residual second difference is \(\sim 1/(2a)\) (coefficient of
\(1/(na)\)).

## Still open

The coefficient \(\beta_3+\beta_1-2\beta_2\) of \(a^{-1}\) in the second
difference. If it vanishes, factor-rate extends to every
\(n^{1/2}=o(L)\). If not, the true rate on \(\sqrt n\ll L=O(n^{3/4})\) is
\(\Theta(1/(nL))\) and the conjecture fails there.

Screen: no blocked approach.
