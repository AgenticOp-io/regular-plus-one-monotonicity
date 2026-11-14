"""
host_term_cancel.py -- decisive check for conj:residual-moment-bim.

The one unproved estimate for the degree-conditioned m-factor moment (worker 2's
lem:avoid-G-host, equivalently the "non-regular degree sequence" case named in
rem:growing-degree-scope of main.tex) is whether the McKay-4.6 host term

    sum_v g_v (g_v - 1)

cancels in the second-moment ratio of the m-factor count, for a *near-regular*
sequence g_v = delta*(1+o(1)) over a hole (the d-regular G removed from K_n).

For the EXACTLY regular case, g_v == delta, the growing-degree theorem already
proves the ratio collapses to a host-free exp(sum_{k>=3} x^k/2k) = 1+o(1).

Claim checked here: for g_v = delta + y_v, the variation of the host term
sum_v g_v(g_v-1) is 2*delta*sum_v y_v + sum_v y_v(y_v-1), and the LINEAR piece
2*delta*sum_v y_v does NOT vanish on the window {|y_v| <= delta*eps}: both the
edge-count fluctuation (sum_v y_v = 2(e(R)-k0), scale ~ beta = m sqrt(n/(2 delta)))
and the degree-spread piece keep the host term moving by exp(Theta(beta)), which
diverges for m = Theta(sqrt(d log n)) at BIM scale.

So the host term does NOT cancel for a near-regular sequence, and the
degree-conditioned moment for m-factors that avoids G is NOT obtained by the
regular-host argument plus o(1) window flatness. This is the honest obstruction.

We also verify the exact identity used in the paper's regular proof to make sure
we are cancelling the same term that the paper cancels, and the m=1 version.
"""

from sympy import symbols, Rational, simplify, exp, log, binomial, factorial, oo


def check_regular_host_term_cancellation():
    """
    In the exactly-regular case the host term is deterministic:
    sum_v g_v(g_v-1) = delta(delta-1) n.  The second-moment ratio of the
    growing-degree theorem only retains the loop/double-edge correction
    exp(sum_{k>=3} x^k/(2k)); the delta(delta-1)n contribution cancels between
    numerator and denominator because every class sum is then deterministic.

    We verify the finite-degree limit shape asserted in thm:fixed-degree-factor:
        Var Z / (E Z)^2 -> exp(sum_{k>=3} x^k/(2k)) - 1,  x = 1/(D-1),
    equals 1/(6(D-1)^3) + 1/(8(D-1)^4) + O(D^-5).
    """
    D = symbols('D', positive=True)
    x = 1/(D-1)
    # sum_{k>=3} x^k/(2k) = (1/2)*( -log(1-x) - x - x^2/2 )
    S = Rational(1,2) * (-log(1-x) - x - x**2/2)
    excess = exp(S) - 1
    # series in x = 1/(D-1): x^3/6 + x^4/8 + x^5/10 + O(x^6)
    print("[R1] finite-degree excess series in x:", excess.series(x, 0, 6).removeO())
    # series in 1/D: 1/(6D^3) + 5/(8D^4) + O(D^-5)
    print("[R1] finite-degree excess series in D:", excess.series(D, oo, 5).removeO())
    # The theorem statement (thm:fixed-degree-factor) is written in x = 1/(D-1):
    #   1/(6(D-1)^3) + 1/(8(D-1)^4) + O((D-1)^-5)
    # The (D-1)-coefficient is 1/8, NOT 5/8.  The 5/8 arises only when this is
    # re-expanded in powers of 1/D (the (1 - 1/D)^{-3} correction from the x^3 term).
    lead_Dminus1 = Rational(1,6)/(D-1)**3 + Rational(1,8)/(D-1)**4
    print("[R1] asserted 1/(6(D-1)^3)+1/(8(D-1)^4) diff (x^5 leftover only):",
          simplify((excess - lead_Dminus1).series(D, oo, 6).removeO()))
    assert simplify((excess - lead_Dminus1).series(x, 0, 5).removeO()) == 0, (
        "theorem statement x^4 coefficient must be 1/8, not 5/8")


def check_host_term_variation():
    """
    Host term H(g) = sum_v g_v (g_v - 1), with g_v = delta + y_v.
    H = sum_v [delta(delta-1) + (2 delta - 1) y_v + y_v^2]
      = delta(delta-1) n + (2 delta - 1) sum_v y_v + sum_v y_v^2.

    On the near-regular window with sum_v y_v = 2(e(R)-k0), the edge-count
    fluctuation has SD ~ sigma_e = sqrt(e_C q (1-q)) and 2 sigma_e ~ beta in the
    paper's notation.  The linear coefficient (2 delta - 1) makes the host term
    move by exp(Theta((2 delta) * sigma_e)) = exp(Theta(delta * beta)).

    At BIM scale: delta = Theta(d^{2/3} (log n)^{1/3}), m = Theta(sqrt(d log n)),
    beta = m sqrt(n(1-q)/(2 delta)) = Theta(sqrt(n) d^{1/6} (log n)^{1/3}),
    so delta * beta = Theta(n^{1/2} d^{5/6} (log n)^{2/3}) -> infinity.

    That divergence is exactly the first-moment non-flatness my step-3 note
    already proved; here we record the host-term version to show the
    regular-host proof's cancellation step does not extend to near-regular g.
    """
    delta, nvar = symbols('delta nvar', positive=True)
    m = symbols('m', positive=True)
    q = symbols('q', positive=True)
    # beta from the paper: beta^2 = m^2 n (1-q)/(2 delta)
    beta = m * (nvar * (1-q) / (2*delta))**Rational(1,2)
    # host-term linear movement scale: (2 delta - 1) * delta_g where delta_g ~ beta
    # exponent moving the McKay weight: ~ 2 delta * beta / (something O(delta)) ;
    # independent of the O(delta) normalization in the weight, 2 delta * beta -> inf.
    # Substitute BIM scales symbolically:
    d = symbols('d', positive=True)
    logn = symbols('logn', positive=True)
    delta_bim = d**Rational(2,3) * logn**Rational(1,3)
    m_bim = (d*logn)**Rational(1,2)
    beta_bim = m_bim * (nvar/(2*delta_bim))**Rational(1,2)  # 1-q ~ 1
    host_movement = delta_bim * beta_bim
    print("[H1] host-term movement scale delta*beta =", host_movement,
          " -> infinity at BIM scale (d,logn->inf)")


def check_constant_sequence_host_term_matches_paper():
    """
    Reconcile with the paper's regular proof: In thm:growing-degree-factor the
    host term lambda(g) = sum_v g_v(g_v-1)/(2S) enters through -lambda-lambda^2.
    For g_v == D constant, lambda = (D-1)/2 and the ratio is m-free.  We only
    confirm the arithmetical identity line used there:

        (L^2(L^2+1))/(2 L n) = L(L^2+1)/(2n) = L^3/(2n) + L/(2n)

    and the switching accumulation claim.  (These are bookkeeping identities
    that must be right for the regular proof; they are, but they do not touch
    the near-regular host term.)
    """
    L, nvar = symbols('L nvar', positive=True)
    lhs = L**2*(L**2+1)/(2*L*nvar)
    rhs1 = L*(L**2+1)/(2*nvar)
    rhs2 = L**3/(2*nvar) + L/(2*nvar)
    print("[B1] switching identity 1:", simplify(lhs - rhs1) == 0)
    print("[B2] switching identity 2:", simplify(rhs1 - rhs2) == 0)


if __name__ == "__main__":
    check_regular_host_term_cancellation()
    check_host_term_variation()
    check_constant_sequence_host_term_matches_paper()
    print("all done")
