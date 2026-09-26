# Regime map: \(G(n,d_1)\subseteq G(n,d_2)\) whp

Updated after reading Gao arXiv:2104.11850 and HLMPW arXiv:2505.22875 carefully.

Excluded pairs: \((d_1,d_2)\in\{(1,2),(n-3,n-2)\}\). Require \(d_in\) even.

## Known regimes (DONE)

| Regime | Citation | Notes |
|---|---|---|
| \(d_1=1\), \(d_2\ge 3\) | HLMPW / earlier | |
| \(\omega(1)=d=o(n^{1/3})\): exact **+1** | **Gao Thm 8** | Primary known +1 window |
| \(\omega((\log n)^7)=d_1\le n^{1/7}/\log n\), any \(d_2\ge d_1\) | Gao + HLMPW Thm 1.2 | |
| \(d_2\ge c\,d_1\), \(c>1\), polylog ≤ degrees ≤ \(n-\mathrm{polylog}\) | GIM | |
| \(d_1=\omega(\log n)\), \(d_2-d_1=\Omega(d_1)\) | BIM 2025 corollary | Sandwich transit |
| Dense increments \(\min\{d_1,d_2-d_1\}=\omega(n/\log n)\) | GIM/HLMPW | |

## Open / our attack surface

| Cell | Status | Plan |
|---|---|---|
| **\(d=o(n^{1/2})\): exact +1** | open; Gao says reachable | **PRIMARY** — `notes/attack-n-half.md` |
| \(n^{1/2}\lesssim d\ll n\): +1 | open | needs new ideas after primary |
| HLMPW TV Cor 3.2 past \(n^{1/10}\) toward \(n^{1/7}\) | open | secondary (decompositions) |
| Odd \(n\) (+2 steps) | open | later |
| Process sandwich (BIM Conj 1.3) | open, hard | not Stage 1 |

## Primary theorem we want

> If \(d\to\infty\) and \(d=o(n^{1/2}/\log^2 n)\), then
> \(\exists\) coupling with \(\mathbb{P}(G(n,d)\subset G(n,d+1))=1-o(1)\).
