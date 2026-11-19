# r20 write-up: what is proved, what is conditional on R2*
(Summary of r15-r20 notes; no scripts re-run for this file.)

## Proved
- R1; switching bound t3 <= 8 L^3/n^3 (k<=3, valid for L = o(n^{1/3})).
- Pairing-model part of log p_U is vertex-local + f(|U|): k-th Ursell difference of a non-star T is O(n^{-(k-1)}) (r16w1, r20a, by hand).
- Hence R2* (k=4) <=> 4th finite difference of log P(simple | U) over T is O(D^a/n^2) (r20a).
- Q(H) = g(H) prod(D-h_v)!/(N-2L-1)!! (r17a); everything reduces to g(H)/g(empty), the same gap as r2(D).
- Exp-form Theorem 6 for one-sided j-stars and S1_1_0 (r10w3).

## Conditional on R2* (= relative-error-o(n^-2) expansion of P(simple | host))
- (B*) |kappa_k| <= C^k k! L^{k+1}/n^{k-1}, k>=4, extending past n^{1/3} to L=o(n^{1/2}).
- Triangle coefficient r2(D) in exp-form Theorem 6.

## Heuristic / numeric only
- Adjacent-pair coefficient c(D) = (D-2)/D (Poisson loops/double-edge count, r20b). Only D=3 checked: prediction 1/3,
  extrapolated data ~0.31. D=4,5,6 unchecked; remainder O(D^b/n^2) unproved.
- r20a's first-order estimate for P3 (-0.11/n at D=3) disagrees with exact (-0.31/n) by ~3x, so the first-order Poisson picture
  is incomplete at k=3; this casts some doubt on r20b's closed form (same method).
- Conditioning on assortativity (r16w2) removes ~97% of the blow-up but residual log-ratio still grows ~linearly in n.
- (B*) disk zeros numerics: nearest zero R*L/n ~ 0.43-0.44 for L=2,3 (r10w2); L>=4 failed.

## Not found
No counterexample to R2*; only saturated stars violate the n^-2 decay. No rigorous two-sided count of simple D-regular graphs containing H.
