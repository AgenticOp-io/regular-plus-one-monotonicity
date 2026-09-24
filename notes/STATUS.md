# Status board

## Rate ladder

```
1/9 << 1/5 << 1/3 << Chernoff inc (chains, D=o(n^{2/5})) << exact Q
PROVED  PROVED  PROVED   PROVED                            OPEN (d>n^{2/5})
         residual container (d at least (log n)^{5/2}); host TV open
```

## Toward Chernoff

- **Longest exact chain:** at \(D=n^{1/4}\), \(v=\Theta(n^{-3/4})\) and \(L=o(n^{1/4})\), from the ratio error \(O(d/n)\).
- **Cor summable:** for \(D\to\infty\) and \(D\le n^{1/6}/\log n\), the chain
  runs up to \(\lfloor n^{1/6}/\log n\rfloor\). One-step total variation is
  \(O(d^{-6/5})\), from a triangle projection whose fourth moment is proved in
  the manuscript. The tail sums as \(O(D^{-1/5})\).
- **Cor chernoff-chains:** G(n,D) ⊂ G(n,D+m) for m=Θ√(D log n),
  when ω(log n)=D=o(n^{2/7}/(log n)^{3/7}) from the coarse ratio error, and
  when ω(log n)=D=o(n^{2/5}/(log n)^{3/5}) after one further switching pass
  (Lemma ratio-error, Corollary chernoff-two-fifths).
  Chain length is L=o(v(D)^{-1/3}) for v=D^{-3}+D^2/n.
  Lemma laplace cancels the odd truncation error, so the sqrt(D/n) log^3 n
  term is absorbed in D^2/n. Relative variance at least 1/(6D^3) still
  forces L=o(D): no n^{1/3} window at polylog degree.
- Residual exact \((d+m)\)-regular container for \(d\ge(\log n)^{5/2}\)
  (below that, Chernoff chains already nest)
- Hall proof for the residual matching no longer uses an empty-cut claim
  (a vertex and its non-neighbourhood). Cuts are two-sided.
- Config-split TV was withdrawn: product containment in the host is exponentially small
- **Hybrid degrees:** for \(d/\log n\to\infty\) and Chernoff \(\varepsilon\), every degree of the thinned residual container is \(d+(1+o(1))\varepsilon d\).
- Switching: the \(2\)-switch count of a residual \(m\)-factor has mean \(m^2(\varepsilon_0 d)^2\), not \(nm^2(\varepsilon_0 d)^2\). There are \(o(1)\) switches per edge for \(d=o(n^{6/11})\), including the whole gap from \(n^{2/7}\) through \(o(\sqrt{n})\). The Azuma exponent does not beat the simplicity weight.
- Sharp residual degrees \((1+o(1))\varepsilon_0 d\) for \(d=\omega(\log n)\)

- Free \(m\)-extension counts are \((1+o(1))\)-flat for all \(d\)-regular graphs
  when \(d=o(n^{2/5}/(\log n)^{1/5})\) (McKay), including past \(n^{2/7}\)

## Next

Host-restricted total variation is open (Conjecture config-split).
Two-switches do not close it: Proposition switch-barrier.
Chernoff nesting now runs to \(o(n^{2/5}/(\log n)^{3/5})\). The gain is a second-moment ratio error \(O(d/n)\) rather than \(O(d^2/n)\): the universal part of the closing-pair count cancels in the ratio, and the host-dependent part sums to \(O(d/n)\). The fourth-moment hypothesis remains open and is no longer the constraint on the chain length. Exact nesting for \(d=\omega(\sqrt{n})\) is still blocked by the enumeration barrier.
A sandwich coupling does not put uniform G(n,d+m) inside the upper graph
already built at degree d (Proposition host-gap). Free flatness counts
factors of the complement, not of the residual.
