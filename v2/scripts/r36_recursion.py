"""r36: backward tilt recursion built from the 2nd-order cluster formula for one factor
Z_j(y;m) = E[y^{|M cap F|} 1{M cap U_j=0}], F L-regular, U_j (j-1)-regular, m=|F cap U_j|.
Predict ln E[x^T] under nu_L x nu_L and compare with (x-1)k1 + (x-1)^2 k2/2, k1=L^2 n/(2(n-1)),
k2 = -L^3/n + L^2/n (main.tex Prop peel-cubic).  Residual should be O(L^4/n^2)."""
import math, sys
from mpmath import mp, mpf, log, exp, diff
mp.dps = 40
def lnZ(n, L, jp, y, m):
    n = mpf(n); w = y - 1; q1 = 1/(n-1); q2 = 1/((n-1)*(n-3))
    W1 = w*(n*L/2 - m) - n*jp/2
    Q2 = w*w*(n*L/2 - m) + n*jp/2
    s0 = w*L - jp
    P2 = (n*s0**2 - 2*s0*w*2*m - (n*(L*w*w + jp)))/2   # sum_v (s_v^2 - sum w^2)/2, o_v-linear part only
    return q1*W1 + (q2 - q1**2)*W1**2/2 - q2*(Q2/2 + P2)
def predict(n, L, x):
    x = mpf(x); y = {}; ln = mpf(0)
    gam = {}
    for j in range(L, 0, -1):
        y[j] = x*exp(sum(gam[k] for k in range(j+1, L+1)))
        gam[j] = diff(lambda m: lnZ(n, L, j-1, y[j], m), 0)
        ln += lnZ(n, L, j-1, y[j], 0) - lnZ(n, L, j-1, mpf(1), 0)
    return ln
if __name__ == "__main__":
    x = 2
    print("n L  predicted  k-formula  resid  resid*n^2/L^4  resid*n/L^3")
    for n, L in [(10**4, 20), (10**4, 40), (10**5, 100), (10**5, 200), (10**6, 300), (10**6, 600)]:
        p = predict(n, L, x)
        f = (x-1)*mpf(L)**2*n/(2*(n-1)) + (x-1)**2/2*(-mpf(L)**3/n + mpf(L)**2/n)
        r = p - f
        print(n, L, mp.nstr(p, 8), mp.nstr(f, 8), mp.nstr(r, 4), mp.nstr(r*n**2/mpf(L)**4, 4), mp.nstr(r*n/mpf(L)**3, 4))
