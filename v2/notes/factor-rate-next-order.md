# Next-order constant for factor-rate-mid

Status: Theorem factor-rate closed for \(n^{3/4}=o(L)\). Workshop below is for
Conjecture factor-rate-mid (\(\sqrt n\ll L=O(n^{3/4})\)).

## Settled

- \(a^{-2}\) second difference vanishes (Lemma sparse-second-diff).
- Ratio error \(O(1/(na))\), hence rate when \(a=\omega(n^{-1/4})\).

## Partial computation

`scripts/next_order_sparse.py`: the \(\EE\Phi_6+\tfrac12\operatorname{Var}W\) second
difference is \(\sim 1/(2a)\) as \(a\to0\) (exact series at \(\lambda=1/2\)).
Star diagrams in \(\kappa_4(X)/24\) are additive (\(\Delta=0\) under the
\((m-1)\) law). If no further cancellation occurs, the true ratio excess is
\(\Theta(1/(nL))\) and Conjecture factor-rate-mid fails; a matching lower bound
is not yet a theorem.

## Attack

Compute the full coefficient \(\beta_3+\beta_1-2\beta_2\) of \(a^{-1}\) over every
degree-\(8\) (and degree-\(6\)) contraction in \(\operatorname{Re}h_m\). If it
vanishes, extend Theorem factor-rate to every \(n^{1/2}=o(L)\). If it equals
\(1/2\), prove the matching lower bound and close the mid window in the negative.

Screen: no blocked approach.
