# ArXiv submission (v1.0)

Canonical source: `main.tex`

## Build locally

```bash
pdflatex main.tex
pdflatex main.tex
```

## Submit

1. Upload `main.tex` (and `main.bbl` if using BibTeX later).
2. Primary classification: **math.CO** (Combinatorics); cross-list **math.PR**.
3. Title: copy from `main.tex`.
4. Abstract: copy the `abstract` environment from `main.tex` (plain text, no `\ref`).
5. Comments line suggestion: `Exact +1 nesting of random regular graphs at every growing degree. Assumes Gao arXiv:2012.01492 Thm 6.`

## Policy

All mathematical claims in this repo intended as theorems must live in `main.tex`
(see `.cursor/rules/arxiv-format.mdc`).
This version is the +1 paper. Chernoff sandwiching and long factors are conjectures, not the submission claim.
