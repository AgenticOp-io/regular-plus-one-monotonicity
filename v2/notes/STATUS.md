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
- **residual-moment** (Theorem residual-moment): matchings \(m=1\) on the
  McKay scale \(\delta(d+\delta)^2/n=o(1)\). The extension to
  \(1<m=o(\sqrt\delta)\) was withdrawn: the uniform-overlap factor
  \(1+O(K/\delta)\) does not control the second moment
  (Proposition overlap-mass). That range is part of
  Conjecture residual-factor-sharp.

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

1. **Mostly closed 2026-11-11**: Theorem growing-degree-factor gives
   relvar -> 0 for every m with delta^3=o(n), min(m,delta-m)^7=o(delta^2 n),
   min(m,delta-m) <= (1/2-c) delta (covers the BIM range on the McKay
   scale). Still open there: the rate itself, the band m ~ delta/2, nearly
   regular hosts, and the residual-law comparison.
   Original item: prove Conjecture residual-factor-sharp (rate \(O(m^2/\delta^3)\), length
   \(m=o(\delta^{3/2})\), including the withdrawn range \(m=o(\sqrt\delta)\)):
   Laplace at overlap \(K\sim nm^2/(2\delta)\), not at the uniform mean
   \(\Theta(m^2)\). The switching bound \(O(\ell/(mn)+m/n)\) accumulates to
   \(\exp(O(nm^3/\delta^2))\) on that overlap and does not tend to \(1\) for
   \(m\ge 2\) (Proposition switching-sparse-mode). At BIM scales
   \(m^2/\delta^3=\Theta(1/d)\to0\) (Proposition residual-sharp-bim).
   **Fixed degree closed** (Theorem fixed-degree-factor): for fixed
   \(\delta\ge3\) and every \(1\le m\le\delta-1\), relvar \(\to
   \exp(\sum_{k\ge3}x^k/(2k))-1\), \(x=1/(\delta-1)\), the matching limit,
   \(m\)-free. The pairing second moment is an exact 1-D hypergeometric sum
   (Lemma factor-one-dim), so there is no overlap-window problem. The gap
   left for \(\delta\to\infty\) is the passage from the pairing to the simple
   graph at relative error \(o(\delta^{-3})\) (Remark fixed-degree-sharp).
   The one-dimensional overlap sum does not determine the McKay weight for
   \(m\ge 2\): \(\lambda\) depends on \(\sum(a_v-\bar a)^2\), and at the mean
   profile the linear shift of \(\lambda^2\) is \(m^2/(2\delta)+O(\delta^{-2})\)
   (Proposition overlap-not-weight). That is not yet a conditional-on-\(A\)
   estimate. At \(m=1\) the exponent at overlap \(1/\delta\) is exactly the
   loop and double-edge correction (Proposition mode-phi).
2. Tilt comparison under \(\mu_D\) / orbit-flat inverse counts → config-split.
3. Cancel the averaged cubic in the two-sided containment ratio → peel
   past \(n^{1/3}\).

See `PROGRAM.md` for the full closed/blocked ledger.
