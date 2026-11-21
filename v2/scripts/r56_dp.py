# exact N(d) for large n: vertex-by-vertex DP, state=histogram of residual degrees of unprocessed vertices.
import sys, math
from functools import lru_cache
from fractions import Fraction
def count(d):
    d=sorted(d,reverse=True); n=len(d); Dm=max(d)
    @lru_cache(None)
    def f(hist,r):  # hist: tuple counts by residual degree (unprocessed), r: residual of vertex being processed
        # process vertex with residual r over hist; then pop next vertex (largest residual) from new hist
        res=0
        def rec(j,left,cur,w):
            nonlocal res
            if j<0:
                if left: return
                res+=w*nxt(tuple(cur));return
            c=hist[j]
            for k in range(min(c,left)+1):
                cur2=list(cur);cur2[j]-=k
                if j>=1: cur2[j-1]+=k
                elif k: continue   # residual 0 can't take edge
                rec(j-1,left-k,cur2,w*math.comb(c,k))
        rec(Dm,r,list(hist),1);return res
    def nxt(h):
        if sum(h)==0:return 1
        r=max(i for i,c in enumerate(h) if c);h2=list(h);h2[r]-=1
        return f(tuple(h2),r)
    h=[0]*(Dm+1)
    for x in d:h[x]+=1
    return nxt(tuple(h))
def lnP(d):
    m=sum(d);df=math.prod(range(m-1,0,-2))
    return math.log(Fraction(count(d)*math.prod(math.factorial(x) for x in d),df))
def G0(d):
    s1=sum(d);s2=sum(x*(x-1) for x in d);return -s2/(2*s1)-s2**2/(4*s1**2)
if __name__=="__main__":
    assert count([2]*4)==3 and count([3]*4)==1 and count([2]*6)==70
    D=int(sys.argv[1])
    for n in map(int,sys.argv[2:]):
        if n*D%2:continue
        d=[D]*n;b=lnP(d)
        out=[]
        for B in(2,4,8):
            if B>n:break
            x=d[:]
            for i in range(0,B,2):x[i]+=1;x[i+1]-=1
            a=lnP(x)-b;e=a-(G0(x)-G0(d));out.append("B%d err=%.5f norm=%.3f"%(B,e,e*n*n/(B*(D+B))))
        print(n,D,*out,flush=True)
