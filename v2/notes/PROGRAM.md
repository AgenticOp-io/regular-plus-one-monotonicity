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
| long-matching-growing | Matching into every host \(D\to\infty\) (band-rate or sublinear variance below \(n/2\)) |
| long-hamilton-dirac | Uniform Hamilton cycle inside every host \(D\ge n/2\); marginal is not \(\mu_2\) |
| long-hamilton-wide | Uniform Hamilton cycle inside every host \(D\ge 3\); still not \(\mu_2\) |
| long-matching-at-least-three | Uniform matching inside every host \(D\ge 3\), including bounded and oscillating degrees |

### Selection (iii)

| Result | Range |
| --- | --- |
| cor:iii-one-orbit | \(D\in\{1,n-2\}\) (single \(S_n\) orbit); not a Chernoff-scale config-split close |

## Workstream A — balanced factors and four-linear long-step

Signed Gao after a matching host leaves \(2t/(Ln)\). Treating that product as
\(1+o(1)\) is not a path past \(n^{1/3}\). Keeping the shift, and subtracting
the adjacent falling factorial, cancels the cubic at every linear density:
Theorem linear-below-sqrt gives \(\Var Z/(\EE Z)^2\to 0\) whenever
\(\min(D,n-D)=\Theta(n)\) and \(L^2=o(n)\). The logarithm that
remains is \(L(a-1)(L(a-1)+a)/(2a^2 n)\) at host density \(a=D/n\), which is
\(L(L-1)/(2n)\) at degree \(n/2\). The argument stops short of \(\sqrt{n}\)
and does not give the factor-rate. The
same principal term, summed on three-edge matchings, has mass
\(-L^8/(48n^2)\) after the constant \(4/n^2\) cancels
(Proposition triple-mass-order). The Theorem 6 error is the same order, so
that coefficient does not identify the cumulant. Do not retry:
binomial-PGF-without-pairwise, quadratic-PGF-without-leftover,
origin-at-typical-k, signed-gao-matching-host.

Still missing:
1. The factor moment for \(L=\omega(\sqrt{n})\) — the part of Conjectures
   factor-moment and factor-rate that Theorem linear-below-sqrt does not reach.
2. Four-linear-margin long-step of length \(\omega(\sqrt{n})\) — Conjecture
   long-step. Theorem deletion-below-sqrt gives the deletion for
   \(L^2=o(n)\). Proposition host-trace: the mean of the first two host
   traces is order \(L^2/n^2\) and does not cancel the identified logarithm
   of order \(L^2/n\). Theorem long-from-peel reduces the coupling to
   in-probability flatness of the ordered sequence of \(L\) successive
   perfect matchings at degrees \(d+L\) and \(n-1-d\). Proposition
   peel-budget: that count has relative variance \(O(L/n)\) if each added
   matching increases the relative variance by \(O(1/n)\), which is the
   scale of one matching (v1 Proposition band-rate). The increment is the
   remaining estimate, and it covers every \(L=o(n)\).
   Lemma deletion-density identifies the size-biased deletion weight with the
   complement matching count. Proposition aligned-peel solves the
   Cauchy--Schwarz recurrence on that covariance: the bound is \(O(L^2/n)\)
   and stops at \(\sqrt{n}\). The additive increment has to cancel inside
   that covariance. Past \(\sqrt{n}\), the upper graph can
   be sampled exactly (Theorem long-exact-upper); what remains on that
   route is \(L^1\)
   flatness of \(a(G)=\sum_{H\supset G}1/Z(H)\) and existence of an \(L\)-factor
   with probability \(1-o(1)\). Flatness of both factor counts is still
   sufficient (Theorem long-from-flat). On eight vertices the \(Z\)-ratio is
   \(15/7\) and the \(a\)-ratio is \(409095/397144\).

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
| factor-moment | Half degree with \(L^2=o(n)\) is Theorem half-below-sqrt. Every linear host in that range is Theorem linear-below-sqrt. Open for \(L=\omega(\sqrt{n})\) |
| factor-rate | Open on the balanced range. The logarithm \(L(a-1)(L(a-1)+a)/(2a^2 n)\) is not \(o(L^3/n^3)\) |
| long-step | Open for \(L=\omega(\sqrt{n})\). Theorem deletion-below-sqrt gives the deletion for \(L^2=o(n)\). Proposition host-trace: the mean of the first two host traces is order \(L^2/n^2\) and does not cancel the identified logarithm of order \(L^2/n\). Theorem long-from-peel reduces the coupling to flatness of an ordered sequence of \(L\) matchings. Proposition peel-budget: an increment \(O(1/n)\) per matching gives relative variance \(O(L/n)\) for every \(L=o(n)\); that increment is open. Proposition aligned-peel: Cauchy--Schwarz against the complement matching count solves as \(O(L^2/n)\) and stops at \(\sqrt{n}\). Past \(\sqrt{n}\), the exact upper graph also reduces it to flatness of \(a(G)\). On eight vertices \(Z\) varies by \(15/7\) and \(a\) by \(409095/397144\). Hamilton coupling is not \(\mu_2\) |

## Next

Priority order:
1. Factor moment for \(L=\omega(\sqrt{n})\) (Workstream A). Every linear host with \(L^2=o(n)\) is Theorem linear-below-sqrt.
2. Lower-tail of \(N\) at \(1/c_n\) under true \(\mu_D\) dependence (Workstream B).
3. In-probability flatness of the two \(L\)-factor counts past \(\sqrt{n}\)
   (Theorem long-from-flat), or residual-moment on the nearly regular window.
   The deletion of length \(L^2=o(n)\) is Theorem deletion-below-sqrt.

Run `python scripts/approach_screen.py` before expanding an attack.
Append Wolfram checks to `v2/notes/wolfram-checks.md`.

## v1

Do not edit `v1/paper/main.tex` except Gao errata.
