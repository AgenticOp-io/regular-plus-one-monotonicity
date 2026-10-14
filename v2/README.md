# v2.0 (in progress)

Chernoff sandwiching, peel identification, and long \(L\)-factors.
This tree is the sequel to `../v1/`. Exact \(+1\) is already proved there.

Do not retitle a conjecture as a theorem unless `paper/main.tex` has a proof
that supports the claim.

## Targets

| Label | Claim | Status |
| --- | --- | --- |
| Q | Chernoff sandwich \(\varepsilon\asymp\sqrt{(\log n)/d}\) | Open |
| config-split | Peel law \(\mathcal{L}_{d,m}\) vs \(\mu_{d+m}\) | Open (iii on \(D\in\{1,n-2\}\) only) |
| residual-moment | Second moment of \(m\)-factors of the BIM residual | Open |
| factor-moment | Balanced \(L\)-factor second moment past \(\sqrt{n}\) | Every linear host with \(L^2=o(n)\) closed; still open for \(L=\omega(\sqrt{n})\) |
| factor-rate | Relative variance \(o(L^3/n^3)\) on that balanced range | Open. The logarithm \(L(a-1)(L(a-1)+a)/(2a^2 n)\) is not this rate |
| long-step | One deletion with \(L=\omega(\sqrt{n})\) and linear margins | Deletion of length \(L^2=o(n)\) closed; still open for \(L=\omega(\sqrt{n})\). The mean of the first two host traces is order \(L^2/n^2\) and does not cancel the identified logarithm of order \(L^2/n\). Flatness of an ordered sequence of \(L\) perfect matchings gives the coupling, and a matching-scale increment \(O(1/n)\) per step sums to relative variance \(O(L/n)\) on the whole range \(L=o(n)\). Cauchy--Schwarz against the complement matching count solves as \(O(L^2/n)\) and stops at \(\sqrt{n}\); the additive increment is a cancellation past that bound. Past \(\sqrt{n}\) the upper graph can be exact; the remaining weight on that route is \(a(G)\). On eight vertices that weight varies by about \(3\%\), while the factor count varies by \(15/7\) |

Ordered jobs: `notes/PROGRAM.md`. Snapshot: `notes/STATUS.md`.

## Layout

```
paper/     v2.0 manuscript
notes/     workshop
```

Shared tools stay at the repo root: `../scripts/wolfram_check.py`,
`../scripts/approach_screen.py`. Append checks to `notes/wolfram-checks.md`.

## Build

```bash
pdflatex paper/main.tex
pdflatex paper/main.tex
```
