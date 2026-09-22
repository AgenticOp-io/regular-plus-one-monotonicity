# ArXiv submission

Canonical source: `main.tex`

## Build locally

```bash
pdflatex main.tex
pdflatex main.tex
```

## Submit

1. Upload `main.tex` (and `main.bbl` if using BibTeX later).
2. Primary classification: **math.CO** (Combinatorics); cross-list **math.PR**.
3. Title/abstract: copy from `main.tex`.
4. Comments line suggestion: `15 pages. Extends Gao's +1 nesting from o(n^{1/3}) to o(sqrt(n)/polylog).`

## Policy

All mathematical claims in this repo intended as theorems must live in `main.tex`
(see `.cursor/rules/arxiv-format.mdc`).
