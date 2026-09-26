# Breakthrough program — past Remark 16(b)

The Gao completion (`o(√n)` exact +1) is frozen as an attributed note.
Everything below is **new enabling math** aimed at exponential range expansion.

## Architecture

```
                    ┌─────────────────────────────────────┐
                    │  QUANTITATIVE SANDWICH (Conjecture Q) │
                    │  ε ≥ κ √(log n / d)                     │
                    │  ⇒ increments ω(√(d log n))            │
                    └──────────────┬──────────────────────────┘
                                   │ if proved
                                   ▼
┌──────────────┐    ┌──────────────────────┐    ┌────────────────────┐
│ Exact +1     │───▶│ HYBRID GLOBAL NESTING │◀───│ BIM fixed-ε        │
│ d=o(√n)      │    │ any d1≤d2 with gap    │    │ geometric jumps    │
│ (Gao/us)     │    │ ≥ max(1, √(d log n))  │    │ (1+ε)^k tower      │
└──────────────┘    └──────────────────────┘    └────────────────────┘
         │
         ▼
┌──────────────────────────────────────────┐
│ LONG SIMULTANEOUS +1 CHAINS (Theorem C)  │
│ window length L ≪ (n/D²)^{1/3}/polylog │
│ NEW — proved from patched η              │
└──────────────────────────────────────────┘
```

## Why this expands “exponentially”

| Tool | Old reach | New reach |
|---|---|---|
| Exact +1 | single step, \(d=o(\sqrt{n})\) | same |
| Simultaneous chain | Gao: relative window \(\varepsilon d\) at \(d\le n^{1/7}\) | **absolute** window \(L\asymp(n/D^2)^{1/3}\); at \(D=\mathrm{polylog}\,n\) get \(L\asymp n^{1/3}\) |
| BIM fixed \(\varepsilon\) | factor \(1+\varepsilon\) | geometric tower: \(d\to(1+\varepsilon)d\to\cdots\to n\) in \(O_\varepsilon(\log n)\) jumps |
| Conjecture Q | — | gap \(\omega(\sqrt{d\log n})\) for **all** \(d\ge C\log n\); covers medium-dense |

Chaining geometric BIM jumps already covers \([C\log n,\,n]\) in \(O(\log n)\) steps (exponential towers in degree).
Long chains fill dense absolute intervals inside the sparse regime.
Q would fill the remaining “medium gap” between \(1\) and \(\varepsilon d\) past \(\sqrt{n}\).

## Priority order

1. **Theorem C — long simultaneous +1 chains** (do now; only uses our η).
2. **Conjecture Q + necessity of Chernoff floor** (state; prove necessity).
3. **Conditional Theorem Q⇒ hybrid increments** (write proof assuming Q).
4. **Attack Q** via BIM switching-path analysis with \(\varepsilon=\varepsilon(n)\).
5. **Dense TV / permanent path** (parallel, higher risk).

## Honesty constraints

- Do not market Theorem C as beating the \(\sqrt{n}\) barrier for exact +1.
- Do not claim Q is proved.
- Attribute BIM for all fixed-\(\varepsilon\) consequences.
- Keep Gao Remark 16(b) attribution on the base exact-+1 theorem.
