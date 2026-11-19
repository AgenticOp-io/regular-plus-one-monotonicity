# r14w1: the conditioning term 9 - 42/D^2 in r2(D) — NOT proved; reduced and sharpened

Script: `v2/scripts/r14w1_poisson.py` (sympy, seconds). Exact data check: `r13w1_r2_formula.py` re-run, fits agree with
r2=(D-1)(11D-16)/D^2 at D=3..7 (3.77778, 5.25, 6.24, 6.94441, 7.46898 vs 7.46939; D=7 is a fit with ~.002 error).

## Decomposition (exact)
E[T] = (n)_3/6 * (D(D-1))^3/((M-1)(M-3)(M-5)) * R,  M=nD,  R = P(simple | rest, 3 vertices of degree D-2, M-6 stubs, no extra edges among a,b,c) / P(simple).
The prefactor is exact; all the content is R = 1 + r1'/n + r2'/n^2.

## What was proved (by computer algebra of exact pairing expectations)
"Poisson" model: R_P = exp(-(Lam' + x - Lam)), Lam = exact E[loops]+E[double edges] in the pairing model (exact formulas
sum C(d,2)/(M-1) + sum_{i<j} 2C(d_i,2)C(d_j,2)/((M-1)(M-3))), x = 3(D-2)^2/(M-7) for the three forbidden edges.
 - First order: gives r1 = 3(D-1)/D exactly (matches r12w1, data).
 - Second order: r2_Poisson = -(3D^3 - 17D^2 - 9D + 56)/D^2.
## What is NOT explained: the second-order residual
 r2 - r2_Poisson = 3(D-2)(D^2-12)/D^2 = 3D - 6 - 36/D + 72/D^2   (D=3..7: -1, 1.5, 4.68, 8, 11.33).
 Grows linearly in D, so the Poisson heuristic is genuinely wrong at n^-2 (it is only right at n^-1). Factor (D-2) = the degree drop is
 natural: the residual vanishes when the three vertices are not perturbed.
 Where it comes from: log P(simple|d) = -Lam(d) + A(d)/n + O(n^-2) where A (cluster terms: triple edges, loop/double overlaps,
 correlations between forbidden a-b-c edges and nearby bad events) is a smooth function of the degree moments.
 Perturbing 3 vertices moves the moments by O(1/n), so A/n changes by O(1/n^2): this gradient dA, plus local a,b,c correlations,
 is exactly the missing term. So the "9 - 42/D^2" claim is equivalent to the identity
   (gradient of A at the D-regular sequence in direction of three degree-(D-2) vertices) + local abc correlation terms = 3(D-2)(D^2-12)/D^2.

## Status
 PROVED: exact decomposition; r1 = 3(D-1)/D from first-order Poisson part; r2_Poisson formula; pairing part (r13w1).
 REDUCED TO (not proved): Lemma G — P_simple(d) = exp(-Lam(d)) (1 + A(d)/M + O(n^-2)) uniformly for bounded degrees with A smooth
   (polynomial in power sums of d), plus the value of the gradient/local terms above. Needs McKay-style 1/n term for general degree
   sequences or a switching argument with second-order accounting; neither was done here.
 CONJECTURED (numerically exact D=3..6, D=7 to 4e-4 relative): r2 = (D-1)(11D-16)/D^2, i.e. conditioning remainder 9-42/D^2.
 NOT DONE: switching proof; computing A for general d (would need exact P(simple|d) data for non-regular d); D>=8.
