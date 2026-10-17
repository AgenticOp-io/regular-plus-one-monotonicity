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
  Lemma a-minus-two-class: only five packages can affect the \(a^{-1}\)
  residue. At \(\lambda=1/2\) the first three give \(\frac{13}{6na}\); the
  \(\kappa_4+\kappa_3\) residue extrapolates to \(-\frac56\), total
  \(\frac43/(na)>0\) (notes/factor-rate-next-order.md). Confirm
  \(-\frac56\) exactly to refute the conjecture.
- **Q**, **config-split**, **residual-moment** (BIM-constrained): open.
  Selection (iii) only on single orbits \(D\in\{1,n-2\}\).
  Unconstrained residual is closed; the host restriction is the obstruction.
  Q is conditional on BIM Conjecture 1.3 (Theorem process-to-Q).

## Also open (not named)

- Peel second moment past \(n^{1/3}\) (ordered peel \(P_L\)).
- Lower tail of the matching count \(Y\).

## Next

1. Factor-rate-mid: exact \(\kappa_4+\kappa_3\) residue (refute if \(>-13/6\)).
2. Host-restricted residual-moment → config-split → Q.
3. Ordered peel \(P_L\) past \(n^{1/3}\).

See `PROGRAM.md` for the full closed/blocked ledger.
