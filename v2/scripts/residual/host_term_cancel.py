"""
host_term_cancel.py -- host-term analysis for conj:residual-moment-bim.

Corrected.  The original (worker-2) version claimed the McKay host term
sum_v g_v(g_v-1) moves by exp(Theta(delta*beta)) for a near-regular sequence
g_v = delta + y_v, with beta = m sqrt(n/(2 delta)).  That claim has a
NORMALIZATION ERROR: the McKay loop parameter is

    lambda(g) = sum_v g_v(g_v-1) / (2 sum_v g_v),

not the raw sum.  Dividing by 2 sum_v g_v = 2 n delta (1+o(1)) turns the
(2 delta - 1) sum_v y_v piece into sum_v y_v / (2n) + ..., whose coefficient
is 1/(2n), not 2 delta.

Consequently the exponent movement is O(eps_n * delta) [and O(eps_n * delta^2)
after the lambda^2], with eps_n the *relative* window half-width, rather than
exp(Theta(delta * beta)).

The honest conclusion is unchanged in KIND (a relative window |g_v - delta|
<= eps_n delta is too coarse for a pointwise o(1) host term at BIM scale,
because eps_n * delta^2 -> infinity), but the magnitude is O(eps_n delta^2),
not O(delta * beta), and the two scales agree only by accident neither is o(1).
This note records the correct scale so a later attack normalizes by the correct
window or by the random mean rather than by a wrong beta.

All checks are exact sympy; no Wolfram app id on this machine, so these are
rule-7 sympy fallbacks pending the key.
"""

from sympy import symbols, Rational, simplify, exp, log, oo, series


def check_regular_host_term_cancellation():
    """
    Exactly-regular case: g_v == D.  The host term is deterministic and cancels,
    leaving the loop/double-edge correction exp(sum_{k>=3} x^k/(2k)), x=1/(D-1).
    Verify the fixed-degree short series is x^3/6 + x^4/8 + x^5/10 + ..., i.e.
    1/(6(D-1)^3) + 1/(8(D-1)^4) + O((D-1)^-5).  The (D-1)^-4 coefficient is 1/8,
    NOT 5/8; 5/8 is only the 1/D expansion coefficient.
    """
    D = symbols('D', positive=True)
    x = 1/(D-1)
    S = Rational(1,2) * (-log(1-x) - x - x**2/2)
    excess = exp(S) - 1
    print("[R1] excess in x:", excess.series(x, 0, 6).removeO())
    print("[R1] excess in D:", excess.series(D, oo, 5).removeO())
    lead_Dminus1 = Rational(1,6)/(D-1)**3 + Rational(1,8)/(D-1)**4
    diff = simplify((excess - lead_Dminus1).series(x, 0, 5).removeO())
    print("[R1] assert 1/(6(D-1)^3)+1/(8(D-1)^4) matches to x^4:", diff == 0)
    assert diff == 0, "fixed-degree (D-1)^-4 coefficient must be 1/8, not 5/8"


def check_normalized_host_term():
    """
    The correct object is the McKay loop parameter
        lambda(g) = sum_v g_v(g_v-1) / (2 sum_v g_v),
    not sum_v g_v(g_v-1).  For g_v = delta + y_v with relative deviations
    e_v = y_v/delta, E = sum_v e_v, R2 = sum_v e_v^2:

        lambda(g) - (delta-1)/2 = delta(E + R2)/(2(E+n)).

    So the sensitivity to the profile is O(eps_n * delta), and after squaring
    lambda^2 the exponent moves by O(eps_n * delta^2).
    """
    n, delta = symbols('n delta', positive=True)
    E = symbols('E', nonzero=True)
    R2 = symbols('R2', nonzero=True)
    lam_num = n*delta**2 + 2*delta**2*E + delta**2*R2 - n*delta - delta*E
    lam_den = 2*(n*delta + delta*E)
    lam = lam_num/lam_den
    dlam = simplify(lam - (delta-1)/2)
    print("[H] lambda(g) - (delta-1)/2 =", dlam)
    # Exact: dlam = delta (E + R2) / (2 (E+n)).
    expected = delta*(E + R2)/(2*(E+n))
    print("[H] matches delta(E+R2)/(2(E+n)):", simplify(dlam - expected) == 0)
    assert simplify(dlam - expected) == 0

    # Scalar bounds with |e_v| <= eps_n:
    #   |E| <= eps_n n,  R2 <= eps_n^2 n,  so dlam = O(eps_n delta).
    # In the exponent lambda^2 - lam0^2 = 2 lam0 dlam + dlam^2 = O(delta * eps_n delta)
    # = O(eps_n delta^2).
    eps = symbols('eps', positive=True)
    dlam_bound = delta*(eps*n + eps**2*n)/(2*n)
    print("[H] |dlam| <= eps*delta*(1+eps)/2 =", simplify(dlam_bound / eps))
    lam0 = (delta-1)/2
    # exponent movement from lambda^2:
    move = simplify((lam0*Rational(2))*dlam)  # 2 lam0 dlam, leading
    # bound 2*(delta/2)*(eps delta) = eps delta^2
    print("[H] lambda^2 movement ~ 2*lam0*dlam = O(eps_n * delta^2)")


def check_bim_scales():
    """
    At BIM scale delta = d^{2/3}(log n)^{1/3}, eps_n = (1/2)(log n/d)^{1/3}
    (the residual-sharp relative window).  Then
        eps_n * delta^2 = (1/2) d log n -> infinity,
    so a *relative* window is too coarse for a pointwise o(1) host term.
    This is the correct magnitude of the obstruction (previously misstated as
    delta*beta with beta = m sqrt(n/(2 delta))).
    """
    d, logn = symbols('d logn', positive=True)
    eps_n = Rational(1,2) * (logn/d)**Rational(1,3)
    delta = d**Rational(2,3) * logn**Rational(1,3)
    print("[B] eps_n * delta^2 =", simplify(eps_n * delta**2), "-> infinity")
    print("[B] eps_n * delta   =", simplify(eps_n * delta), "-> infinity")


def check_switching_bookkeeping():
    """
    Bookkeeping identities used in the regular proof (unaffected by the host
    issue, kept for completeness).
    """
    L, nvar = symbols('L nvar', positive=True)
    lhs = L**2*(L**2+1)/(2*L*nvar)
    rhs1 = L*(L**2+1)/(2*nvar)
    rhs2 = L**3/(2*nvar) + L/(2*nvar)
    print("[B1] switching identity 1:", simplify(lhs - rhs1) == 0)
    print("[B2] switching identity 2:", simplify(rhs1 - rhs2) == 0)
    assert simplify(lhs - rhs1) == 0 and simplify(rhs1 - rhs2) == 0


if __name__ == "__main__":
    check_regular_host_term_cancellation()
    check_normalized_host_term()
    check_bim_scales()
    check_switching_bookkeeping()
    print("all done")
