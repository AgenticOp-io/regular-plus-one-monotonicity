# r14w2: MC (exact-uniform simple D-regular via pairing+rejection) check of the CM leading terms used in c0:
#  S2 = sum_dir (t)_2  vs nD*E(t)_2,  E(t)_2=(D-1)^4(D-2)^2/(nD)^2
#  X1 = E sum_{v outside {u}+L} s_v  (eL term), X2 = E sum_v C(s_v,2)  (the "pairs"=C4-type term), L = random j-subset of N(u)
# usage: python r14w2_mc.py D n N j seed
import sys, numpy as np, itertools
from math import comb
def sample(n,D,rng):
    st=np.repeat(np.arange(n),D)
    while True:
        p=rng.permutation(st); a,b=p[0::2],p[1::2]
        if (a==b).any(): continue
        k=np.minimum(a,b)*n+np.maximum(a,b)
        if len(np.unique(k))<len(k): continue
        A=np.zeros((n,n),np.int32); A[a,b]=1; A[b,a]=1; return A
D,n,N,j,seed=map(int,sys.argv[1:6]); rng=np.random.default_rng(seed)
subs=list(itertools.combinations(range(D),j)); res=[]
for _ in range(N):
    A=sample(n,D,rng); C=A@A; np.fill_diagonal(C,0); T=A*C
    S2=(T*(T-1)).sum(); S3=(T*(T-1)*(T-2)).sum()
    nb=[np.nonzero(A[u])[0] for u in range(n)]
    x1=x2=0.
    for u in range(n):
        for s in subs:
            L=nb[u][list(s)]; sv=A[u]+A[L].sum(0)
            m=np.ones(n,bool); m[u]=False; m[L]=False; sv=sv[m]
            x1+=(sv).sum(); x2+=(sv*(sv-1)/2).sum()
    res.append([S2,S3,x1/(n*len(subs)),x2/(n*len(subs))])
r=np.array(res); mu=r.mean(0); se=r.std(0,ddof=1)/np.sqrt(N)
nD=n*D
pS2=nD*((D-1)**2*(D-2)/nD)**2
eL=comb(j,2)*(D-1)**2/nD; p1=(j+1)*D-2*j-2*eL
p2=j*(D-j)*(D-1)**2/nD+comb(j,2)*(D-1)**3/nD
print(f'D={D} n={n} j={j} N={N} S2/pred {mu[0]/pS2:.3f}+-{se[0]/pS2:.3f} | sum s_v {mu[2]:.4f}+-{se[2]:.4f} pred {p1:.4f} | sum C(s,2)*n {mu[3]*n:.3f}+-{se[3]*n:.3f} pred {p2*n:.3f} ratio {mu[3]/p2:.3f}',flush=True)
