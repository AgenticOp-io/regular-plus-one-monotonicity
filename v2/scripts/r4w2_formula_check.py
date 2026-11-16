"""Closed form for the pairing-level second/first moment ratio of r-factors in a host profile h:
  E_pair Z^2/(E_pair Z)^2 = E_pi[f(S)1_{S even}]  ~=  sqrt((hb-1)/(hb-2)) * exp( c*Delta^2*(hb-1)/(hb-2) ),
  c = hb^3/(2 n rho^2 D^2),  Delta = sum_v r_v^2/h_v - n rho^2/hb  ~ D^2 sum y^2/hb^3.
(parity factor 1/2, f(m*)=sqrt2, 1-c sigma^2=(hb-2)/(2(hb-1)); regular case = paper's sqrt((D-1)/(D-2)).)"""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('scripts',1)[0]+'scripts')
from r4w2_pairing_shift import log_ratio
rng = np.random.default_rng(7)
print("  n  hb  D  y-spread | exact log ratio | formula | Delta")
for n, hb, D, amp in [(100,12,9,1),(200,12,9,1),(400,12,9,1),(200,16,12,2),(400,16,12,2),(400,20,15,2)]:
    y = rng.integers(-amp, amp+1, n); y[n//2:] = -y[:n//2]
    h = hb + y; rho = hb - D
    ex, _ = log_ratio(list(h), D)
    Delta = sum((hv-D)**2/hv for hv in h) - n*rho**2/hb
    c = hb**3/(2*n*rho**2*D**2)
    pred = 0.5*np.log((hb-1)/(hb-2)) + c*Delta**2*(hb-1)/(hb-2)
    print(f"{n:4d} {hb:3d} {D:2d}  var={y.var():.2f} | {ex:.4f} | {pred:.4f} | {Delta:.2f}")
    assert abs(ex-pred) < 0.1*max(1, ex) , "formula off"
# regime table: exponent  K := c Delta^2 with sigma_y^2 = hb(1-p); BIM scaling
print("\nexponent c*Delta^2 = n D^2 s^2/(2 rho^2 hb^3) (s^2=var y), s^2 = hb:  ~ n/(2 eps^2 D)")
for n, d, L in [(10**6, 30, 1), (10**8, 100, 1)]:
    lg = np.log(n); D = d**(2/3)*lg**(1/3); eps = (lg/d)**(1/3); hb=(1+eps)*D; rho=eps*D
    K = n*D**2*hb/(2*rho**2*hb**3)
    print(f"n={n:.0e} d={d}: D={D:.1f} eps={eps:.3f}  c*Delta^2={K:.3g}  vs D^2={D*D:.0f}  D^3/n={D**3/n:.2g}")
