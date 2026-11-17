"""r9w1: fit kappa3(S) coefficients over d-regular complement graphs H: kappa3 = A(n,d) + B(d)*t(H) + C(d)*c4(H); exact (rational) linear algebra.
Output: B, C as polynomials in p and w1, per d; then polynomial in d."""
import random, itertools, sys, pickle
import sympy as sp
from r9w1_k3 import kappa3_poly, counts, comp_edges
p, w, d_ = sp.symbols("p w1 d")
random.seed(1)
def rand_regular(n, d, swaps=200):
    E = {frozenset((i, (i+s) % n)) for i in range(n) for s in range(1, d//2+1)}
    if d % 2: E |= {frozenset((i, i+n//2)) for i in range(n//2)}
    E = set(E)
    for _ in range(swaps):
        a, b = random.sample(sorted(map(sorted, E)), 2)
        if random.random() < .5: c, dd = (a[0], b[1]), (b[0], a[1])
        else: c, dd = (a[0], b[0]), (a[1], b[1])
        e1, e2 = frozenset(c), frozenset(dd)
        if len(e1) == 2 and len(e2) == 2 and e1 not in E and e2 not in E and e1 != e2:
            E -= {frozenset(a), frozenset(b)}; E |= {e1, e2}
    return [tuple(sorted(e)) for e in E]
def kap(n, Hedges):
    G0 = comp_edges(n, Hedges)   # G0 = complement of H; kappa3 uses complement of G0 = H
    out = kappa3_poly(n, G0)
    return sum(w**j*2**(3-j)*sum(c*p**e for e, c in P.items()) for j, P in out.items())
def fit(n, d, ns=5):
    rows = []; seen = set()
    tries = 0
    while len(rows) < ns and tries < 60:
        tries += 1; H = rand_regular(n, d); G0 = comp_edges(n, H)
        # counts of H itself
        t, c4 = counts(n, H)
        if (t, c4) in seen: continue
        seen.add((t, c4)); rows.append((t, c4, kap(n, H)))
    M = sp.Matrix([[1, t, c] for t, c, _ in rows]); b = sp.Matrix([sp.expand(k) for *_, k in rows])
    sol = (M.T*M).LUsolve(M.T*b)
    res = sp.simplify((M*sol-b).applyfunc(sp.expand))
    assert all(x == 0 for x in res), "residual nonzero: kappa3 not affine in (t,c4)"
    return [sp.factor(sp.expand(s)) for s in sol], len(rows), sorted(seen)
if __name__ == "__main__":
    n = int(sys.argv[1]); ds = [int(x) for x in sys.argv[2:]]
    for d in ds:
        s, k, seen = fit(n, d)
        print(f"n={n} d={d} rows={k} (t,c4)={seen}\n  B(t-coef)={s[1]}\n  C(c4-coef)={s[2]}", flush=True)
