# Final-window attack

## Done

- Thm process-to-Q: BIM Conj 1.3 ⇒ Conjecture Q
- Thm window: Q for \(d\ge n^\sigma\) ⇔ final surplus window \(d^{2/3}\to d^{1/2}\)
- Lem residual: \(\delta(R)\in[\varepsilon_0 d/2,\,2\varepsilon_0 d]\) a.a.s.
- **Thm hybrid:** \(H=G\cup R_q\) with \(q=\varepsilon/\varepsilon_0\) satisfies
  - \(G\subset H\) a.a.s.
  - \(\mathbb{P}(e\in H)=(1+\varepsilon)d/n+o(d/n)\)
  - degree mean \((1+\Theta(\varepsilon))d\), variance \(\Theta(\varepsilon d)\)

## Dead end recorded

Independent thinning of all of \(G^*_0\) (not just \(R\)) destroys
\(\Theta(n d^{2/3})\) edges of \(G\). Must thin only the residual.

## Remaining gap

Contiguity / TV: \(H\) vs \(G(n,(1+\varepsilon)d/n)\).
The regular constraint on \(G\subset H\) is the dependence obstacle.

## Next micro-steps

1. Compare the number of triangles (or small subgraphs) in \(H\) vs ER at the same \(p\).
   If all small subgraph counts match, contiguity machinery may apply.
2. Write \(H\) as a configuration-model object: \(d\)-regular planted + thinned residual.
3. Bound \(\mathrm{TV}(H,\,G(n,p))\) via Stein / size-biased couplings on degrees.
