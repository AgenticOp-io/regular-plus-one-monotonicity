# Status board

## Rate ladder (quantitative sandwich)

```
fixed ε  <<  1/9 (all d)  <<  1/3 (d≥n^σ)  <<  hybrid Chernoff container  <<  1/2 ER Chernoff
              PROVED           PROVED         PROVED (marginals)           OPEN (contiguity)
                                                   │
                              process Conj 1.3 ════╧══⇒ Q   (PROVED implication)
                              window d^{2/3}→d^{1/2}       (PROVED reduction)
```

## Publishable claims

| Claim | Strength | Where |
|---|---|---|
| Quant.\ sandwich \(1/9\) | all \(d\ge C\log n\) | Thm quant |
| Quant.\ sandwich \(1/3\) | \(d\ge n^{\sigma}\) | Thm quant-third |
| Process ⇒ Chernoff Q | conditional | Thm process-to-Q |
| Window reduction | Q ⇔ final window | Thm window |
| Residual degree room | \(\delta(R)\asymp\varepsilon_0 d\) | Lem residual |
| Hybrid Chernoff container | \(G\subset H\), correct marginals at Chernoff \(\varepsilon\) | Thm hybrid |

## Ceiling / dead ends

- BIM B2 cannot beat \(1/3\) (either side)
- GIM structure incompatible with Chernoff for all \(d<n\)
- B2-residual defect at Chernoff worse than perfect \(1/3\)

## Next

Contiguity of hybrid \(H=G\cup R_q\) to \(G(n,(1+\varepsilon)d/n)\).
