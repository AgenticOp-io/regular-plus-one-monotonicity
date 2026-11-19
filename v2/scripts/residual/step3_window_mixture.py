"""Checks for v2/paper/residual/step3-window-mixture.tex (sympy fallback; no Wolfram app id).

[E] exact enumeration on C = K_6 minus a perfect matching (d = 1, the octahedron), m = 1, 2:
  E1  sum_{|R|=k} Z(R) = Z(C) binom(e-N, k-N), i.e. E[Z | e(R)=k] = Z(C) h(k), h(k) = (k)_N/(e)_N.
  E2  planting: sum_{|R|=k, R in E} Z(R) = Z(C) binom(e-N,k-N) pi_k, pi_k = P_pl,k(E) (double count).
  E3  planted degrees have mean 2k/n (given F and k).
  E4  as polynomials in q: E[Z 1_E] = Z(C) sum_k P(k) h(k) pi_k, and
      E[Z^2 1_E] >= Z(C)^2 sum_k P(k) h(k)^2 pi_k^2 / P(E | k)  (checked at q = 1/3).
[A] sympy algebra:
  A1  (a-i)/(b-i) - a/b = -i(b-a)/(b(b-i))   and   (k-i)/(k0-i) - k/k0 = i(k-k0)/(k0(k0-i)).
  A2  chi^2 identity: sum nu f^2 / (sum nu f)^2 = sum w^2/nu with w = nu f / sum nu f.
  A3  Chernoff exponent: eta^2 delta = 6 log n, t = eta delta - 1  =>  t^2/(3 delta) = 2 log n - 2 eta/3 + 1/(3 delta).
  A4  constant sequences: McKay exponent difference Delta(delta+2) - Delta(delta) = 0 exactly;
      bounds nm(delta-2m-2)/((delta+2)(delta-m)) <= B(delta+2)-B(delta) <= nm(2/(delta-m) - 1/delta + 1/delta^2)
      (algebra of the two bounds + a numeric spot check of B against them).
  A5  BIM scales: beta^2 = m^2 n/(2 delta), m/(eta_n delta), eta_n sqrt(n delta), delta^2/(nm), delta^3/n exponents.
Run: python step3_window_mixture.py   (exits nonzero on failure)
"""
from itertools import combinations
from math import comb, lgamma, log
import sympy as s

# ---------------- [E] exact enumeration ----------------
n = 6
G = {(0, 1), (2, 3), (4, 5)}
EC = [e for e in combinations(range(n), 2) if e not in G]
e = len(EC)


def degs(mask):
    d = [0] * n
    for i, (u, v) in enumerate(EC):
        if mask >> i & 1:
            d[u] += 1
            d[v] += 1
    return d


def factors(m):
    return [M for M in range(1 << e) if all(x == m for x in degs(M))]


q = s.symbols('q', positive=True)
for m, (lo, hi) in [(1, (3, 5)), (2, (3, 5)), (1, (2, 3)), (2, (4, 4))]:
    Fs = factors(m)
    ZC, N = len(Fs), m * n // 2
    assert ZC > 0
    inE = [lo <= min(degs(R)) and max(degs(R)) <= hi for R in range(1 << e)]
    Z = [sum(1 for F in Fs if F & ~R == 0) for R in range(1 << e)]
    lhs_mean = 0
    rhs_mean = 0
    lhs_sq = 0
    rhs_sq = 0
    for k in range(N, e + 1):
        Rs = [R for R in range(1 << e) if bin(R).count('1') == k]
        # E1
        assert sum(Z[R] for R in Rs) == ZC * comb(e - N, k - N)
        assert s.ff(k, N) / s.ff(e, N) == s.Rational(comb(e - N, k - N), comb(e, k))
        # E2: planted pairs (F, U)
        planted = 0
        for F in Fs:
            rest = [i for i in range(e) if not F >> i & 1]
            Us = [sum(1 << i for i in U) for U in combinations(rest, k - N)]
            planted += sum(inE[F | U] for U in Us)
            # E3
            for v in range(n):
                tot = sum(degs(F | U)[v] for U in Us)
                assert s.Rational(tot, len(Us)) == s.Rational(2 * k, n)
        assert sum(Z[R] for R in Rs if inE[R]) == planted
        pi = s.Rational(planted, ZC * comb(e - N, k - N))
        h = s.ff(k, N) / s.ff(e, N)
        Pk = comb(e, k) * q ** k * (1 - q) ** (e - k)
        PEk = s.Rational(sum(inE[R] for R in Rs), len(Rs))
        lhs_mean += sum(Z[R] for R in Rs if inE[R]) * q ** k * (1 - q) ** (e - k)
        rhs_mean += Pk * ZC * h * pi
        lhs_sq += sum(Z[R] ** 2 for R in Rs if inE[R]) * q ** k * (1 - q) ** (e - k)
        if PEk:
            rhs_sq += Pk * ZC ** 2 * h ** 2 * pi ** 2 / PEk
    assert s.expand(lhs_mean - rhs_mean) == 0                     # E4 identity
    assert (lhs_sq - rhs_sq).subs(q, s.Rational(1, 3)) >= 0        # E4 inequality
    print(f"[E] m={m} window=[{lo},{hi}] Z(C)={ZC}: E1-E4 OK")

# ---------------- [A] algebra ----------------
a, b, i, k, k0 = s.symbols('a b i k k0', positive=True)
assert s.simplify((a - i) / (b - i) - a / b + i * (b - a) / (b * (b - i))) == 0
assert s.simplify((k - i) / (k0 - i) - k / k0 - i * (k - k0) / (k0 * (k0 - i))) == 0
print("[A1] ratio inequalities OK")

nu = s.symbols('nu1:4', positive=True)
f = s.symbols('f1:4', positive=True)
S1 = sum(x * y for x, y in zip(nu, f))
w = [x * y / S1 for x, y in zip(nu, f)]
assert s.simplify(sum(x * y ** 2 for x, y in zip(nu, f)) / S1 ** 2 - sum(wi ** 2 / x for wi, x in zip(w, nu))) == 0
print("[A2] chi^2 identity OK")

dl, L = s.symbols('delta logn', positive=True)
eta = s.sqrt(6 * L / dl)
assert s.simplify((eta * dl - 1) ** 2 / (3 * dl) - (2 * L - 2 * eta / 3 + 1 / (3 * dl))) == 0
print("[A3] Chernoff exponent OK")

d, m_, nn, x = s.symbols('d m n x', positive=True)
lam = lambda y: (y - 1) / 2
fl = lambda y: lam(y) + lam(y) ** 2


def Delta(D):  # McKay exponent of N(D-m; G+F)/N(D; G), constant sequences, d-regular G, m-factor F
    return -fl(D - m_) + fl(D) - (d + m_) * (D - m_) / 2 + d * D / 2


assert s.simplify(Delta(dl + 2) - Delta(dl)) == 0
lower = nn * m_ * (2 / (dl + 2) - 1 / (dl - m_))
assert s.simplify(lower - nn * m_ * (dl - 2 * m_ - 2) / ((dl + 2) * (dl - m_))) == 0
print("[A4] McKay Delta difference = 0; lower-bound algebra OK")


def B(nv, D, mv):  # n log (D)_m + log[(n(D-m)-1)!!/(nD-1)!!], via (2r-1)!! = 2^r Gamma(r+1/2)/sqrt(pi)
    df = lambda r: r * log(2) + lgamma(r + 0.5)
    return nv * sum(log(D - j) for j in range(mv)) + df(nv * (D - mv) // 2) - df(nv * D // 2)


for nv, D, mv in [(10 ** 6, 200, 20), (10 ** 7, 500, 30), (10 ** 5, 100, 1)]:
    diff = B(nv, D + 2, mv) - B(nv, D, mv)
    lo_, hi_ = nv * mv * (D - 2 * mv - 2) / ((D + 2) * (D - mv)), nv * mv * (2 / (D - mv) - 1 / D + 1 / D ** 2)
    assert lo_ <= diff <= hi_, (nv, D, mv, lo_, diff, hi_)
    print(f"[A4] n={nv} delta={D} m={mv}: {lo_:.1f} <= B(d+2)-B(d) = {diff:.1f} <= {hi_:.1f};  nm/delta = {nv*mv/D:.1f}")

# A5: scales with delta = d^(2/3) L^(1/3), m = (d L)^(1/2)  (L = log n), as powers of (n, d, L)
dd = d ** s.Rational(2, 3) * L ** s.Rational(1, 3)
mm = s.sqrt(d * L)
etan = s.sqrt(6 * L / dd)
checks = {
    'beta^2 = m^2 n/(2 delta)': (mm ** 2 * nn / (2 * dd), nn * d ** s.Rational(1, 3) * L ** s.Rational(2, 3) / 2),
    'm/(eta_n delta)': (mm / (etan * dd), d ** s.Rational(1, 6) * L ** s.Rational(-1, 6) / s.sqrt(6)),
    'eta_n/eps0 (eps0 = C3 (L/d)^(1/3), C3=1)': (etan / (L / d) ** s.Rational(1, 3), s.sqrt(6)),
    'delta^3/n': (dd ** 3 / nn, d ** 2 * L / nn),
    'delta^2/(n m)': (dd ** 2 / (nn * mm), d ** s.Rational(5, 6) * L ** s.Rational(1, 6) / nn),
    'm sqrt(n)/delta (fixed-edge-count heuristic)': (mm * s.sqrt(nn) / dd, s.sqrt(nn) * d ** s.Rational(-1, 6) * L ** s.Rational(1, 6)),
}
for name, (lhs, rhs) in checks.items():
    assert s.simplify(s.powsimp(lhs / rhs, force=True)) == 1, name
    print(f"[A5] {name} = {rhs}")
print("OK")
