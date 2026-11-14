"""
avoid_g_host2.py -- exact first- AND second-order host dependence of the m-factor
second-moment ratio for a near-regular host g = delta + y with a d-regular hole G.

From the paper's McKay estimate, exponent of the four-pairing second moment carries
   -lambda(g) - lambda(g)^2 - mu(g,X)
for g in the four classes.  For the regular case these collapse.  For near-regular,
lambda(g) = T_g/(2 S_g) with S_g = n delta + e, T_g = n delta(delta-1) + (2delta-1)e + s2.

We compute, to SECOND order in the window parameters (e, s2), the ratio
   Phi = (E1+E2+E3+E4) - 2*E0
and ask whether its (e, s2)-dependent part is o(1) at BIM scale.  The paper's regular
identity says Phi = -x/2 - x^2/4 + O(D^3/n) when e=s2=0.  The new question is the
e-, s2- derivative and curvature of Phi.

Key scales (BIM, McKay constraint delta^3 = d^2 logn = o(n)):
   e ~ sigma_e = sqrt(n delta/2)        (edge-count SD)
   s2 ~ sqrt(n) m ...  (degree-spread SD, see step3 note: m sqrt n /(sqrt2 delta))
Linear movement:    m * sigma_e / n  = m sqrt(delta/(2n)) -> 0.
Quadratic movement: (2delta) * sigma_e / S_g  ~ 2 delta * beta /(n delta) = 2 beta / n
                     = 2 m sqrt(n/(2delta))/n = m sqrt(2/(n delta)).
Wait: lambda = T/(2S).  d lambda/de = (2delta-1)/(2 S) - T/(2 S^2) ~ (2delta)/(2 n delta) - ...
Actually compute exactly.
"""

from sympy import symbols, Rational, simplify, expand, series, diff, sqrt, oo

delta, m, n, d = symbols('delta m n d', positive=True)
e, s2 = symbols('e s2', real=True)
r = delta - m   # constant degree after one m-factor removed

def T_of(coef, e, s2):
    return n*coef*(coef-1) + (2*coef-1)*e + s2

def S_of(coef, e):
    return n*coef + e

def lam(coef, e, s2):
    return T_of(coef, e, s2)/(2*S_of(coef, e))

# First-moment host exponent (single factor, host g=delta+y, factor removes m):
#   Phi_1 = -lam(delta) - lam(delta)^2 - [ -lam(r) - lam(r)^2 ]
# (mu terms: G contributes d delta n /(2 S) type terms; we handle separately below)
lD = lam(delta, e, s2)
lR = lam(r, e, s2)
Phi1 = (-lD - lD**2) - (-lR - lR**2)

# derivatives at e=s2=0
Phi1_e1 = simplify(Phi1.diff(e).subs({e:0, s2:0}))
Phi1_e2 = simplify(Phi1.diff(e,2).subs({e:0, s2:0}))
Phi1_s1 = simplify(Phi1.diff(s2).subs({e:0, s2:0}))
Phi1_s2 = simplify(Phi1.diff(s2,2).subs({e:0, s2:0}))

print("=== FIRST MOMENT host dependence (Phi1 = -lam(delta)-lam^2 minus -lam(r)-lam^2) ===")
print("dPhi1/de            =", Phi1_e1)
print("d^2Phi1/de^2        =", Phi1_e2)
print("dPhi1/ds2           =", Phi1_s1)
print("d^2Phi1/ds2^2       =", Phi1_s2)

# Curvature in e:  (1/2) Phi1_e2 * e^2 with e ~ sigma_e = sqrt(n delta /2)
sigma_e = sqrt(n*delta/2)
curv_e = Rational(1,2)*Phi1_e2*sigma_e**2
print()
print("curvature-in-e contribution to Phi1 (e ~ sqrt(n delta/2)) =", simplify(curv_e))

# The linear term: Phi1_e1 * sigma_e
lin_e = Phi1_e1*sigma_e
print("linear-in-e contribution =", simplify(lin_e))
