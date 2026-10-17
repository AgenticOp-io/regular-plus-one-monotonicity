# Factor-rate-mid: \(a^{-1}\) second difference

Status: obstruction recorded (Lemma phi6-varw-delta, Remark
factor-rate-mid-obstruction). Mid window still open.

## Exact package

The coefficient of \(n^{-1}\) in \(\EE\Phi_6+\tfrac12\operatorname{Var}W\) has
second difference
\[
\Delta d^{(6,4)}=\frac{1-\lambda}{2\lambda\,a}+O(1)
\]
as \(a\to0\) (`scripts/next_order_sparse.py`). Residue
\(\lim_{a\to0}a\Delta d^{(6,4)}=(1-\lambda)/(2\lambda)\) checked by exact
rational arithmetic at \(\lambda\in\{1/3,2/5,1/2,3/5,3/4\}\) (errors \(O(a)\)
at \(a=1/40\)). At \(\lambda=1/2\) the series refines to
\(\frac1{2a}-\frac38+O(a)\). So this package alone gives
\(\frac{1-\lambda}{2\lambda\,na}+O(n^{-1})\) in \(\Delta\operatorname{Re}h\).

## Partial \(\kappa_4\)

`scripts/beta_second_diff.py` adds star+path diagrams for \(\kappa_4(X)/24\).
On the grid \(a\in\{1/5,\ldots,1/20\}\),
\[
D\cdot a\in[0.56,0.60]
\]
(larger than \(1/2\)), so those diagrams do not cancel the \(a^{-1}\) pole.
Mixed-factor (non-additive) pieces are visible: at \(a=1/10\),
\(d_3^{(\kappa_4)}\approx4.31>2\cdot1.74\approx d_2\) additivity.

## Exact C35 package

At \(\lambda=1/2\),
\[
\Delta d^{(3,5)}
=
\frac{-104a^2+52a-5}{3a(2a-1)}
=
\frac5{3a}-14+O(a)
\]
(`scripts/beta_c35_exact.py`). So \(-\operatorname{Cov}(X,\Im\Phi_5)\) alone
gives \(\frac5{3na}+O(n^{-1})\). Combined with
\(\Delta d^{(6,4)}=\frac1{2a}-\frac38+O(a)\), the two packages sum to
\(\frac{13}{6na}+O(n^{-1})\).

## Inventory beyond those two (`scripts/beta_full_inventory.py`)

At \(\lambda=1/2\), second-difference residues \(a\Delta d\) on a grid:

| \(a\) | \(a\Delta_{\mathrm{p64}}\) | \(a\Delta_{\kappa_4}\) | \(a\Delta_{\mathrm{C35}}\) | \(a\Delta_{\kappa_3}\) | \(a\Delta_{\mathrm{tot}}\) |
|------:|--------------------------:|----------------------:|-------------------------:|----------------------:|-------------------------:|
| 1/8   | 0.495 | 0.070 | 0.056 | −0.110 | 0.511 |
| 1/10  | 0.488 | 0.083 | 0.350 | −0.147 | 0.773 |
| 1/12  | 0.485 | 0.092 | 0.556 | −0.174 | 0.959 |
| 1/16  | 0.485 | 0.104 | 0.821 | −0.209 | 1.202 |
| 1/20  | 0.487 | 0.112 | 0.985 | −0.231 | 1.353 |

All three \(n^5\)-scale trees for \(\kappa_4(X)\) (star, path, fork) and both
\(n^4\)-scale diagrams for \(\kappa_3(X,X,W)\) (star and path) shift the
residue by \(O(1)\) but do not cancel \(\frac{13}{6}\). At \(a=1/40\),
\[
\begin{align*}
a\Delta_{\kappa_4}&\approx0.328
\quad(\mathrm{star}\,0.092+\mathrm{path}\,0.037+\mathrm{fork}\,0.200),\\
a\Delta_{\kappa_3}&\approx-1.030
\quad(\mathrm{star}\,-0.277+\mathrm{path}\,-0.754).
\end{align*}
\]
Net \(\kappa_4+\kappa_3\approx-0.70\), against \(\frac{13}{6}\approx2.17\) from
the two exact packages. Full inventoried sum (`beta_inventory_run.py`):

| \(a\) | \(a\Delta_{\mathrm{tot}}\) |
|------:|---------------------------:|
| 1/10  | 0.510 |
| 1/20  | 0.901 |
| 1/40  | 1.111 |

Linear extrapolation suggests \(\beta_{\mathrm{inv}}\approx\frac43>0\).
Lemma a-minus-two-class in the paper asserts these five packages exhaust the
\(a^{-2}\) class (so the tail is \(o(1/(na))\) for \(a=\omega(n^{-1/2})\)).
The remaining gap is an exact evaluation of
\(\lim_{a\to0}a\Delta(\kappa_4/24-\kappa_3/6)\); if that limit is greater than
\(-\frac{13}{6}\), Conjecture factor-rate-mid fails.

## What would close the mid window

1. **Cancel:** full \(\beta_3+\beta_1-2\beta_2=0\) over every degree-6/8/10/12
   contraction in \(\operatorname{Re}h\) → extend Theorem factor-rate to all
   \(L\gg\sqrt n\).
2. **Match:** prove \(\Delta\operatorname{Re}h\sim\frac{c}{na}\) with \(c>0\) →
   Conjecture factor-rate-mid fails (relative variance \(\Theta(1/L)\)).

Screen: `middle` — no blocked approach.
