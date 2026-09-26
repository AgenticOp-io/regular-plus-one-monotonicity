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
4. Author: David Peterson. Affiliation: AgenticOps. Email: david@agenticop.io.
5. Abstract (plain text for the arXiv form):

```
Let G(n,d) be the uniform random d-regular graph on n labelled vertices. Gao proved that G(n,d) and G(n,d+1) can be coupled so that G(n,d) is contained in G(n,d+1) with high probability whenever d tends to infinity and d = o(n^{1/3}), and indicated that the sharper edge probabilities of Gao (arXiv:2012.01492) should extend the same argument to d = o(n^{1/2}). We carry out that extension, then continue it through every sublinear degree, the complementary dense range, and the linear band, where the edge estimate does not start and a Cauchy second moment of the matching count on the simple graph closes the remaining gap. The result is an exact +1 coupling whenever d tends to infinity and n-d tends to infinity, assuming Gao (arXiv:2012.01492, Theorem 6) on the two sparse sides. The same estimates nest G(n,d) in G(n,D) whenever the gap is below the matching-count chain length at degree d, including linear-band chains of length o(n^{2/5}) and, below sqrt(n), simultaneous chains of every exponent strictly less than 1/2. Reading the error budget of the Kim-Vu sandwich proof of Behague, Il'kovic, and Montgomery (arXiv:2510.20765) with absolute switching constants yields vanishing rates epsilon >= C(log n/d)^{1/9}, epsilon >= C(log n/d)^{1/5}, and the process-optimal epsilon >= C(log n/d)^{1/3} for all d >= C log n. The Chernoff floor epsilon ~ sqrt((log n)/d) and the identification of the matching peel with the uniform regular law are left open.
```

6. Comments line: `Exact +1 nesting of random regular graphs at every growing degree. Assumes Gao arXiv:2012.01492 Thm 6.`

## Policy

All mathematical claims in this repo intended as theorems must live in `main.tex`
(see `.cursor/rules/arxiv-format.mdc`).
This version is the +1 paper. Chernoff sandwiching and long factors are conjectures, not the submission claim.
