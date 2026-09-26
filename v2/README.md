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
| factor-moment | \(L\)-factor second moment for \(n^{1/2}=o(L)=o(n)\) |
| factor-rate | Relative variance \(o(L^3/n^3)\) in that range |
| long-step | One deletion of an \(L\)-factor with \(L=\omega(\sqrt{n})\) |

v1.0 already proved the reductions. This tree must supply a missing
hypothesis, not re-prove an implication.

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
