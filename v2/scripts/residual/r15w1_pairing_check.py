"""r15w1: pairing-level (exact) second/first moment ratio of m-factors for host degrees g=delta+y
(y=+-t half/half, s2^2=t^2) vs regular, in a BIM-like shape m<<delta. Prediction K=n m^2 s2^4/(2 rho^2 delta^3)."""
import sys, numpy as np
sys.path.insert(0, '.')
from r4w2_pairing_shift import log_ratio
for delta, m, t in [(40, 6, 5), (40, 6, 3), (60, 8, 6)]:
    for n in [200, 400, 800, 1600]:
        reg = [delta]*n
        non = [delta+t]*(n//2) + [delta-t]*(n//2)
        a, _ = log_ratio(reg, delta-m); b, _ = log_ratio(non, delta-m)
        rho = delta-m; K = n*m*m*t**4/(2*rho**2*delta**3)  # r=m, D=rho: roles swapped, K formula symmetric in the swap only approximately
        print(f"delta={delta} m={m} t={t} n={n}: logratio reg={a:.3f} nonreg={b:.3f}  K={K:.3f}")
