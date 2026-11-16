import numpy as np, sys
import math
gammaln=np.vectorize(math.lgamma)
rng=np.random.default_rng(1)
def L(m): return gammaln(2*m+1)-gammaln(m+1)-m*np.log(2)
def kap(c,y,s):  # cumulant mgf of Lambda over uniform pairing of class with cell counts c (rows) ; s tilt
    m=c.sum(-1); W=c@y; Q=c@(y*y); Qu=Q-W*W/m
    u4=(c*(y[None,:]-(W/m)[:,None])**4).sum(-1)
    mean=W*W/(2*m)-Qu/(2*(m-1)); var=(Qu**2-u4)/(2*(m-1))
    return s*mean+s*s*var/2
def run(n,hb,D,ys,cnt,ts,N=4000):
    y=np.repeat(ys,cnt).astype(float); assert len(y)==n and abs(y.sum())<1e-9
    h=hb+y; r=h-D; th,tr,tD=h.sum(),r.sum(),n*D
    b=np.empty((N,n))
    for i in range(N): b[i]=rng.hypergeometric(r.astype(int),(h-r).astype(int),r.astype(int))
    S=b.sum(1); ok=(S%2==0)
    f=np.exp(L(th/2)+L(S/2)+2*L((tr-S)/2)+L((tD-tr+S)/2)-2*L(tr/2)-2*L(tD/2))*ok
    out=[]
    for t in ts:
        e=np.zeros(N)
        for i in range(N):
            c=np.stack([b[i],r-b[i],r-b[i],h-2*r+b[i]])
            e[i]=kap(c,y,2*t).sum()
        k1=kap(np.stack([r,h-r]),y,t).sum()
        out.append((t,(f*np.exp(e-2*k1)).mean(),(f*np.exp(e-2*k1)).std()/np.sqrt(N)))
    return out
if __name__=="__main__":
    hb,D=12,9
    for n in (120,240,480):
        cnt=[n//4,n//2,n//4]
        print("n",n,"regular-ish ref sqrt((h-1)/(h-2))=",np.sqrt((hb-1)/(hb-2)))
        for t,v,se in run(n,hb,D,[-1,0,1],cnt,[0,.01,.02,.03,.04,.05,.06,.08,.1]): print(f" t={t:.3f} R={v:.3f} +-{se:.3f}")
