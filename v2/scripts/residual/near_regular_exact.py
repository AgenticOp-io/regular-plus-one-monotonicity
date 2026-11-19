"""Step 1 (near-regular host): pairing-level identities used in
v2/paper/residual/step1-near-regular.tex.

(P1) 1/d - 1/D = -(d-D)/D^2 + (d-D)^2/(d D^2); hence, as <d> = D,
     dq := <m^2/d> - m^2/D = m^2 <(d-D)^2/(d D^2)>  (>= 0).
(P2) psi''(alpha0) sigma^2(D) = D/(2(D-1)) for real D (as in Lemma factor-rate),
     alpha0 = m^2/D, sigma^2(D) = m^2 (D-m)^2/(D^2 (D-1)).
(P3) Xi := n psi'' dq^2 / (2 (1 - psi'' sigma^2)) at dq = m^2 T / D^3 equals
     n m^2 T^2 (D-1) / (2 D^3 (D-m)^2 (D-2)).
(P4) Gaussian sum: sum_A N(A; n q, n s^2) * exp(c (A - n a0)^2 / n), c = psi''/2,
     equals (1 - 2 c s^2)^{-1/2} exp(c n dq^2 / (1 - 2 c s^2))  (completing the square).
(P5) G(x) >= c1 KL(p+x || p) on the support, p = m/D <= 0.45: min ratio on a grid.
     (G as in Lemma factor-rate.)  Also G''(0)/KL''(0) = (1-2p)/(1-p).
Run: python near_regular_exact.py   (exits nonzero on failure)
"""
import math

import sympy as s

D, m, T, n, d, A, c, s2, a0, dq = s.symbols('D m T n d A c s2 a0 dq', positive=True)

# (P1)
P1 = s.simplify(1 / d - 1 / D - (-(d - D) / D ** 2 + (d - D) ** 2 / (d * D ** 2))) == 0
print("(P1)", P1)
# (P2)
alpha0 = m ** 2 / D
psi2 = 1 / (2 * alpha0) + 1 / (m - alpha0) + 1 / (2 * (D - 2 * m + alpha0))
sig2 = m ** 2 * (D - m) ** 2 / (D ** 2 * (D - 1))
P2 = s.simplify(psi2 * sig2 - D / (2 * (D - 1))) == 0
print("(P2)", P2)
# (P3)
Xi = n * psi2 * (m ** 2 * T / D ** 3) ** 2 / (2 * (1 - D / (2 * (D - 1))))
P3 = s.simplify(Xi - n * m ** 2 * T ** 2 * (D - 1) / (2 * D ** 3 * (D - m) ** 2 * (D - 2))) == 0
print("(P3)", P3)
# (P4) Gaussian integral identity, variable u = A - n a0, mean n dq, variance n s2
u = s.symbols('u', real=True)
dens = s.exp(-(u - n * dq) ** 2 / (2 * n * s2)) / s.sqrt(2 * s.pi * n * s2)
num = {c: s.Rational(1, 7), s2: 2, n: 5, dq: s.Rational(3, 10)}  # 2 c s2 < 1
f = s.lambdify(u, (dens * s.exp(c * u ** 2 / n)).subs(num), 'mpmath')
import mpmath
val = mpmath.quad(f, [-mpmath.inf, 0, mpmath.inf])
target = (1 - 2 * c * s2) ** s.Rational(-1, 2) * s.exp(c * n * dq ** 2 / (1 - 2 * c * s2))
P4 = abs(val - float(target.subs(num))) < 1e-10
print("(P4)", P4)


# (P5)
def KL(a, b):
    t = 0.0
    if a > 0:
        t += a * math.log(a / b)
    if a < 1:
        t += (1 - a) * math.log((1 - a) / (1 - b))
    return t


worst = 1.0
for p in [k / 1000 for k in range(1, 451)]:
    r = p / (1 - p)
    for j in range(1, 400):
        for x in (-p * j / 400, (1 - p) * j / 400):
            y1, y2 = p + x, p - r * x
            if not (0 <= y1 <= 1 and 0 <= y2 <= 1):
                continue
            k1 = KL(y1, p)
            if k1 < 1e-14:
                continue
            G = k1 - KL(y2, p) / r
            worst = min(worst, G / k1)
print("(P5) min G/KL over p in (0,0.45], grid:", round(worst, 4))
pp, xx = s.symbols('p x', positive=True)
KLs = lambda a, b: a * s.log(a / b) + (1 - a) * s.log((1 - a) / (1 - b))
Gs = KLs(pp + xx, pp) - (1 - pp) / pp * KLs(pp - pp / (1 - pp) * xx, pp)
P5b = s.simplify(s.diff(Gs, xx, 2).subs(xx, 0) / s.diff(KLs(pp + xx, pp), xx, 2).subs(xx, 0)
                 - (1 - 2 * pp) / (1 - pp)) == 0
print("(P5) G''(0)/KL''(0) = (1-2p)/(1-p):", P5b)
assert P1 and P2 and P3 and P4 and P5b and worst > 0.05
print("OK")
