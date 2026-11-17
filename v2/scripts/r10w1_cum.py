"""r10w1: exact cumulants k2..k5 of host statistics over X~G(H,p), H d-regular, vs subgraph counts of H.
Stats: S=a*k+2*P2 (host sum of squares), F=W^2-Q (r6 pairing-mean Lambda up to 1/(2(M-1))), C3=sum h^3.
Fit: kappa_j = lin comb of {1,t,c4,c5,diamond,K4,...}(H); exact rational least squares; report residual."""
import sys, itertools, random
import numpy as np, networkx as nx, sympy as sp
from fractions import Fraction as Fr

def hist(n, H, stat):
    m = len(H); masks = np.arange(1 << m, dtype=np.int64)
    rho = np.zeros((1 << m, n), dtype=np.int64); k = np.zeros(1 << m, dtype=np.int64)
    for i, (a, b) in enumerate(H):
        bit = (masks >> i) & 1; rho[:, a] += bit; rho[:, b] += bit; k += bit
    v = stat(rho, k)
    key = v * 64 + k
    u, c = np.unique(key, return_counts=True)
    return u, c, m

def cums(u, c, m, p, kmax=5):
    p = Fr(p); q = 1 - p
    vals = u // 64; ks = u % 64
    w = {}
    for v, k, cc in zip(vals.tolist(), ks.tolist(), c.tolist()):
        w[v] = w.get(v, 0) + cc * p**k * q**(m-k)
    mu = sum(v*x for v, x in w.items())
    cm = {j: sum((v-mu)**j * x for v, x in w.items()) for j in range(2, kmax+1)}
    k = {2: cm[2], 3: cm[3], 4: cm[4]-3*cm[2]**2, 5: cm[5]-10*cm[3]*cm[2]}
    return k

def feats(G):
    A = nx.to_numpy_array(G, dtype=np.int64); n = len(A)
    A2 = A@A; t = int(np.trace(A@A2))//6
    # c4: closed 4-walks minus degenerate
    d = A.sum(1); c4 = (int(np.trace(A2@A2)) - int((d*d).sum()*2 - d.sum()))//8
    # diamonds: pairs of triangles sharing an edge = sum over edges C(common,2)
    dia = sum(int(A2[a, b])*(int(A2[a, b])-1)//2 for a, b in G.edges())
    k4 = sum(1 for q in itertools.combinations(range(n), 4) if all(A[x, y] for x, y in itertools.combinations(q, 2)))
    c5 = sum(1 for cyc in nx.simple_cycles(G, length_bound=5) if len(cyc) == 5)
    return (t, c4, c5, dia, k4)

def graphs(n, d, num, seed=0):
    rng = random.Random(seed); out = {}
    for _ in range(num):
        G = nx.random_regular_graph(d, n, seed=rng.randrange(10**9))
        out.setdefault(feats(G), G)
    return out

if __name__ == "__main__":
    n, d, p = int(sys.argv[1]), int(sys.argv[2]), Fr(sys.argv[3])
    D = n-1-d; w1 = 2+4*D
    hb = D + d*p
    stats = {
     "S": lambda r, k: w1*k + (r*(r-1)).sum(1),            # = w1 k + 2 P2
     "T": lambda r, k: 2*k + (r*(r-1)).sum(1),
     "C3": lambda r, k: ((D+r)**3).sum(1),
    }
    # F needs hbar rational: scale by den
    den = hb.denominator
    def Fst(r, k):
        h = D + r; y = h*den - int(hb*den)    # den*y
        W = (h*y).sum(1); Q = (h*y*y).sum(1)
        return W*W - Q*den                    # = den^2 (W_true^2 - Q_true)
    stats["F"] = Fst
    gs = graphs(n, d, int(sys.argv[4]) if len(sys.argv) > 4 else 60)
    rows = []
    for f, G in gs.items():
        H = list(G.edges())
        r = {}
        for nm, st in stats.items():
            u, c, m = hist(n, H, st); r[nm] = cums(u, c, m, p)
        rows.append((f, r))
    print("n,d,p", n, d, p, "#graphs(distinct feats)", len(rows))
    names = ["t", "c4", "c5", "dia", "K4"]
    for nm in stats:
        for j in (2, 3, 4, 5):
            Mx = sp.Matrix([[1] + [sp.Rational(x) for x in f] for f, _ in rows])
            ys = sp.Matrix([sp.Rational(r[nm][j].numerator, r[nm][j].denominator) for _, r in rows])
            # drop constant-feature columns
            cols = [0] + [i+1 for i in range(5) if len({f[i] for f, _ in rows}) > 1]
            M2 = Mx[:, cols]
            piv = M2.rref()[1]; cols = [cols[i] for i in piv]; M2 = Mx[:, cols]   # independent columns only
            sol = (M2.T*M2).LUsolve(M2.T*ys)
            res = (M2*sol - ys); ok = all(x == 0 for x in res)
            print(nm, "k%d" % j, "exact-fit" if ok else "NOT-fit(max res %.3g)" % float(max(abs(x) for x in res)),
                  {(["1"]+names)[c]: str(sol[i]) for i, c in enumerate(cols)} if ok else "")
