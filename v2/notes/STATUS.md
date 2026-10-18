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

## Open (named)

- **residual-moment** (BIM-constrained): open.
  Unconstrained fixed-length \(m\)-factor moment at \(\delta=o(n^{1/2})\) is
  Theorem residual-factor-fixed. At \(m=1\), second-moment gap on \(\mu_\delta\)
  is closed; remaining gap is first-moment/contiguity of \(R\) with
  \(\mu_\delta\) (Corollary residual-matching-proxy,
  Proposition residual-to-peel-weight). At BIM length
  \(m=\Theta\sqrt{d\log n}\) one has \(m\gg\sqrt\delta\), so unconstrained
  item needs sparse MLLT; residual-law comparison still open
  (Proposition residual-two-gaps). Linear unconstrained is
  Theorem residual-unconstrained.
- **config-split**: open. Selection (iii) only on single orbits
  \(D\in\{1,n-2\}\); needs lower-tail of \(N\) at \(1/c_n\) plus asymptotic
  peel-weight flatnesses on \(G^*_0\).
- **Q**: open; conditional on BIM Conjecture 1.3 (Theorem process-to-Q).

## Also open (not named)

- Peel second moment past \(n^{1/3}\) (ordered peel \(P_L\)).
  Lemma peel-from-factor: \(D(F)\)-flatness would transfer factor-moment;
  FJS precision is not enough for \(M/m\to1\) (Remark fjs-not-flat).
- Lower tail of the matching count \(Y\) (blocked routes unchanged).

## Next

1. Contiguity of BIM residual \(R\) with \(\mu_\delta\) (\(m=1\)), or config-model
   \(m\)-factor moment at \(\delta=o(n^{1/2})\).
2. Selection (iii) / lower-tail of \(N\) → config-split → Q.
3. IM25 cancellation for ordered peel past \(n^{1/3}\).

See `PROGRAM.md` for the full closed/blocked ledger.
