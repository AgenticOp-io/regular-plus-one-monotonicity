# v2.0 status

Bar is 2.0. v1.0 is sent.

## Closed

- Factor second moment for near-complete lengths \(D-L=o(n^{1/3})\), including
  past \(\sqrt{n}\) (Theorem factor-complementary): complementation in the host
  plus the \(o(n^{1/3})\) moment of v1.
- Factor rate on the same side (Theorem factor-rate-complementary):
  \(L=\Theta(n)\) forces \(o(1)=o(L^3/n^3)\).
- Long deletion past \(\sqrt{n}\) from degree \(o(n^{1/3})\) to near-complete
  (Theorem long-sparse-near-complete): free split plus complementation.
- Long deletion past \(\sqrt{n}\) from every linear degree to an \((n-2)\)-regular
  graph (Theorem long-linear-matching-gap): matching concentration in the
  complement plus \(S_n\)-transitivity on perfect matchings. Three margins
  linear; gap \(n-d-L=2\).
- Factor rate \(O(1/n)\) when \(D-L=1\) (strengthening of factor-rate-complementary).
- Selection item (iii) on single \(S_n\) orbits \(D\in\{1,n-2\}\)
  (Corollary iii-one-orbit); not a config-split close at Chernoff scale.

## Still open (named)

- Q, config-split, residual-moment: fully open.
- factor-moment, factor-rate: open only for \(\min(L,D-L)=\omega(n^{1/3})\).
- long-step: open under four linear margins; sparse-to-near-complete and
  linear-to-\((n-2)\) are closed.

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

Lower-tail of \(N\) at \(1/c_n\) under the true tilted \(\mu_D\) dependence,
or a signed comparison on the balanced factor range
\(\min(L,D-L)=\omega(n^{1/3})\), or four-linear-margin long-step.
