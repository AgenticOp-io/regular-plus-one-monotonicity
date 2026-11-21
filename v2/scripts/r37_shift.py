"""r37: (1) which role assignment of K is right (factor degree D vs residual rho); (2) Lambda-shift experiment:
planted (Z-weighted) vs null pairing law of Lambda=sum_{pairs} y_i y_j. Rigorous link: TV(P,P*)=E(1-Z/EZ)_+ so
Z/EZ->1 in prob  <=>  TV(null, planted)->0. If z=(mean*-mean)/sd ~ sqrt(K) -> inf, weak law FAILS."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0] if '/' in __file__ else '.')
from r4w2_pairing_shift import log_ratio
def Kf(n, h, D, s2sq):  # r4w2: factor degree D, residual rho=h-D
    rho = h - D; return n*D**2*s2sq**2/(2*rho**2*h**3)
def host(n, h, t): y = np.array([t, -t]*(n//2)); return h + y, y
# (1) exact pairing log ratio (regular baseline subtracted) vs both K assignments; r15w1 points (delta=40,m=6,t=3), n=200
print("exact pairing log-ratio minus regular vs K(D=m) and K(D=delta-m):")
for (h, m, t) in [(40, 34, 3), (40, 34, 5)]:  # D=34 reproduces r15w1's 3.99/29.96; D=6 hits a domain error in r4w2 log_ratio (not chased)
    n = 200; hv, y = host(n, h, t)
    ex = log_ratio(list(hv), m)[0] - log_ratio([h]*n, m)[0]
    print(f" h={h} D={m} t={t}: exact={ex:.2f}  K(D=m)={Kf(n,h,m,t*t):.2f}  K(D=h-m)={Kf(n,h,h-m,t*t):.2f}")
# (2) Lambda separation, null vs planted, pairing level
def pair_sum(w, rng):
    p = rng.permutation(w); return float((p[0::2]*p[1::2]).sum())
rng = np.random.default_rng(0)
for (n, h, D, t) in [(2000, 40, 6, 6), (2000, 40, 6, 9), (4000, 40, 6, 9)]:
    hv, y = host(n, h, t); r = hv - D
    wall = np.repeat(y, hv); wR = np.repeat(y, r); wF = np.repeat(y, D)
    assert len(wall) % 2 == 0 and len(wR) % 2 == 0 and len(wF) % 2 == 0
    nul = np.array([pair_sum(wall, rng) for _ in range(1500)])
    pl = np.array([pair_sum(wR, rng) + pair_sum(wF, rng) for _ in range(1500)])
    K = Kf(n, h, D, t*t); z = (pl.mean()-nul.mean())/nul.std()
    print(f"n={n} h={h} D={D} t={t}: K={K:.1f} sqrtK={K**.5:.2f} z={z:.2f} sd*/sd0={pl.std()/nul.std():.2f}")
# (3) regime B corrected K = n m^2 s2^4 /(2 (delta-m)^2 delta^3), s2^2=delta
print("regime B, d=n^(1/4): K_correct vs delta^2 vs r33's formula")
for n in [1e6, 1e9, 1e12]:
    d = n**.25; L = np.log(n); m = (d*L)**.5; de = d**(2/3)*L**(1/3)
    print(f" n={n:.0e}: K={n*m*m/(2*(de-m)**2*de):.3e} delta^2={de*de:.3e} r33-style={n*de*de/(2*m*m):.3e}")
