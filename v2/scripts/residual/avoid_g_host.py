"""
avoid_g_host.py -- exact first-moment host dependence for the near-regular residual
(worker-2 lem:avoid-G-host).

Setup.  C = K_n \\ G with G d-regular; H ~ Unif(Omega(C, g)) where the residual
degree sequence is g_v = delta + y_v (near-regular).  We track the EXACT dependence
of the first moment E[Z | g] on the profile coordinates

    e  = sum_v y_v,      s2 = sum_v y_v^2,

without collapsing them to 0.  The McKay loop parameter (correctly normalised) is

    lambda(g) = sum_v g_v(g_v-1)/(2 sum_v g_v)
              = (n delta(delta-1) + (2 delta-1) e + s2) / (2 (n delta + e)).

We compute the first-moment exponent at degree profile g = delta+y (host) versus
g-m = r+y with r = delta-m (host minus one m-factor), and read off the e,s2
dependence.  The mu (forbidden G) term is the same G in both and contributes a
profile dependence only through the F-edges to first order; the leading question is
the lambda dependence.

Result (exact, sympy):

    dPhi1/de  = (r - delta)/(2n) = -m/(2n),
    dPhi1/ds2 = 0.

That is, relative to the loop parameter lambda(g), the degree-spread direction
s2 = sum_y y_v^2 cancels exactly, and the edge-count direction e = sum_v y_v enters
only with the small coefficient -m/(2n).  This is the correct magnitude of the
*loop-parameter* host dependence.  The actual non-flatness of the first moment is
driven by the configuration prefactor (see residual-bim-host-obstruction.md), which is
not part of the loop parameter; this file isolates the loop contribution to confirm it
is not the obstruction.

For the DEGREE-CONDITIONED residual, g is fixed, so e and s2 are fixed numbers, and
the relevant question is how E[Z|g] varies as g ranges over the window.  The loop
parameter lambda(g) contributes only -m e/(2n) to the first-moment exponent (this file's
assertion), which is o(1) pointwise.  The DOMINANT dependence is the configuration
prefactor (2M-1)!!/prod_v g_v!, whose leading effect for two constant sequences
delta and delta+2 is n log(n/delta) -> infinity (see residual-bim-host-obstruction.md and
residual_window_means.py for the exact verified rate).  The loop parameter is NOT the
obstruction; the prefactor n log(n/delta) is.

The fixed exact-degree statements (thm:residual-matching-constrained, m=1) are
unaffected: there e = s2 = 0 and the prefactor is deterministic.
"""

from sympy import symbols, Rational, simplify

delta, m, n, d = symbols('delta m n d', positive=True)
e, s2 = symbols('e s2', real=True)
r = delta - m


def Lam(coef):
    """lambda for a constant-degree-coef + y profile: coef in {delta, r}."""
    S = n*coef + e
    T = n*coef*(coef-1) + (2*coef-1)*e + s2
    return T/(2*S)


lam_delta = Lam(delta)
lam_r = Lam(r)

# first-moment host exponent: -lambda - lambda^2 at delta versus r
Phi1 = (-lam_delta - lam_delta**2) - (-lam_r - lam_r**2)

print("lambda(delta+y) =", simplify(lam_delta))
print("dPhi1/de  =", simplify(Phi1.diff(e).subs({e: 0, s2: 0})))
print("dPhi1/ds2 =", simplify(Phi1.diff(s2).subs({e: 0, s2: 0})))

assert simplify(Phi1.diff(e).subs({e: 0, s2: 0})) == (r - delta)/(2*n) == -m/(2*n)
assert simplify(Phi1.diff(s2).subs({e: 0, s2: 0})) == 0

print("NOTE: the loop parameter lambda(g) contributes only -m/(2n) per unit e (o(1)).")
print("The DOMINANT non-flatness is the configuration prefactor (2M-1)!!/prod_v g_v!;")
print("see residual-bim-host-obstruction.md and residual_window_means.py: its leading")
print("effect for constant sequences delta -> delta+2 is n log(n/delta) -> infinity.")

# BIM scale check of the (relative-window) exponent shift
logn = symbols('logn', positive=True)
eps_n = Rational(1,2) * (logn/d)**Rational(1,3)
delta_bim = d**Rational(2,3) * logn**Rational(1,3)
m_bim = (d*logn)**Rational(1,2)
shift = m_bim * eps_n * delta_bim / 2
print("BIM first-moment exponent shift (relative window):", simplify(shift))

print("OK")
