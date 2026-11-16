# r6: what (iii') actually requires, and whether the log-normal obstruction matters

Labels: [P] proved/elementary, [H] heuristic argument, [N] numerical. main.tex not edited. No new script (nothing numerical was needed or run).

## 1. Requirement [P]
`worker1_config_split.txt` sec. 4: (iii') is a(G0) = (1+o(1)) abar outside a set of mu_D-mass o(1), and (iii') <=> d_TV(nu_D, mu_D) -> 0,
via d nu_D/d mu_D = Y = a/abar with E_mu Y = 1. Downstream items (iv) / conj:config-split / conj:Q only use TV.
So (iii') needs **TV closeness of the planted law to mu_D, i.e. Y -> 1 in probability over G0 ~ mu_D**.
It does NOT need N/E[N] -> 1 in probability or in L2 under G(n,p). (PROGRAM.md only lists selection (iii) as a row; the primed
form lives in the worker1 note, and r4/r5/r6 notes already say it should be read as a TV statement.)
Caveat: N/EN -> 1 in L2 is *sufficient* (via Lemma 1 / planting reduction) but not necessary.

## 2. Does the log-normal obstruction matter? [H, not proved]
Facts: nu_D(G0) = p^{Dn/2} E[1/N | G0 subset G], so Y(G0) = E[1/N | G0 subset G] / its mu_D-average.
Suppose log N = f(host statistic S) + o(1), with S = host degree-sequence functional (the pairing-mean of Lambda, ~ -sum y_v^2 / 2(M-1)),
and e^{-beta Lambda}-dependence giving log-normal N with variance K = beta^2 Var(Lambda) not small (r4 Sec 8, r6 tilted note Sec 5).
Then Y is the ratio of the law of S given "G0 subset G" integrated against e^{-f}. A fluctuation of N of size sqrt(K) is harmless
for Y unless **the conditional law of S given G0 depends on G0**. Given G0 (D-regular), G = G0 + G(n,p) on the complement, and
 - every host degree is D + r_v with r_v ~ Bin(n-1-D, p): the mean of S is G0-independent;
 - Var-level: sum_v r_v^2 involves the 2-path count of the complement graph = n*C(n-1-D,2), G0-independent since complement of a regular graph is regular;
 - G0 enters only through 4-cycle / higher cycle counts of G0 (cumulants of order >= 3 in S), a relative effect O(D/n)-ish per cumulant.
So the G0-dependent part of log Y is expected to be K * O(D^a/n) -> 0, Y -> 1 in probability, **despite sd(log N) = sqrt(K) -> infinity**.
Hence under the true requirement the log-normal obstruction is not an obstruction by itself; the earlier "Sec 5 Honest obstruction"
(r6_tilted_second_moment.md) conflated N/EN -> 1 with Y -> 1. This is also why (iii') fails only through G0-dependence (triangles, small cycles of G0:
the small-subgraph-conditioning condition |eta_k| = o(D^{-k/2}) of worker1 sec 4), not through N's spread.

## 3. What this does and does not give
- NOT proved: the claim that the law of S (hence of N) given G0 is G0-independent to o(1) in the sense needed (needs the cycle-count
  cumulant bound above, uncomputed). NOT proved: the Gaussian step of the tilted pairing moment; the numerical R(-beta) < 1 values remain
  Gaussian-truncation artifacts [N] and are irrelevant to the TV route, which does not use a second moment of N at all.
- Consequence for the programme: stop trying to make N concentrate under G(n,p) (the tilted second moment). The live statement is
  Y -> 1, i.e. show E[1/N | G0] is flat across G0 up to o(1) in L1. A one-line proof route: condition on host degree sequence
  (sufficient statistic for N up to o(1), conjectural) and compare the degree-sequence laws given different G0 in TV.
- If instead the downstream use were the planting reduction (Lemma 1, E|Z-1|), the obstruction DOES bite (needs L1/L2 of N/EN).
- Not done: a numerical stress test of the Gaussian step at cumulant level (judged unnecessary under the TV requirement; would be needed
  only if one insists on the L2 route). Suggested check if wanted: exact small-n Var of S given two non-isomorphic G0 (cycle-count effect).
