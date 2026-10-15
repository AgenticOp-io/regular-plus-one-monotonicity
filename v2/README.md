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
| factor-moment | Balanced \(L\)-factor second moment past \(\sqrt{n}\) | Every linear host with \(L^2=o(n)\) closed; still open for \(L=\omega(\sqrt{n})\). Gao-precision switching accumulates \(\exp(O(L^3/n))\), coarser than the entropy remainder \(O(L^4/n^2)\) by a factor \(L/n\) (Proposition switching-accumulation) |
| factor-rate | Relative variance \(o(L^3/n^3)\) on that balanced range | Open. The logarithm \(L(a-1)(L(a-1)+a)/(2a^2 n)\) is not this rate |
| long-step | One deletion with \(L=\omega(\sqrt{n})\) and linear margins | Closed for every \(L=o(n)\) with four linear margins. The matching count has relative variance \(O(1/n^2)\) at every linear degree, one matching deletion has total variation \(O(1/n)\), and \(L\) steps are a union bound \(O(L/n)\). |

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
