# v2.0 work program

v1.0 is sent. Active manuscript: `v2/paper/main.tex`.

## Workstream A — sequential product closed as a negative; complementation positive

Signed Gao after a matching host leaves \(2t/(Ln)\). Not past \(n^{1/3}\) for
balanced lengths.

Complementation in the host: \(Z_L=Z_{D-L}\) pathwise. With the v1 moment at
length \(D-L=o(n^{1/3})\), the factor second moment and factor rate hold for
near-complete \(L=D-o(n^{1/3})\), including past \(\sqrt{n}\)
(Theorems factor-complementary, factor-rate-complementary in `v2/paper/main.tex`).

Free split plus complementation: long deletion of length \(\Theta(n)\) from
degree \(o(n^{1/3})\) to near-complete (Theorem long-sparse-near-complete).
Linear-margin long-step stays open: complementary moment cannot feed both ends.

## Workstream B — hard gaps recorded

Blocked / identified:
- Target \(c_n=1/(|\Omega|p^{Dn/2})\); contain-first mean is biased.
- \(S_n\) to iso-types only; \(d\nu/d\mu\propto\mathbb{E}[1/N\mid\mathrm{containment}]\).
- Edges under \(\nu_D\) match \(\mu_D\); triangles need flat class weights.
- Conditional triangle first-moment proxy is
  \(\bigl((1+\varepsilon)/(2+\varepsilon)\bigr)^3\pi^3\), not \(\pi^3\).
- Switches: \(N\to\infty\), logarithmic bound only \(D^{O(1)}\);
  depth-\(D\) BFS only \(\exp(O(D\log D))\), still below bulk.
- Sandwich posterior ≠ first peel flatness.
- Second moment of \(N\): pairwise \(p^{-(K_{12}-K_{012})}\).
- Free-flat ≠ residual flatness.
- Regular-plus-sprinkle: degree variance \(\Theta(\varepsilon D)\) vs \(\Theta(D)\);
  TV→1 as \(\varepsilon\to 0\); posterior uniformity does not transfer.

- Exact \(n=6\), \(D=2\): inverse-count ratio across iso-types in \([1.07,1.16]\);
  triangle \(\nu/\mu\in[0.885,0.942]\) (ledger `v2/notes/small-n-inv.md`).
- Literal \(Z_d\) flatness fails on \(K_6\) at \((d,m)=(1,1)\): \(Z_1(C_6)=2\),
  \(Z_1(C_3\cup C_3)=0\).

Still missing (no fake closes):
1. Lower-tail of \(N\) at threshold \(1/c_n\) (Proposition iii-as-tail) —
   not a moment about \(\mathbb{E}[N]\), not near-disjoint factors, not switches.
2. Three peel-weight flatnesses on \(G^*_0\) (asymptotic \(Z_d\), not literal;
   first flatness is not the sandwich posterior).
3. Second moment on actual \(R=G^*_0\setminus G\).
4. Binomial thinning or BIM Conjecture 1.3 — not hybrid, not sprinkle.

## v1

Do not edit `v1/paper/main.tex` except Gao errata.
