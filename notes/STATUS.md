# Status board

## Rate ladder

```
1/9 (all d)  <<  1/5 (d≥n^τ)  <<  1/3 (d≥n^σ)  <<  1/2 Chernoff
  PROVED         PROVED            PROVED            OPEN
```

## Blockers (now precise)

| Goal | Barrier |
|---|---|
| Global 1/5 (Conj U) | Lemma 7.1 truncation: η≥√λ with λ≥(log n/δ)^{1/4} |
| Global 1/3 (Hyp P) | I6 uses sets of size Θ(λn); needs redesign for linear sets |
| Chernoff 1/2 | Process architecture (Conj 1.3 / window) |

## Proved toward Chernoff

- process ⇒ Q
- window reduction
- hybrid marginals (not contiguous)
