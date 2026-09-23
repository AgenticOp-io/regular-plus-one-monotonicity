# Final-window attack

## Done

- Exact PMs in the residual for \(d\ge(\log n)^{5/2}\), via bipartite Hall.
  The one-sided cut bound is false (non-neighbourhood of a vertex).
  The repair uses expansion up to size \(s_0\) and two-sided cuts beyond it.
- Exact (d+m)-regular container in the same degree range.
  Smaller \(d\) is already covered by Chernoff chains.
- Config-split / Chernoff inc for d=o(n^{1/7}) (CFG25)
- **Cor chernoff-chains:** Chernoff increments for
  ω(log n)=D=o(n^{2/7}/(log n)^{3/7}) via +1 chains.
  The sqrt(d/n) log^3 n truncation is removed by the odd cancellation in lem:laplace.
- Switching degree concentrates for the uniform **simple** Chernoff \(m\)-factor.
  \(m^2/\delta_0\to\infty\), so simplicity is rare in the stub model; the Azuma tail
  \(\exp(-\Omega(nm\delta_0^2))\) still beats the witness bound
  \(\exp(O(mn\log(n/m)))\).
- Sharp residual degrees \((1+o(1))\varepsilon_0 d\) when \(d=\omega(\log n)\), so the
  switch count is centred at \(nm^2(\varepsilon_0 d)^2\).

## Remaining

Conjecture config-split for d=ω(n^{2/7}) (past the chain ceiling).
Host-gap: product containment in the degree-d upper graph is exp(-Θ(nd log(n/d))).

## Note

Chain increments are the nesting theorem up to \(n^{1/4}\). The residual container
is the route past that ceiling; its law is not yet \(G(n,d+m)\).
