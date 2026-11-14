# residual-moment-bim: the host-term obstruction (corrected scale)

## Summary

`conj:residual-moment-bim` (relative variance `o(1)` of the number of `m`-factors of
`R = G*_0 \ G`, conditionally on `G`) is **open**.  Its single unproved ingredient for
the degree-conditioned form is `lem:avoid-G-host`: for every `d`-regular `G` and every
`g` in the residual degree window, under `H ~ Unif(Omega(C,g))` with `C = K_n \ G`, the
`m`-factor count has `Var/E^2 -> 0` uniformly in `G,g`.  Equivalently this is the
"non-regular degree sequence" case of `rem:growing-degree-scope`.

## The obstruction, with the correct normalisation

The regular proof (`thm:growing-degree-factor`) collapses the McKay exponents because for
`g_v == D` the host term is deterministic and cancels in every ratio.

For a near-regular sequence the correct McKay object is the **loop parameter**

    lambda(g) = sum_v g_v(g_v-1) / (2 sum_v g_v),

not the raw `sum_v g_v(g_v-1)`.  Writing `g_v = delta(1+e_v)` with relative deviations
`e_v`, `E = sum_v e_v`, `R2 = sum_v e_v^2`,

    lambda(g) - (delta-1)/2 = delta (E + R2) / (2 (E+n)).      (exact, sympy)

Dividing by `2 sum_v g_v = 2 n delta (1+o(1))` is the step the earlier worker-2 note
dropped: it quoted `sum_v g_v(g_v-1) = delta(delta-1)n + (2 delta - 1) sum y_v + sum y_v^2`
and carried the raw `(2 delta - 1)` coefficient, which is the normalisation error.

For a *relative* window `|e_v| <= eps_n` one has `|E| <= eps_n n` and `R2 <= eps_n^2 n`,
so

    |lambda(g) - (delta-1)/2| <= eps_n delta (1+eps_n)/2 = O(eps_n delta),

and the exponent carries `lambda^2`, whose movement is

    2 lambda_0 dlambda = O(delta · eps_n delta) = O(eps_n delta^2).

At BIM scale `delta = d^{2/3}(log n)^{1/3}` and `eps_n = (1/2)(log n/d)^{1/3}` (the
residual-sharp relative window), one gets

    eps_n delta^2 = (1/2) d log n -> infinity,

so a *relative* window is too coarse for a pointwise `o(1)` host term.  This is the honest
obstruction, and its correct magnitude is `O(eps_n delta^2)`, not the `Theta(delta·beta)`
(with `beta = m sqrt(n/(2 delta))`) quoted earlier.  The two scales are unrelated; the
earlier one had a dimensionally wrong `m` in the numerator and a missing `1/(2 n delta)`
normalisation.

## What therefore closes it (or refutes it)

For the degree-conditioned form to hold at BIM scale one needs either

1. a first-moment formula flat in `g` to `1+o(1)` across a window of *absolute* width
   `eps_n delta` with `eps_n delta^2 = o(1)` (i.e. `eps_n = o(delta^{-2})`), which is far
   tighter than the residual-sharp relative window; or
2. a normalisation by the random mean `E[Z | G, deg R]`, which a weak law of large numbers
   gives but which does not by itself feed `prop:residual-to-peel-weight` (it wants a
   deterministic `nu_n`); or
3. a direct estimate of the residual-law second moment that does not route through
   near-regular host flatness.

## Verified (sympy, `v2/scripts/residual/host_term_cancel.py`)

* `[R1]` fixed-degree excess is `x^3/6 + x^4/8 + x^5/10 + O(x^6)`, `x = 1/(D-1)`, so the
  `(D-1)^-4` coefficient is **1/8**; the `1/D` expansion is `1/(6D^3) + 5/(8D^4) + O(D^-5)`.
* `[H]`  `lambda(g) - (delta-1)/2 = delta(E+R2)/(2(E+n))` exactly.
* `[F]`  (`avoid_g_host.py`) first-moment host exponent `Phi1(e,s2)` has
  `dPhi1/de = -m/(2n)` and `dPhi1/ds2 = 0` exactly: the degree-spread direction
  `s2 = sum y_v^2` cancels, and the edge-count direction `e = sum y_v` enters with
  the small coefficient `-m/(2n)`.
* `[B]`  `eps_n delta^2 = d log n / 2 -> infinity` at BIM scale; the first-moment
  exponent shift is `m eps_n delta / 2 = d^{5/6}(log n)^{7/6}/4 -> infinity`.
* `[B1],[B2]` switching bookkeeping identities (unaffected).

## Note on the matching case

`thm:residual-matching-constrained` conditions on **exact** degree `delta`, where `g` is
constant and `lambda(g) = (delta-1)/2` is deterministic, so it is unaffected.  The
window-mixture step `lem:residual-window-means` claims a `1+O(eps_n)` shift across the
relative window; by `[H]` the correct shift of the loop parameter is `O(eps_n delta)`,
so that lemma's stated error is too optimistic unless the host `mu`-term supplies an
additional cancellation.  This is a separate item to verify for `m=1`.
