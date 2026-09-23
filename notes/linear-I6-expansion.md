# Linear-I6 expansion redesign (Hypothesis P) — PROVED

## Goal (achieved for lower bounds)

Two-vertex path lower bounds at
\[
\lambda=\Theta\Bigl(\sqrt{\frac{\log n}{\delta}}\Bigr)
\]
for all \(\delta\ge C\log n\), by expanding connecting sets to linear size
\(\mu_0 n\) before applying I6.

## Architecture (in `paper/main.tex`)

| Piece | Label | Status |
|---|---|---|
| Crude \(N_{F\setminus K}\) expansion | Lemma `lem:crude-exp` | proved |
| Path lower at Chernoff \(\lambda\) | Thm `thm:path-lower-chernoff` | proved (Phases A–C) |
| Path upper at \(1/4\) via truncation | Thm `thm:U` | proved |
| Global rate \(1/5\) | Thm `thm:quant-fifth` | proved |

## Why BIM stopped at \(\lambda n\)

Claim 6.4 sets final \((X,Y)\) of size \(\Theta(\lambda n)\). I6 at
\(\mu=\Theta(\lambda)\) forces \(\lambda^3\delta=\Omega(\log n)\).

## Two-phase fix

- **Phase A:** BIM I3/I4 up to \(S_A=\lambda n/(100\delta)\).
- **Phase B:** Lemma crude-exp + one \(K\)-step reaches \(\mu_0 n\) (since
  \(d\lambda=\Omega(\sqrt{d\log n})\)).
- **Phase C:** Lemma 6.15 at \(\mu=\mu_0\); only needs \(\lambda^2\delta=\Omega(\log n)\).

## Rate consequences

| Path error | B2 rate | Status |
|---|---|---|
| Lower \(\sqrt{\cdot}\), upper \((\cdot)^{1/4}\) | **1/5 global** | **proved** |
| Both sides \(\sqrt{\log n/\delta}\) | 1/3 global | needs non-truncation upper |

Truncation necessarily gives \(\eta=\Omega(\sqrt{\lambda})\), so Chernoff-scale
lower bounds unlock \(1/4\) upper (Thm U) but not \(1/2\) upper.
