# r25: symbolic check of the first-order constant of E[#k-cycles] in random D-regular graphs.
# E C_k = (D-1)^k/(2k) * (1 + f1(k)/n + O(n^-2)), derived in v2/notes/r25_lemma_L1.md.
import sympy as sp

n, D, e = sp.symbols('n D epsilon', positive=True)
s1, s2 = sp.symbols('s1 s2', positive=True)

# G0(s) = -lam1 - lam2 in normalized moments s_r = (1/n) sum_v (d_v)_r
G0 = -s2 / (2 * s1) - s2**2 / (4 * s1**2)
reg = {s1: D, s2: D * (D - 1)}
assert sp.simplify(G0.subs(reg) + (D - 1) / 2 + (D - 1)**2 / 4) == 0


def f1(k):
    # exact prefactor n^(k)/(2k) (D(D-1))^k / prod_{j<k}(nD-2j-1), divided by its limit (D-1)^k/(2k);
    # its 1/n coefficient is the sum of the per-factor ones (each factor is 1 + c/n + O(n^-2))
    factors = [1 - i * e for i in range(k)] + [1 / (1 - (2 * j + 1) * e / D) for j in range(k)]
    pref1 = sum(sp.diff(f, e).subs(e, 0) for f in factors)
    # local change: k vertices lose 2 points each
    d1 = -2 * k
    d2 = k * ((D - 2) * (D - 3) - D * (D - 1))
    dG0 = (sp.diff(G0, s1) * d1 + sp.diff(G0, s2) * d2).subs(reg)  # coefficient of 1/n
    EZ = k * (D - 2)**2 / D  # n * E[#rest pairs parallel to a cycle edge]
    return sp.simplify(pref1 + dG0 - EZ)


f4, f3 = f1(4), f1(3)
k = sp.Symbol('k')
general = -k * (k - 1) / 2 + 2 * k + (k**2 - 4 * k) / D
for kk in range(3, 9):
    assert sp.simplify(f1(kk) - general.subs(k, kk)) == 0
assert sp.simplify(f4 - 2) == 0
assert sp.simplify(f3 - (3 - 3 / D)) == 0
# r24a exact-DP Richardson values
for DD, f_num, e_num in [(3, 2.000007, 1.99973), (4, 2.00010, 2.25017), (5, 2.0021, 2.4042)]:
    assert abs(float(f4.subs(D, DD)) - f_num) < 5e-3 and abs(float(f3.subs(D, DD)) - e_num) < 5e-3
print('f1(4) =', f4, '  e1 = f1(3) =', f3, '  f1(k) =', sp.simplify(general))
print('OK')
