# Final-window attack

## Done

- Thm process-to-Q: BIM Conj 1.3 ⇒ Conjecture Q
- Thm window: Q for **all** \(d\ge C\log n\) ⇔ final surplus window \(d^{2/3}\to d^{1/2}\)
  (upgraded once global rate 1/3 was proved)
- Lem residual: \(\delta(R)\in[\varepsilon_0 d/2,\,2\varepsilon_0 d]\) a.a.s.
- **Thm hybrid:** \(H=G\cup R_q\) with \(q=\varepsilon/\varepsilon_0\) satisfies
  - \(G\subset H\) a.a.s.
  - \(\mathbb{P}(e\in H)=(1+\varepsilon)d/n+o(d/n)\)
  - degree mean \((1+\Theta(\varepsilon))d\), variance \(\Theta(\varepsilon d)\)
  - now for all \(d\ge C\log n\)

## Dead end recorded

- Independent thinning of all of \(G^*_0\) destroys edges of \(G\)
- Contiguity of hybrid \(H\) to ER blocked by \(\chi^2=\Theta(dn)\)

## Remaining gap

Produce \(H\sim G(n,(1+\varepsilon)d/n)\) with \(G\subset H\), by thinning only \(R\).
Matching-room remark: \(R\) has degree room for \(m=\Theta\sqrt{d\log n}\)
perfect matchings; if extractable and container contiguous to
\(G(n,d+m)\), get the increment form of Q.

## Next micro-steps

1. Extract \(m=\lfloor C\sqrt{d\log n}\rfloor\) edge-disjoint near-perfect
   matchings from \(R\) (Hällström / configuration / Rödl nibble on the
   \(\varepsilon_0 d\)-regular residual).
2. Show the graph \(G\) plus those matchings is contiguous to \(G(n,d+m)\).
3. Or: run a short deletion process only on \(R\), with switching relative to
   the planted \(G\).
