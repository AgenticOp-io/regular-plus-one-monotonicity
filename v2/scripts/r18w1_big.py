# u_T for D=3 shapes at large even n, high-precision logs (Decimal). Uses r5w3_exact.contains (already poly-time DP; no new counter needed).
# usage: python r18w1_big.py SHAPE n...
import sys, os, itertools, time
from decimal import Decimal, getcontext
getcontext().prec = 80
sys.setrecursionlimit(100000)
sys.path.insert(0, os.path.dirname(__file__))
from r5w3_exact import make, contains, Nseq
D = 3
N = make(D)
P = lambda k: [(i, i + 1) for i in range(k)]
SH = {'P3': P(3), 'P4': P(4), 'P5': P(5), 'P6': P(6), '2e': [(0, 1), (2, 3)],
      'P2+P2': [(0, 1), (1, 2), (3, 4), (4, 5)], 'P3+e': [(0, 1), (1, 2), (2, 3), (4, 5)]}
name = sys.argv[1]
S = SH[name]
K = len(S)
for n in map(int, sys.argv[2:]):
    t = time.time()
    tot = Nseq(N, D, [D] * n)
    lp = lambda U: (Decimal(contains(N, n, D, list(U))) / Decimal(tot)).ln() if U else Decimal(0)
    u = sum((-1) ** (K - r) * lp(U) for r in range(K + 1) for U in itertools.combinations(S, r))
    print(name, n, 'u=%.6e' % u, 't=%.1fs' % (time.time() - t), flush=True)
