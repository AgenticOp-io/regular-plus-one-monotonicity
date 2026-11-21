"""r41: (a) x-scan of the r36 recursion residual (x!=2, kappa_k k>=3 shows as non-quadratic x dependence);
(b) Monte-Carlo check of the a-priori overlap tail: m=|F cap U| where U = union of j-1 disjoint-conditioned PMs."""
import random, math, sys
sys.path.insert(0, "v2/scripts")
from mpmath import mpf, nstr
from r36_recursion import predict
def part_a():
    for x in (1.5, 2, 3, 5):
        row = []
        for n, L in [(10**5, 100), (10**6, 300)]:
            f = (x-1)*mpf(L)**2*n/(2*(n-1)) + (x-1)**2/2*(-mpf(L)**3/n + mpf(L)**2/n)
            row.append(nstr((predict(n, L, x)-f)*n**2/mpf(L)**4, 4))
        print("x", x, "resid*n^2/L^4 at (1e5,100),(1e6,300):", row)
def pm(n):
    p = list(range(n)); random.shuffle(p)
    return {frozenset(p[i:i+2]) for i in range(0, n, 2)}
def part_b(n=40, L=4, trials=3000):
    F = set(); 
    for _ in range(L): F |= pm(n)          # approx L-regular union (multi-edges merge)
    ms = []
    for _ in range(trials):
        U = set(); m = 0
        for i in range(L-1):
            while True:
                M = pm(n)
                if not (M & U): break
            m += len(M & F); U |= M
        ms.append(m)
    mu = sum(ms)/trials; var = sum((a-mu)**2 for a in ms)/trials
    print(f"n={n} L={L}: E m={mu:.3f} var={var:.3f}  Poisson(L(L-1)/2*...)={(L-1)*L/2:.2f}  max={max(ms)}")
part_a(); part_b(); part_b(60, 5, 1500)
