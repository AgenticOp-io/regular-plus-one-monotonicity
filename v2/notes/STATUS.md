# v2.0 status

Bar is 2.0. v1.0 is sent.

## Closed (named)

- **factor-moment** (Theorem factor-moment): every linear host with
  \(n^{1/2}=o(L)=o(n)\) and \(\min(L,D-L)=\omega(n^{1/3})\).
- **factor-rate** (Theorem factor-rate / former Conjecture factor-rate):
  complementary, dense-host, linear length, and \(n^{3/4}=o(L)\).
- **factor-rate-mid** (Theorem factor-rate-mid-fail): residue
  \(287(1-\lambda)/(216\lambda\,na)\).
- **long-step** (Theorem long-step / long-step-all).
- **unconstrained residual** (Theorem residual-unconstrained).
- **residual-moment** (Theorem residual-moment / former Conjecture
  residual-moment at fixed \(m\)): every fixed \(m\ge 1\) on the McKay
  scale \(\delta(d+\delta)^2/n=o(1)\), including
  \(d=o(n^{3/8}(\log n)^{-1/3})\). Bern\(|\deg=\mathrm{Unif}(\Omega(C,g))\);
  constrained \(m\)-factor \(L^2\); window mixture.

## Open (named)

- **residual-moment-bim** (Conjecture residual-moment-bim): BIM length
  \(m=\Theta\sqrt{d\log n}\) with \(m\gg\sqrt\delta\). Needs sparse MLLT /
  residual-law comparison (Proposition residual-two-gaps).
  Proposition bim-residual-scale: formal package scale
  \(\Theta(n/(\delta m))\), vanishes iff
  \(d=\omega(n^{6/7}(\log n)^{-5/7})\), predicted diverge on
  \(d=o(n^{3/4}/\mathrm{polylog})\).
- **config-split**: open. Selection (iii) only on single orbits
  \(D\in\{1,n-2\}\). Proposition iii-two-sided:
  \(a-c_n=I_{\mathrm{low}}-I_{\mathrm{surv}}\); on \(n=6\) two-sided is
  \(0.019\,c_n\) (C₆) vs pointwise \(1.15\,c_n\), still not flat across types.
- **Q**: open; conditional on BIM Conjecture 1.3 (Theorem process-to-Q).

## Also open (not named)

- Peel second moment past \(n^{1/3}\) (Proposition peel-cubic-gap /
  peel-transfer-threshold / IM25 cancellation).
- Lower tail of the matching count \(Y\) (blocked routes unchanged).
- Residual-moment past McKay scale \(\delta(d+\delta)^2/n\not\to0\).

## Next

1. Sparse MLLT error at vanishing \(\lambda\) (or refute package persistence)
   for Conjecture residual-moment-bim.
2. Two-sided Stieltjes / tilt comparison → config-split → Q.
3. Averaged cubic in containment ratio → ordered peel past \(n^{1/3}\).

See `PROGRAM.md` for the full closed/blocked ledger.
