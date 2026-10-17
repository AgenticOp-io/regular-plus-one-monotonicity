# v2.0 status

Bar is 2.0. v1.0 is sent.

## Closed (named)

- **factor-moment** (Theorem factor-moment): every linear host with
  \(n^{1/2}=o(L)=o(n)\) and \(\min(L,D-L)=\omega(n^{1/3})\).
- **factor-rate** (Theorem factor-rate / former Conjecture factor-rate):
  complementary, dense-host, linear length, and \(n^{3/4}=o(L)\).
  Proof of the sparse side: Lemma sparse-second-diff kills \(a^{-2}\) in the
  ratio, leaving \(O(1/(na))=o(a^3)\) iff \(a=\omega(n^{-1/4})\).
- **long-step** (Theorem long-step / long-step-all): every \(L\ge1\) with two
  linear margins.
- **unconstrained residual** (Theorem residual-unconstrained): factor-moment
  on a uniform \(\delta\)-regular host (no BIM edge restriction).

## Open (named)

- **factor-rate-mid**: \(\sqrt n\ll L=O(n^{3/4})\).
  Obstruction: \(\EE\Phi_6+\tfrac12\operatorname{Var}W\) alone gives
  \(\Delta=1/(2na)+O(1/n)\) (Lemma phi6-varw-delta); star/path \(\kappa_4\)
  does not cancel it (notes/factor-rate-next-order.md). Full cancel or matching
  lower bound still needed.
- **Q**, **config-split**, **residual-moment** (BIM-constrained): open.
  Selection (iii) only on single orbits \(D\in\{1,n-2\}\).
  Unconstrained residual is closed; the host restriction is the obstruction.
  Q is conditional on BIM Conjecture 1.3 (Theorem process-to-Q).

## Also open (not named)

- Peel second moment past \(n^{1/3}\) (ordered peel \(P_L\)).
- Lower tail of the matching count \(Y\).

## Next

1. Factor-rate-mid: remaining packages vs \(\frac1{2na}\) (cancel or match).
2. Host-restricted residual-moment → config-split → Q.
3. Ordered peel \(P_L\) past \(n^{1/3}\).

See `PROGRAM.md` for the full closed/blocked ledger.
