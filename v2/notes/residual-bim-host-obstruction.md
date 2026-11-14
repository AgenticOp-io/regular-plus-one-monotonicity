# residual-moment-bim: what is actually needed and the host-term obstruction

Status after step 3 (window mixture) and the decisive host-term check.

## Summary

`conj:residual-moment-bim` (relative variance `o(1)` of the number of `m`-factors of
`R = G*_0 \ G`, conditionally on `G`) is **open**, and the literal statement is
**false**; see the step-3 fragment. After step 3 the only surviving true form is the
*degree-conditioned* form, whose single unproved ingredient is worker 2's
`lem:avoid-G-host`:

> for every `d`-regular `G` and every `g` in the residual degree window, under
> `H ~ Unif(Omega(C, g))` with `C = K_n \ G`, the `m`-factor count has
> `Var/E^2 -> 0` uniformly in `G, g`.

Equivalently (rem:growing-degree-scope) this is the "non-regular degree sequence"
case of `thm:growing-degree-factor`.

## The obstruction (this is the honest conclusion)

The regular proof (`thm:growing-degree-factor`) collapses the four McKay exponents
because for `g_v == D` the host term

    H(g) = sum_v g_v (g_v - 1)

is deterministic and equal to `D(D-1) n`, so it cancels in every first-moment and
second-moment ratio. For a near-regular sequence `g_v = delta + y_v`,

    H(g) = delta(delta-1) n + (2 delta - 1) sum_v y_v + sum_v y_v^2 .

The linear piece does **not** vanish on the window `{|y_v| <= eps·delta}`:

* the edge-count fluctuation `sum_v y_v = 2(e(R) - k0)` has standard deviation of
  order `beta = m sqrt(n(1-q)/(2 delta))`;
* the resulting McKay-exponent movement is `Theta(delta·beta)`;
* at BIM scale `delta = Theta(d^{2/3}(log n)^{1/3})`, `m = Theta(sqrt(d log n))`,

        delta·beta = Theta( sqrt(n) · d^{5/6} (log n)^{2/3} ) -> infinity.

So the host term moves the mean by `exp(Theta(delta·beta))` across the window, and
the regular-host cancellation step does **not** extend to near-regular hosts. This is
the same first-moment non-flatness already proved in step 3 (`thm:s3-window-diverges`,
`prop:s3-means-not-flat`), seen now at the level of the McKay host term.

**Consequence.** `lem:avoid-G-host` is not a missing line of algebra; it is a genuine
obstruction in the `o(1)`-flatness of the first moment, exactly as step 3 concluded. The
overlap/`K` second-moment machinery of `thm:growing-degree-factor` is *downstream* of a
first-moment flatness that fails at BIM scale for a non-regular residual.

## What therefore closes it (or refutes it)

For the degree-conditioned form to hold at BIM scale one needs either

1. a first-moment formula for the count of `m`-factors of `Unif(Omega(C,g))` that is
   flat in `g` to `1+o(1)` across the window (denied by `Theta(delta·beta) -> inf`
   under the Bernoulli/`Unif` residual law); or
2. a normalisation by the random mean `E[Z | G, deg R]` (the step-3 item (ii) form),
   which is what a weak law of large numbers actually gives, and which does not by
   itself feed `prop:residual-to-peel-weight` (which wants a deterministic `nu_n`).

Neither is settled. The first is obstructed as above; the second leaves the
peel-weight / total-variation transfer open (gap 3 of the step-3 fragment).

## Verified

`v2/scripts/residual/host_term_cancel.py` (sympy):

* `[R1]` the fixed-degree excess is `exp(S)-1 = 1/(6D^3) + 5/(8D^4) + O(D^-5)`, where
  `S = sum_{k>=3} x^k/(2k)`; this exposed and fixed the wrong `D^-4` coefficient
  (`1/8` -> `5/8`) in `thm:fixed-degree-factor` (main.tex line 5534).
* `[H1]` the host-term movement `delta·beta` -> infinity at BIM scale, explicitly.
* `[B1]`,`[B2]` the switching bookkeeping identities in the regular proof.

## Note on the matching case

At `m=1` the host-term movement is `Theta(n^{1/2} d^{1/2}/delta^{... })` -> still
divergent for `delta = o(n^{1/2})`; this is exactly why `lem:residual-window-means`
(the `m=1` window flatness) is false, as step 3 proved. The `m=1` *exact-degree*
statement (`thm:residual-matching-constrained`, degree exactly `delta`) is unaffected,
because there `g` is constant and `H` is deterministic.
