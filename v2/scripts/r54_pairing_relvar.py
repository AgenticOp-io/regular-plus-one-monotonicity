# Exact pairing-model relvar of the factor count (Lemma factor-one-dim), float64 + lgamma.
import numpy as np, sys
from math import comb, lgamma, log, exp
def lM(N):
    if N<0 or N%2: return -np.inf
    return lgamma(N+1)-(N/2)*log(2)-lgamma(N/2+1)
def lMv(N):
    return np.array([lM(int(x)) for x in np.asarray(N)])
def pw(h,n):
    r=np.array([1.0]); b=h
    while n:
        if n&1: r=np.convolve(r,b)
        n>>=1
        if n: b=np.convolve(b,b)
    return r
def relvar(n,d,m):
    h=np.array([comb(m,a)*comb(d-m,m-a)/comb(d,m) for a in range(m+1)])
    p=pw(h,n); A=np.arange(len(p))
    c=lM(d*n)-2*lM(m*n)-2*lM((d-m)*n)
    t=np.log(np.where(p>1e-250,p,np.nan))+lMv(A)+2*lMv(m*n-A)+lMv((d-2*m)*n+A)+c
    return np.exp(t[np.isfinite(t)]).sum()-1
if __name__=="__main__":
    for d in (6,10,16,24):
        x=1/(d-1); lim=exp(sum(x**k/(2*k) for k in range(3,200)))-1
        for m in sorted({1,2,d//4,d//2-1,d//2,d//2+1,d-1}):
            if not 1<=m<d: continue
            print(d,m,*[f"{relvar(n,d,m)*6*d**3:.4f}" for n in (200,800,3200)],f"lim*6d^3={lim*6*d**3:.4f}")
