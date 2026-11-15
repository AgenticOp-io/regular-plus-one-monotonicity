"""
r2_worker2_peel.py -- round 2 for the peel second moment past n^{1/3}.

(1) (R1) closed.  Deterministic bound of the gamma^3 remainder of lem:containment-ratio(b),
    and the v^T Q^-1 v, T^2 psi'' and delta-variance terms dropped by sign
    (E[P^2] >= (E P)^2 by Cauchy-Schwarz, so only the upper bound is needed).
    Constants checked in sympy; the bound is checked in floating point at n = 400.
(2) (R2) at k = 3.  For ANY S_n-invariant law of L-regular graphs, the probabilities of all
    3-edge shapes are fixed by n, L and the triangle density t3.  So kappa3 is an exact
    rational function of (n, L, t3).  It is checked against brute-force enumeration of
    nu_L for n <= 8, shape by shape and as kappa3.
(3) Next order.  Exact series of the computable exponent in 1/n with L symbolic: the
    L^2 and L^3/n coefficients vanish, no L^5/n^2 term exists, and the L^4/n^2
    coefficient D4 is computed.

Run:  python v2/scripts/residual/r2_worker2_peel.py
Writes v2/notes/r2_worker2_peel.txt.
"""
import itertools
import math
from fractions import Fraction
from pathlib import Path

import numpy as np
from sympy import (Matrix, Rational, binomial, cancel, diff, eye, factor, ff, log, ones,
                   series, simplify, sqrt, symbols, expand, expand_func)

PROOF = r"""
=====================================================================================
PROOFS AND STATUS
=====================================================================================
Notation as in lem:containment-ratio: s = Ln/2, N0 = C(n,2), lambda(e) = (lam N0 - e)/(N0 - e),
psi(e) = (N0-e) H(lambda(e)), U = F1 u F2, x_j = deg_U(j) = 2L - t_j, sum_j t_j = 2T, 0 <= t_j <= L,
Lam = lambda_U(1-lambda_U), Q = Q(K_n - U) (unweighted signless Laplacian), v_j = -(1-lambda_U)(x_j - xbar).

(P0) Only the upper bound is needed.  E[P_L^2] >= (E P_L)^2 (Cauchy-Schwarz), so
     Var P_L/(E P_L)^2 -> 0 iff limsup E[P_L^2]/(E P_L)^2 <= 1.  Every nonpositive term in
     Delta(F1,F2) = log P(U c G) - log P(F1 c G) - log P(F2 c G) can be dropped.

(P1) Entropy, main part, exact.  Taylor at 2s with Lagrange remainder:
       psi(2s-T) - 2psi(s) + psi(0) = f(L) - T psi'(2s) + (T^2/2) psi''(xi),
     f(L) := psi(2s) - 2psi(s) + psi(0) deterministic, psi'(2s) = log lambda(2s) = log lambda(Ln),
     psi'' = -(1-lambda(e))/(lambda(e)(N0-e)) < 0.  So the T^2 term is <= 0: drop it.
     psi^(k) = O(n^{-2(k-1)}) on [0, Ln] (lambda(e) stays in [c/2, 1-c/2]), hence
       f(L) = -(1/lam - 1) L^2 n/(2(n-1)) + A L^3/n + O(L^4/n^2)          (A as in round 1)
     and -log lambda(Ln) = log(1/lam) + B L/n + O(L^2/n^2).

(P2) The quadratic -1/2 Lam^-1 v^T Q^-1 v is <= 0 (Q is positive definite): drop it.
     The delta-variance term -1/2 delta^T W_U^-1 delta of the cumulant part is <= 0: drop it.

(P3) The gamma^3 remainder, deterministic.  g(beta) = sum_{jk not in U} log(1+e^{b_j+b_k}) - beta.d
     has g(b1+gamma) = psi(|U|) - 1/2 Lam^-1 v^T Q^-1 v + R3 EXACTLY, with
       |R3| <= (1/6) sup|sigma''| sum_{jk not in U} |gamma_j+gamma_k|^3 = G3/(36 sqrt3).
     Bound on gamma = Lam^-1 Q^-1 v.  Q = Q0 - R, Q0 = (n-2)I + J, R = Q(U), ||R||_inf = 2 max x_j <= 4L.
     ||Q0^-1||_inf <= 3/(2(n-2)).  For n-2 >= 12L (true for L <= n^{1/2}/2, n >= 600):
     ||R Q0^-1||_inf <= 1/2, so ||Q^-1||_inf <= 3/(n-2).  Since sum v = 0, Q0^-1 v = v/(n-2), and
       Q^-1 v - v/(n-2) = Q0^-1 R Q^-1 v,   |.|_inf <= (3/(2(n-2))) 4L (3/(n-2)) ||v||_inf <= 18 L^2/(n-2)^2,
     using |v_j| <= |t_j - tbar| <= L.  So Lam|gamma_j| <= |t_j - tbar|/(n-2) + 18L^2/(n-2)^2 and
       G3 <= 4(n-1) sum_j |gamma_j|^3,   sum_j |t_j - tbar|^3 <= 4(sum t_j^3 + n tbar^3)
          <= 4(L^2 * 2T + 8T^3/n^2) <= 16 L^2 T            (t_j <= L, T <= Ln/2),
       G3 <= 16(n-1) Lam^-3 [16 L^2 T/(n-2)^3 + 18^3 n L^6/(n-2)^6] = O(L^2 T/n^2 + L^6/n^4).
     (Checked numerically above; the true G3 is far smaller, ~L^2/n^2, but the bound suffices.)

(P4) Conclusion of (R1).  With the determinant part <= C(L^2+T)/n and the cumulant part
     <= C(L^2/n + LT/n^2) (both from the lemma's own proof) and the O(1/n) IM25 errors:
       Delta(F1,F2) <= f(L) + beta_n T + eps_n,
       beta_n = -log lambda(Ln) + C(1/n + L^2/n^2),   eps_n = C(1 + L^2)/n + C L^6/n^4,
     uniformly over L-regular F1, F2, L <= n^{1/2}/2.  No LT/n or L^3/n error is left: the only
     LT/n piece is B L T/n inside -log lambda(Ln), which is exact.

(P5) Reduction (proved).  With y_n = e^{beta_n} = lam^-1 (1 + B L/n + O(1/n + L^2/n^2)),
       E[P_L^2]/(E P_L)^2 <= exp(f(L) + eps_n + O(L^2/n)) E_{nu_L x nu_L}[y_n^T].
     Write log E[y^T] = (y-1) k1 + (y-1)^2 k2/2 + Rtail(y), k1 = L^2 n/(2(n-1)) and k2 the exact
     second factorial cumulant (k2 = -L^3/n + L^2/n + O(L^4/n^2 + L^3/n^2)).  Then
       (y_n-1) k1 + (y_n-1)^2 k2/2 + f(L)
         = [A + B/(2 lam) - (1/lam-1)^2/2] L^3/n + O(L^2/n + L^4/n^2) = O(L^2/n + L^4/n^2),
     the L^2 terms cancelling exactly (both carry n/(n-1)).  Hence
       Var P_L/(E P_L)^2 <= exp(O(1/n + L^2/n + L^4/n^2 + L^6/n^4) + Rtail(y_n)) - 1.
     THEOREM (conditional only on (R2*)): if Rtail(y_n) <= o(1) on a range L = L_n <= n^{1/2}/2,
     L = o(n^{1/2}), then Var P_L/(E P_L)^2 -> 0 there.  (R1) is no longer an assumption.

(R2*)  [OPEN]  Rtail(y) = log E_{nu_L x nu_L}[y^T] - (y-1)k1 - (y-1)^2 k2/2 = o(1), uniformly
     for y within O(L/n) of 1/lam, L = o(n^{1/2}).  Equivalently: the factorial cumulants of
     T = |F1 n F2| beyond k = 2, summed with weights (y-1)^k/k!, are o(1).
     Evidence:
       k = 3 exactly: kappa3 is an explicit rational function of (n, L, t3), t3 = P(abc c F),
       for EVERY S_n-invariant L-regular law; brute-force equal on nu_L at n <= 8.  Leading order
         kappa3 = 5L^4/n^2 + n^3 (t3 - L^3/n^3)^2 + O(L^3/n^2 + L^5/n^3 + n^2 t3^2 + L^2 t3).
       So the k = 3 term is o(1) for L = o(n^{1/2}) PROVIDED t3 = O(L^3/n^3) (brute force:
       t3/((L)_3/(n-1)_3) = 3/4 at (6,3), 145/157 at (8,3)).  A clustered law with
       t3 ~ L^2/n^2 would give kappa3 ~ L^4/n, so this input is genuinely needed.
       Heuristic for all k: kappa_k = O_k(L^{k+1}/n^{k-1}) (binomial(Ln/2, L/n) has exactly this
       scale, and each extra linked edge costs n/L), which gives Rtail = O(L^4/n^2) -> 0.
     Not proved: the triangle density of nu_L at the L^3/n^3 scale, any bound on kappa_k, k >= 4,
     and summability of the tail.  Brute force at n <= 8 cannot test L-scaling.

(R2) as stated in prop:peel-cubic-cancels (O(L^{2k-1}/n^{k-1})) is weaker than the true k=3
     scale; with the corrected scale the method reaches L = o(n^{1/2}), not only o(n^{2/5}).

NEXT ORDER.  There is no L^5/n^2 term: none of psi, -log lambda(Ln), k2, k3 has an L^5/n^2
     monomial (sympy, part (3), with t3 = theta (L)_3/(n-1)_3 for any bounded theta).
     The next order is L^4/n^2.  Its coefficient from the computable pieces (psi s^4 term,
     T^2 psi'' at E_y[T^2], second-order tilt, k2's L^4/(2n^2), k3's 5L^4/n^2) is
       D4 = [7(l-1)(l^2+l+1)/12 + (l-1)/4 - 2(l-1) + (l-8)(l-1)^2/4 - 5(l-1)^3/6] / l^3 = 0
     identically in lambda: the L^4/n^2 order cancels as well, as the colouring heuristic
     (rem:no-l2n) predicts.  This is exact algebra given its inputs, not a theorem about R.
     Pieces not in D4: v^T Q^-1 v (~ L^2/n + L^3/n^2 heuristically: E sum (t_j - tbar)^2 ~ L^2),
     gamma^3 (~ L^2/n^2), determinant (L^2/n + L^3/n^2: tr M^k ~ L^k/n^{k-1}), cumulants
     (bounded only by L^2/n + LT/n^2 in the lemma; whether they carry an L^4/n^2 piece is
     NOT checked), kappa_k for k >= 4 (heuristically L^5/n^3).
     For L = o(n^{1/2}) every one of these orders is o(1) anyway; no cancellation at L^4/n^2 is
     needed for the theorem.  It would matter only past n^{1/2}, where the containment lemma
     itself (IM25 hypothesis ||d - lam g||_inf = O(n^{1/2})) no longer applies.
"""

L, n, lam, t, th, z = symbols('L n lambda t theta z', positive=True)
out = []
def say(s=''):
    print(s); out.append(s)

# =====================================================================================
# (1) (R1): gamma^3 remainder and v^T Q^-1 v
# =====================================================================================
say('(1) (R1) CLOSED: containment-ratio(b) upper bound with no LT/n or L^3/n error')
# Q0 = Q(K_n) = (n-2)I + J,  Q0^-1 = (I - J/(2(n-1)))/(n-2),  ||Q0^-1||_inf <= 3/(2(n-2))
for nn in (6, 8, 11):
    Q0 = (nn-2)*eye(nn) + ones(nn, nn)
    Q0i = (eye(nn) - ones(nn, nn)/(2*(nn-1)))/(nn-2)
    assert Q0*Q0i == eye(nn)
    assert max(sum(abs(Q0i[i, j]) for j in range(nn)) for i in range(nn)) <= Rational(3, 2)/(nn-2)
# sup |(d/dx)^3 log(1+e^x)| = sup |s(1-s)(1-2s)| = 1/(6 sqrt 3), attained at s = (3-sqrt3)/6
s_ = symbols('s')
g3 = s_*(1-s_)*(1-2*s_)
assert simplify(g3.subs(s_, (3-sqrt(3))/6) - 1/(6*sqrt(3))) == 0 and simplify(diff(g3, s_).subs(s_, (3-sqrt(3))/6)) == 0
# psi'' < 0: psi''(e) = -(1-lambda(e))/(lambda(e)(N0-e)) (checked in worker2_peel_cubic.py)
say('    sympy: Q0^-1 formula and ||Q0^-1||_inf <= 3/(2(n-2)) (n=6,8,11); sup|sigma\'\'| = 1/(6 sqrt3).')

def round_robin(nn):                     # the n-1 perfect matchings of the circle 1-factorization of K_n
    m = nn - 1
    return [[(r, nn-1)] + [((r+i) % m, (r-i) % m) for i in range(1, nn//2)] for r in range(m)]

def reg_graph(nn, LL, rng, rounds=None):
    rr = round_robin(nn)
    pick = rng.choice(nn-1, LL, replace=False) if rounds is None else rounds
    perm = rng.permutation(nn)
    A = np.zeros((nn, nn), bool)
    for r in pick:
        for a, b in rr[r]:
            A[perm[a], perm[b]] = A[perm[b], perm[a]] = True
    return A

def r1_check(A1, A2, D):
    nn = len(A1); LL = A1[0].sum()
    U = A1 | A2; x = U.sum(1).astype(float); tj = (A1 & A2).sum(1)
    T = int(tj.sum())//2; N0 = nn*(nn-1)/2; EU = U.sum()/2
    lU = (D*nn/2 - EU)/(N0 - EU); Lam = lU*(1-lU)
    v = -(1-lU)*(x - x.mean())
    comp = ~U & ~np.eye(nn, dtype=bool)                    # K_n - U
    Q = np.diag(comp.sum(1)).astype(float) + comp
    Qiv = np.linalg.solve(Q, v); gam = Qiv/Lam
    b = 0.5*np.log(lU/(1-lU)); d = D - x
    iu = np.triu_indices(nn, 1); keep = comp[iu]
    def gfun(beta):
        S = (beta[:, None] + beta[None, :])[iu][keep]
        return np.logaddexp(0, S).sum() - beta @ d
    psiU = (N0 - EU)*(-lU*np.log(lU) - (1-lU)*np.log(1-lU))
    assert abs(gfun(np.full(nn, b)) - psiU) < 1e-7*N0          # g(b1) = psi(|U|)
    quad = 0.5*(v @ Qiv)/Lam
    R3 = gfun(b + gam) - psiU + quad
    G3 = (np.abs(gam[:, None] + gam[None, :])[iu][keep]**3).sum()
    bound = 16*(nn-1)/Lam**3*(16*LL**2*T/(nn-2)**3 + 18**3*nn*LL**6/(nn-2)**6)
    assert abs(R3) <= G3/(36*math.sqrt(3)) + 1e-9 and G3 <= bound and quad >= 0
    return LL, T, R3, G3, G3/(LL**2*max(T, 1)/nn**2), quad, quad/(max((tj**2).sum(), 1)/nn)

rng = np.random.default_rng(1)
nn, D = 400, 160
say(f'    float check at n={nn}, D={D} (lambda={D/(nn-1):.4f}); F1, F2 = L random rounds of a relabelled')
say('    circle 1-factorization (any L-regular pair is allowed: the bound is deterministic).')
say('      L    T   R3=gamma^3 rem.  G3=sum|g_j+g_k|^3  G3/(L^2T/n^2)  (1/2)L^-1 vQ^-1v  ratio to sum t_j^2/n')
cases = [(LL, 0) for LL in (4, 7, 10)] + [(10, 20), (10, 100)]
for LL, k in cases:
    A1 = reg_graph(nn, LL, rng)
    if k:                                                 # F2 = F1 with k vertices relabelled: large T, uneven t_j
        perm = np.arange(nn); sub = rng.choice(nn, k, replace=False); perm[sub] = rng.permutation(sub)
        A2 = A1[np.ix_(perm, perm)]
    else: A2 = reg_graph(nn, LL, rng)
    r = r1_check(A1, A2, D)
    say(f'    {r[0]:3d} {r[1]:5d}   {r[2]: .3e}       {r[3]:.3e}         {r[4]:.3e}       {r[5]:.3e}        {r[6]:.3f}')
say('    all asserts pass: |R3| <= G3/(36 sqrt3), G3 <= explicit bound, vQ^-1v >= 0.')

# =====================================================================================
# (2) exact kappa3
# =====================================================================================
N0 = n*(n-1)/2
p1 = L/(n-1)
pP2 = L*(L-1)/((n-1)*(n-2))                       # cherry: neighbourhood is a uniform L-set
p2M = p1*(L*n/2 - 2*L + 1)/binomial(n-2, 2)        # edge count
pK13 = L*(L-1)*(L-2)/((n-1)*(n-2)*(n-3))
t3s = symbols('t3', positive=True)
pP3 = ((L-1)*pP2 - t3s)/(n-3)                      # degree at an end of a cherry
pP2e = (L*pP2 - 2*pP3 - pK13)/(n-4)                # degree at a vertex off a cherry
p3M = (L*p2M - 4*pP2e)/(n-5)                       # degree at a vertex off a 2-matching
assert simplify(2*pP3 + (n-4)*pP2e - (L-1)*p2M) == 0   # the remaining relation is implied
cnt = {'K3': binomial(n, 3), 'K13': n*binomial(n-1, 3), 'P3': n*(n-1)*(n-2)*(n-3)/2,
       'P2e': n*binomial(n-1, 2)*binomial(n-3, 2), '3M': ff(n, 6)/48}
pr = {'K3': t3s, 'K13': pK13, 'P3': pP3, 'P2e': pP2e, '3M': p3M}
assert all(sum(c.subs(n, k) for c in cnt.values()) == binomial(k*(k-1)//2, 3) for k in range(6, 14))
m1 = N0*p1**2
m2 = 2*(n*binomial(n-1, 2)*pP2**2 + ff(n, 4)/8*p2M**2)
m3 = 6*sum(cnt[k]*pr[k]**2 for k in cnt)
kappa2 = m2 - m1**2
kappa3 = m3 - 3*m2*m1 + 2*m1**3

def at_t(expr, order):
    r = cancel(expand_func(expr).subs(n, 1/t))
    return expand(series(r, t, 0, order+1).removeO())

t3_model = th*L*(L-1)*(L-2)/((n-1)*(n-2)*(n-3))    # theta = 1: 'independent colours' triangle density
k3ser = at_t(kappa3.subs(t3s, t3_model), 3)
say()
say('(2) (R2) at k=3: exact kappa3 for every S_n-invariant law of L-regular graphs')
say('    pi(shape) fixed by n, L, t3 = P(triangle in F); relation (iii) is implied (sympy).')
say(f'    kappa3 = {factor(k3ser.coeff(t, 2))} / n^2')
say(f'           + {factor(k3ser.coeff(t, 3))} / n^3 + ...   [t3 = theta (L)_3/(n-1)_3]')
say('    => kappa3 = 5 L^4/n^2 + O(L^3/n^2 + L^6/n^3): Theta(L^4/n^2), not L^5/n^2.')
lin = factor(at_t(diff(kappa3, t3s).subs(t3s, 0), 0))
quad = factor(at_t(diff(kappa3, t3s, 2)/2*t**3, 0))       # coefficient of t3^2, times n^-3
assert lin == -2*L*(L**2 - 3*L + 3) and quad == 1
say(f'    kappa3 is quadratic in t3: d/dt3 at 0 -> {lin},  (1/2) d^2/dt3^2 = n^3 (1 + O(1/n)).')
say('    Leading t3-dependence n^3 t3^2 - 2 L^3 t3 = n^3 (t3 - L^3/n^3)^2 - L^6/n^3, and the t3-free')
say('    part has +L^6/n^3: so kappa3 = 5L^4/n^2 + n^3 (t3 - L^3/n^3)^2 + lower order.')
say('    The k=3 term is o(1) for L = o(n^{1/2}) as soon as t3 = O(L^3/n^3).')

# ---------------- brute force over nu_L ----------------
def perfect_matchings(vs):
    if not vs: yield (); return
    a = vs[0]
    for i in range(1, len(vs)):
        for m in perfect_matchings(vs[1:i] + vs[i+1:]):
            yield ((a, vs[i]),) + m

def shape(es):
    deg = {}
    for a, b in es:
        deg[a] = deg.get(a, 0) + 1; deg[b] = deg.get(b, 0) + 1
    vs, ds = len(deg), sorted(deg.values())
    return {3: 'K3', 4: 'K13' if ds[-1] == 3 else 'P3', 5: 'P2e', 6: '3M'}[vs]

def brute(nn, LL):
    edges = list(itertools.combinations(range(nn), 2)); eid = {e: i for i, e in enumerate(edges)}
    pms = [sum(1 << eid[e] for e in m) for m in perfect_matchings(list(range(nn)))]
    w = {}
    def rec(k, union):
        if k == LL: w[union] = w.get(union, 0) + 1; return
        for m in pms:
            if not m & union: rec(k+1, union | m)
    rec(0, 0)
    masks = np.array(list(w), np.uint64); ws = np.array(list(w.values()), np.int64); Z = int(ws.sum())
    hist = {}
    for i in range(len(masks)):
        T = np.bitwise_count(masks[i] & masks).astype(np.int64)
        bc = np.bincount(T, weights=ws)                    # float64 exact here: totals < 2^53
        for tv in np.nonzero(bc)[0]:
            hist[int(tv)] = hist.get(int(tv), 0) + int(ws[i])*int(bc[tv])
    shp = {}
    for S in itertools.combinations(range(len(edges)), 3):
        mS = np.uint64(sum(1 << j for j in S))
        c = int(ws[(masks & mS) == mS].sum())
        shp.setdefault(shape([edges[j] for j in S]), set()).add(Fraction(c, Z))
    return hist, Z*Z, shp, len(masks)

def fact_moments(hist, Z2):
    return [sum(Fraction(c*math.perm(tv, k), Z2) for tv, c in hist.items()) for k in range(4)]

say()
say('    brute force over nu_L (exact rationals): every 3-edge shape has one probability (S_n),')
say('    equal to the formula at the observed t3; kappa2, kappa3 equal the closed forms.')
bf = {}
for nn, LL in [(6, 2), (6, 3), (8, 2), (8, 3)]:   # shortcut: (8,4) is ~10^6 ordered tuples; skipped, n=10 too
    hist, Z2, shp, nf = brute(nn, LL)
    assert all(len(v) == 1 for v in shp.values())
    pv = {k: next(iter(v)) for k, v in shp.items()}
    t3v = Rational(pv.get('K3', Fraction(0)).numerator, pv.get('K3', Fraction(1)).denominator)
    sub = {n: nn, L: LL, t3s: t3v}
    for k, v in pv.items():
        assert Rational(v.numerator, v.denominator) == pr[k].subs(sub), (nn, LL, k)
    fm = fact_moments(hist, Z2)
    k2b = fm[2] - fm[1]**2; k3b = fm[3] - 3*fm[2]*fm[1] + 2*fm[1]**3
    k2f, k3f = kappa2.subs(sub), kappa3.subs(sub)
    assert Rational(k2b.numerator, k2b.denominator) == k2f and Rational(k3b.numerator, k3b.denominator) == k3f
    thv = t3v/t3_model.subs({n: nn, L: LL, th: 1}) if LL >= 3 else None
    bf[(nn, LL)] = hist, Z2
    say(f'      n={nn} L={LL} ({nf} unions): t3 = {t3v}' + (f' (theta = {thv})' if thv is not None else ' (L=2: no triangles)')
        + f', kappa3 = {k3b} = formula  OK')

# =====================================================================================
# (3) series of the computable exponent
# =====================================================================================
H = lambda p: -p*log(p) - (1-p)*log(1-p)
h = (1-z)*H((lam-z)/(1-z))                       # psi(e) = N0 h(e/N0)
hd = [simplify(diff(h, z, k).subs(z, 0)) for k in range(6)]
sig = L/(n-1)
f_psi = N0*sum(hd[k]*(2**k - 2)*sig**k/math.factorial(k) for k in range(2, 6))   # psi(2s)-2psi(s)+psi(0)
w = (1-lam)/(lam - 2*sig)                        # y - 1,  y = 1/lambda(Ln)
lz = (lam - 2*sig)/(1 - 2*sig)
psi2 = -(1-lz)/(lz*N0*(1 - 2*sig))               # psi''(2s)
ww = symbols('ww')
def trunc(e, k=2):                                # drop t^j, j > k, of a polynomial in t
    e = expand(e); return sum(e.coeff(t, j)*t**j for j in range(k+1))
# each piece expanded to t^2 separately (series of the whole rational expression is too slow)
m1S, k2S, k3S = (at_t(x, 2) for x in (m1, kappa2, kappa3.subs(t3s, t3_model)))
wS, psi2S, fS = at_t(w, 2), at_t(psi2, 2), at_t(f_psi, 2)
K = m1S*ww + k2S*ww**2/2 + k3S*ww**3/6           # log E[(1+ww)^T], k <= 3
K1 = (1+ww)*diff(K, ww); K2 = (1+ww)*diff(K1, ww) # d/dbeta, d^2/dbeta^2
sub_w = lambda e: trunc(e.subs(ww, wS))
parts = {
    'psi 2nd diff': fS,
    'T^2 psi\'\'': trunc(psi2S/2*(sub_w(K2) + trunc(sub_w(K1)**2))),
    'kappa1 w (tilt)': sub_w(m1S*ww),
    'kappa2 w^2/2': sub_w(k2S*ww**2/2),
    'kappa3 w^3/6': sub_w(k3S*ww**3/6),
}
ser = expand(sum(parts.values()))
c0, c1, c2 = (expand(simplify(ser.coeff(t, j))) for j in range(3))
say()
say('(3) series of log E[P_L^2]/(E P_L)^2 from the computable pieces (psi, T^2 psi\'\', exact tilt,')
say('    kappa1..kappa3), n = 1/t, L symbolic:')
say(f'    t^0 : {factor(c0)}')
say(f'    t^1 : L^3 coeff = {factor(c1.coeff(L, 3))}   (cubic cancellation, reproduced)')
say(f'          L^2 coeff = {factor(c1.coeff(L, 2))}   [incomplete: det/cumulant parts also O(L^2/n)]')
assert c0 == 0 and simplify(c1.coeff(L, 3)) == 0 and c1.coeff(L, 4) == 0
assert all(simplify(c2.coeff(L, k)) == 0 for k in range(5, 9))
D4 = factor(simplify(c2.coeff(L, 4)))
say(f'    t^2 : L^5..L^8 coeffs = 0 (no L^5/n^2 term)')
say(f'          L^4 coeff  D4 = {D4}')
say(f'          D4 at lambda=1/2: {simplify(D4.subs(lam, Rational(1, 2)))},  lambda=1/3: {simplify(D4.subs(lam, Rational(1, 3)))}')
tot = 0
for k, ex in parts.items():
    cc = factor(simplify(expand(ex).coeff(t, 2).coeff(L, 4)))
    tot += cc
    say(f'            {k:16s}: {cc}')
assert simplify(tot - D4) == 0
say('    D4 = 0 identically: the L^4/n^2 order cancels too.' if D4 == 0 else
    '    D4 != 0: the L^4/n^2 order does not cancel among these pieces.')

# n <= 8 brute force: the k>=3 tail R3+(y) = log E y^T - (y-1)k1 - (y-1)^2 k2/2 at y = 2 (lambda=1/2)
say()
say('    n<=8 brute force, y=2: tail log E[y^T] - w k1 - w^2 k2/2  vs  w^3 kappa3/6 (w=1):')
for (nn, LL), (hist, Z2) in bf.items():
    fm = fact_moments(hist, Z2)
    EY = sum(Fraction(c*2**tv, Z2) for tv, c in hist.items())
    k1v, k2v, k3v = fm[1], fm[2]-fm[1]**2, fm[3]-3*fm[2]*fm[1]+2*fm[1]**3
    tail = math.log(EY) - float(k1v) - float(k2v)/2
    say(f'      n={nn} L={LL}: tail = {tail:+.5f},  kappa3/6 = {float(k3v)/6:+.5f}')

say(PROOF)
Path('v2/notes/r2_worker2_peel.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('\nwrote v2/notes/r2_worker2_peel.txt')
