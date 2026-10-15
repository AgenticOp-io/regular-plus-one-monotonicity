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

- Successive uniform peeling above half degree (Theorem successive-peel):
  peel \(L\) uniform perfect matchings from a uniform \(D\)-regular graph,
  \(D-L+1\ge n/2\), \(D\le(1-c)n\). Dirac makes every step defined,
  containment is sure, the top is exact, and the bottom is within
  \(C_cL/n\) of \(\mu_{D-L}\). Dual statement below half degree.
- Bounded peel moments give peel flatness (Theorem peel-bounded-to-flat):
  if shorter peel counts on the complementary degrees have relative second
  moment at most \(1+B\), then \(\EE|P_L/\EE P_L-1|\le C_c\sqrt{1+B}\,L/n\).
  Unconditional at \(L=2\): \(O(1/n)\). Concerns \(P_L\), not \(Z_L\).
- Two-matching peel variance (Theorem two-peel-variance): \(\Var P_2/(\EE P_2)^2
  =O(1/n)\) at every linear degree, from fourth moments of the matching count
  (v1 Lemma band-fourth) and the pair measure. Hence
  \(\EE|P_3/\EE P_3-1|=O(1/n)\) above half degree (Corollary
  three-peel-flat). The same step for \(P_3\) needs eighth moments of the
  matching count; the induction stops at length three.

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
- long-step: closed for every \(L=o(n)\) with four linear margins
  (Theorem long-step). The matching count has relative variance \(O(1/n^2)\)
  at every linear degree (Theorem matching-linear-rate). One matching deletion
  then has total variation \(O(1/n)\) (Lemma matching-step-l1), and \(L\) such
  steps are a union bound \(O(L/n)\). The \(1/n\) coefficient in the matching
  ratio is the equal-radius origin, the radius shift \(-\gamma k/n\), the
  width, and the angular traces; the cubic remainder and the determinant
  shift are both \(O(k/n^2)\) for \(k\le\log n\) (Lemma mismatch-shift).
  Theorem deletion-below-sqrt remains the factor-moment route for \(L^2=o(n)\).
  Factor-count flatness for \(L=\omega(\sqrt{n})\) stays open. On all 19355
  four-regular graphs on eight vertices the \(L=2\) excess is
  \(89344/17363889\), about \(1/24\) of the logarithm \(1/8\)
  (Remark eight-factors). A sample of twenty-five six-regular graphs on
  twelve vertices has \(2\)-factor relative variance about \(5\cdot 10^{-4}\),
  against the logarithm \(1/12\). The half-degree package through order
  \(1/n^2\) is \(L(L-1)/(2n)-L(8L^3-24L^2+15L-3)/(6n^2)\), which at
  \(t=L^2/n\) is \(t/2-(4/3)t^2\) and is negative for \(t>3/8\). That
  package is not the ratio, and the degree-variance correction together with
  the Gaussian width does not restore \(o(1)\). The logarithm is not the
  excess. In \(G(n,p)\) the second-moment ratio is
  \(\exp(L^2(1-p)/(2p))\) for \(L^3=o(p^2 n)\) (Gao 2013, Theorem 2.1), and
  that exponential is the edge count: the same count in \(G(n,m)\)
  concentrates (Theorem 2.4). It is not a lower bound on a regular host
  (Remark binomial-edge). Small subgraph conditioning predicts an excess
  \(\tfrac12(-\log(1-x)-x-x^2/2)\) with \(x=1/(D-1)\), independent of \(L\),
  because the factor chain along a path has eigenvalue \(-1/(D-1)\) for
  every \(L\) (Remark cycle-prediction). The counts match that order. This
  is a heuristic; the configuration second moment is blocked on linear
  hosts. The coarser
  Cauchy--Schwarz recurrence with the older input \(O(1/n)\)
  (Proposition aligned-peel) still stops at \(\sqrt{n}\).
  Lemma deletion-density now takes the second moment \(O(1/n^2)\) from
  Theorem matching-linear-rate. One statistic then shifts by
  \(|\mu|\sqrt{\varepsilon\cdot O(1/n^2)}\) under that size bias
  (Lemma size-bias-shift). The formal recurrence with that input solves
  as \(O(L^2/n^2)\) for every \(L=o(n)\) (Proposition aligned-peel-square).
  The recurrence itself is not proved: the size-biased variance adds a
  covariance against \(W\), and the fourth moment of \(W\) is only
  \(O(1/n^2)\), the same order as its second moment. It also controls the
  ordered peel count \(P_L=\sum D(F)\), not \(Z_L\). For a \(2\)-factor,
  \(D(F)=2^{c(F)}\) when every cycle is even.
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
  total variation is below \(1/200\). On that same enumeration \(a=W\mu\),
  where \(W\) is the \(2\)-factor count of the complement and runs through the
  integers \(248\) through \(255\), and the conditional mean \(\mu\) of \(1/Z\)
  has maximum-to-minimum ratio \(6227311/6205375\). The covariance of \(W\) and
  \(\mu\) is positive. The flatness of \(a\) is the flatness of a factor count
  on a \(5\)-regular host, not a compensation between \(W\) and \(1/Z\).

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
