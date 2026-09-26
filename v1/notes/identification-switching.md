# Identification via switchings

## Proved

- Exact PM peel for \(d\ge(\log n)^{5/2}\); container in that range.
  (Smaller \(d\): Chernoff chains.) Hall uses two-sided cuts only.
- **Prop host-gap:** independent G(n,d+m) sits in the degree-d upper graph
  with probability exp(-Θ(nd log(n/d))). CFG25 does not transfer by conditioning.
- Chernoff nesting in this range is the chain corollary, up to n^{2/7}
- **Sharp residual degrees** for \(d=\omega(\log n)\): \(\deg_R=(1+o(1))\varepsilon_0 d\)
- **Switch count corrected:** mean \(m^2(\varepsilon_0 d)^2\), not \(nm^2(\varepsilon_0 d)^2\).
  Per-edge count \(m\delta^2/n=\Theta(d^{11/6}(\log n)^{7/6}/n)\) is \(o(1)\) for
  \(d=o(n^{6/11})\), hence on the whole gap from \(n^{2/7}\) through \(o(\sqrt{n})\).
  Azuma does not dominate the simplicity weight \(\exp(-O(mn\log(n/m)))\).

- **Free extension flatness** (McKay): \(N_m(G)=(1+o(1))N_m(G')\) for all
  \(d\)-regular \(G,G'\), whenever \(d=o(n^{2/5}/(\log n)^{1/5})\).
  This includes \(d=\omega(n^{2/7})\).

## Open

**Conjecture config-split:** host-restricted TV against \(\mu_{d+m}\), past the chain ceiling \(n^{2/7}\).
Free flatness counts factors of the complement, not of the residual.
