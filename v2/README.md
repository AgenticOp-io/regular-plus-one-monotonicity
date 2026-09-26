# v2.0 (in progress)

Chernoff sandwiching, peel identification, and long \(L\)-factors.
This tree is the sequel to `../v1/`. Exact \(+1\) is already proved there.

Do not retitle a conjecture as a theorem unless `paper/main.tex` has a proof
that supports the claim.

## Targets

| Label | Claim |
| --- | --- |
| Q | Chernoff sandwich \(\varepsilon\asymp\sqrt{(\log n)/d}\) |
| config-split | Peel law \(\mathcal{L}_{d,m}\) vs \(\mu_{d+m}\) |
| residual-moment | Second moment of \(m\)-factors of the BIM residual |
| factor-moment | Balanced \(L\)-factor second moment: \(n^{1/2}=o(L)\) and \(\min(L,D-L)=\omega(n^{1/3})\) (near-complete side closed) |
| factor-rate | Relative variance \(o(L^3/n^3)\) on that balanced range (near-complete side closed) |
| long-step | One deletion of an \(L\)-factor with \(L=\omega(\sqrt{n})\) |

v1.0 is sent. This tree is the bar. The reductions are already proved;
this tree must supply a missing hypothesis.

Ordered jobs: `notes/PROGRAM.md`.

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
