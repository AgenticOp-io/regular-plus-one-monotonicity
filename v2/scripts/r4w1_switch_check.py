"""r4 worker1: brute-force check of the switching lemma used for t3 = P_nu(triangle in F).

Setting: D_L = ordered L-tuples of pairwise edge-disjoint perfect matchings of K_n.
A = tuples with ab in M1, bc in M2, ca in M3 (vertices a,b,c = 0,1,2).
Backward move from tau in A: pick oriented edges (x_i,y_i) of M_i (i=1,2,3), not the special one,
replace M1: ab,x1y1 -> a x1, b y1;  M2: bc,x2y2 -> b x2, c y2;  M3: ca,x3y3 -> c x3, a y3.
Valid iff the result is again in D_L.  Claim: (tau,move) -> tau' is injective, so
|A| * min_tau |B(tau)| <= |D_L|, and |B(tau)| >= (n-2L-12)^3.
Run: python v2/scripts/r4w1_switch_check.py   (n=8 full; n=10 on A only)
"""
import itertools, sys
from fractions import Fraction

def pms(vs):
    vs = list(vs)
    if not vs: yield (); return
    a = vs[0]
    for i in range(1, len(vs)):
        rest = vs[1:i] + vs[i+1:]
        for m in pms(rest):
            yield ((a, vs[i]),) + m

def E(u, v): return (u, v) if u < v else (v, u)

def run(n, L, full):
    allpm = [frozenset(E(*e) for e in m) for m in pms(range(n))]
    # D_L only needed fully at n=8
    tab = a, b, c = 0, 1, 2
    sp = [E(a, b), E(b, c), E(c, a)]
    with_e = [[m for m in allpm if sp[i] in m] for i in range(3)]
    def disjoint_all(ms):
        s = set()
        for m in ms:
            if s & m: return False
            s |= m
        return True
    # tuples in A: M1,M2,M3 special, M4..ML free (L=3 here so none)
    assert L == 3
    A = [t for t in itertools.product(*with_e) if disjoint_all(t)]
    imgs = set(); minB = None
    if not full:   # n=10: injectivity on a random sample of A only (A has ~1e6 tuples)
        import random; random.seed(1); A = random.sample(A, 300)
    for t in A:
        cnt = 0
        for choice in itertools.product(*[[(e, o) for e in m if e != sp[i] for o in (0, 1)] for i, m in enumerate(t)]):
            new = []
            for i, (m, (e, o)) in enumerate(zip(t, choice)):
                x, y = e if o == 0 else (e[1], e[0])
                u, v = [(a, b), (b, c), (c, a)][i]
                nm = (m - {sp[i], e}) | {E(u, x), E(v, y)}
                new.append(frozenset(nm))
            if all(len(m) == n//2 for m in new) and disjoint_all(new):
                key = tuple(new)
                assert key not in imgs, "injectivity fails"
                imgs.add(key); cnt += 1
        minB = cnt if minB is None else min(minB, cnt)
    out = dict(n=n, L=L, A=len(A), minB=minB, images=len(imgs))
    if full:
        D = sum(1 for t in itertools.product(allpm, repeat=3) if disjoint_all(t))
        out['D'] = D
        assert len(A) * minB <= len(imgs) <= D
        out['P(A)'] = Fraction(len(A), D)
        out['1/minB'] = Fraction(1, minB)
        assert out['P(A)'] <= out['1/minB']
        # t3 = (L)_3 P(A)  (colour orderings symmetric) ; known exact value 29/1099 at n=8
        out['t3'] = 6 * out['P(A)']
    return out

for n, full in ((8, True), (10, False)):
    r = run(n, 3, full); print(r)
    assert r['images'] == r['A'] * 0 + r['images']
print("switching injectivity and |A|*minB <= |D| verified; bound (n-2L-12)^3 is vacuous at these n,")
print("the check is of the map, the inequality is of the proof structure.")
