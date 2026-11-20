# r28: exact test of r27's growing-D claim for the 4-cycle. g(n) = n*(E q * 8/(D-1)^4 - 1) = f1 + c(D)/n + c2(D)/n^2 + ...
# r27 predicts f1 = 2 for every D and c(D) = O(D) (no D^2/n^2 term). Fit a+b/n+c/n^2 through the last 3 exact points (rationals).
# usage: python r28_growing_D_exact.py D nmax
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from r5w3_exact import make, contains
from r23a_counts import HOSTS, ncopies
sys.setrecursionlimit(100000)

def fit3(pts):  # exact a + b/n + c/n^2 through 3 points
    (n1, g1), (n2, g2), (n3, g3) = pts
    import sympy as sp
    a, b, c = sp.symbols('a b c')
    s = sp.solve([a + b / sp.Integer(m) + c / sp.Integer(m)**2 - sp.Rational(g.numerator, g.denominator) for m, g in pts], [a, b, c])
    return s[a], s[b], s[c]

D, nmax = int(sys.argv[1]), int(sys.argv[2]); N = make(D); pts = []
for n in range(D + 2, nmax + 1):
    if n * D % 2: continue
    Eq = Fr(contains(N, n, D, HOSTS['C4']) * ncopies(n, 'C4'), contains(N, n, D, []))
    pts.append((n, n * (Eq * 8 / (D - 1)**4 - 1)))
    if len(pts) >= 3:
        a, b, c = fit3(pts[-3:])
        print(D, n, 'g=%.4f  f1~%.4f  c(D)~%.3f  c/D=%.3f  c/D^2=%.4f' % (float(pts[-1][1]), a, b, b / D, b / D**2), flush=True)
