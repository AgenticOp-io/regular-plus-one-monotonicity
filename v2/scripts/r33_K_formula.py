"""r33: compare r15w1 recorded exact pairing log-ratios (two-type host, y=+-t) with K=n(delta-m)^2 t^4/(2 m^2 delta^3).
Also: window scaling in regime (B) -- K vs the McKay-transfer cost delta^2. Pure arithmetic; exact values copied from r15w1."""
exact = {(40,6,3):(200,3.99),(40,6,5):(200,29.96),(60,8,6):(200,24.2)}
for (de,m,t),(n,ex) in exact.items():
    K = n*(de-m)**2*t**4/(2*m**2*de**3)
    print(f"delta={de} m={m} t={t} n={n}: exact={ex} K={K:.2f} ratio={ex/K:.2f}  K/delta^2={K/de**2:.4f}")
# regime B: m^2=d log n, delta=d^(2/3)(log n)^(1/3), s2^2~delta (typical G(n,p)-type), d=n^(1/4)
import math
for n in [1e6,1e9,1e12]:
    d=n**0.25; L=math.log(n); m2=d*L; de=d**(2/3)*L**(1/3)
    K=n*de**2/(2*m2); print(f"n={n:.0e}: K~{K:.3e}, delta^2={de**2:.3e}, K/delta^2={K/de**2:.3e}")
