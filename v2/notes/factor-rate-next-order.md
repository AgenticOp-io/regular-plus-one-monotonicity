# Factor-rate-mid: \(a^{-1}\) second difference

Status: **closed for general \(\lambda\)** (Theorem factor-rate-mid-fail).
Residue \(\frac{287(1-\lambda)}{216\lambda\,na}\); relative variance
\(\sim\frac{287(1-\lambda)}{216\lambda\,L}\).
Packages:
\(\beta_{\mathrm{p64}}=\frac{1-\lambda}{2\lambda}\) and
\(\beta_{\mathrm{C35}}=\frac{5(1-\lambda)}{3\lambda}\) exact
(`scripts/beta_c35_lam.py`);
\(\beta_{\kappa_3}=-\frac{131(1-\lambda)}{108\lambda}\)
(`scripts/beta_k3_lam_float.py`, exact closed form at \(\lambda=1/2\));
\(\beta_{\kappa_4}=\frac{3(1-\lambda)}{8\lambda}\)
(`scripts/beta_k4_lam_grid.py`, exact closed form at \(\lambda=1/2\)).
Sum identity checked in `wolfram-checks.md`.

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

Exact (`scripts/beta_k3_fraction.py`, Lemma k3xxw-delta):
\[
\Delta d^{(3,3,4)}
=
\frac{4258a^2-2129a+262}{216\,a\,(2a-1)}
=
-\frac{131}{108\,a}+O(1)
\]
at \(\lambda=\tfrac12\). After the first three exact packages and \(\kappa_3\),
\[
\beta=\frac{13}{6}-\frac{131}{108}=\frac{103}{108}>0
\]
already, before \(\kappa_4\). Exact (`scripts/beta_k4_fraction.py`):
\[
a\Delta d^{(4)}
=
\frac{-1022a^2+511a-72}{192(2a-1)}
=
\frac38+O(a),
\]
checked at \(a\in\{1/8,1/10,1/12\}\) by integer Wick sums. Full residue
\(\frac{13}{6}+\frac38-\frac{131}{108}=\frac{287}{216}\)
(Theorem factor-rate-mid-fail).

## General \(\lambda\)

Exact \(\kappa_3\) second-difference samples at \(\lambda=2/5\)
(`scripts/beta_k3_fraction.py`):
\[
a\Delta d^{(3,3,4)}\in
\Bigl\{-\tfrac{791863}{1368576},-\tfrac{24001}{31104},-\tfrac{3261023}{3545856}\Bigr\}
\]
at \(a\in\{1/8,1/10,1/12\}\), with candidate residue
\(-\frac{131}{108}\cdot\frac{1-\lambda}{\lambda}=-\frac{131}{72}\).
Float extrapolation (`scripts/beta_k3_lam_float.py`) on
\(\lambda\in\{1/3,2/5,1/2,3/5,2/3\}\) matches that candidate to \(O(10^{-2})\).
\(\kappa_4\) grid (`scripts/beta_k4_lam_grid.py`, chunked Wick):

| \(\lambda\) | \(a\Delta\) at \(1/10\) | at \(1/20\) | \(b_0\sim 2y_{20}-y_{10}\) | cand \(\frac{3(1-\lambda)}{8\lambda}\) |
|------------:|------------------------:|------------:|---------------------------:|--------------------------------------:|
| \(2/5\) | 0.298 | 0.417 | 0.536 | 0.562 |
| \(1/2\) | 0.203 | 0.284 | 0.365 | 0.375 |
| \(3/5\) | 0.143 | 0.194 | 0.245 | 0.250 |

Errors are \(O(a)\) from the two-point linear fit.

## Mid window closed

Residue \(\frac{287(1-\lambda)}{216\lambda\,na}>0\) for \(\lambda\in(0,1)\).
Relative variance \(\Theta(1/L)\) throughout \(\sqrt n\ll L=O(n^{3/4})\).

Screen: `middle` — no blocked approach.

## Sparse host densities (\(\lambda\to0\), \(a=o(\lambda)\))

Lemma sparse-package-residues:
- C35 exact: \(\lambda=1/10\to15\), \(\lambda=1/5\to20/3\)
  (`scripts/beta_c35_lam.py`).
- \(\Phi_6+\tfrac12\mathrm{Var}W\) extrapolation
  (`scripts/next_order_sparse.py` / `pieces`):

| \(\lambda\) | \(a=\lambda/8\) | \(a=\lambda/16\) | \(2y_{16}-y_8\) | cand \((1-\lambda)/(2\lambda)\) |
|------------:|----------------:|-----------------:|---------------:|--------------------------------:|
| \(1/10\) | 5.101 | 4.779 | 4.457 | 4.5 |
| \(1/15\) | 8.029 | 7.481 | 6.933 | 7.0 |
| \(1/20\) | 10.961 | 10.185 | 9.409 | 9.5 |

Does not extend Theorem mllt-sparse; only the package residues.
