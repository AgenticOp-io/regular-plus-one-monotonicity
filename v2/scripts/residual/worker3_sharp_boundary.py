"""
worker3_sharp_boundary.py -- is delta = o(n^{1/6}) a real barrier for the
1/(6 delta^3) m-factor rate?  Checks for v2/notes/worker3_sharp_boundary.txt.

Replaces the stale version (which only tabulated hypothetical error sizes).

Literature formulas under test (transcribed; see the note for sources):
  MW91  (McKay-Wormald 1991, as quoted in Liebenau's lecture notes Thm 3.6):
        P(pairing with degrees d simple)
          = exp(-M2/(2M) - M2^2/(4M^2) - M2^2 M3/(2M^4) + M2^4/(4M^5)
                + M3^2/(6M^3) + O(Delta^3/M)),   M_k = sum [d_i]_k.
  G20-6 (Gao, arXiv:2012.01492, Thm 6) with H1 empty:
        P(uv in G(d) | H2 absent) = (d_u d_v/M)
            (1 - M2^2/M^3 - M2/M^2 - sum_{(x,y) in W} d_x d_y/M^2)
            (1 - phibar/M) (1 + O(Delta^5 n/M^3)),
        phibar = -2(d_u+d_v) + 2 - sum_{x~u in H2} d_x - sum_{y~v in H2} d_y
                 - (d_u+d_v-2) M2/M + d_u d_v.

Sections:
  A  sympy: cubic MW91 terms cancel in the four-class ratio (leading orders).
  B  exact regular-graph counts (DP) against MW91.
  C  G20-6 against exact d=1 (perfect-matching) arithmetic: edge probability
     given a forbidden matching, and P(avoid a perfect matching).
  D  exact barrier exponents: which error resolves 1/(6 delta^3), which is
     absorbed in the stated slack O(delta^2 m/n).
  E  sympy: the Gao20 Thm 6 sequential product for P(H in G(n,D)) equals the McKay
     exponent -lambda-lambda^2-mu+(D^2-1)/4 exactly at order n^0, for general H;
     each Thm-6 ingredient is needed; new budget table.
Run:  python v2/scripts/residual/worker3_sharp_boundary.py
"""
import sys
from functools import lru_cache
from math import comb, factorial
from fractions import Fraction
import sympy as sp
from mpmath import mp, mpf, log

mp.dps = 40
sys.setrecursionlimit(100000)


def df(k):  # (k)!! for odd k, (-1)!! = 1
    r = 1
    while k > 1:
        r *= k
        k -= 2
    return r


# ---------------------------------------------------------------- section A
def section_A():
    print("== A. MW91 cubic terms in the four-class ratio (sympy) ==")
    d, n, D, L, a = sp.symbols('d n D L abar', positive=True)

    def T(M1, M2, M3):
        return -M2**2*M3/(2*M1**4) + M2**4/(4*M1**5) + M3**2/(6*M1**3)

    Treg = sp.simplify(T(n*d, n*d*(d-1), n*d*(d-1)*(d-2)))
    print("  T_reg(d) =", sp.factor(Treg))
    lead = sp.limit(Treg*n/d**3, d, sp.oo)
    assert lead == sp.Rational(-1, 12)
    print("  T_reg(d)*n/d^3 -> ", lead, " (the -d^3/(12n) of the regular count)")

    # ratio combination: R-class (mean degree D-2L+abar) + whole graph - 2 * (D-L)-regular
    comb_ = (Treg.subs(d, D-2*L+a) + Treg.subs(d, D) - 2*Treg.subs(d, D-L))*n
    # scale D=t, L = l*t^(1/2)-ish is awkward; expand as polynomial part in D at fixed L, abar
    ser = sp.series(sp.together(comb_), D, sp.oo, 3).removeO()
    ser = sp.expand(ser)
    print("  n*[T_reg(D-2L+abar)+T_reg(D)-2T_reg(D-L)] at D->oo (L, abar fixed):")
    print("     ", sp.collect(ser, D))
    assert sp.expand(ser).coeff(D, 3) == 0
    c2 = sp.expand(ser).coeff(D, 2)
    assert sp.simplify(c2 + a/4) == 0          # only -abar D^2/4, abar ~ L^2/D
    c1 = sp.expand(ser).coeff(D, 1)
    print("   D^3 coeff = 0, D^2 coeff =", c2, ", D coeff =", sp.factor(c1))
    # with abar = L^2/D the whole thing is O(D L^2):
    tot = sp.expand(sp.series(sp.together(comb_.subs(a, L**2/D)), D, sp.oo, 2).removeO())
    print("   at abar = L^2/D:  ", sp.collect(tot, D), " + O(1/D)   => O(D L^2 / n)")
    assert tot.coeff(D, 2) == 0 and tot.coeff(D, 3) == 0

    # Gao -sum p^2/2 terms: |X| gamma^2/(2 n^2) for R against 2 * (Ln/2)(D-L)^2/(2n^2)
    g = ((L*n - n*L**2/(2*D))*(D-2*L+L**2/D)**2 - L*n*(D-L)**2)/(2*n**2)*n
    gs = sp.expand(sp.series(sp.together(g), D, sp.oo, 1).removeO())
    print("  n*[-sum p^2/2 (R) + 2 sum p^2/2 (R')] = -(", sp.collect(gs, D), ") + ...")
    assert gs.coeff(D, 2) == 0                 # the L D^2/n terms cancel
    print("   L D^2 coefficient = 0  => O(D L^2 / n)")


# ---------------------------------------------------------------- section B
def count_regular(n, d):
    """Exact number of labelled simple d-regular graphs on n vertices."""
    @lru_cache(maxsize=None)
    def f(c):  # c[j-1] = number of live vertices with remaining degree j
        if not any(c):
            return 1
        r = max(j for j in range(1, d+1) if c[j-1])
        c = list(c)
        c[r-1] -= 1
        tot = 0

        def rec(j, left, ways, ks):
            nonlocal tot
            if j > d:
                if left == 0:
                    new = [c[i] - ks[i] + (ks[i+1] if i+1 < d else 0) for i in range(d)]
                    tot += ways * f(tuple(new))
                return
            for k in range(0, min(c[j-1], left) + 1):
                rec(j+1, left-k, ways*comb(c[j-1], k), ks + [k])
        rec(1, r, 1, [])
        return tot
    c0 = [0]*d
    c0[d-1] = n
    return f(tuple(c0))


def Treg_num(d, n):
    return Fraction(-(d-1)**3*(d-2), 2*d*n) + Fraction((d-1)**4, 4*d*n) + Fraction((d-1)**2*(d-2)**2, 6*d*n)


def logfrac(num, den):
    return log(mpf(num)) - log(mpf(den))


def section_B(reg_cache):
    print("== B. exact regular counts vs MW91 ==")
    known = {(4, 3): 1, (6, 3): 70, (8, 3): 19355, (5, 4): 1, (6, 4): 15, (7, 4): 465}
    for (n, d), v in known.items():
        assert count_regular(n, d) == v, (n, d)
    print("  DP reproduces known counts", known)
    plan = {2: (40, 60), 3: (40, 60), 4: (30, 40), 5: (20, 26), 6: (14, 18)}
    print("  kappa(d) := lim n*(log P_simple + (d^2-1)/4 - T_reg(d));  MW91 says O(d^2)")
    for d, (n1, n2) in plan.items():
        vals = []
        for n in (n1, n2):
            N = count_regular(n, d)
            reg_cache[(n, d)] = N
            lp = logfrac(N*factorial(d)**n, df(d*n-1))
            vals.append(n*(lp + mpf(d*d-1)/4 - mpf(Treg_num(d, n).numerator)/Treg_num(d, n).denominator))
        kap = (n2*vals[1] - n1*vals[0])/(n2-n1)      # removes the 1/n^2 term
        nT = float(Treg_num(d, 1))
        print(f"  d={d}: n*resid at n={n1},{n2}: {float(vals[0]):+.5f} {float(vals[1]):+.5f}"
              f"  extrap kappa={float(kap):+.5f}  kappa/d^2={float(kap)/d/d:+.4f}"
              f"   [n*T_reg={nT:+.4f}; without T: {(float(kap)+nT)/d/d:+.4f} d^2]")


# ---------------------------------------------------------------- section C
def section_C(reg_cache):
    print("== C. Gao20 Thm 6 against exact arithmetic ==")
    # C1: d=1, exact conditional edge probability given a forbidden matching H2
    def A(nn, i):   # P(uniform PM of K_nn avoids i given disjoint edges)
        return sum(Fraction((-1)**j*comb(i, j)*df(nn-2*j-1), df(nn-1)) for j in range(i+1))
    print("  C1 (d=1): n^2*(exact/formula - 1) should stay bounded (error O(1/n^2))")
    for n in (200, 400, 800):
        i = n//4
        # (a) uv disjoint from H2: |W| = 2i, phibar = -1
        ex = Fraction(1, n-1)*A(n-2, i)/A(n, i)
        fo = Fraction(1, n)*(1-Fraction(2*i, n*n))*(1+Fraction(1, n))
        # (b) u and v each on an H2 edge (ux, vy): |W| = 2(i-2), phibar = -3
        ex2 = Fraction(1, n-1)*A(n-2, i-2)/A(n, i)
        fo2 = Fraction(1, n)*(1-Fraction(2*(i-2), n*n))*(1+Fraction(3, n))
        # same with the W term or the neighbour term dropped: must NOT stay bounded
        foW = Fraction(1, n)*(1+Fraction(1, n))
        foN = Fraction(1, n)*(1-Fraction(2*(i-2), n*n))*(1+Fraction(1, n))
        print(f"   n={n}: (a) {float((ex/fo-1)*n*n):+.4f}  (b) {float((ex2/fo2-1)*n*n):+.4f}"
              f"   | no-W: {float((ex/foW-1)*n*n):+.1f}  no-nbr: {float((ex2/foN-1)*n*n):+.1f}")
    # C2: P(G(n,d) avoids a perfect matching); sequential product of Thm 6 predicts
    #     log P = -d/2 - (d^2+d)/(4n) + O(1/n^2)
    print("  C2: n*(log P(G(n,d) avoids PM) + d/2) -> -(d^2+d)/4 predicted")
    for n in (200, 400):
        v = n*(log(mpf(A(n, n//2).numerator)) - log(mpf(A(n, n//2).denominator)) + mpf(1)/2)
        print(f"   d=1 n={n}: {float(v):+.5f}   predicted -0.5")
        assert abs(v + mpf(1)/2) < mpf(2)/n
    # (the d>=2 pair-DP of the killed attempt failed brute force at (6,2); removed)


# ---------------------------------------------------------------- section D
def section_D():
    """Exact barrier arithmetic, delta = n^s, m = n^(t*s) i.e. m = delta^t.
    An error E resolves the coefficient 1/(6 delta^3) iff E*delta^3 -> 0;
    it is absorbed in the stated slack O(delta^2 m/n) iff E/(delta^2 m/n) = O(1)."""
    print("== D. barrier exponents (exact) ==")
    s, t = sp.symbols('s t', nonnegative=True)
    dl, m = sp.Symbol('dl'), sp.Symbol('m')
    nn = sp.Symbol('n')
    errs = {
        "Gao21 Thm14 / McK85 (enumeration)": dl**3/nn,
        "Gao20 Thm6 sequential (Remark 8)":  dl**2*m/nn,
        "MW91 level (no forbidden-edge version exists)": dl**2/nn,
        "(ii) class-sum": m**4/nn,
        "(iii) pairing-sum": m**5/(dl**2*nn),
        "(iv) K-dependence": m**2*dl/nn,
    }

    def expo(E):  # log_n of E*delta^3 at delta=n^s, m=delta^t
        e = sp.expand_log(sp.log(E*dl**3).subs({dl: nn**s, m: nn**(t*s)}), force=True)
        return sp.simplify(e/sp.log(nn))

    def sup_s(E, tv):  # largest s with exponent < 0
        return sp.solve(sp.Eq(expo(E).subs(t, tv), 0), s)[0]
    print("  max s (delta=o(n^s)) for E*delta^3 -> 0:")
    print(f"  {'error':48s} {'m=O(1)':>8s} {'m=delta^(1/2)':>14s}")
    res = {}
    for name, E in errs.items():
        res[name] = (sup_s(E, 0), sup_s(E, sp.Rational(1, 2)))
        print(f"  {name:48s} {str(res[name][0]):>8s} {str(res[name][1]):>14s}")
    assert res["Gao21 Thm14 / McK85 (enumeration)"][0] == sp.Rational(1, 6)
    assert res["Gao20 Thm6 sequential (Remark 8)"] == (sp.Rational(1, 5), sp.Rational(2, 11))
    assert res["(iv) K-dependence"][0] == sp.Rational(1, 4)
    # with Gao21 replaced by Gao20 Thm6, binding at m=O(1) is 1/5 (not 1/2, not 2/5)
    others = [k for k in errs if not k.startswith(("Gao21", "MW91"))]
    assert min(res[k][0] for k in others) == sp.Rational(1, 5)
    print("  => with Gao20 Thm6 in place of Gao21 Thm14 the coefficient barrier is")
    print("     delta^5 m = o(n): n^{1/5} at m=O(1), n^{2/11} at m=delta^{1/2}.")
    # absorption into the stated slack O(delta^2 m / n)
    slack = dl**2*m/nn
    print("  absorbed into O(delta^2 m/n)?  (ratio E/slack)")
    for name, E in errs.items():
        r = sp.simplify(E/slack)
        print(f"   {name:48s} {r}")
    assert sp.simplify(errs["Gao21 Thm14 / McK85 (enumeration)"]/slack) == dl/m  # not absorbed unless m ~ delta
    assert sp.simplify(errs["(ii) class-sum"]/slack) == m**3/dl**2              # absorbed iff m <= delta^{2/3}
    # the slack term reaches 0 at m = delta^{1/2} exactly up to delta = o(n^{2/5})
    e = sp.expand_log(sp.log(slack.subs({dl: nn**s, m: nn**(s/2)})), force=True)/sp.log(nn)
    assert sp.solve(sp.Eq(sp.simplify(e), 0), s)[0] == sp.Rational(2, 5)
    print("  slack delta^2 m/n -> 0 at m=delta^{1/2} iff delta=o(n^{2/5}): the conjecture's range.")


# ---------------------------------------------------------------- section E
def thm6_sequential(D, hb, v2, s11, wfac=2, nbr=1, var=1):
    """n^0 part of sum_k [log p_k - log(du dv / Mtilde)] for P(H in G(n,D)),
    H added in uniformly random order, p_k from Gao20 Thm 6 with H2 empty.
    H enters only through hb = 2|H|/n, v2 = sum h_v^2/n, s11 = sum_{xy in H} h_x h_y/n.
    wfac/nbr/var switch the W-term, the neighbour sums in phibar, the Bin variance."""
    t = sp.Symbol('tau', positive=True)
    e, V2, S11 = hb/2, v2, s11
    Mt = D - hb*t
    m2 = D*(D-1) - t*hb*(2*D-1) + t**2*v2 + var*t*(1-t)*hb
    SW = wfac*t*(e*(D-1)**2 - (D-1)*t*(V2-2*e) + t**2*(S11-V2+e))
    T1 = e*(m2**2/Mt**3 + m2/Mt**2 + SW/Mt**2)
    phi = (-4*D*e + 2*t*(V2-2*e) + 2*e
           - nbr*t*((D-1)*(V2-2*e) - 2*t*(S11-V2+e))
           - (2*D*e - t*(V2-2*e) - 2*e)*m2/Mt
           + e*D**2 - D*t*(V2-2*e) + t**2*(S11-V2+e))
    return -sp.integrate(sp.apart(sp.together(T1 + phi/Mt), t), (t, 0, 1))


def section_E():
    print("== E. Gao20 Thm 6 sequential product = McKay exponent at order n^0 (sympy) ==")
    D, hb, v2, s11 = sp.symbols('D hbar v2 s11', positive=True)
    lam = (D*(D-1) - hb*(2*D-1) + v2)/(2*(D-hb))     # lambda(g), g = D - h, exact in n
    mu = (hb*D**2/2 - D*v2 + s11)/(D-hb)              # mu(g,H)
    E = -lam - lam**2 - mu + (D**2-1)/4
    # sum_k log((Dn-2k)/(Dn-1-2k)) -> (1/2) log(D/(D-hb))  (pairing vs Thm-6 main factor)
    shift = sp.log(D) - sp.log(D-hb)
    C = thm6_sequential(D, hb, v2, s11)
    diff = sp.simplify(sp.expand_log(C - E - shift/2, force=True))
    # sympy leaves log(-(D-hb)) branches; check numerically at random points too
    pts = [(7, sp.Rational(3, 2), sp.Rational(13, 4), sp.Rational(11, 8)),
           (23, 5, 31, 59), (sp.Rational(101, 3), 2, 5, 7)]
    for p in pts:
        val = sp.N(diff.subs(dict(zip((D, hb, v2, s11), p))), 30)
        assert abs(val) < 1e-25, (p, val)
    print("   C - [-lambda - lambda^2 - mu + (D^2-1)/4] - (1/2)log(D/(D-hbar)) = 0  (symbolic; 3 points to 1e-25)")
    # sensitivity: each Thm-6 ingredient is needed
    for kw in ({'wfac': 1}, {'nbr': 0}, {'var': 0}):
        Cb = thm6_sequential(D, hb, v2, s11, **kw)
        val = sp.N((Cb - E - shift/2).subs({D: 7, hb: 2, v2: 5, s11: 7}), 20)
        assert abs(val) > 1e-3, kw
        print(f"   altered {kw}: residual {float(sp.re(val)):+.5f}  (identity fails, as it must)")
    # perfect matching: E = 1/4 (Bollobas-McKay e^{1/4})
    assert sp.simplify(E.subs({hb: 1, v2: 1, s11: sp.Rational(1, 2)}) - sp.Rational(1, 4)) == 0
    print("   H = perfect matching: exponent = 1/4 (Bollobas-McKay)")
    # new budget table with enumeration error delta^2 m/n
    s = sp.Symbol('s')
    print("   sharp-rate budgets after the upgrade (E*delta^3): delta^5 m/n, m^4 delta^3/n,"
          " m^5 delta/n, m^2 delta^4/n")
    for tv, want in ((0, sp.Rational(1, 5)), (sp.Rational(1, 2), sp.Rational(2, 11)),
                     (sp.Rational(2, 3), sp.Rational(3, 17))):
        ex = [5 + tv, 3 + 4*tv, 1 + 5*tv, 4 + 2*tv]          # delta-exponents, m = delta^tv
        sup = min(1/sp.Rational(x) for x in ex)
        assert sup == want, (tv, sup)
        print(f"     m = delta^{tv}: delta = o(n^{sup})")


if __name__ == "__main__":
    cache = {}
    section_A()
    section_B(cache)
    section_C(cache)
    section_D()
    section_E()
    print("DONE worker3")
