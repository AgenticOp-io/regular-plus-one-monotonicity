# v2.0 status

Bar is 2.0. v1.0 is sent.

## Closed

- Factor second moment for near-complete lengths \(D-L=o(n^{1/3})\), including
  past \(\sqrt{n}\) (Theorem factor-complementary): complementation in the host
  plus the \(o(n^{1/3})\) moment of v1.
- Factor second moment for near-complete hosts throughout the McKay range
  \(\ell(s+\ell)^2/n=o(1)\) for every \(\ell\ge 1\) (Theorem factor-dense-host),
  including co-length one with \(n-D=o(n^{1/2})\); McKay enumeration on the
  sparse complement (the \(L\to\infty\) in v1 free-flat-L is not required).
- Factor second moment for co-length one on every sublinear host \(D=o(n)\)
  (Theorem factor-sublinear-colength-one), including past \(\sqrt{n}\); from the
  matching variance in the sublinear nesting theorem of v1.
- Factor rate on the linear and near-complete-host sides (Theorems
  factor-rate-complementary, factor-rate-dense-host); strengthened to
  \(O(1/n)\) when \(D-L=1\) on linear hosts.
- Long deletion past \(\sqrt{n}\) from degree \(o(n^{1/3})\) to near-complete
  (Theorem long-sparse-near-complete): free split plus complementation.
- Long deletion past \(\sqrt{n}\) leaving a matching gap
  (Theorem long-matching-gap): for every \(d\le n/2-1\), Dirac on the complement
  plus \(S_n\)-transitivity gives \(G\sim\mu_d\subset H\sim\mu_{n-2}\) a.s.; the
  linear band \(d>n/2-1\) uses matching concentration instead. Gap
  \(n-d-L=2\).
- Long nesting from a matching into every Dirac host \(D\ge n/2\)
  (Theorem long-matching-into-dirac): same Dirac + transitivity, upper degree
  any \(D\in[n/2,n-1]\).
- Long nesting of a matching into every growing degree
  (Theorem long-matching-growing): below \(n/2\), band-rate or the sublinear
  matching variance replaces Dirac; failure probability \(o(1)\); both
  marginals exact. Includes \(\omega(\sqrt{n})=D=o(n)\).
- Co-length one near half degree: relative variance \(O((t^2+1)/n^2)\) at
  host degree \(n/2+t\) (distance-rate), sharpening the \(O(1/n)\) bound.
- Selection item (iii) on single \(S_n\) orbits \(D\in\{1,n-2\}\)
  (Corollary iii-one-orbit); not a config-split close at Chernoff scale.

## Still open (named)

- Q, config-split, residual-moment: fully open.
- factor-moment, factor-rate: open only for \(\min(L,D-L)=\omega(n^{1/3})\).
- long-step: open under four linear margins; sparse-to-near-complete,
  matching-gap-to-\((n-2)\), and matching-into-Dirac are closed.

## Recorded negatives (not conjecture closes)

- Sprinkle / sandwich / literal peel flatnesses blocked on six vertices.
- Switches, switch-BFS, switch-path flattening of \(a\): all miss.
- Near-disjoint and edge-disjoint packing miss bulk.
- Independence-approx \(\mathrm{Var}N/(\mathbb{E}N)^2=\exp(\Theta(Dn))\); G0-edge factors cancel.
- Tilt need not help: on \(n=6\), tilted/untilted \(\mathbb{E}[p^{-\Delta}]\approx 0.551\).
- Independent indicators / crude Azuma / moments about \(\mathbb{E}[N]\): miss bulk lower tail.
- Item (iii) = Laplace / weighted lower-tail integral; \(n=6\) criterion fails with non-flat \(a\).
- Residual-moment lives on nearly regular degrees of scale \(\varepsilon_0 d\).
- Signed Gao after matching host leaves \(\Theta(L/n)\) per step.

## Next

1. Signed comparison on balanced \(\min(L,D-L)=\omega(n^{1/3})\) (Workstream A).
2. Lower-tail of \(N\) at \(1/c_n\) under true tilted \(\mu_D\) dependence
   (Workstream B).
3. Four-linear-margin long-step, or residual-moment on the nearly regular
   window.

See `PROGRAM.md` for the full closed/blocked ledger.
