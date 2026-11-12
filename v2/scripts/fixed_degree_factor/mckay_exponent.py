"""Lemma mckay-exponent: the four sequential McKay exponents for a pair of
L-factors, evaluated at the typical overlap (a_v iid hypergeometric(D; L, L),
pairing sums at their means), minus P(simple) and twice the single-factor
exponent, equal -x/2 - x^2/4 with x = 1/(D-1), for every L. Also checks the
single-factor constant -(D^2-2)/4 and the L=1 case against Gao21 eq. (8).
Run: python mckay_exponent.py   (exits nonzero on failure)
"""
import sympy as s

L, D, b = s.symbols('L D beta', positive=True)


def exponent_identity(L, D, Ea, Ea2):
    def E(c):  # E[c0 + c1 a + c2 a^2]
        return c[0] + c[1] * Ea + c[2] * Ea2
    q = Ea
    g0 = D - 2 * L
    lamB = E((0, -1, 1)) / (2 * q)
    E1 = -lamB - lamB ** 2
    lam1 = E((L * (L - 1), -(2 * L - 1), 1)) / (2 * (L - q))
    mu1 = E((0, L, -1)) ** 2 / (2 * q * (L - q))
    mu2 = mu1 + E((L * L, -2 * L, 1)) ** 2 / (2 * (L - q) ** 2)
    E2 = -lam1 - lam1 ** 2 - mu1
    E3 = -lam1 - lam1 ** 2 - mu2
    lamg = E((g0 * (g0 - 1), 2 * g0 - 1, 1)) / (2 * (g0 + q))
    Eag = E((0, g0, 1))
    Emag = E((L * g0, L - g0, -1))
    mug = (Eag ** 2 / (2 * q) + Emag ** 2 / (L - q)) / (g0 + q)
    E4 = -lamg - lamg ** 2 - mug
    return E1, E2, E3, E4


# hypergeometric moments
Ea = L ** 2 / D
Ea2 = L ** 2 * (L - 1) ** 2 / (D * (D - 1)) + Ea
E1, E2, E3, E4 = exponent_identity(L, D, Ea, Ea2)
c1 = ((D - L) ** 2 - 1) / 4 + L * (D - L) / 2
E0 = -(L ** 2 - 1) / 4 - c1
x = 1 / (D - 1)
total = s.simplify(E1 + E2 + E3 + E4 - (D ** 2 - 1) / 4 - 2 * E0 - (-x / 2 - x ** 2 / 4))
single = s.simplify(E0 + (D ** 2 - 2) / 4)
# L = 1, a in {0,1} with mean beta: compare E4 + (D^2-1)/4 with Gao21 eq. (8)
_, _, E3b, E4b = exponent_identity(1, D, b, b)
phi = (4 * (D - 2) ** 2 - (D ** 2 - 5) * b ** 2 - (2 * D ** 2 - 14 * D + 20) * b) / (4 * (D - 2 + b) ** 2)
gao = s.simplify(E4b + (D ** 2 - 1) / 4 - phi)
print("total exponent - (-x/2 - x^2/4) =", total)
print("single exponent + (D^2-2)/4     =", single)
print("L=1: E4 + (D^2-1)/4 - phi(D,beta) =", gao, "; E3 =", s.simplify(E3b))
assert total == 0 and single == 0 and gao == 0 and s.simplify(E3b + s.Rational(1, 2)) == 0
print("OK")
