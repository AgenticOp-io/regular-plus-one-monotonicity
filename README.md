# Regular +1 monotonicity (v1.0)

Private AgenticOp-io research repo. Canonical manuscript: `paper/main.tex`.

**v1.0 is the exact \(+1\) paper.** The theorem is a coupling \(G(n,d)\subset G(n,d+1)\) whenever \(d\to\infty\) and \(n-d\to\infty\), assuming Gao arXiv:2012.01492 Theorem 6 on the sublinear and dense sides. Chernoff sandwiching, peel identification, and long \(L\)-factors are stated as conjectures and live in the sequel project `regular-plus-one-sequel`.

## Main results (proved)

1. **Exact +1** at every growing degree (`thm:plus-one`).
2. **Short-range nesting** \(G(n,d)\subset G(n,D)\) when the gap is below the chain length at degree \(d\).
3. **Matching-count chains**, including high-moment windows of every exponent strictly below \(1/2\), and linear-band chains of length \(o(n^{2/5})\).
4. **Quantitative sandwich** rates \(1/9\), \(1/5\), and process-optimal \(1/3\).
5. **Reductions** (not closes): BIM process conjecture \(\Rightarrow\) Q; factor-moment \(\Rightarrow\) long-step; container identification \(\Rightarrow\) Chernoff increments.

## Layout

```
paper/     LaTeX (deliverable)
notes/     workshop ledger
scripts/   Wolfram checker and approach screen
src/       experiments
archive/   chat history
```

## Build

```bash
pdflatex paper/main.tex
pdflatex paper/main.tex
```

MiKTeX on this machine: `pdflatex` from the `paper/` directory, twice.

## Policy

Math intended as a theorem lives in `paper/main.tex`. New closed-form identities are checked with `python scripts/wolfram_check.py` (see `.cursor/rules/`). The Wolfram app id stays in `.wolfram-appid` and is not committed.

## Sequel

`../regular-plus-one-sequel` — Conjectures Q, config-split, residual-moment, factor-moment, factor-rate, and long-step. Do not import those as theorems into this repo.
