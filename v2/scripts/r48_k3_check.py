"""r48 step 1: validate the degree-3 cluster formula  e3 = D3/6 - (A1 - B + Tr)  by brute force,
and check ln Z truncation error (deg2 vs deg3) against exact Z on small random-regular F u U (n=16)."""
import itertools, random, math
def graph(n,d,seed):
    r=random.Random(seed)
    while True:
        pts=[v for v in range(n) for _ in range(d)]; r.shuffle(pts); E=set(); ok=True
        for i in range(0,len(pts),2):
            a,b=pts[i],pts[i+1]
            if a==b or (min(a,b),max(a,b)) in E: ok=False;break
            E.add((min(a,b),max(a,b)))
        if ok: return E
def stats(E,w):
    E=list(E); adj=lambda e,f: e!=f and len(set(e)&set(f))>0
    e1=sum(w[e] for e in E); Q2=sum(w[e]**2 for e in E); Q3=sum(w[e]**3 for e in E)
    nb={e:[f for f in E if adj(e,f)] for e in E}
    P2=sum(w[e]*w[f] for e in E for f in nb[e])/2
    D3=e1**3-3*e1*Q2+2*Q3
    A1=sum(w[e]*w[f]*(e1-w[e]-w[f]) for e in E for f in nb[e])/2
    B=sum(w[e]*(sum(w[f] for f in nb[e])**2-sum(w[f]**2 for f in nb[e]))/2 for e in E)
    Tr=sum(w[e]*w[f]*w[g] for e,f,g in itertools.combinations(E,3) if adj(e,f) and adj(e,g) and adj(f,g))
    return e1,Q2,P2,D3/6-(A1-B+Tr)
def brute(E,w):
    E=list(E); e=[0.0]*4
    for k in range(4):
        for S in itertools.combinations(E,k):
            vs=[x for ed in S for x in ed]
            if len(set(vs))==2*k: e[k]+=math.prod(w[ed] for ed in S)
    return e
if __name__=="__main__":
    n=16; F=graph(n,3,1); U=graph(n,2,2)
    for a in (0.5,1.0):
        w={e:(-1.0 if e in U else a) for e in F|U}
        e1,Q2,P2,e3=stats(F|U,w); b=brute(F|U,w)
        e2=(e1*e1-Q2)/2-P2
        print("a",a,"e2",e2,b[2],"e3",e3,b[3]); assert abs(e2-b[2])<1e-9 and abs(e3-b[3])<1e-9
        q=lambda k: 1/math.prod(n-1-2*i for i in range(k))
        # exact Z needs all k; matching up to n/2
        Z=0
        E=list(F|U)
        # DP over matchings via recursion
        from functools import lru_cache
        nbr={}
        for (x,y) in E: nbr.setdefault(x,[]).append((y,w[(x,y)])); nbr.setdefault(y,[]).append((x,w[(x,y)]))
        @lru_cache(None)
        def poly(mask):  # coefficients of matching polynomial on remaining vertices, by size
            if mask==0: return (1.0,)
            v=(mask&-mask).bit_length()-1; m2=mask&~(1<<v)
            r=list(poly(m2))
            for (y,wt) in nbr.get(v,[]):
                if m2>>y&1:
                    s=poly(m2&~(1<<y))
                    r+= [0.0]*(len(s)+1-len(r))
                    for i,c in enumerate(s): r[i+1]+=wt*c
            return tuple(r)
        c=poly((1<<n)-1); Z=sum(c[k]*q(k) for k in range(len(c)))
        l2=q(1)*e1+(q(2)-q(1)**2)*e1**2/2-q(2)*(Q2/2+P2)
        l3=l2+q(3)*e3-q(1)*q(2)*e1*e2+q(1)**3*e1**3/3
        # note l2 uses q2*e2 - q1^2 e1^2/2 = same as above
        print(" lnZ exact %.6f  deg2 err %.2e  deg3 err %.2e"%(math.log(Z),math.log(Z)-l2,math.log(Z)-l3))
