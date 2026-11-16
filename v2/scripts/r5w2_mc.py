# MC at pairing level: 2-type hosts (A: h=hA,r=rA ; B: h=hB,r=0). log Z vs cross count c and A-A degree stats.
import numpy as np, sys
rng=np.random.default_rng(1)
def Z(pairs,nA,rA):
    sh=(rA+1,)*nA; a=np.zeros(sh); a[(0,)*nA]=1.0
    for u,v in pairs:
        b=a.copy()
        if u==v:
            if rA<2: continue
            sl_dst=[slice(None)]*nA; sl_src=[slice(None)]*nA
            sl_dst[u]=slice(2,None); sl_src[u]=slice(0,rA-1)
            b[tuple(sl_dst)]+=a[tuple(sl_src)]
        else:
            # add 1 to u and v
            sl_dst=[slice(None)]*nA; sl_src=[slice(None)]*nA
            sl_dst[u]=slice(1,None); sl_src[u]=slice(0,rA)
            sl_dst[v]=slice(1,None); sl_src[v]=slice(0,rA)
            b[tuple(sl_dst)]+=a[tuple(sl_src)]
        a=b
    return a[(rA,)*nA]
def run(nA,nB,hA,hB,rA,T):
    cell=np.array([v for v in range(nA) for _ in range(hA)]+[nA+v for v in range(nB) for _ in range(hB)])
    out=[]
    while len(out)<T:
        p=rng.permutation(len(cell)); P=cell[p].reshape(-1,2)
        cross=int(((P[:,0]<nA)!=(P[:,1]<nA)).sum())
        AA=[(int(a),int(b)) for a,b in P if a<nA and b<nA]
        z=Z(AA,nA,rA)
        if z<=0: continue
        d=np.bincount(np.array(AA).ravel(),minlength=nA) if AA else np.zeros(nA)
        out.append((np.log(z),cross,(d**2).sum()))
    return np.array(out)
if __name__=="__main__":
    nA,nB,hA,hB,rA,T=map(int,sys.argv[1:7])
    o=run(nA,nB,hA,hB,rA,T)
    y,c,q=o[:,0],o[:,1],o[:,2]
    print("n",nA+nB,"Var logZ",y.var(),"; E Z^2/(EZ)^2 =",np.mean(np.exp(2*y))/np.mean(np.exp(y))**2)
    for name,X in (("c",[c]),("c,sumd2",[c,q])):
        A=np.column_stack([np.ones(len(y))]+X); co=np.linalg.lstsq(A,y,rcond=None)[0]; r=y-A@co
        print(" resid var given",name,r.var(),"coef",co[1:], "ratio(cond 2nd mom)",np.mean(np.exp(2*r))/np.mean(np.exp(r))**2)
