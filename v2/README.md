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
| factor-moment | Balanced \(L\)-factor second moment past \(\sqrt{n}\) | Open only for \(\min(L,D-L)=\omega(n^{1/3})\) on linear hosts; near-complete factors/hosts and sublinear co-length one closed |
| factor-rate | Relative variance \(o(L^3/n^3)\) on that balanced range | Same open/closed split as factor-moment |
| long-step | One deletion with \(L=\omega(\sqrt{n})\) and linear margins | Open under four linear margins; sparse-to-near-complete and matching-gap-to-\((n-2)\) closed |

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
