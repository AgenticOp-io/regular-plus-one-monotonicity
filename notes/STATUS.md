# Status board

## Rate ladder

```
1/9 << 1/5 << 1/3 << Chernoff inc (chains, D=o(n^{2/7})) << exact Q
PROVED  PROVED  PROVED   PROVED                            OPEN (d>n^{2/7})
         residual container (d at least (log n)^{5/2}); host TV open
```

## Toward Chernoff

- **Exact +1:** \(d=o(\sqrt{n})\). The old \(\log^3 n\) loss was the Laplace truncation; Lemma laplace absorbs it, and the Chebyshev schedule \(\alpha=\max(d^{-1},(d^2/n)^{1/8})\) has crossover \(d=n^{1/10}\).
- **Cor chernoff-chains:** G(n,D) ⊂ G(n,D+m) for m=Θ√(D log n),
  when ω(log n)=D=o(n^{2/7}/(log n)^{3/7}).
  Chain length is L=o(v(D)^{-1/3}) for v=D^{-3}+D^2/n.
  Lemma laplace cancels the odd truncation error, so the sqrt(D/n) log^3 n
  term is absorbed in D^2/n. Relative variance at least 1/(6D^3) still
  forces L=o(D): no n^{1/3} window at polylog degree.
- Residual exact \((d+m)\)-regular container for \(d\ge(\log n)^{5/2}\)
  (below that, Chernoff chains already nest)
- Hall proof for the residual matching no longer uses an empty-cut claim
  (a vertex and its non-neighbourhood). Cuts are two-sided.
- Config-split TV was withdrawn: product containment in the host is exponentially small
- Switching degree of the uniform simple Chernoff \(m\)-factor concentrates
  (simplicity is rare, but the Azuma tail still dominates)
- Sharp residual degrees \((1+o(1))\varepsilon_0 d\) for \(d=\omega(\log n)\)

- Free \(m\)-extension counts are \((1+o(1))\)-flat for all \(d\)-regular graphs
  when \(d=o(n^{2/5}/(\log n)^{1/5})\) (McKay), including past \(n^{2/7}\)

## Next

Host-restricted total variation is open (Conjecture config-split).
A sandwich coupling does not put uniform G(n,d+m) inside the upper graph
already built at degree d (Proposition host-gap). Free flatness counts
factors of the complement, not of the residual.
