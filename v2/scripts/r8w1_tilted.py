"""r8w1: (A) Gaussian lemma: TV-close laws, exp-weight ratio. (B) exact G0-dependence of cumulants of T=sum r_v^2."""
import itertools, math
import numpy as np

# (A) S~N(0,1) vs S'~N(delta,s^2); weight w=e^{-b S}, K=b^2. ratio E'w/Ew exact = exp(-b*delta + b^2(s^2-1)/2)
def ratio_num(b, delta, s):
    f = lambda x, m, sd: math.exp(-b*x)*math.exp(-(x-m)**2/(2*sd*sd))/(sd*math.sqrt(2*math.pi))
    def I(m, sd):
        x = np.linspace(m-14*sd-b*sd*sd, m+14*sd+abs(b)*sd*sd, 400001)
        return np.trapezoid([f(t, m, sd) for t in x[::40]], x[::40])
    return I(delta, s)/I(0, 1)
def tv_gauss(delta, s):
    x = np.linspace(-40, 40, 400001); g = lambda m, sd: np.exp(-(x-m)**2/(2*sd*sd))/(sd*np.sqrt(2*np.pi))
    return 0.5*np.trapezoid(abs(g(delta, s)-g(0, 1)), x)
for K in [4, 16, 64, 256]:
    b = math.sqrt(K); d = K**-0.25; s = 1.0   # mean shift K^{-1/4}: TV ~ d -> 0 but Y -> 0
    r = ratio_num(b, d, s); assert abs(math.log(r) - (-b*d)) < 1e-6
    print(f"A shift  K={K:4d} delta={d:.3f} TV={tv_gauss(d,s):.3f} Y={r:.3e} predicted exp(-sqrtK*delta)={math.exp(-b*d):.3e}")
for K in [4, 16, 64, 256]:
    b = math.sqrt(K); s = 1+1/math.sqrt(K)   # variance change eps~K^{-1/2}: TV ->0, Y = exp(K eps/2) -> inf
    r = ratio_num(b, 0, s); assert abs(math.log(r) - b*b*(s*s-1)/2) < 1e-6
    print(f"A scale  K={K:4d} s={s:.3f} TV={tv_gauss(0,s):.3f} Y={r:.3e}")

# (B) exact cumulants of T=sum_v r_v^2, r_v degree in G(complement of G0, p)
def cum(vals, probs):
    m = (vals*probs).sum(); c = vals-m
    return m, (c**2*probs).sum(), (c**3*probs).sum(), (c**4*probs).sum()-3*((c**2*probs).sum())**2
def run(name, n, edges0, p):
    E0 = set(map(frozenset, edges0))
    H = [e for e in itertools.combinations(range(n), 2) if frozenset(e) not in E0]
    m = len(H); T = np.zeros(2**m); P = np.zeros(2**m)
    for mask in range(2**m):
        r = [0]*n; k = 0
        for i, (a, b) in enumerate(H):
            if mask >> i & 1: r[a] += 1; r[b] += 1; k += 1
        T[mask] = sum(x*x for x in r); P[mask] = p**k*(1-p)**(m-k)
    assert abs(P.sum()-1) < 1e-12
    t0 = sum(1 for a, b, c in itertools.combinations(range(n), 3) if {frozenset((a,b)),frozenset((b,c)),frozenset((a,c))} <= E0)
    print(f"B {name}: triangles(G0)={t0}  mean,var,k3,k4 =", [round(float(x), 9) for x in cum(T, P)])
    return cum(T, P)
cyc = lambda n: [(i, (i+1) % n) for i in range(n)]
for p in [0.3, 0.5]:
    a = run("C6      ", 6, cyc(6), p); b = run("2xK3    ", 6, cyc(3)+[(3+i, 3+(i+1) % 3) for i in range(3)], p)
    assert abs(a[0]-b[0]) < 1e-9 and abs(a[1]-b[1]) < 1e-9 and abs(a[2]-b[2]) > 1e-6   # mean,var equal; k3 differs
q3 = [(a, b) for a in range(8) for b in range(a+1, 8) if bin(a ^ b).count("1") == 1]
k44 = [(a, b) for a in range(4) for b in range(a+1, 4)]+[(4+a, 4+b) for a in range(4) for b in range(a+1, 4)]
for p in [0.3]:
    a = run("Q3      ", 8, q3, p); b = run("2xK4    ", 8, k44, p)
    assert abs(a[0]-b[0]) < 1e-9 and abs(a[1]-b[1]) < 1e-9
print("OK")
