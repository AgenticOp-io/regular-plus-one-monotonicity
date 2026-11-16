"""Exact pairing-model second/first-moment ratio E Z^2/(E Z)^2 for r-factors of a host profile h_v
(r_v = h_v - D), regular vs non-regular.  Tests whether y-dependence of the class-overlap mean
mu_S = sum r_v^2/h_v (shift ~ D^2 sum y^2/h^3) is visible at pairing level."""
import numpy as np
from math import lgamma
def gammaln(x): return np.vectorize(lgamma)(x) if np.ndim(x) else lgamma(x)
def lc(a,b): return lgamma(a+1)-lgamma(b+1)-lgamma(a-b+1)
def hyp_pmf(ks, N, K, n):  # overlap of two K-subsets of N (K=n)
    return np.array([np.exp(lc(K,k)+lc(N-K,n-k)-lc(N,n)) for k in ks])

def ldf(m):  # log (2m-1)!!  (m pairs), m>=0 real-integer
    return gammaln(2*m+1)-m*np.log(2)-gammaln(m+1)

def log_ratio(h, D):
    h = np.asarray(h); r = h - D; n = len(h)
    assert h.sum() % 2 == 0 and r.sum() % 2 == 0
    pmf = np.array([1.0])
    for hv, rv in zip(h, r):
        ks = np.arange(max(0, 2*rv-hv), rv+1)
        pmf = np.convolve(pmf, hyp_pmf(ks, hv, rv, rv))
    S = np.arange(len(pmf)); ok = (S % 2 == 0) & (pmf > 0)
    S = S[ok]; p = pmf[ok]
    tot_h, tot_r, tot_D = h.sum(), r.sum(), D*n
    M1 = (tot_r - S)/2; Ms = (tot_D - tot_r + S)/2   # pairs in R1', rest
    lf = (ldf(tot_h/2) + ldf(S/2) + 2*ldf(M1) + ldf(Ms)
          - 2*ldf(tot_r/2) - 2*ldf(tot_D/2))
    lw = np.log(p) + lf
    m = lw.max()
    return m + np.log(np.exp(lw-m).sum()), (S*p).sum()/p.sum()

if __name__ == "__main__":
    rng = np.random.default_rng(1)
    for n, hb, D in [(60, 12, 9), (120, 12, 9), (120, 16, 12), (240, 16, 12)]:
        reg = [hb]*n
        y = rng.integers(-1, 2, n); y[: n//2] = np.abs(y[: n//2]); y[n//2:] = -y[: n//2]  # sum 0
        nonreg = list(hb + y)
        lr0, m0 = log_ratio(reg, D); lr1, m1 = log_ratio(nonreg, D)
        mu_pred = sum((hv-D)**2/hv for hv in nonreg)
        sig2 = np.var(y)
        pred_shift = D**2*sig2*n/hb**3
        print(f"n={n} h={hb} D={D} var y={sig2:.2f}: log ratio reg={lr0:.4f} nonreg={lr1:.4f}; "
              f"mean S reg={m0:.2f} nonreg={m1:.2f} shift={m1-m0:.2f} (pred {pred_shift:.2f})")
