"""r38: check the defect-0 part T0(d) (exact, vertex-disjoint shapes, F_m(N) exact) is Lipschitz:
T0(d')-T0(d) = e^{G0(s')}-e^{G0(s)} + O(1/n^2), d=D-regular, d'=D-2 on k vertices. Prints n^2*residual."""
import sys
from mpmath import mp, mpf, binomial, factorial, exp
mp.dps = 80

def T0(n, D, k, V=70):
    f = [mpf(D*(D-1))]*(n-k) ; fp = mpf((D-2)*(D-3))
    # e_v(f) = coefficients of (1+f x)^(n-k) (1+fp x)^k
    a = [binomial(n-k, i)*mpf(D*(D-1))**i for i in range(V+1)]
    b = [binomial(k, i)*fp**i for i in range(min(k, V)+1)]
    e = [sum(a[i-j]*b[j] for j in range(min(i, k)+1)) for i in range(V+1)]
    N = D*n - 2*k
    Fm = [mpf(1)]
    for i in range(V): Fm.append(Fm[-1]*(N-2*i-1))
    tot = mpf(0)
    for j in range(V+1):
        for kk in range((V-j)//2+1):
            v = j+2*kk
            tot += (-1)**(j+kk)/(factorial(j)*factorial(kk))*factorial(v)*e[v]/(mpf(2)**j*mpf(4)**kk*Fm[v])
    s1 = mpf(N)/n
    s2 = ((n-k)*mpf(D*(D-1))+k*fp)/n
    G0 = -s2/(2*s1)-s2**2/(4*s1**2)
    return tot, exp(G0)

for D in (3, 4, 6):
    for k in (1, 4):
        print("D", D, "k", k, " n^2*[ (T0'-T0) - (e^G0'-e^G0) ]  and n*(T0'-T0)")
        for n in (200, 400, 800, 1600, 3200):
            t1, g1 = T0(n, D, k); t0, g0 = T0(n, D, 0)
            res = (t1-t0)-(g1-g0)
            print("  n=%5d  n^2*res=%10.4f   n*dT0=%9.5f" % (n, float(n*n*res), float(n*(t1-t0))))
