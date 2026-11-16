"""r7: exact factorial cumulants kappa_1..K of T=|F1 cap F2| for F1,F2 iid nu_L (small n, brute force).
m_k=E(T)_k = k! sum_{|S|=k} p_S^2 ; log sum m_k w^k/k! = sum kappa_k w^k/k!.  Exact Fractions.
Run: python v2/scripts/r7_kappa_exact.py n L K"""
import sys, itertools, numpy as np, networkx as nx
from fractions import Fraction as Fr
from math import factorial, comb
n, L, K = map(int, sys.argv[1:4])
E = list(itertools.combinations(range(n), 2)); eid = {e: i for i, e in enumerate(E)}
def pms(vs):
    if not vs: yield 0; return
    a = vs[0]
    for i in range(1, len(vs)):
        for m in pms(vs[1:i] + vs[i+1:]): yield m | (1 << eid[(a, vs[i])])
pm = np.array(sorted(pms(list(range(n)))), dtype=np.uint64)
parts = [(int(m), i) for i, m in enumerate(pm)]
for _ in range(L-1):
    nxt = []
    for m, i in parts:
        for j in np.nonzero((pm[i+1:] & np.uint64(m)) == 0)[0]: nxt.append((m | int(pm[i+1+j]), i+1+j))
    parts = nxt
masks = np.array([m for m, _ in parts], dtype=np.uint64); N = len(masks)
print(f"n={n} L={L}: PMs={len(pm)}, unordered disjoint L-sets={N}")
# classes of k-edge subgraphs
mk = []
for k in range(1, K+1):
    classes = []  # (rep mask, graph, copies)
    buckets = {}
    for S in itertools.combinations(range(len(E)), k):
        g = nx.Graph([E[i] for i in S]); h = nx.weisfeiler_lehman_graph_hash(g, iterations=3)
        for c in buckets.setdefault(h, []):
            if nx.is_isomorphic(c[1], g): c[2] += 1; break
        else: buckets[h].append([sum(1 << i for i in S), g, 1]) if h in buckets else None
    tot = Fr(0)
    for b in buckets.values():
        for rep, g, cp in b:
            r = np.uint64(rep); c = int(np.count_nonzero((masks & r) == r)); tot += cp * Fr(c, N)**2
    mk.append(factorial(k) * tot)
# formal log: a_k = m_k/k! ; log(1+sum a_k w^k) coefficients c_k ; kappa_k = k! c_k
a = [Fr(1)] + [mk[k-1] / factorial(k) for k in range(1, K+1)]
c = [Fr(0)] * (K+1)
for k in range(1, K+1):  # c_k = a_k - (1/k) sum_{j=1}^{k-1} j c_j a_{k-j}
    c[k] = a[k] - sum(j * c[j] * a[k-j] for j in range(1, k)) / k
for k in range(1, K+1):
    kap = factorial(k) * c[k]; print(f" kappa_{k} = {float(kap):.8g}", f" L^(k+1)/n^(k-1) = {L**(k+1)/n**(k-1):.5g}", f" ratio/k! = {float(kap)/L**(k+1)*n**(k-1)/factorial(k):.4g}" if k > 1 else "")
