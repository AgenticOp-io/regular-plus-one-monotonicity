# v2.0 status

Bar is 2.0. v1.0 is sent.

## Closed (named)

- **factor-moment** (Theorem factor-moment): every linear host with
  \(n^{1/2}=o(L)=o(n)\) and \(\min(L,D-L)=\omega(n^{1/3})\).
- **factor-rate** (Theorem factor-rate / former Conjecture factor-rate):
  complementary, dense-host, linear length, and \(n^{3/4}=o(L)\).
  Proof of the sparse side: Lemma sparse-second-diff kills \(a^{-2}\) in the
  ratio, leaving \(O(1/(na))=o(a^3)\) iff \(a=\omega(n^{-1/4})\).
- **factor-rate-mid** (Theorem factor-rate-mid-fail / former Conjecture
  factor-rate-mid): residue
  \(\Delta\operatorname{Re}h\sim\frac{287(1-\lambda)}{216\lambda\,na}\) from the
  five \(a^{-2}\)-class packages (exact \(\Phi_6+\tfrac12\mathrm{Var}W\) and
  C35 on a \(\lambda\)-grid; exact \(\kappa_3,\kappa_4\) at \(\lambda=1/2\);
  float second-difference extrapolation for \(\kappa_3,\kappa_4\) at general
  \(\lambda\)), so
  \(\Var Z/(\EE Z)^2\sim\frac{287(1-\lambda)}{216\lambda\,L}\ne o(L^3/n^3)\)
  for \(\sqrt n\ll L=O(n^{3/4})\).
- **long-step** (Theorem long-step / long-step-all): every \(L\ge1\) with two
  linear margins.
- **unconstrained residual** (Theorem residual-unconstrained): factor-moment
  on a uniform \(\delta\)-regular host (no BIM edge restriction).
- **residual matching first moment** (Theorem residual-matching-mean /
  Corollary residual-first-moment): Bernoulli residual has
  \(\EE[Y(R)|G]=p^{n/2}Z_\partial(G)\).
- **residual-moment at \(m=1\), McKay scale** (Theorem residual-moment-m1):
  Bern\(|\deg=\mathrm{Unif}(\Omega(C,g))\); constrained matching \(L^2\) on
  \(\Omega(C,\delta)\); window means flat; closes Conjecture residual-moment
  at \(m=1\) whenever \(\delta(d+\delta)^2/n=o(1)\), including
  \(d=o(n^{3/8}(\log n)^{-1/3})\).

## Open (named)

- **residual-moment** (BIM-constrained): open at BIM length
  \(m=\Theta\sqrt{d\log n}\) (needs sparse MLLT + residual-law comparison;
  Proposition residual-two-gaps). At \(m=1\), closed on the McKay scale
  (Theorem residual-moment-m1); open past \(\delta(d+\delta)^2/n\not\to0\).
  Package residues as \(\lambda\to0\) with \(a=o(\lambda)\): Lemma
  sparse-package-residues.
- **config-split**: open. Selection (iii) only on single orbits
  \(D\in\{1,n-2\}\); needs lower-tail of \(N\) at \(1/c_n\) (pointwise
  Proposition iii-as-tail, or the weaker weighted integral
  Proposition iii-weighted-tail) plus asymptotic peel-weight flatnesses
  on \(G^*_0\).
- **Q**: open; conditional on BIM Conjecture 1.3 (Theorem process-to-Q).

## Also open (not named)

- Peel second moment past \(n^{1/3}\) (ordered peel \(P_L\)).
  Proposition peel-transfer-threshold: multiplicative \(D(F)\)-flatness on
  the \(\mu_L\)-bulk would transfer Theorem factor-moment past
  \(n^{1/3}\); FJS precision is not enough (Remark fjs-not-flat). Alternate
  route: IM25 cubic cancellation after Proposition im-containment.
- Lower tail of the matching count \(Y\) (blocked routes unchanged).

## Next

1. Sparse MLLT / residual-law comparison for BIM-length residual-moment;
   extend constrained matching past McKay scale.
2. Weighted/pointwise lower-tail of \(N\) at \(1/c_n\) → config-split → Q.
3. \(D(F)\)-flatness or IM25 cancellation for ordered peel past \(n^{1/3}\).

See `PROGRAM.md` for the full closed/blocked ledger.
