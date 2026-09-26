# v2.0 work program

v1.0 is sent. Active manuscript: `v2/paper/main.tex`.

## Closed (do not reopen)

### Factor second moment / rate (short complementary length)

| Theorem | Range |
| --- | --- |
| factor-complementary | Linear host, \(D-L=o(n^{1/3})\), including past \(\sqrt{n}\) |
| factor-rate-complementary | Same; \(O(1/n)\) when \(D-L=1\) |
| factor-dense-host | Near-complete host, McKay range \(\ell(s+\ell)^2/n=o(1)\) for every \(\ell\ge 1\) (incl.\ co-length one with \(n-D=o(n^{1/2})\)) |
| factor-rate-dense-host | Same |
| factor-sublinear-colength-one | Co-length one on every host \(D=o(n)\), including past \(\sqrt{n}\) |

Tools: host complementation \(Z_L=Z_{D-L}\); v1 factor-third; McKay
enumeration (McK85) / free-extension flatness; sublinear matching variance.

### Long deletions past \(\sqrt{n}\)

| Theorem | Range |
| --- | --- |
| long-sparse-near-complete | \(d+\ell=o(n^{1/3})\) to degree \(n-1-\ell\) |
| long-matching-gap | Every \(d\le n/2-1\) to degree \(n-2\) (Dirac + \(S_n\)-transitivity); linear band \(d>n/2-1\) via matching concentration |
| long-matching-into-dirac | Matching into every host \(D\ge n/2\) (Dirac + \(S_n\)-transitivity) |

### Selection (iii)

| Result | Range |
| --- | --- |
| cor:iii-one-orbit | \(D\in\{1,n-2\}\) (single \(S_n\) orbit); not a Chernoff-scale config-split close |

## Workstream A — balanced factors and four-linear long-step

Signed Gao after a matching host leaves \(2t/(Ln)\). Not past \(n^{1/3}\) for
balanced lengths. Do not retry: binomial-PGF-without-pairwise,
quadratic-PGF-without-leftover, origin-at-typical-k, signed-gao-matching-host.

Still missing:
1. Signed (or other) second-moment comparison on
   \(\min(L,D-L)=\omega(n^{1/3})\) with linear host — Conjectures
   factor-moment and factor-rate.
2. Four-linear-margin long-step — Conjecture long-step. Complementary moment
   cannot feed both ends (Remark long-complement-empty). Matching-gap needs a
   single isomorphism type (gap \(2\) only).

## Workstream B — peel, residual, Chernoff Q

Blocked / identified (do not retry):
- Target \(c_n=1/(|\Omega|p^{Dn/2})\); contain-first mean is biased.
- \(S_n\) to iso-types only; \(d\nu/d\mu\propto\mathbb{E}[1/N\mid\mathrm{containment}]\).
- Edges under \(\nu_D\) match \(\mu_D\); triangles need flat class weights.
- Conditional triangle first-moment proxy is
  \(\bigl((1+\varepsilon)/(2+\varepsilon)\bigr)^3\pi^3\), not \(\pi^3\).
- Switches: \(N\to\infty\), logarithmic bound only \(D^{O(1)}\);
  depth-\(D\) BFS only \(\exp(O(D\log D))\), still below bulk.
- Sandwich posterior ≠ first peel flatness; free-flat ≠ residual flatness.
- Second moment of \(N\): pairwise \(p^{-(K_{12}-K_{012})}\).
- Bernoulli residual diverges; regular-plus-sprinkle TV stays positive.
- Exact \(n=6\), \(D=2\): inverse-count ratio across iso-types in \([1.07,1.16]\);
  triangle \(\nu/\mu\in[0.885,0.942]\); literal \(Z_1\) not flat on \(K_6\).

Still missing (no fake closes):
1. Lower-tail of \(N\) at threshold \(1/c_n\) (Proposition iii-as-tail) —
   not a moment about \(\mathbb{E}[N]\), not near-disjoint factors, not switches.
2. Three peel-weight flatnesses on \(G^*_0\) (asymptotic \(Z_d\), not literal).
3. Second moment on actual \(R=G^*_0\setminus G\) (nearly regular of scale
   \(\varepsilon_0 d\)).
4. Binomial thinning or BIM Conjecture 1.3 — not hybrid, not sprinkle.
   That is Conjecture Q at Chernoff scale.

## Named status

| Conjecture | Status |
| --- | --- |
| Q | Open |
| config-split | Open (iii on single orbits only) |
| residual-moment | Open |
| factor-moment | Open only for \(\min(L,D-L)=\omega(n^{1/3})\) on linear hosts |
| factor-rate | Open only on that same balanced range |
| long-step | Open under four linear margins; matching-gap and matching-into-Dirac closed |

## Next

Priority order:
1. Signed comparison on balanced \(\min(L,D-L)=\omega(n^{1/3})\) (Workstream A).
2. Lower-tail of \(N\) at \(1/c_n\) under true \(\mu_D\) dependence (Workstream B).
3. Four-linear-margin long-step, or residual-moment on the nearly regular window.

Run `python scripts/approach_screen.py` before expanding an attack.
Append Wolfram checks to `v2/notes/wolfram-checks.md`.

## v1

Do not edit `v1/paper/main.tex` except Gao errata.
