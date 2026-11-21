"""r32: brute-force check of S1 (collision/Bonferroni bounds for Pi_sigma(d)), uniform in D.
Pi(d)=sum over injective phi:[v]->[n] of prod_x (d_phi(x))_{r_x}. Only r matters."""
import itertools, random, math
from math import comb, factorial

def ff(d, r):  # falling factorial (d)_r
    p = 1
    for i in range(r): p *= d - i
    return max(p, 0) if d >= r else 0

def Pi(d, r):
    n = len(d); tot = 0
    for phi in itertools.permutations(range(n), len(r)):
        w = 1
        for x, v in zip(r, phi): w *= ff(d[v], x)
        tot += w
    return tot

def coll(d, a, b): return sum(ff(x, a) * ff(x, b) for x in d)
def S(d, r): return [sum(ff(x, q) for x in d) for q in r]

random.seed(1); worst = {"lo": 1e9, "rem": 0, "lip": 0}; cnt = 0
for _ in range(400):
    D = random.randint(3, 7); n = random.randint(7, 11); v = random.randint(2, 4)
    r = [random.randint(1, D) for _ in range(v)]
    dd = [D] * n
    for _ in range(random.randint(0, 3)):
        dd[random.randrange(n)] -= random.randint(0, 2)
    dd = [max(x, 0) for x in dd]; Bp = sum(D - x for x in dd)
    lead = math.prod(ff(D, q) for q in r)
    P = Pi(dd, r); Sv = S(dd, r)
    assert Pi([D] * n, r) == math.prod(range(n, n - v, -1)) * lead  # exact for regular
    assert P <= n**v * lead                                         # (a)
    assert P >= (n - Bp)**v * lead - comb(v, 2) * n**(v - 1) * lead  # (b)
    S0 = math.prod(Sv)
    S1 = sum(coll(dd, r[x], r[y]) * math.prod(Sv[z] for z in range(v) if z not in (x, y))
             for x, y in itertools.combinations(range(v), 2))
    assert S0 - S1 <= P <= S0 - S1 + comb(comb(v, 2), 2) * n**(v - 2) * lead  # (c) Bonferroni
    rem = (P - (S0 - S1)) / (n**(v - 2) * lead)
    worst["rem"] = max(worst["rem"], rem / max(v**4 / 8, 1e-9))
    # falling-factorial product identity
    for x in range(0, D + 1):
        a, b = r[0], r[1]
        assert ff(x, a) * ff(x, b) == sum(comb(a, j) * comb(b, j) * factorial(j) * ff(x, a + b - j) for j in range(min(a, b) + 1))
    # (d) Lipschitz: regular vs deficient d, relative change <= v*B'/n*(1+v^2/2n)+v^4/8n^2
    rel = abs(Pi([D] * n, r) - P) / (n**v * lead)
    bound = v * Bp / n * (1 + v**2 / (2 * n)) + v * v / (2 * n) * 0 + v**4 / (8 * n**2) + v * v / (2 * n)  # see note: includes (n)_v vs n^v
    worst["lip"] = max(worst["lip"], rel / bound)
    cnt += 1
print("cases", cnt, "all asserts passed; max rem/(v^4/8 bound)=%.3f, max lip ratio=%.3f" % (worst["rem"], worst["lip"]))
assert worst["rem"] <= 1 and worst["lip"] <= 1

# (e) sum_l l^4 x^l/l! = e^x (x^4+6x^3+7x^2+x) (Touchard) <= 1.1 x^4 e^x for x>=162 (x=2D^4, D>=3)
for D in range(3, 12):
    x = 2.0 * D**4
    assert x**4 + 6 * x**3 + 7 * x**2 + x <= 1.1 * x**4, D
print("moment bound ok")
