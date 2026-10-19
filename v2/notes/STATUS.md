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
- **residual-moment** (Theorem residual-moment): every
  \(m=o(\sqrt\delta)\) on the McKay scale
  \(\delta(d+\delta)^2/n=o(1)\), including
  \(d=o(n^{3/8}(\log n)^{-1/3})\). Bern\(|\deg=\mathrm{Unif}(\Omega(C,g))\);
  Gao relative error \(O(\delta^2 m/n)\); overlap leftover \(O(m^2/\delta)\);
  window mixture. (Upgraded from fixed \(m\), then from \(m=o(\delta^{1/3})\).)

## Open (named)

- **residual-moment-bim** (Conjecture residual-moment-bim): BIM length
  \(m=\Theta\sqrt{d\log n}\) with \(m/\sqrt\delta\to\infty\). Needs sparse MLLT /
  residual-law comparison (Proposition residual-two-gaps).
  Proposition bim-residual-scale: formal package scale
  \(\Theta(n/(\delta m))\) (conditional on residue persistence).
  Proposition package-not-persist: that residue cannot persist at \(m=1\),
  since matching variance is \(1/(6\delta^3)\to0\) while \(\Theta(n/\delta)\to\infty\).
  Proposition mllt-vanishing-margin: linear-margin weights degrade to
  \(\Theta(\lambda)\) as \(\lambda\to0\), so Theorem mllt-sparse does not transfer.
- **config-split**: open. Selection (iii) only on single orbits
  \(D\in\{1,n-2\}\). Proposition iii-two-sided:
  \(a-c_n=I_{\mathrm{low}}-I_{\mathrm{surv}}\); on \(n=6\) two-sided is
  \(0.019\,c_n\) (C₆) vs pointwise \(1.15\,c_n\); on \(n=8\) MC,
  \(C_5\cup C_3\) still \(\approx 0.09\,c_n\) below the mean.
- **Q**: open; conditional on BIM Conjecture 1.3 (Theorem process-to-Q).

## Also closed (strengthening / obstruction)

- **peel-second-moment-third** (two-sided sandwich): Lemmas avoid-overlap
  (factor case) and decomp-overlap are two-sided; Theorem
  peel-second-moment-third is now
  \(\exp(\pm C(L^3+1)/n)\) rather than a one-sided upper bound.
  Range still \(L=o(n^{1/3})\) for variance \(\to0\); the gap remains the
  averaged cubic (Proposition peel-cubic-gap).
- **package-not-persist** (Proposition package-not-persist): mid-window
  five-package residue cannot persist at matching length on sparse hosts.

## Also open (not named)

- Peel second moment past \(n^{1/3}\) (Proposition peel-cubic-gap /
  peel-transfer-threshold). Containment and decomposition overlap are both
  two-sided; the gap remains the averaged \(O(L^3/n)\) after quadratic
  cancellation.
- Lower tail of the matching count \(Y\) (blocked routes unchanged).
- Residual-moment past McKay scale \(\delta(d+\delta)^2/n\not\to0\).

## Next

1. Sparse-host leading term for \(m\)-factor variance (not the mid-window
   residue) / config-model → Conjecture residual-moment-bim.
2. Tilt comparison under \(\mu_D\) / orbit-flat inverse counts → config-split.
3. Cancel the averaged cubic in the two-sided containment ratio → peel
   past \(n^{1/3}\).

See `PROGRAM.md` for the full closed/blocked ledger.
