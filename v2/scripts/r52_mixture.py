# r52: (a) q_k = E[t^k], t=1/g^2, g^2/2~Gamma((n+1)/2)  (b) tail of t>2/n under k-tilt  (c) cumulant remainder of E_t e^{s t} vs q1 s+(q2-q1^2)s^2/2
from mpmath import mp, mpf, gamma, quad, exp, log, gammainc, nsum, factorial, inf
mp.dps = 50
def q(n,k):
    r = mpf(1)
    for i in range(1, k+1): r /= (n-2*i+1)
    return r
# (a) exact identity: E[(g^2)^-k] = 2^-k Gamma(a-k)/Gamma(a)
for n in (10, 40, 1000):
    a = mpf(n+1)/2
    for k in (1, 2, 3, 5):
        assert abs(2**-k*gamma(a-k)/gamma(a)/q(n,k) - 1) < mpf(10)**-40
print("(a) q_k = E[t^k] exact: OK")
# (b) under k-tilt, g^2/2 ~ Gamma(a-k); P(g^2 < n/2) = P(Gamma(a-k) < n/4)
for n in (100, 1000, 10000):
    for k in (0, 10, 50):
        a = mpf(n+1)/2 - k
        p = gammainc(a, 0, mpf(n)/4, regularized=True)
        print("(b) n=%d k=%d  P(t>2/n | k-tilt) = %.2e" % (n, k, float(p)))
# (c) full sum_k s^k q_k/k! (k<=n/2) vs 2nd-order cumulant formula; s = (x-1) L n/2, x=2
def rem(n, L):
    s = mpf(L)*n/2
    K = n//2
    tot, term = mpf(0), mpf(1)
    for k in range(0, K+1):
        if k > 0: term *= s*(1/mpf(n-2*k+1))/k
        tot += term
    lnE = log(tot)
    q1, q2 = q(n,1), q(n,2)
    return lnE - (q1*s + (q2-q1**2)*s**2/2)
for n in (10**3, 10**4, 10**5):
    for L in (5, 10, 20):
        if L*L < n/4:
            r = rem(n, L)
            print("(c) n=%d L=%d rem=%.3e  rem*n^2/L^3=%.3f" % (n, L, float(r), float(r*n*n/L**3)))
