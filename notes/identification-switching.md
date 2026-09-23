# Identification via switchings

## Proved

- Exact PM peel for \(d\ge(\log n)^{5/2}\); container in that range.
  (Smaller \(d\): Chernoff chains.) Hall uses two-sided cuts only.
- **Prop host-gap:** independent G(n,d+m) sits in the degree-d upper graph
  with probability exp(-Θ(nd log(n/d))). CFG25 does not transfer by conditioning.
- Chernoff nesting in this range is the chain corollary, up to n^{2/7}
- **Sharp residual degrees** for \(d=\omega(\log n)\): \(\deg_R=(1+o(1))\varepsilon_0 d\)
- **Switch concentration for simple Chernoff factors:** \(m^2/\delta_0\to\infty\), so
  simplicity is rare, but one witness \(m\)-factor gives
  \(P(S\mid A)\ge\exp(-O(mn\log(n/m)))\), which the Azuma tail
  \(\exp(-\Omega(nm\delta_0^2))\) dominates. Centre \(nm^2(\varepsilon_0 d)^2\).

- **Free extension flatness** (McKay): \(N_m(G)=(1+o(1))N_m(G')\) for all
  \(d\)-regular \(G,G'\), whenever \(d=o(n^{2/5}/(\log n)^{1/5})\).
  This includes \(d=\omega(n^{2/7})\).

## Open

**Conjecture config-split:** host-restricted TV against \(\mu_{d+m}\), past the chain ceiling \(n^{2/7}\).
Free flatness counts factors of the complement, not of the residual.
