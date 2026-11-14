# residual-moment-bim: final resolution (verified)

## Verdict

`conj:residual-moment-bim` is **false as literally stated**, and this is now a
*completed* result with the obstruction identified exactly, not an open gap.

After step 3 (window mixture) the only surviving true form is the degree-conditioned
form whose ingredient is `lem:avoid-G-host` (worker 2): for `H ~ Unif(Omega(C,g))`,
`C = K_n \ G`, `G` `d`-regular, `g` in the residual degree window, the `m`-factor count
has `Var/E^2 -> 0` uniformly in `G,g`.

## The obstruction, located exactly

The regular proof (`thm:growing-degree-factor`) uses the McKay estimate (main.tex
line 5744-5757):

    N(g,X) · prod_v g_v! / (2M-1)!! = exp(−lambda(g) − lambda(g)^2 − mu(g,X) + O(Δ^2/M)),
    lambda(g) = sum_v g_v(g_v−1) / (2·sum_v g_v),   mu(g,X) = sum_{ij in X} g_i g_j / sum_v g_v.

There are **two** host-dependent pieces, and they behave differently:

### (a) The loop parameter lambda(g) is flat (this part is FINE)

Write `g_v = delta + y_v`, `e = sum_v y_v`, `s2 = sum_v y_v^2`.  Exactly (sympy):

    lambda(g) − (delta−1)/2 = delta·(E + R2) / (2(E+n)),
    E = e/delta (relative),  R2 = s2/delta^2 (relative).

For a *relative* window `|y_v| <= eps·delta`:

    |lambda(g) − (delta−1)/2| <= eps·delta·(1+eps)/2 = O(eps·delta).

In the four-pairing second-moment ratio of `thm:growing-degree-factor` the *first*
moment of `lambda` cancels exactly (the paper's `lem:mckay-exponent` identity is an
exact rational identity in `D,L`), and the curvature in `e` is exactly `0` while the
`ds2` curvature is `O(delta^-2 n^-2)`.  So **lambda contributes only a constant (`O(m)`)**,
and does not by itself obstruct `Var/E^2 -> 0`.

### (b) The configuration-model prefactor is NOT flat (this is the obstruction)

The ratio `N(C,g;F)/N(C,g)` carries the prefactor `(2M-1)!!/prod_v g_v!` (McKay's
enumeration).  For two *constant* sequences `delta` and `delta+2`, the exact leading term
is (verified with high-precision log-gamma, `residual_window_means.py`):

    log[ N(delta+2) / N(delta) ] = n log(n/delta) + O(n/delta)  → infinity.

For `delta=200, n=10^6` this is `8,507,239`, against `n log(n/delta) = 8,517,193`
(relative error ~0.1%).  The earlier `nm/delta` figure (`10^5` here) is wrong by a
factor ~85; the correct rate is `n log(n/delta)`, not `nm/delta`.  (The two coincide only
in their *divergence*, not their magnitude.)

Consequently the first moment `E[Z | G, deg R = g]` moves by

    exp( Theta(n log(n/delta)) ) = (n/delta)^{Theta(n)}

across a constant shift of the window, which diverges enormously for `delta = o(n)`.
This is the corrected rate replacing both the `beta`-scale and the `e^{n/delta}` scale
quoted in earlier versions.  The loop parameter squared contributes only the subleading
`eps·delta^2` form; the dominant prefactor is `n log(n/delta)`.

## Conclusion of the theorem

The first moment `E[Z | G, deg R = g]` is **not flat** across the residual degree window:
it varies by `exp(Theta(n log(n/delta))) = (n/delta)^{Theta(n)}` over typical values of
`e(R)`.  Therefore

* the degree-window mixture diverges (step 3, `thm:s3-window-diverges`), and
* there is **no deterministic `nu_n`** with `N_m(R)/nu_n -> 1` in probability
  (`prop:residual-to-peel-weight` cannot be fed by this).

The literature conjecture is therefore refuted in its stated form; there is nothing to
"fix" that recovers a deterministic concentration.  The only surviving statements are:

1. the **exact-degree** form (`thm:residual-matching-constrained` for `m=1`, and the
   `thm:growing-degree-factor` regular case for every `m`), where `g` is constant and the
   prefactor is deterministic; and
2. the **random-mean-normalised** concentration (step 3 item (ii)) conditional on
   `lem:avoid-G-host` — a weak law around `E[Z | G, deg R]`, not around a deterministic `nu_n`.

## What "fix all" correctly means

There is no algebraic fix that makes the literal conjecture true: the `n log(n/delta)`
prefactor sensitivity is the genuine content of the `G(n,M)`-type threshold `p sqrt n -> infinity`
for perfect matchings, now for `m`-factors.  The honest fixes are:

* **Correct the paper**: `lem:residual-window-means` (which asserts `1+O(eps_n)` flatness)
  and `cor:residual-matching-window` are false; the mean flatness fails by
  `(n/delta)^{Theta(n)}`.  These must be marked as false/withdrawn, with the exact-degree
  theorem retained.
* **Record the correct substitute**: degree-conditioned concentration around the random
  mean, conditional on the (still-open) `lem:avoid-G-host`, which no deterministic
  peel-weight normaliser absorbs.

## Verified (sympy)

* `avoid_g_host.py`  — `lambda(g)-(delta-1)/2 = delta(E+R2)/(2(E+n))`; `dPhi1/de = -m/(2n)`,
  `dPhi1/ds2 = 0`, `d^2Phi1/de^2 = 0` exactly.
* `avoid_g_host2.py` — same first-order facts; `ds2^2` curvature `O(delta^-2 n^-2)`.
* prefactor numerics (`math.lgamma`, `residual_window_means.py`) — `delta→delta+2` shift
  is `n log(n/delta) + O(n/delta)`; e.g. for `(delta,n)=(200,10^6)` it is `8,507,239`
  against `8,517,193`.  This corrects the earlier `nm/delta` figure.
* `host_term_cancel.py` — fixed-degree excess series and switching identities.
* `main.tex` line 5534 — `(D-1)^-4` coefficient corrected `5/8 → 1/8` (the `1/D`
  expansion gives `5/(8D^4)`; the `(D-1)` form is `1/8(D-1)^4`).
