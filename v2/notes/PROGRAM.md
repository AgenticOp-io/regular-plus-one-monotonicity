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
   The logarithm \(L(L-1)/(2n)\) is not that moment: on all 19355 four-regular
   graphs on eight vertices the \(L=2\) excess is \(89344/17363889\), about
   \(1/24\) of \(1/8\) (Remark eight-factors). A sample of twenty-five
   six-regular graphs on twelve vertices has \(2\)-factor relative variance
   about \(5\cdot 10^{-4}\), against \(1/12\). The half-degree package
   through order \(1/n^2\) is \(t/2-(4/3)t^2\) at \(t=L^2/n\), which is
   negative for \(t>3/8\) and is therefore not the ratio.
   The binomial factor \(\exp(L^2(1-p)/(2p))\) is the edge-count fluctuation
   of \(G(n,p)\) (Gao, Random Structures Algorithms 2013, Theorem 2.1); in
   \(G(n,m)\) the same count concentrates for \(L^3=o(p^2 n)\) (Theorem 2.4).
   A regular host fixes the edge count, and Theorem linear-below-sqrt already
   passes that restriction. Multiplying the switching error
   \(O(\ell/(Ln)+L/n)\) through \(\ell\le\kappa L^2\) produces
   \(\exp(O(L^3/n))\) (Proposition switching-accumulation), which is coarser
   than the entropy remainder \(O(L^4/n^2)\) by the factor \(L/n\).
   That switching precision does not pass \(\sqrt{n}\). The missing
   cancellation is inside the entropy remainder.
   Short-cycle prediction (Remark cycle-prediction): the factor/non-factor
   chain along a path has second eigenvalue \(-1/(D-1)\) for every \(L\), so
   small subgraph conditioning predicts excess
   \(\tfrac12(-\log(1-x)-x-x^2/2)\), \(x=1/(D-1)\), independent of \(L\).
   The counts at \(D=4,5,6\) are of that order. Not a proof: the
   configuration-model input is blocked on linear hosts. The live route is
   the cycle-count identification on the simple graph for all \(k\le n\).
2. Four-linear-margin long-step — closed as Theorem long-step for every
   \(L=o(n)\). Theorem matching-linear-rate is the matching variance
   \(O(1/n^2)\): the origin, the vertex-radius correction \(-\gamma k/n\),
   the Gaussian width, and the angular traces average to zero against the
   intersection tilt. Lemma matching-step-l1 turns that variance into
   total variation \(O(1/n)\) for one step, by the identity
   \(Z|1/Z-1/\mathbb{E}Z|=|1-Z/\mathbb{E}Z|\). A union bound of \(L\) steps
   is \(O(L/n)\). Factor-count flatness past \(\sqrt{n}\) stays open.

3. Peel side, proved: Theorem successive-peel (explicit peel, sure
   containment, \(O(L/n)\) for the lower law above half degree) and
   Theorem peel-bounded-to-flat (bounded peel second moments imply
   \(L^1\) flatness of \(P_L\) at rate \(\sqrt{1+B}\,L/n\); unconditional at
   \(L=2\)). Theorem two-peel-variance gives \(P_2\) relative variance
   \(O(1/n)\), so \(L=3\) is unconditional (Corollary three-peel-flat).
   Lemma fixed-moments and Theorem peel-moments make every fixed \(L\)
   unconditional (Corollary fixed-peel-flat, \(O_L(1/n)\)).
   Theorem uniform-moments (McKay 2011, Corollary 5) and Theorem
   log-peel-flat reach \(L\le\varepsilon_1\log n\).
   Theorem peel-second-moment and Corollary poly-peel-flat reach
   \(L\le n^{\varepsilon_2}\) directly.
   Proposition im-containment (Isaev--McKay 2025) supplies containment
   probabilities to any precision for subgraphs of degree \(\le n^{1/2}\),
   so the enumeration range is no longer the obstruction.
   Lemma containment-ratio, Theorem peel-second-moment-third and Corollary
   peel-flat-third use it for an upper bound with error \(O((L^3+1)/n)\):
   peel flatness \(O(L/n)\) for every \(L\le n^{1/3}\).
   Route past \(n^{1/3}\): notes/multicolour-llt-skeleton.md (unproved)
   reduces factor-moment at linear \(L\) to a cumulant constant
   \(C(\alpha,\lambda)\) plus a vector outside-region estimate. \(C\equiv0\) is now
   Lemma cumulant-constant, so Theorem factor-moment-conditional holds under
   Hypothesis mllt, and Theorem mllt proves the hypothesis on \(K_n\): the
   factor second moment at linear length is now unconditional, and with
   Theorem long-step the long-step coupling holds at every length with two
   linear margins (Corollary long-step-all). Theorem factor-moment-sparse
   extends the factor moment to \(L\ge n^{3/4+\eta}\) (rate \(O(n^{-1/8})\)) via
   IM25 Theorem 2.6 in density-rescaled coordinates; factor-moment is open
   only on \(\sqrt n\ll L\le n^{3/4+o(1)}\).
   Remaining: (ii) extend Theorem mllt to \(a\ge n^{-1/2+\varepsilon}\) (sparse
   colours, \(p_0\to0\)); (iii) compute the order-\(n/L^2\) second difference
   (factor-rate).
   Alternative next: expand the Isaev--McKay cumulant formula for \(K_n-F_1\cup F_2\)
   against \(K_n-F_1\), \(K_n-F_2\), \(K_n\) through order \(L^4/n^2\) and average
   over the overlap structure; this is the remaining content of
   factor-moment between \(n^{1/3}\) and \(n^{1/2}\). An edge-probability theorem for
   the uniform ordered-matching-decomposition law (needed for \(P_L\to Z_L\)
   via the v1 factor-third route). The lower tail of \(Y\) is blocked (see STATUS).

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
| long-step | Closed for every \(L=o(n)\) with four linear margins (Theorem long-step). Matching variance \(O(1/n^2)\) is Theorem matching-linear-rate; one step has total variation \(O(1/n)\) (Lemma matching-step-l1). Factor-count flatness past \(\sqrt{n}\) stays open. Hamilton coupling is not \(\mu_2\) |

## Next

Priority order:
1. Factor moment for \(L=\omega(\sqrt{n})\) (Workstream A). Every linear host with \(L^2=o(n)\) is Theorem linear-below-sqrt.
2. Lower-tail of \(N\) at \(1/c_n\) under true \(\mu_D\) dependence (Workstream B).
3. In-probability flatness of the two \(L\)-factor counts past \(\sqrt{n}\)
   (Theorem long-from-flat), or residual-moment on the nearly regular window.
   The four-linear deletion of length \(L=o(n)\) is Theorem long-step.

Run `python scripts/approach_screen.py` before expanding an attack.
Append Wolfram checks to `v2/notes/wolfram-checks.md`.

## v1

Do not edit `v1/paper/main.tex` except Gao errata.
