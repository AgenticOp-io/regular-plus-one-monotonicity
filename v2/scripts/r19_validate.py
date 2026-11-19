# independent brute-force check of r5w3_exact.contains for D=3 (labelled cubic graphs, n=6,8)
import sys, os, itertools
sys.path.insert(0, os.path.dirname(__file__))
from r5w3_exact import make, contains, Nseq
D = 3; N = make(D)
def cubic(n):
    E = list(itertools.combinations(range(n), 2)); deg = [0]*n; cur = []
    def rec(i):
        if i == len(E):
            if all(d == D for d in deg): yield tuple(cur)
            return
        if len(E) - i < sum(D - d for d in deg) // 2: return
        a, b = E[i]
        if deg[a] < D and deg[b] < D:
            deg[a] += 1; deg[b] += 1; cur.append(E[i]); yield from rec(i+1); cur.pop(); deg[a] -= 1; deg[b] -= 1
        yield from rec(i+1)
    return [set(g) for g in rec(0)]
P = lambda k: [(i, i+1) for i in range(k)]
S = {'P3': P(3), 'P4': P(4), 'P5': P(5), 'P6': P(6), '2e': [(0,1),(2,3)], 'P3+e': [(0,1),(1,2),(2,3),(4,5)]}
for n in (6, 8):
    G = cubic(n); assert len(G) == Nseq(N, D, [D]*n), (len(G), Nseq(N, D, [D]*n))
    for k, s in S.items():
        if max(max(e) for e in s) < n:
            b = sum(set(s) <= g for g in G); c = contains(N, n, D, list(s))
            print(n, k, b, c, 'OK' if b == c else 'MISMATCH')
