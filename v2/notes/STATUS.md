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
- Uniform Hamilton cycle inside every Dirac host \(D\ge n/2\)
  (Theorem long-hamilton-dirac). The cycle marginal is uniform on Hamilton
  cycles, not on \(2\)-regular graphs.
- The same coupling for every degree \(D\ge 3\) (Theorem long-hamilton-wide):
  fixed degree by Robinson–Wormald, degrees from \(10^7\) up to a small linear
  fraction by Cooper–Frieze–Reed, and degrees above \(\sqrt{n}\log n\) by
  Krivelevich–Sudakov–Vu–Wormald. Failure probability \(o(1)\); both marginals
  exact. The gap is still \(\omega(\sqrt{n})\) above \(\sqrt{n}\log n\). Not
  \(\mu_2\), and not selection (iii).
- Uniform perfect matching inside every degree \(D\ge 3\), including degrees
  that stay bounded or oscillate (Theorem long-matching-at-least-three), from
  the same Hamiltonicity. The growing-degree matching theorem needs \(D\to\infty\)
  for its variance bound.
- Co-length one near half degree: relative variance \(O((t^2+1)/n^2)\) at
  host degree \(n/2+t\) (distance-rate), sharpening the \(O(1/n)\) bound.
- Selection item (iii) on single \(S_n\) orbits \(D\in\{1,n-2\}\)
  (Corollary iii-one-orbit); not a config-split close at Chernoff scale.

## Still open (named)

- Q, config-split, residual-moment: fully open.
- factor-moment: closed on every linear host for \(L^2=o(n)\)
  (Theorem linear-below-sqrt; degree \(n/2\) is Theorem half-below-sqrt).
  That is every length \(o(\sqrt{n})\), and it stops short of \(\sqrt{n}\). Still open for
  \(L=\omega(\sqrt{n})\).
- factor-rate: still open on the balanced range. At host density \(a=D/n\) the
  logarithm is \(L(a-1)(L(a-1)+a)/(2a^2 n)\), which specialises to
  \(L(L-1)/(2n)\) at degree \(n/2\) and is not \(o(L^3/n^3)\).
- The signed three-matching principal mass is \(-L^8/(48n^2)\)
  (Proposition triple-mass-order). It does not identify the cumulant.
- long-step: open for one deletion of length \(\omega(\sqrt{n})\).
  Theorem deletion-below-sqrt gives the deletion for \(L^2=o(n)\)
  between linear degrees, for every length \(o(\sqrt{n})\). It stops short of
  \(\sqrt{n}\). The length \(o(n^{1/3})\) remains Theorem third-step.
  Proposition host-trace: at half degree the mean of the first two host traces
  is order \(L^2/n^2\) and does not cancel the identified logarithm of order
  \(L^2/n\).
  Theorem long-from-peel: in-probability flatness of the ordered sequence of
  \(L\) successive perfect matchings, at degrees \(d+L\) and \(n-1-d\), gives
  the coupling. Proposition peel-budget: the matching count has relative
  variance \(O(1/n)\), and if each added matching increases the relative
  variance by a further \(O(1/n)\), the sequence has relative variance
  \(O(L/n)\) and the long step follows for every \(L=o(n)\). That increment
  is the remaining estimate.
  Lemma deletion-density: the size-biased matching deletion has Radon--Nikodym
  derivative equal to the complement matching count, with relative variance
  \(O(1/n)\) and fourth moment \(O(1/n^2)\).
  Proposition aligned-peel: Cauchy--Schwarz on that covariance solves as
  relative variance \(O(L^2/n)\), which tends to \(0\) only for \(L=o(\sqrt{n})\).
  The additive increment is a cancellation past this alignment.
  On all 3507 five-regular graphs on eight vertices the peel excesses for
  \(j=1,2,3\) are \(1024/1785375\), \(25079/11569230\), and \(77949/13712410\);
  divided by \(j^2\) times the first excess they are \(626975/663552\) and
  \(3092626575/2808301568\), near \(1\) rather than the additive quotients
  \(1/2\) and \(1/3\).
  Past \(\sqrt{n}\), the upper graph can be sampled exactly
  (Theorem long-exact-upper); the coupling then needs \(L^1\) flatness of the
  inverse-weighted extension count \(a(G)\) and an \(L\)-factor with
  probability \(1-o(1)\). On eight vertices, with deletion length \(2\), \(Z\)
  varies by \(15/7\) while \(a\) varies by \(409095/397144\), and the lower
  total variation is below \(1/200\).

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

1. Factor moment for \(L=\omega(\sqrt{n})\) (Workstream A). Every linear host
   with \(L^2=o(n)\) is Theorem linear-below-sqrt.
2. Lower-tail of \(N\) at \(1/c_n\) under true tilted \(\mu_D\) dependence
   (Workstream B).
3. Four-linear-margin long-step of length \(\omega(\sqrt{n})\), or residual-moment
   on the nearly regular window. The deletion of length \(L^2=o(n)\)
   is Theorem deletion-below-sqrt.

See `PROGRAM.md` for the full closed/blocked ledger.
