# Factor-rate-mid: \(a^{-1}\) second difference

Status: obstruction recorded (Lemma phi6-varw-delta, Remark
factor-rate-mid-obstruction). Mid window still open.

## Exact package

At \(\lambda=1/2\), the coefficient of \(n^{-1}\) in
\(\EE\Phi_6+\tfrac12\operatorname{Var}W\) has second difference
\[
\Delta d^{(6,4)}=\frac1{2a}-\frac38+O(a)
\]
(`scripts/next_order_sparse.py`, exact sympy series). So this package alone
gives \(\frac1{2na}+O(n^{-1})\) in \(\Delta\operatorname{Re}h\).

## Partial \(\kappa_4\)

`scripts/beta_second_diff.py` adds star+path diagrams for \(\kappa_4(X)/24\).
On the grid \(a\in\{1/5,\ldots,1/20\}\),
\[
D\cdot a\in[0.56,0.60]
\]
(larger than \(1/2\)), so those diagrams do not cancel the \(a^{-1}\) pole.
Mixed-factor (non-additive) pieces are visible: at \(a=1/10\),
\(d_3^{(\kappa_4)}\approx4.31>2\cdot1.74\approx d_2\) additivity.

## What would close the mid window

1. **Cancel:** full \(\beta_3+\beta_1-2\beta_2=0\) over every degree-6/8/10/12
   contraction in \(\operatorname{Re}h\) → extend Theorem factor-rate to all
   \(L\gg\sqrt n\).
2. **Match:** prove \(\Delta\operatorname{Re}h\sim\frac{c}{na}\) with \(c>0\) →
   Conjecture factor-rate-mid fails (relative variance \(\Theta(1/L)\)).

Screen: no blocked approach.
