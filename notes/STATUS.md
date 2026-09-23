# Status board

## Rate ladder

```
1/9 << 1/5 << 1/3 (all d) << exact container << Chernoff inc (d=o(n^{1/7}))
PROVED  PROVED  PROVED          PROVED             PROVED
                                                 << all d (config-split conj)
                                                    OPEN
```

## Toward Chernoff

- Exact PM peel ⇒ Ω_m(R) nonempty
- **Thm config-split:** TV(L, μ_{d+m})→0 for d+m=o(n^{1/7}) via CFG25 ⊕ M_m^⊕
- **Cor chernoff-inc-sparse:** G(n,d) ⊂ G(n,d+m) a.a.s. at m=Θ√(d log n)
- **Conj config-split:** same for all d ≥ C log n

## Next

Extend past n^{1/7} (dense CFG25 analogue / host-restricted switchings).
