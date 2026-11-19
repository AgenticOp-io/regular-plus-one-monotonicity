"""Exact pairing-level E[Z^2]/E[Z]^2 (Z = # L-factors of a uniform pairing with cell sizes h_v), regular vs non-regular host.
Z^2 sum is done exactly over class vectors by polynomial product in s=sum a_v (log-scaled floats)."""
import numpy as np, math, random
from math import lgamma
def ldf(m): return 0.0 if m<=0 else lgamma(m+1)-(m/2)*math.log(2)-lgamma(m/2+1)   # log (m-1)!! for even m>=0... (m-1)!! = m!/(2^(m/2)(m/2)!)
def lmul(hs,L):
    n=len(hs); S=sum(hs)
    # per-cell polynomial in z=a: weight h!/(a!(L-a)!^2 (h-2L+a)!) , use log-sum via scaled convolution
    poly=np.array([1.0]); lsc=0.0
    for h in hs:
        w=np.array([math.exp(lgamma(h+1)-lgamma(a+1)-2*lgamma(L-a+1)-lgamma(h-2*L+a+1)-(lgamma(h+1)-lgamma(L+1)**2*0)) for a in range(L+1)])
        sc=w.max(); lsc+=math.log(sc); poly=np.convolve(poly,w/sc); poly/=poly.max(); lsc+=0  # renormalise below
    return poly,lsc
def ratio(hs,L):
    n=len(hs); S=sum(hs)
    # exact via logs: accumulate polynomial with tracked log scale
    poly=np.array([1.0]); ls=0.0
    for h in hs:
        w=np.array([math.exp(lgamma(h+1)-lgamma(a+1)-2*lgamma(L-a+1)-lgamma(h-2*L+a+1)-(lgamma(h+1)-2*lgamma(L+1)-lgamma(h-2*L+1))) for a in range(L+1)])
        poly=np.convolve(poly,w); m=poly.max(); poly/=m; ls+=math.log(m)
    # constants dropped above: prod h!/(L!^2 (h-2L)!) -> included via -(...) normalisation, so add back
    lc=sum(lgamma(h+1)-2*lgamma(L+1)-lgamma(h-2*L+1) for h in hs)
    terms=[]
    for s,p in enumerate(poly):
        c=nL=n*L-s
        if s%2 or c%2 or p<=0: continue
        terms.append(math.log(p)+ldf(s)+2*ldf(c)+ldf(S-2*n*L+s))
    mx=max(terms); lz2=ls+lc+mx+math.log(sum(math.exp(t-mx) for t in terms))-ldf(S)
    lz1=sum(lgamma(h+1)-lgamma(L+1)-lgamma(h-L+1) for h in hs)+ldf(n*L)+ldf(S-n*L)-ldf(S)
    return math.exp(lz2-2*lz1)
if __name__=="__main__":
    from statistics import NormalDist
    from r3_worker1_host_exponent import psi
    from fractions import Fraction as Fr
    nd=NormalDist()
    for h,L,n in [(30,3,200),(60,3,200),(120,3,200),(240,3,200),(120,6,200),(240,6,200)]:
        x=1/(h-1); base=math.log(ratio([h]*n,L))+float(psi([h]*n,L)); print(f"h={h} L={L} regular: log total={base:+.3e}  (x^3/6 ~ {x**3/6:.2e})")
        for c in (0.5,1):
            ys=[round(c*math.sqrt(h)*nd.inv_cdf((i+.5)/n)) for i in range(n)]; ys[0]-=sum(ys)
            if sum(h+y for y in ys)%2: ys[1]+=1
            hs=[h+y for y in ys]; assert min(hs)>2*L+1
            m2=sum(y*y for y in ys)/n; mu=sum(hs)/n
            tp=math.log(ratio(hs,L)); ps=float(psi(hs,L)); tot=tp+ps
            print(f"   m2/h={m2/h:.2f}  pairing log={tp:+.3e} psi={ps:+.3e}  total={tot:+.3e}  vs regular(h)  d={tot-base:+.2e}  m2/h^2={m2/h**2:.2e}")
