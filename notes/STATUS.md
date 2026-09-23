# Status board

## Rate ladder

```
1/9 (all d)  <<  1/5 (all d)  <<  1/3 (d≥n^σ)  <<  1/3 (all d)  <<  1/2 Chernoff
  PROVED         PROVED            PROVED            COND (Hyp P)      OPEN
                 (linear I6)
```

## Blockers (now precise)

| Goal | Barrier |
|---|---|
| Global 1/3 (Hyp P upper) | Two-vertex upper at √(log n/δ): truncation and L² both stop at (·)^{1/4} |
| Chernoff 1/2 | Process architecture (Conj 1.3 / window) |

## Proved recently

- Lemma crude-exp + Thm path-lower-chernoff (linear I6)
- Thm U + Thm quant-fifth (**global 1/5**)
- Lemma one-vertex-chernoff (Chernoff-scale one-vertex upper, free from G1+G2)
- Rem second-moment: L² on long paths has relative SD Θ((log n/δ)^{1/4}) — same ceiling as truncation

## Next

Exponential-moment / Freedman / growing-degree Kim–Vu on the path polynomial
to break the √λ barrier for two-vertex upper bounds.
