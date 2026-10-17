# v2.0 status

Bar is 2.0. v1.0 is sent.

## Closed (named)

- **factor-moment** (Theorem factor-moment / former Conjecture factor-moment):
  \(\Var Z/(\EE Z)^2=o(1)\) whenever \(\min(D,n-D)=\Theta(n)\) and
  \(n^{1/2}=o(L)=o(n)\) with \(\min(L,D-L)=\omega(n^{1/3})\).
  Proof: complementary sides + linear-below-sqrt for \(L^2=o(n)\) +
  multi-colour LLT (mllt / mllt-sparse) with \(c_3+c_1-2c_2=0\) and WLOG
  \(L\le D/2\) by complementation. Sparse range:
  \(a\ge\omega(n)\,n^{-1/2}\) any \(\omega\to\infty\), signed annulus of width
  \(K(na)^{-1/2}\), even-cumulant modulus \(O(n^{-1}a^{-2})=O(\omega^{-2})\).
- **long-step** (Theorem long-step / long-step-all): coupling
  \(\PP(G_d\subseteq G_{d+L})=1-o(1)\) for every \(L\ge1\) with two linear
  margins.

## Partially closed (named)

- **factor-rate**: closed for linear \(L\) and for \(n^{3/4}=o(L)\)
  (Corollaries factor-rate-linear, factor-rate-sparse); complementary /
  dense-host sides closed. Open for \(n^{1/2}\ll L=O(n^{3/4})\).
  The \(a^{-2}\) second difference vanishes
  (Lemma sparse-second-diff / precision-lead); error in the ratio is
  \(O(1/(na))\), hence the \(n^{3/4}\) threshold.

## Still open (named)

- **Q**, **config-split**, **residual-moment**: fully open.
  Selection (iii) only on single orbits \(D\in\{1,n-2\}\).

## Also open (not named)

- Peel second moment past \(n^{1/3}\) (two-sided cubic cancellation for \(P_L\)).
- Lower tail of the matching count \(Y\).

## Next

1. Factor-rate on \(\sqrt n\ll L=O(n^{3/4})\): cancel the \(1/(na)\)
   second difference (or prove a matching lower bound).
2. Residual-moment on the nearly regular BIM window → config-split → Q.
3. Ordered peel \(P_L\) past \(n^{1/3}\).

See `PROGRAM.md` for the full closed/blocked ledger.
