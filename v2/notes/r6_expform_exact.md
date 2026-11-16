# r6: exact computation of the exp-form (Conjecture B) ratio -- PLAN (stub, updated below)

Status labels used: **proved** / **numerical** / **conjecture**.  main.tex untouched.

## Plan
1. Faster/more general exact engine `v2/scripts/r6_exact.py`: same degree-class DP N(c) as r5w3 but (a) any host
   (edge list, u, v), (b) many hosts per process sharing the memo, (c) multiprocessing over (D, host, n), (d) floats-free (exact ints).
2. Refit n^2*err_exp and n^2*err_prod on larger n / D, adversarial hosts (irregular, dense stars, mixed degrees, |H1|~8-10).
3. Extract the explicit n^-2 coefficient c(H1,u,v) of the exp form from the data; guess closed form in host statistics.
4. Second-order switching proof attempt for that coefficient.

## Results
(filled in below)
