"""r10w1: exact Delta log E e^{-c T} between two 3-regular H on n=10 (p=1/2), vs cycle-leading series sum_k (-2cpq)^k Delta c_k(H)(?)/k!*k! .
Sign: log E e^{-cT} = sum (-c)^k kappa_k/k!, so cycle part = sum_k (-2cpq)^k Dc_k."""
import numpy as np, math
from r10w1_cum import graphs, feats
n, d, p = 10, 3, 0.5
gs = graphs(n, d, 300); fs = sorted(gs)
lo, hi = fs[0], fs[-1]
def logmgf(G, c):
    H = list(G.edges()); m = len(H); ms = np.arange(1 << m)
    r = np.zeros((1 << m, n)); k = np.zeros(1 << m)
    for i, (a, b) in enumerate(H):
        bit = (ms >> i) & 1; r[:, a] += bit; r[:, b] += bit; k += bit
    T = (r*r).sum(1); lw = k*math.log(p) + (m-k)*math.log(1-p)
    x = lw - c*T; mx = x.max(); return mx + math.log(np.exp(x-mx).sum())
print("feats lo/hi (t,c4,c5,dia,K4):", lo, hi)
for c in [0.05, 0.1, 0.2, 0.3, 0.5]:
    exact = logmgf(gs[hi], c) - logmgf(gs[lo], c)
    lead = sum((-2*c*p*(1-p))**k * (hi[k-3]-lo[k-3]) for k in (3, 4, 5))
    print(f"c={c}: exact Dlog={exact:.6g}  cycle-leading(k=3..5)={lead:.6g}")
