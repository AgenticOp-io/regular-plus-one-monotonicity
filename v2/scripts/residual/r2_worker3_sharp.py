"""
r2_worker3_sharp.py -- round 2, track 3: rigorous step 5 of the sequential Gao20 Thm 6
product, and what lies past delta^5 m = o(n).  Checks for v2/notes/r2_worker3_sharp.txt.

Gao20 Thm 6 (arXiv:2012.01492 v3, read from the PDF), H2 = empty, d = D*1:
  P(uv in G | H1 in) = (1+O(Delta^5 n/M^3)) (du dv/Mt) (1 - Mt2^2/Mt^3 - Mt2/Mt^2
                        - sum_{(x,y) in W} dx dy/Mt^2) (1 - phibar/Mt),
  d = D - deg_{H1}, Mt = sum d, Mt2 = sum d(d-1), W = ordered (x,y): xy in H1, xu,yv notin H1,
  {x,y} disjoint from {u,v};  phibar = -2(du+dv)+2 - sum_{x in N_H1(u)} dx - sum_{y in N_H1(v)} dy
                               - (du+dv-2) Mt2/Mt + du dv.
Sections
  1  exact symbolic: the main-term integral = McKay exponent + (1/2)log(D/(D-hbar)),
     rational part and log coefficient separately (no numerics).
  2  exact enumeration (Fraction) of sum_k E[A_k+B_k] over all orders for small H, against the
     main-term integral: the step-5 difference is O(e/n^2)-type and inside the explicit bound.
  3  exact: the Thm-6 per-edge error is genuinely Theta(D^2/n^2) (empty host).
  4  exact star family P(K_{1,r} in G(n,D)) = (D)_r/(n-1)_r against the Proposition;
     4b edge by edge: Gao's product form vs the exp(-A-B) form.
  5  past n^{1/5}: ratio cancellation of a smooth second-order Thm-6 term; budget tables.
Run:  python v2/scripts/residual/r2_worker3_sharp.py      (ends "DONE r2_worker3")
"""
import itertools
import random
from fractions import Fraction as Fr
import sympy as sp
from mpmath import mp, mpf, quad, log as mlog

mp.dps = 30
D, hb, v2, s11, t, s, n = sp.symbols('D hbar v2 s11 t s n', positive=True)


def mckay_E(D, hb, v2, s11):
    """-lambda-lambda^2-mu+(D^2-1)/4 for g = D - h, per-vertex statistics."""
    lam = (D*(D-1) - hb*(2*D-1) + v2)/(2*(D-hb))
    mu = (hb*D**2/2 - D*v2 + s11)/(D-hb)
    return -lam - lam**2 - mu + (D**2-1)/4


def integrand(D, hb, v2, s11, t):
    """sum_f [main term of A_f+B_f] at Poisson time t, via per-vertex statistics."""
    e = hb/2
    Mt = D - hb*t
    m2 = D*(D-1) - t*hb*(2*D-1) + t**2*v2 + t*(1-t)*hb
    P1, P2 = v2 - hb, s11 - v2 + e            # sum h(h-1)/n,  sum_{xy}(hx-1)(hy-1)/n
    SW = 2*t*(e*(D-1)**2 - (D-1)*t*P1 + t**2*P2)
    T1 = e*(m2**2/Mt**3 + m2/Mt**2 + SW/Mt**2)
    phi = (-2*(2*D*e - t*P1) + 2*e - t*((D-1)*P1 - 2*t*P2)
           - (2*D*e - t*P1 - 2*e)*m2/Mt + e*D**2 - D*t*P1 + t**2*P2)
    return T1 + phi/Mt


# ------------------------------------------------------------------ section 1
def section_1():
    print("== 1. main-term integral = McKay exponent + (1/2)log(D/(D-hbar)), exact ==")
    # t = (D-s)/hbar, dt = -ds/hbar: C = -int_0^1 = -(1/hbar) int_{D-hbar}^{D} F(s) ds,
    # F a Laurent polynomial in s (the only denominators are powers of Mt = s).
    F = sp.expand(sp.cancel(integrand(D, hb, v2, s11, (D-s)/hb)*s**4))
    poly = sp.Poly(F, s)
    rat, a_m1 = 0, 0
    for (k,), a in poly.terms():
        p = k - 4                                   # power of s
        if p == -1:
            a_m1 = a
        else:
            rat += a*(D**(p+1) - (D-hb)**(p+1))/(p+1)
    log_coeff = sp.simplify(-a_m1/hb)               # coefficient of log(D/(D-hbar)) in C
    rat_part = -rat/hb
    assert log_coeff == sp.Rational(1, 2), log_coeff
    assert sp.cancel(rat_part - mckay_E(D, hb, v2, s11)) == 0
    print("   C = R + (1/2) log(D/(D-hbar)),  R - [-lam-lam^2-mu+(D^2-1)/4] = 0 identically")
    return sp.lambdify((D, hb, v2, s11), rat_part + log_coeff*sp.log(D/(D-hb)), 'mpmath')


# ------------------------------------------------------------------ section 2
def AB_exact(Dv, nv, edges, S, f):
    """A + B of Gao20 Thm 6 (H2 empty) at state H1 = S (set of edge indices), next edge f."""
    deg = [0]*nv
    for i in S:
        x, y = edges[i]
        deg[x] += 1
        deg[y] += 1
    d = [Dv - k for k in deg]
    Mt = sum(d)
    M2 = sum(k*(k-1) for k in d)
    u, v = f
    Sset = {frozenset(edges[i]) for i in S}
    W = 0
    for i in S:
        a, b = edges[i]
        for x, y in ((a, b), (b, a)):
            if {x, y} & {u, v}:
                continue
            if frozenset((x, u)) in Sset or frozenset((y, v)) in Sset:
                continue
            W += d[x]*d[y]
    Nu = sum(d[x] for x in range(nv) if frozenset((x, u)) in Sset)
    Nv = sum(d[y] for y in range(nv) if frozenset((y, v)) in Sset)
    A = Fr(M2*M2, Mt**3) + Fr(M2, Mt**2) + Fr(W, Mt**2)
    phib = -2*(d[u]+d[v]) + 2 - Nu - Nv - Fr((d[u]+d[v]-2)*M2, Mt) + d[u]*d[v]
    return A + phib/Mt


def exact_linear_sum(Dv, nv, edges):
    """sum_k E[A_k+B_k] over a uniform order, exactly, by enumerating all (S, f)."""
    e = len(edges)
    tot = Fr(0)
    for j in range(e):
        acc, cnt = Fr(0), 0
        for S in itertools.combinations(range(e), j):
            Ss = set(S)
            for fi in range(e):
                if fi not in Ss:
                    acc += AB_exact(Dv, nv, edges, S, edges[fi])
                    cnt += 1
        tot += acc/cnt
    return tot


def stats(nv, edges):
    h = [0]*nv
    for x, y in edges:
        h[x] += 1
        h[y] += 1
    return (Fr(2*len(edges), nv), Fr(sum(k*k for k in h), nv),
            Fr(sum(h[x]*h[y] for x, y in edges), nv), max(h))


def step5_bound(e, nv, Dlt, c):
    """explicit step-5 bound of the note (smoothing 90 + means 24, and the W term)."""
    return (90/c**5 + 24/c**3)*e/nv**2 + 6*Dlt**2*e/(c**2*nv**2)


def section_2(Cfun):
    print("== 2. step 5: exact enumeration over all orders vs the main-term integral ==")
    print("   n * E_lin ~ O(1) scale; n^2*(E_lin - I)/e should stay bounded (error O(Delta^2 e/n^2))")
    rng = random.Random(7)

    def graph_main(Dv, nv, edges):
        # graph-level main term, integrated numerically; must equal -C(stats)
        h = [0]*nv
        for x, y in edges:
            h[x] += 1
            h[y] += 1
        e = len(edges)
        nb = [[] for _ in range(nv)]
        for x, y in edges:
            nb[x].append(y)
            nb[y].append(x)

        def g(tt):
            M = Dv*nv - 2*e*tt
            m2 = sum(Dv*(Dv-1) - (2*Dv-1)*k*tt + k*k*tt*tt + k*tt*(1-tt) for k in h)
            Wm = 2*tt*sum((Dv-1-(h[x]-1)*tt)*(Dv-1-(h[y]-1)*tt) for x, y in edges)
            tot = 0
            for u, v in edges:
                du, dv = Dv-(h[u]-1)*tt, Dv-(h[v]-1)*tt
                Nu = tt*sum(Dv-1-(h[x]-1)*tt for x in nb[u] if x != v)
                Nv = tt*sum(Dv-1-(h[y]-1)*tt for y in nb[v] if y != u)
                ph = -2*(du+dv) + 2 - Nu - Nv - (du+dv-2)*m2/M + du*dv
                tot += m2**2/M**3 + m2/M**2 + Wm/M**2 + ph/M
            return tot
        return quad(g, [0, 1])

    cases = []
    # perfect matchings and cycles: e proportional to n
    for nv in (12, 16, 20, 24):
        cases.append(("PM", 4, nv, [(2*i, 2*i+1) for i in range(nv//2)]))
    for nv in (8, 10, 12):
        cases.append(("cycle", 5, nv, [(i, (i+1) % nv) for i in range(nv)]))
    # a fixed 11-edge graph padded with isolated vertices: e fixed, n growing
    base = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 5), (5, 3), (5, 6), (6, 7), (7, 0), (1, 6)]
    for nv in (10, 20, 40):
        cases.append(("fixed11", 6, nv, base))
    # random graph, max degree <= 3
    while True:
        es = set()
        while len(es) < 11:
            a, b = rng.sample(range(11), 2)
            es.add((min(a, b), max(a, b)))
        es = sorted(es)
        if stats(11, es)[3] <= 3:
            break
    cases.append(("random", 6, 11, es))
    out = {}
    for name, Dv, nv, edges in cases:
        e = len(edges)
        hbv, v2v, s11v, Dlt = stats(nv, edges)
        c = Fr(Dv - Dlt, Dv)                       # h_v <= (1-c) D
        El = exact_linear_sum(Dv, nv, edges)
        Ig = graph_main(Dv, nv, edges)
        Ic = -Cfun(mpf(Dv), mpf(hbv.numerator)/hbv.denominator,
                   mpf(v2v.numerator)/v2v.denominator, mpf(s11v.numerator)/s11v.denominator)
        assert abs(Ig - Ic) < mpf(10)**-20, (name, Ig, Ic)   # graph form reduces to (hbar,v2,s11)
        diff = mpf(El.numerator)/El.denominator - Ig
        bnd = step5_bound(e, nv, Dlt, float(c))
        assert abs(diff) <= bnd
        out[(name, nv)] = diff
        print(f"   {name:8s} D={Dv} n={nv:2d} e={e:2d} Delta={Dlt}: n*E_lin={float(nv*El):+9.4f}"
              f"  n^2(E_lin-I)/e={float(diff*nv*nv/e):+8.4f}   bound/|diff|={float(bnd/abs(diff)):.0f}")
    # e fixed, n doubling: diff*n^2 converges (no 1/n piece)
    r = [out[("fixed11", k)]*k*k for k in (10, 20, 40)]
    assert abs(r[2]-r[1]) < abs(r[1]-r[0])
    print("   graph-form main term == closed form C(D,hbar,v2,s11) in every case (1e-20)")


# ------------------------------------------------------------------ section 3
def section_3():
    print("== 3. Thm-6 per-edge error is genuinely Theta(D^2/n^2) (H1 empty, exact) ==")
    Mt, M2 = D*n, D*(D-1)*n
    phib = -4*D + 2 - 2*(D-1)*M2/Mt + D**2
    q = D**2/Mt*(1 - M2**2/Mt**3 - M2/Mt**2)*(1 - phib/Mt)
    p = D/(n-1)                                      # exact, by symmetry
    ser = sp.series(sp.simplify(q/p - 1), n, sp.oo, 3).removeO()
    assert sp.simplify(ser + (D**2 - D + 1)/n**2) == 0
    print("   q/p - 1 = -(D^2-D+1)/n^2 + O(D^3/n^3): Gao's O(D^2/n^2) per edge is attained")


# ------------------------------------------------------------------ section 4
def section_4():
    print("== 4. star K_{1,r}: P = (D)_r/(n-1)_r exactly, against the Proposition ==")
    r = sp.Symbol('r', positive=True)
    # rho = sum_{i<r} log((Dn-1-2i)/(D(n-1-i))) + lam + lam^2 + mu - (D^2-1)/4
    # lambda, mu for g = D - h, h = (r, 1 x r, 0 x (n-r-1))
    Sg = D*n - 2*r
    Sgg = (n-r-1)*D*(D-1) + r*(D-1)*(D-2) + (D-r)*(D-r-1)
    lam = Sgg/(2*Sg)
    mu = r*(D-r)*(D-1)/Sg

    def rho_num(Dv, rv, nv):
        tot = sum(mlog(mpf(Dv*nv-1-2*i)/(Dv*(nv-1-i))) for i in range(rv))
        sub = {D: Dv, r: rv, n: nv}
        L = mpf(sp.Rational(lam.subs(sub)))
        return tot + L + L*L + mpf(sp.Rational(mu.subs(sub))) - mpf(Dv*Dv-1)/4
    # symbolic 1/n and 1/n^2 coefficients of rho for integer r (sum done termwise)
    x = sp.Symbol('x')        # x = 1/n
    i = sp.Symbol('i', integer=True, nonnegative=True)
    term = sp.log((D/x-1-2*i)/(D*(1/x-1-i)))
    tser = sp.expand(sp.series(term, x, 0, 3).removeO())
    sum_ser = sum(sp.summation(sp.expand(tser).coeff(x, k), (i, 0, r-1))*x**k for k in (1, 2))
    rest = (lam + lam**2 + mu - (D**2-1)/4).subs(n, 1/x)
    rser = sp.series(rest, x, 0, 3).removeO()
    rho_ser = sp.expand(sum_ser + rser)
    c0 = sp.simplify(rho_ser.coeff(x, 0))
    c1 = sp.factor(sp.simplify(rho_ser.coeff(x, 1)))
    c2 = sp.factor(sp.simplify(rho_ser.coeff(x, 2)))
    assert c0 == 0
    print("   n^0 coefficient of rho: 0")
    print("   n^-1 coefficient:", c1)
    print("   n^-2 coefficient:", c2)
    # Proposition allows K (r D^2/n^2 + 1/(D n)); the truth is smaller: no 1/n term at all,
    # and the n^-2 coefficient has no positive power of D (no r D^2 term: Gao's per-edge
    # D^2/n^2 of section 3 does not accumulate along the star).
    assert c1 == 0
    c2inf = sp.expand(sp.limit(c2, D, sp.oo))
    assert sp.expand(c2inf - (r**3/6 + 5*r**2/4 + r/12)) == 0
    print("   n^-2 coefficient at D -> oo:", c2inf, " (= O(r^3) = O(e Delta^2))")
    for Dv, rv, nv in ((8, 4, 10**4), (20, 10, 10**5), (40, 20, 10**6)):
        val = rho_num(Dv, rv, nv)
        pred = mpf(sp.N(c1.subs({D: Dv, r: rv})))/nv + mpf(sp.N(c2.subs({D: Dv, r: rv})))/nv**2
        assert abs(val - pred) < mpf(Dv)**4/mpf(nv)**3
        print(f"   D={Dv} r={rv} n={nv}: rho={float(val):+.3e}  series={float(pred):+.3e}"
              f"  rho*n^2/(r D^2) after 1/n part = {float((val - mpf(sp.N(c1.subs({D:Dv,r:rv})))/nv)*nv*nv/(rv*Dv*Dv)):+.4f}")
    # leading r*D^2 part of the n^-2 coefficient (accumulated Gao error, cf. section 3)
    lead = sp.limit(c2.subs(r, sp.Symbol('a')*D)/D**3, D, sp.oo)
    print("   n^-2 coeff at r = a D, leading D^3 part:", sp.factor(lead))

    # 4b: edge by edge along the star.  State: j leaves already attached to the centre v;
    # next edge v-u, u a fresh leaf.  Exact p_j = (D-j)/(n-1-j) (N(v) is a uniform D-set).
    j, x = sp.symbols('j x', positive=True)          # x = 1/n
    nn = 1/x
    du, dv = D, D - j
    Mt = D*nn - 2*j
    M2 = (nn-j-1)*D*(D-1) + j*(D-1)*(D-2) + (D-j)*(D-j-1)
    A = M2**2/Mt**3 + M2/Mt**2                        # W is empty: every H1 edge meets v
    B = (-2*(du+dv) + 2 - j*(D-1) - (du+dv-2)*M2/Mt + du*dv)/Mt
    p = (D-j)/(nn-1-j)
    eta_prod = sp.expand(sp.series(sp.log(p*Mt/(du*dv)) - sp.log((1-A)*(1-B)), x, 0, 3).removeO())
    eta_exp = sp.expand(sp.series(sp.log(p*Mt/(du*dv)) + A + B, x, 0, 3).removeO())
    for name, et in (("Gao (1-A)(1-B)", eta_prod), ("exp(-A-B)     ", eta_exp)):
        assert sp.simplify(et.coeff(x, 0)) == 0 and sp.simplify(et.coeff(x, 1)) == 0
        print(f"   log(p_j/q_j), {name}: n^-2 coeff =", sp.factor(sp.simplify(et.coeff(x, 2))))
    e2p = sp.simplify(eta_prod.coeff(x, 2))
    e2e = sp.simplify(eta_exp.coeff(x, 2))
    assert sp.expand(e2p.subs(j, 0) - (D**2 - D + 1)) == 0       # = section 3
    assert sp.degree(sp.expand(e2e*D**2), D) <= 2                  # no D^2 growth in exp form
    print("   => the D^2/n^2 error of Thm 6 is the cross term AB; the exp form has per-edge")
    print("      error O((1+j^2)/n^2) along the star, uniformly in D")
    return c1, c2


# ------------------------------------------------------------------ section 5
def section_5():
    print("== 5. past delta^5 m = o(n): cancellation of a smooth second-order Thm-6 term ==")
    m, a1, a2, a3, al, be = sp.symbols('m psi1 psi2 psi3 alpha beta')
    # Suppose the per-edge error were (1/n^2)[D^2 psi(hbar*t/D) + alpha D (s_u+s_v) + beta D h_u..]
    # psi(y) = psi1 y + psi2 y^2/2 + psi3 y^3/6 (+ psi0: a constant psi0 is the same as psi(0)).
    # Summed over a Poisson-ordered process (e = hbar n/2 edges):
    #   (D^2/n^2) e int_0^1 psi(hbar t/D) dt = (D^3/(2n)) Psi(hbar/D),  Psi' = psi
    #   alpha D/n^2 sum_f E[s_u+s_v] = alpha D (v2 - hbar)/(2n)
    p0 = sp.Symbol('psi0')
    Psi = lambda y: p0*y + a1*y**2/2 + a2*y**3/6 + a3*y**4/24
    T = lambda hbar, v2_: D**3*Psi(hbar/D)/(2*n) + al*D*(v2_ - hbar)/(2*n)
    q = m**2/D
    Ea2 = q + m**2*(m-1)**2/(D*(D-1))
    hX, v2X = 2*m - q, 4*m**2 - 4*m*q + Ea2              # X = F1 u F2, h_v = 2m - a_v
    R = sp.expand(sp.series(sp.together((T(hX, v2X) - 2*T(m, m**2))*n), D, sp.oo, 2).removeO())
    # the single-process size is D^2 m/n (the slack); in the ratio the D^2 m term is gone
    single = sp.expand(sp.series(sp.together(T(m, m**2)*n), D, sp.oo, 2).removeO())
    assert sp.expand(single).coeff(D, 2) != 0
    assert sp.expand(R).coeff(D, 2) == 0 and sp.expand(R).coeff(D, 3) == 0
    print("   one process:  n*T(F) =", sp.collect(single, D), "+ ...   (size D^2 m: the slack)")
    print("   ratio X - 2F: n*R    =", sp.collect(R, D), "+ O(1/D)  => O(D m^2/n + m^3/n)")
    # budgets (E * delta^3 -> 0), delta = n^s, m = delta^tv
    print("   sup s with delta=o(n^s), all budgets E*delta^3 -> 0:")
    for tv in (0, sp.Rational(1, 2), sp.Rational(2, 3), 1):
        proved = [sp.Rational(1, 5 + tv), 1/sp.Rational(3 + 4*tv), 1/sp.Rational(1 + 5*tv),
                  1/sp.Rational(4 + 2*tv)]
        # delta^3 * D^3 m / n^2 -> 0: delta^(6+tv) = o(n^2)
        cond = [sp.Rational(2, 1)/(6 + tv), 1/sp.Rational(3 + 4*tv), 1/sp.Rational(1 + 5*tv),
                1/sp.Rational(4 + 2*tv)]
        print(f"     m = delta^{tv}:  proved delta = o(n^{min(proved)}),"
              f"  conditional delta = o(n^{min(cond)})")
        if tv == 0:
            assert min(proved) == sp.Rational(1, 5) and min(cond) == sp.Rational(1, 4)


if __name__ == "__main__":
    Cfun = section_1()
    section_2(Cfun)
    section_3()
    section_4()
    section_5()
    print("DONE r2_worker3")
