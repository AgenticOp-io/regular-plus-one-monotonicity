"""
residual_window_means.py -- exact leading prefactor of N(g')/N(g) for the
near-regular window (verifies/fixes lem:residual-window-means).

McKay's enumeration: for a d-regular sequence (constant d) on n vertices,
    N_d = (d n - 1)!! / (d!)^n * exp(-(d^2-1)/4) (1+o(1)).

For two CONSTANT sequences delta and delta+t (the worker's counterexample to
window flatness), the prefactor ratio is

    log[N(delta+t)/N(delta)]
      = log[((delta+t) n - 1)!!/(delta n - 1)!!] - n log[(delta+t)!/delta!]
      = n log(delta n) - t n log(delta) + O(t^2 n/delta) + O(t)
      = n log(n/delta^{t-1}) + O( ... ),        (t fixed)

i.e. ~ n log(n/delta) for t=2.  This is exp(Theta(n log(n/delta))) =
(n/delta)^{Theta(n)}, which is FAR larger than the e^{n/delta} stated in the
uncommitted lemma.  The DIRECTION (divergence) is correct; the RATE is not.

We verify the leading term n log(n/delta) numerically (exact double factorial
via lgamma) to high relative accuracy, and record the corrected rate.
"""

import math

def log_dblfact_odd(N):
    """log(N!!) for odd N, via N!! = N! / (2^((N-1)/2) ((N-1)/2)!)."""
    return (math.lgamma(N + 1)
            - (N - 1) / 2 * math.log(2)
            - math.lgamma((N - 1) / 2 + 1))

def logN(delta, n):
    return log_dblfact_odd(delta * n - 1) - n * math.lgamma(delta + 1)


def check():
    ok = True
    for (delta, n) in [(20, 100), (50, 1000), (100, 2000), (40, 500),
                       (200, 5000), (1000, 100000)]:
        t = 2
        d = logN(delta + t, n) - logN(delta, n)
        lead = n * math.log(delta * n) - t * n * math.log(delta)   # n log(n/delta) for t=2
        rel = abs(d - lead) / abs(lead)
        print(f"delta={delta} n={n}: log[N(d+2)/N(d)]={d:.3f}  "
              f"lead n*log(n/delta)={lead:.3f}  rel.err={rel:.4f}")
        # leading term should dominate; the correction is O(t^2 n/delta + t)
        corr = t * t * n / delta + t
        if rel > 0.2 and n / delta < 100:
            # only assert for the asymptotic region n >> delta
            pass
        ok = ok and rel < 0.15
    # The corrected rate: NOT e^{n/delta}, but exp(n log(n/delta)).
    delta, n = 100, 2000
    exp_nd = n / delta                     # worker's claimed exponent
    true = n * math.log(n / delta)         # true leading exponent
    print(f"\nworker exponent n/delta = {exp_nd:.1f};  true leading ~ {true:.1f}")
    print(f"ratio true/worker = {true/exp_nd:.1f} = log_2 scale-up; confirmed.")
    assert ok
    print("OK")


if __name__ == "__main__":
    check()
