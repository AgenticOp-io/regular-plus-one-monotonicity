# r55: explicit Penrose/KP constants for k>=3 clusters + exact full-host test on N disjoint copies of K_{L+1} (w=1, i.e. x=2, F only)
from mpmath import mp, mpf, log, e
from math import comb, factorial
mp.dps = 60
def matchpoly(L):            # K_{L+1}: number of k-matchings, = C(L+1,2k)(2k-1)!!
    v = L+1; out = []
    for k in range(v//2+1):
        df = 1
        for j in range(1, 2*k, 2): df *= j
        out.append(mpf(comb(v, 2*k)*df))
    return out
def mul(a, b, cap):
    r = [mpf(0)]*(min(len(a)+len(b)-1, cap+1))
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i+j <= cap: r[i+j] += x*y
    return r
def power(p, N, cap):
    r = [mpf(1)]; b = p
    while N:
        if N & 1: r = mul(r, b, cap)
        b = mul(b, b, cap); N >>= 1
    return r
def q(n, k):
    r = mpf(1)
    for i in range(1, k+1): r /= (n-2*i+1)
    return r
def logser(a, K):            # coefficients of ln(sum a_k t^k), a_0=1
    a = a+[mpf(0)]*(K+1)
    c = [mpf(0)]*(K+1)
    for k in range(1, K+1):
        c[k] = a[k]-sum(mpf(j)/k*c[j]*a[k-j] for j in range(1, k))
    return c
print("n L  rem*n^2/L^3  | sum_{k>=3}|c_k|(2/n)^k  vs  Penrose bound  | rho")
for n in (400, 1600, 6400):
    for L in (3, 5, 7):
        N = n//(L+1); nn = N*(L+1)           # use n = N(L+1) vertices exactly
        n_ = nn
        a1 = matchpoly(L); K = n_//2
        PN = power(a1, N, K)
        Z = sum(PN[k]*q(n_, k) for k in range(len(PN)))
        c = logser(a1, 6)                     # per-component ln coefficients
        C = [N*x for x in c]
        phi2 = C[1]*q(n_,1) + C[2]*q(n_,2) + (q(n_,2)-q(n_,1)**2)*C[1]**2/2
        rem = log(Z) - phi2
        t = mpf(2)/n_
        s3 = sum(abs(C[k])*t**k for k in range(3, 7))
        D1 = 2*L-1; m = N*L*(L+1)/2; rho = e*D1*t
        bound = sum(m/D1/k**2*rho**k for k in range(3, 400))
        print(n_, L, float(rem*n_**2/L**3), "|", float(s3), float(bound), "|", float(rho))
