import numpy as np
from math import lgamma
gammaln=np.vectorize(lgamma)
from math import comb, log, sqrt
def lM(N):  # log (N-1)!!, N even
    N=np.asarray(N,float); return gammaln(N+1)-gammaln(N/2+1)-(N/2)*log(2)
def R(n,d,m):
    h=np.array([comb(m,a)*comb(d-m,m-a)/comb(d,m) for a in range(m+1)])
    # pmf via repeated FFT-free convolution in log-safe float (n moderate)
    pmf=np.array([1.0])
    # binary powering
    base=h.copy(); k=n
    while k:
        if k&1: pmf=np.convolve(pmf,base)
        base=np.convolve(base,base); k>>=1
        base/=base.sum(); pmf/=pmf.sum()
    A=np.arange(len(pmf)); ok=(A%2==0)&(pmf>0)
    A=A[ok]; p=pmf[ok]
    lg=lM(A)+2*lM(m*n-A)+lM((d-2*m)*n+A)+lM(d*n)-2*lM(m*n)-2*lM((d-m)*n)
    return float(np.sum(p*np.exp(lg)))
for d in [3,4,6,10]:
    for m in range(1,d):
        n=4000 if (m*4000)%2==0 else 4001
        if (d*n)%2 or (m*n)%2: n+=1
        r=R(n,d,m); t=sqrt((d-1)/(d-2))
        print(f"d={d} m={m} n={n} R={r:.6f} target={t:.6f} diff*n={(r-t)*n:.3f}")
