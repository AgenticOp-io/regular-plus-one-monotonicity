"""
worker2_peel_cubic.py -- exact L^3/n coefficients for the peel second moment.

Second-moment ratio (proof of thm:peel-second-moment-third):
    log R = log E_{nu_L x nu_L}[ exp(Delta(F1,F2)) ] ,
    Delta = log P(F1 u F2 in G) - log P(F1 in G) - log P(F2 in G).

(1) lem:containment-ratio(b).  The only pieces of order L^3/n or LT/n in Delta are
    in the entropy psi(e) = (N0-e) H(lambda(e)), lambda(e) = (lam N0 - e)/(N0 - e):
        Delta_psi(T) = psi(2s-T) - 2 psi(s) + psi(0),  s = Ln/2.
    Expanding: Delta_psi = T log(1/lam) - L^2(1/lam-1)/2 + A L^3/n + B L T/n + ...
    with A = s^3 psi'''(0) * n/L^3 and B from -psi'(2s) = -log lambda(2s).
    (The determinant and cumulant parts are O((L^2+T)/n + LT/n^2) by the lemma;
    the v^T Q^{-1} v and gamma^3 pieces are O(sum t_j^2 / n), whose overlap average
    is O(L^2/n + L^4/n^2).)
(2) lem:decomp-overlap.  log E[x^T] = (x-1) N0 p1^2 + (x-1)^2 kappa2/2 + ...
    with p1 = L/(n-1) and kappa2 = E[T(T-1)] - (E T)^2 the 2nd factorial cumulant.
    kappa2 depends only on L-regularity + S_n invariance (adjacent and disjoint
    pair probabilities are forced), so it is exact in closed form; it is checked
    against brute-force enumeration of nu_L at small n.  Then C(x) = lim n kappa2/L^3 * (x-1)^2/2.
(3) Combination: cubic coefficient of log R =
        A + (1/2) * d(x-1)/d(L/n) [tilt from B] + C(1/lam).

Run:  python v2/scripts/residual/worker2_peel_cubic.py
Writes v2/notes/worker2_peel_cubic.txt.
"""
import itertools
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
from sympy import Rational, Symbol, cancel, diff, expand, factor, factorial, log, simplify, symbols

L, lam, n, e, x = symbols('L lambda n e x', positive=True)
out = []
def say(s=''):
    print(s); out.append(s)

# ---------------- (1) containment-ratio side ----------------
N0 = n*(n-1)/2
lam_e = (lam*N0 - e)/(N0 - e)
H = lambda p: -p*log(p) - (1-p)*log(1-p)
psi = (N0 - e)*H(lam_e)
t = Symbol('t', positive=True)                             # t = 1/n
def at0(expr, order=0):                                    # Taylor coeff of a rational fn of n at t=1/n -> 0
    r = cancel(expr.subs(n, 1/t))
    return cancel(diff(r, t, order).subs(t, 0)/factorial(order))
# psi' = log lambda(e) and psi'' = -(1-lam_e)/(lam_e (N0-e)): checked at random rational points
d2c = -(1-lam_e)/(lam_e*(N0-e))
for pt in [{n: 40, lam: Rational(3, 10), e: 17}, {n: 101, lam: Rational(5, 9), e: 333}]:
    assert abs((diff(psi, e) - log(lam_e)).subs(pt).evalf(40)) < 1e-30
    assert abs((diff(psi, e, 2) - d2c).subs(pt).evalf(40)) < 1e-30
d3_0 = cancel(diff(d2c, e).subs(e, 0))
assert cancel(d3_0 + (1-lam**2)/(lam**2*N0**2)) == 0       # psi'''(0) = -(1-lam^2)/(lam^2 N0^2)
s = L*n/2
A = at0(s**3*d3_0*n/L**3)                                  # second difference of s^3 term: (8-2)/6 = 1
k2 = at0(s**2*d2c.subs(e, 0)/L**2)
u = cancel(lam_e.subs(e, 2*s)/lam - 1)                     # -log lambda(2s) = log(1/lam) - log(1+u)
B = factor(-at0(u, 1)/L)
say('(1) lem:containment-ratio(b), entropy part:')
say(f'    L^2 coefficient  = {k2}   (paper: -(1/lam-1)/2)')
say(f'    A  (L^3/n)       = {A}   = -(1-lam^2)/(2 lam^2)')
say(f'    B  (L T/n)       = {B}   i.e. effective log x = log(1/lam) + B L/n')

# numeric check of A and B with the exact psi at large n (mpmath, 60 digits)
mp.mp.dps = 60
def psi_num(ev, nn, ll):
    N = mp.mpf(nn)*(nn-1)/2; le = (ll*N - ev)/(N - ev)
    return (N - ev)*(-le*mp.log(le) - (1-le)*mp.log(1-le))
for nn, LL, ll in [(10**6, 40, mp.mpf('0.3')), (10**7, 200, mp.mpf('0.55'))]:
    sv = mp.mpf(LL)*nn/2
    dpsi = psi_num(2*sv, nn, ll) - 2*psi_num(sv, nn, ll) + psi_num(0, nn, ll)
    pred = -mp.mpf(LL)**2*(1/ll-1)/2*nn/(nn-1) - (1-ll**2)/(2*ll**2)*mp.mpf(LL)**3/nn
    resid = (dpsi - pred)/(mp.mpf(LL)**3/nn)
    say(f'    numeric n={nn} L={LL} lam={ll}: (Delta_psi - pred)/(L^3/n) = {mp.nstr(resid, 6)}  (-> 0 as L/n -> 0)')
    assert abs(resid) < 1e-3
    Tv = 7
    dT = (psi_num(2*sv-Tv, nn, ll) - psi_num(2*sv, nn, ll))/Tv - mp.log(1/ll)
    say(f'      per-T slope minus log(1/lam), times n/L = {mp.nstr(dT*nn/LL, 8)}  vs B = {mp.nstr(2*(1-ll)/ll, 8)}')
    assert abs(dT*nn/LL - 2*(1-ll)/ll) < 1e-3

# ---------------- (2) decomp-overlap side ----------------
p1 = L/(n-1)
P_adj = p1*(L-1)/(n-2)
q_dis = p1*(L*n/2 - 2*L + 1)/(N0 - 2*n + 3)
kappa2 = 2*N0*(n-2)*(P_adj**2 - p1**4) + N0*(N0 - 2*n + 3)*(q_dis**2 - p1**4) - N0*p1**4
kap_series = expand(at0(kappa2, 1)*t + at0(kappa2, 2)*t**2).subs(t, 1/n)
assert at0(kappa2) == 0
cub = lambda ex: expand(at0(ex*n)).coeff(L, 3)                # exact coefficient of L^3/n
lead = cub(kappa2)
adj_part = cub(2*N0*(n-2)*(P_adj**2 - p1**4))
dis_part = cub(N0*(N0-2*n+3)*(q_dis**2 - p1**4))
assert expand(at0(kappa2*n)) == -L**3 + L**2           # n kappa2 -> -L^3 + L^2
say()
say('(2) lem:decomp-overlap, second factorial cumulant of T (exact for any S_n-invariant L-regular law):')
say(f'    kappa2 = (adjacent pairs) + (disjoint pairs) - N0 p1^4')
say(f'    kappa2 to O(1/n): {kap_series}')
say(f'    L^3/n coefficient of kappa2: adjacent {adj_part} + disjoint {dis_part} = {lead}  (the +L^2/n piece is below cubic order)')
C = lead*(x-1)**2/2
say(f'    => log E[x^T] = (x-1) L^2 n/(2(n-1)) + C(x) L^3/n + ...,  C(x) = {C}')

# brute force: enumerate nu_L exactly, compare E T and kappa2 with the closed forms
def perfect_matchings(vs):
    if not vs: yield (); return
    a = vs[0]
    for i in range(1, len(vs)):
        rest = vs[1:i] + vs[i+1:]
        for m in perfect_matchings(rest):
            yield ((a, vs[i]),) + m
def popcount(a):
    a = a.astype(np.uint64); c = np.zeros(a.shape, np.int64)
    while a.any():
        c += (a & np.uint64(1)).astype(np.int64); a >>= np.uint64(1)
    return c
def brute(nn, LL):
    eid = {pr: i for i, pr in enumerate(itertools.combinations(range(nn), 2))}
    pms = [sum(1 << eid[ed] for ed in m) for m in perfect_matchings(list(range(nn)))]
    w = {}
    def rec(k, union):
        if k == LL: w[union] = w.get(union, 0) + 1; return
        for m in pms:
            if not m & union: rec(k+1, union | m)
    rec(0, 0)
    masks = np.array(list(w), dtype=np.uint64); ws = np.array(list(w.values()), dtype=np.int64)
    Z = int(ws.sum()); S1 = S2 = 0
    for i in range(len(masks)):
        T = popcount(masks[i] & masks)
        S1 += int(ws[i]) * int((ws*T).sum()); S2 += int(ws[i]) * int((ws*T*(T-1)).sum())
    ET = Fraction(S1, Z*Z); ETT = Fraction(S2, Z*Z)
    return ET, ETT - ET**2, len(masks)
say()
say('    brute force over nu_L (exact rationals):')
for nn, LL in [(6, 2), (6, 3), (8, 2), (8, 3)]:   # shortcut: n=10 is ~2e5 unions, O(N^2) pairs too slow here
    ET, k2b, nf = brute(nn, LL)
    ETf = Rational(nn*(nn-1), 2)*Rational(LL, nn-1)**2
    k2f = kappa2.subs({n: nn, L: LL})
    ok = (Rational(ET.numerator, ET.denominator) == ETf) and (Rational(k2b.numerator, k2b.denominator) == k2f)
    say(f'      n={nn} L={LL} ({nf} unions): E T = {ET} (formula {ETf}),  kappa2 = {k2b} (formula {k2f})  {"OK" if ok else "MISMATCH"}')
    assert ok

# ---------------- (3) combination in the second-moment ratio ----------------
tilt = Rational(1, 2)*diff((1/lam)*(1 + B*t) - 1, t)   # L^2/2 * extra (x-1) per unit L/n
total = simplify(A + tilt + C.subs(x, 1/lam))
say()
say('(3) cubic (L^3/n) coefficient of log E[P_L^2]/(E P_L)^2:')
say(f'    A (containment)            = {simplify(A)}')
say(f'    tilt of x by B             = {simplify(tilt)}')
say(f'    C(1/lam) (decomp-overlap)  = {simplify(C.subs(x, 1/lam))}')
say(f'    total                      = {total}')
assert total == 0
say('    => CANCELS identically in lambda.')
say()
say('STATUS')
say(' exact (sympy, plus checks): A, B from psi; kappa2 closed form (brute-force-equal on nu_L, n<=8, L<=3);')
say('   C(x) = -(x-1)^2/2; total cubic = 0.  The old D2 = (7-6/lam-1/lam^2)L^3/n was a toy model')
say('   (degree-homogeneous McKay exponent), not either lemma; discard it.')
say(' NOT proven (needed to turn cancellation into a theorem past n^{1/3}):')
say('  - lem:containment-ratio bounds the gamma^3 remainder and v^T Q^-1 v only by LT/n, L^3/n;')
say('    their true size is O(sum_j t_j^2/n) whose overlap average is O(L^2/n + L^4/n^2) -- estimate, not proved.')
say('  - decomp-overlap: factorial cumulants k>=3 assumed O(L^{2k-1}/n^{k-1}) (k=3: L^5/n^2); heuristic.')
say('  - det/cumulant parts taken from the lemma (O((L^2+T)/n + LT/n^2)), no cubic term.')
say(' Next barrier if the above holds: L^5/n^2 (k=3 cluster) -> L = o(n^{2/5}); L^4/n^2 terms fine to n^{1/2}.')

Path('v2/notes/worker2_peel_cubic.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('\nwrote v2/notes/worker2_peel_cubic.txt')
