"""r4 worker1: size of the k=3 term of R2* at L = c n^{1/2}, from the exact kappa3 of r2_worker2
(printed series, theta = t3 (n-1)_3/(L)_3; here t3 = theta (L)_3/(n-1)_3).
Shows: kappa3 -> 5 c^4 (theta=1), so R2* is false (not o(1)) at L = Theta(n^{1/2}); it needs L = o(n^{1/2}).
Also evaluates the switching bound t3 <= (L)_3/(n-2L-12)^3, i.e. theta <= ((n-1)(n-2)(n-3)/(n-2L-12)^3) -> 1+O(L/n).
Run: python v2/scripts/r4w1_k3_at_sqrt.py
"""
from fractions import Fraction as F

def k3_series(n, L, th):
    # printed truncation: orders n^-2, n^-3 (higher orders are O(L^k/n^4 ...) relative)
    a = L**2*(L-1)*(5*L-7)/n**2
    b = L**2*(L**4*th**2 - 2*L**4*th + L**4 - 6*L**3*th**2 + 12*L**3*th - 12*L**3
              + 13*L**2*th**2 - 28*L**2*th + 66*L**2 - 12*L*th**2 + 30*L*th - 120*L
              + 4*th**2 - 12*th + 66)/n**3
    return a + b

for c in (0.25, 0.5, 1.0):
    for n in (10**4, 10**6, 10**8):
        L = int(c*n**0.5)
        # switching bound at L=c sqrt n gives theta <= (n-1)(n-2)(n-3)/(n-2L-12)^3 = 1 + O(c/sqrt n)
        th_max = (n-1)*(n-2)*(n-3)/(n-2*L-12)**3
        print(f"c={c} n={n:>9} L={L:>5}  kappa3(theta=1)={k3_series(n,L,1.0):9.4f}  5c^4={5*c**4:7.4f}"
              f"  kappa3(theta_max={th_max:.5f})={k3_series(n,L,th_max):9.4f}")
# t3-scale sanity: kappa3 with theta = 1+delta is 5c^4 + c^6 delta^2 + ...: any theta=O(1) keeps k3 = O(L^4/n^2+L^6/n^3)
for th in (0.5, 2.0, 10.0):
    n = 10**8; L = int(0.1*n**0.5)
    print(f"theta={th}: kappa3={k3_series(n, L, th):.6f}  (L^4/n^2={L**4/n**2:.2e}, L^6/n^3={L**6/n**3:.2e})")
