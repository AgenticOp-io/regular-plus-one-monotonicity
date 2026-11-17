"""r8w2: exact law of T=|F1&F2| (F1,F2 iid nu_L, small n) -> zeros of P(y)=E y^T, Cauchy-radius test of (B*).
Cauchy: |kappa_k|/k! <= M/R^k, R=dist(1, zeros). (B*) <=> R >= n/(C L), M ~ nL.  Run: python r8w2_zeros.py n L"""
import sys, itertools, numpy as np
n, L = map(int, sys.argv[1:3])
E = list(itertools.combinations(range(n), 2)); eid = {e: i for i, e in enumerate(E)}
def pms(vs):
    if not vs: yield 0; return
    a = vs[0]
    for i in range(1, len(vs)):
        for m in pms(vs[1:i] + vs[i+1:]): yield m | (1 << eid[(a, vs[i])])
pm = np.array(sorted(pms(list(range(n)))), dtype=np.uint64)
parts = [(int(m), i) for i, m in enumerate(pm)]
for _ in range(L-1):
    parts = [(m | int(pm[j]), j) for m, i in parts for j in i+1+np.nonzero((pm[i+1:] & np.uint64(m)) == 0)[0]]
masks = np.array([m for m, _ in parts], dtype=np.uint64); N = len(masks)
h = np.zeros(n*L//2+1)
# symmetry: F1 uniform = (M1 canonical) + (L-1) more disjoint PMs, equidistributed over orbits; F2 over all N sets
i1 = [i for i in range(len(pm)) if all(((int(pm[i])>>eid[(2*j,2*j+1)])&1) for j in range(n//2))][0]
ext = [(int(pm[i1]), -1)]  # sets {M1} + (L-1) other PMs, indices increasing (M1 excluded)
for _ in range(L-1):
    ext = [(m | int(pm[j]), j) for m, i in ext for j in range(i+1, len(pm)) if j != i1 and (int(pm[j]) & m) == 0]
F1 = np.array([m for m, _ in ext], dtype=np.uint64)
for a in range(0, len(F1), 200):
    c = np.bitwise_count(F1[a:a+200, None] & masks[None, :]); h += np.bincount(c.ravel(), minlength=len(h))
p = h/h.sum(); mu = (p*np.arange(len(p))).sum()
assert abs(mu - n*(n-1)/2*(L/(n-1))**2) < 1e-9, mu
z = np.roots(p[::-1]); d = np.abs(z-1)
# cumulants from the zeros: kappa_k/k! = -(1/k) sum_j (1/(1-z_j))^k * (-1)^? ; just report radius
R = d.min(); print(f"n={n} L={L} N={N} mu={mu:.4f} nearest-zero dist R={R:.4f} at {z[d.argmin()]:.4f}  n/L={n/L:.3f}  R*L/n={R*L/n:.4f}  deg={len(p)-1}")
