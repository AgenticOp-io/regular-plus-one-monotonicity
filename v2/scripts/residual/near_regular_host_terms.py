"""Step 1 (near-regular host), McKay host terms.

Degrees d_v = D(1 + eps*beta_v), vertex averages <beta>=0, <beta^2>=s2,
<beta^3>=s3, <beta^4>=s4.  Overlap a_v | d_v ~ hypergeometric(d_v; m, m).
Evaluates, with every class sum replaced by its vertex average of the
conditional moments and every pairing sum by its replaced mean (as in
Lemma mckay-exponent of main.tex):

  total = E1+E2+E3+E4 - (lam_d + lam_d^2) - 2*E0

and expands in eps.  Checks:
  (H0) eps^0 term = -x/2 - x^2/4, x = 1/(D-1)  (regular identity)
  (H1) eps^1 term = 0
  (H2) eps^2 term: the host terms sum_v d_v(d_v-1) cancel at order
       D^2 s2 = tau^2 and the remainder is printed exactly.
Run: python near_regular_host_terms.py   (exits nonzero on failure)
"""
import sympy as s

D, m, eps = s.symbols('D m epsilon', positive=True)
s2, s3, s4 = s.symbols('s2 s3 s4')
ORDER = 4
bmom = {0: 1, 1: 0, 2: s2, 3: s3, 4: s4}


def avg(f):
    """<f(d_v)> for f a function of d = D(1+eps*beta), to O(eps^ORDER)."""
    beta = s.Symbol('beta')
    ser = s.series(f(D * (1 + eps * beta)), eps, 0, ORDER + 1).removeO()
    ser = s.expand(ser)
    return sum(_bavg(ser.coeff(eps, k), beta) * eps ** k for k in range(ORDER + 1))


def _bavg(poly, beta):
    p = s.Poly(s.expand(poly), beta)
    return sum(c * bmom[mon[0]] for mon, c in zip(p.monoms(), p.coeffs()))


Ea_d = lambda d: m ** 2 / d
Ea2_d = lambda d: m ** 2 / d + m ** 2 * (m - 1) ** 2 / (d * (d - 1))

q = avg(Ea_d)
Ea2 = avg(Ea2_d)
Ead = avg(lambda d: d * Ea_d(d))          # <d a>
Edd = avg(lambda d: d * d)                 # <d^2>  (<d> = D exactly)


def E(c0, c1, c2):  # <c0 + c1 a + c2 a^2>, c_i constants
    return c0 + c1 * q + c2 * Ea2


lamB = E(0, -1, 1) / (2 * q)
E1 = -lamB - lamB ** 2
lam1 = E(m * (m - 1), -(2 * m - 1), 1) / (2 * (m - q))
mu1 = E(0, m, -1) ** 2 / (2 * q * (m - q))
mu2 = mu1 + E(m * m, -2 * m, 1) ** 2 / (2 * (m - q) ** 2)
E2 = -lam1 - lam1 ** 2 - mu1
E3 = -lam1 - lam1 ** 2 - mu2
# R: g_v = d_v - 2m + a_v
Eg = D - 2 * m + q
Egg1 = Edd - 4 * m * D + 4 * m * m + 2 * Ead - 4 * m * q + Ea2 - Eg   # <g(g-1)>
lamg = Egg1 / (2 * Eg)
Eag = Ead - 2 * m * q + Ea2                                            # <a g>
Emag = m * Eg - Eag                                                    # <(m-a) g>
mug = (Eag ** 2 / (2 * q) + Emag ** 2 / (m - q)) / Eg
E4 = -lamg - lamg ** 2 - mug
# whole graph and single factor
lamd = (Edd - D) / (2 * D)
lamF = (m - 1) / 2
lamR1 = (Edd - 2 * m * D + m * m - (D - m)) / (2 * (D - m))
muF = m * (D - m) / 2
E0 = -lamF - lamF ** 2 - lamR1 - lamR1 ** 2 - muF

total = E1 + E2 + E3 + E4 - (lamd + lamd ** 2) - 2 * E0
ser = s.series(total, eps, 0, 3).removeO()
c = [s.factor(s.simplify(ser.coeff(eps, k))) for k in range(3)]
x = 1 / (D - 1)
ok0 = s.simplify(c[0] - (-x / 2 - x ** 2 / 4)) == 0
ok1 = c[1] == 0
print("eps^0:", c[0], " == -x/2-x^2/4 :", ok0)
print("eps^1:", c[1])
print("eps^2 coefficient (multiply by eps^2; tau^2 = D^2 eps^2 s2):")
print("   ", c[2])
c2_over_tau2 = s.factor(s.simplify(c[2] / (D ** 2 * s2)))
print("eps^2 / tau^2 =", c2_over_tau2)
print("  leading in 1/D at m fixed:", s.limit(c2_over_tau2 * D, D, s.oo), "/ D")
# host terms individually are O(tau^2): show the lamd^2 piece
print("lam_d^2 eps^2 coeff / tau^2 =",
      s.simplify(s.series(lamd + lamd ** 2, eps, 0, 3).removeO().coeff(eps, 2) / (D ** 2 * s2)))
h2 = (2 * D ** 2 * (m - 1) + D - m) / (2 * (D - m) * (D - 1) ** 4)   # coefficient of tau^2
ok2 = s.simplify(c2_over_tau2 - h2) == 0
print("(H2) eps^2 term = tau^2 (2D^2(m-1)+D-m)/(2(D-m)(D-1)^4):", ok2)
assert ok0 and ok1 and ok2
# (H3) orders eps^3, eps^4 in central moments kappa_k = <(d-D)^k> = D^k eps^k <beta^k>:
#   eps^3 term = kappa3 * h3,  eps^4 term = kappa4 * h4 + tau^4 * h22.
ser4 = s.series(total, eps, 0, ORDER + 1).removeO()
c3 = s.Poly(s.expand(s.simplify(ser4.coeff(eps, 3))), s2, s3, s4).as_dict()
c4 = s.Poly(s.expand(s.simplify(ser4.coeff(eps, 4))), s2, s3, s4).as_dict()
assert set(c3) <= {(0, 1, 0)} and set(c4) <= {(0, 0, 1), (2, 0, 0)}, (c3.keys(), c4.keys())
h3 = s.factor(s.simplify(c3.get((0, 1, 0), 0) / D ** 3))
h4 = s.factor(s.simplify(c4.get((0, 0, 1), 0) / D ** 4))
h22 = s.factor(s.simplify(c4.get((2, 0, 0), 0) / D ** 4))
print("(H3) h3  =", h3)
print("     h4  =", h4)
print("     h22 =", h22)
# bounds quoted in the tex for D >= 8, 1 <= m <= 0.45 D (ratios bounded on a grid):
#   |h3| <= K m (1 + m/D) / D^4,  |h4| <= K m^2 / D^5 (+ K/D^5 when m small),  |h22| <= K m^2 / D^4
worst = {}
for Dv in (8, 16, 64, 256, 1024, 4096, 2 ** 16):
    for mv in sorted({1, 2, 3, Dv // 8, Dv // 4, int(0.45 * Dv)}):
        if mv < 1:
            continue
        sub = {D: Dv, m: mv}
        for name, val, scale in [("h3", h3, mv * (1 + mv / Dv) / Dv ** 4),
                                 ("h4", h4, (mv ** 2 + 4) / Dv ** 5),
                                 ("h22", h22, (mv ** 2 + 1) / Dv ** 4)]:
            worst[name] = max(worst.get(name, 0), abs(float(val.subs(sub))) / scale)
print("(H3) max |h|/scale on grid:", {k: round(v, 3) for k, v in worst.items()})
assert all(v < 50 for v in worst.values())
print("OK")
