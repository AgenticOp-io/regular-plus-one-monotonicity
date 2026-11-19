"""Step 1 (near-regular host): the pairing-level overlap shift is real.

For a degree sequence with n/2 vertices of degree D-b and n/2 of degree D+b,
computes the exact pairing second moment of the m-factor count,
    E Z^2/(E Z)^2 = sum_A P(S=A) g(A),
S = sum of independent hypergeometric(d_v; m, m), g as in
Lemma factor-one-dim with Dn replaced by sum_v d_v (the derivation there is
per cell and goes through verbatim), and compares log of it with the
Gaussian prediction
    -1/2 log(1 - psi'' sbar^2) + n psi'' dq^2 / (2 (1 - psi'' sbar^2)),
dq = <m^2/d> - m^2/D, sbar^2 = <Var h_v>, psi'' at alpha0 = m^2/D.
The second term (Xi) grows linearly in n: the exact-degree pairing moment
does not concentrate unless n m^2 tau^4 / D^5 -> 0.
Also checks the exact formula on a tiny case by brute-force enumeration of
pairings.
Run: python near_regular_pairing_shift.py  (exits nonzero on failure)
"""
import itertools
import math
from fractions import Fraction

import numpy as np

gammaln = np.vectorize(math.lgamma)


def logM(N):  # log (N-1)!!
    N = np.asarray(N, dtype=float)
    return gammaln(N + 1) - (N / 2) * math.log(2) - gammaln(N / 2 + 1)


def hyp(d, m):
    return np.array([math.comb(m, a) * math.comb(d - m, m - a) / math.comb(d, m) for a in range(m + 1)])


def exact_log_ratio(degs, m, window=False):
    pmf = np.array([1.0])
    for d in degs:
        pmf = np.convolve(pmf, hyp(d, m))
    n, E2 = len(degs), sum(degs)
    A = np.arange(len(pmf))
    keep = np.ones(len(A), bool)
    if window:
        mean = sum(m * m / d for d in degs)
        sd = math.sqrt(sum(m * m * (d - m) ** 2 / (d * d * (d - 1)) for d in degs))
        keep = np.abs(A - mean) <= 15 * sd
    # shortcut: float tails below ~1e-300 are noise amplified by g; the window
    # is 15 sd (tails are bounded analytically by I > psi, Lemma factor-rate).
    ok = (A % 2 == 0) & (pmf > 0) & keep
    A, P = A[ok], pmf[ok]
    lg = (logM(A) + 2 * logM(m * n - A) + logM(E2 - 2 * m * n + A) + logM(E2)
          - 2 * logM(m * n) - 2 * logM(E2 - m * n))
    w = np.log(P) + lg
    mx = w.max()
    return mx + math.log(np.exp(w - mx).sum())


def prediction(degs, m):
    n = len(degs)
    D = sum(degs) / n
    a0 = m * m / D
    q = sum(m * m / d for d in degs) / n
    s2 = sum(m * m * (d - m) ** 2 / (d * d * (d - 1)) for d in degs) / n
    psi2 = 1 / (2 * a0) + 1 / (m - a0) + 1 / (2 * (D - 2 * m + a0))
    k = 1 - psi2 * s2
    return -0.5 * math.log(2 * k), n * psi2 * (q - a0) ** 2 / (2 * k)


def brute(degs, m):
    """E Z^2/(E Z)^2 over all pairings, exact rationals (tiny cases)."""
    pts = [(v, i) for v, d in enumerate(degs) for i in range(d)]

    def pairings(ps):
        if not ps:
            yield []
            return
        a = ps[0]
        for j in range(1, len(ps)):
            for rest in pairings(ps[1:j] + ps[j + 1:]):
                yield [(a, ps[j])] + rest

    Z1 = Z2 = cnt = 0
    for P in pairings(pts):
        z = 0
        for sub in itertools.product((0, 1), repeat=len(P)):
            deg = [0] * len(degs)
            for (x, y), s in zip(P, sub):
                if s:
                    deg[x[0]] += 1
                    deg[y[0]] += 1
            z += all(t == m for t in deg)
        Z1 += z
        Z2 += z * z
        cnt += 1
    return Fraction(Z2 * cnt, Z1 * Z1)


ok = True
# tiny brute-force check of the per-cell formula with unequal degrees
for degs, m in [((1, 3, 2, 2), 1), ((3, 3, 1, 1), 1), ((2, 4, 2, 2), 1), ((3, 1, 2, 2, 3, 1), 1)]:
    b = brute(degs, m)
    e = math.exp(exact_log_ratio(list(degs), m))
    print("brute", degs, m, float(b), "formula", e)
    ok &= abs(float(b) - e) < 1e-9 * e
# growth in n
for D, b, m in [(6, 1, 1), (6, 1, 2), (8, 2, 2)]:
    for n in (1000, 2000, 4000, 8000):
        degs = [D - b] * (n // 2) + [D + b] * (n // 2)
        ex = exact_log_ratio(degs, m, window=True)
        c, xi = prediction(degs, m)
        print(f"D={D} b={b} m={m} n={n}: log ratio exact {ex:.5f}  pred {c + xi:.5f}  (Xi={xi:.5f})")
        ok &= abs(ex - c - xi) < 0.05 + 0.1 * xi
assert ok
print("OK")
