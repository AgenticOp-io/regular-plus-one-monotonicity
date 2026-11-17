# Exact P(y)=E y^T, T=|E(G1)∩E(G2)|, G1,G2 iid uniform L-regular on n vertices; nearest zero of P to y=1.
# L=2: G1 over iso classes (cycle type) weighted; else all pairs (small n). Usage: r10w2_zeros.py L n
import sys, itertools, numpy as np, mpmath as mp
from collections import Counter
L,n=int(sys.argv[1]),int(sys.argv[2])
E=[(i,j) for i in range(n) for j in range(i+1,n)]; idx={e:k for k,e in enumerate(E)}
def gen():
    deg=[0]*n; out=[]
    def rec(k,mask):
        if k==len(E):
            if all(d==L for d in deg): out.append(mask)
            return
        i,j=E[k]
        # prune: vertex i finished after its last edge (i,n-1)
        if j==n-1 and deg[i]!=L and not (deg[i]+1==L and deg[j]<L): pass
        if deg[i]<L and deg[j]<L:
            deg[i]+=1;deg[j]+=1; rec(k+1,mask|(1<<k)); deg[i]-=1;deg[j]-=1
        rem=n-1-j
        if deg[i]+rem>=L or j<n-1 and False:
            if j==n-1 and deg[i]!=L: return
            rec(k+1,mask)
    rec(0,0); return out
G=gen(); N=len(G); print("N=",N,flush=True)
lo=np.array([g&((1<<63)-1) for g in G],dtype=np.uint64); hi=np.array([g>>63 for g in G],dtype=np.uint64)
def pc(a): # popcount uint64
    a=a-((a>>np.uint64(1))&np.uint64(0x5555555555555555)); a=(a&np.uint64(0x3333333333333333))+((a>>np.uint64(2))&np.uint64(0x3333333333333333))
    a=(a+(a>>np.uint64(4)))&np.uint64(0x0f0f0f0f0f0f0f0f); return (a*np.uint64(0x0101010101010101))>>np.uint64(56)
def cls(g): # cheap invariant: sorted component sizes + edge count (exact for L=2 up to cycle type)
    import networkx as nx
    H=nx.Graph([E[k] for k in range(len(E)) if g>>k&1]); return tuple(sorted(len(c) for c in nx.connected_components(H)))
if L==2:
    reps={}; cnt=Counter()
    for g in G:
        c=cls(g); cnt[c]+=1; reps.setdefault(c,g)
    src=[(reps[c],cnt[c]) for c in reps]
else: src=[(g,1) for g in G]
hist=np.zeros(len(E)+1)
for g,wt in src:
    t=pc(lo&np.uint64(g&((1<<63)-1)))+pc(hi&np.uint64(g>>63))
    hist+=wt*np.bincount(t.astype(np.int64),minlength=len(E)+1)
hist/=hist.sum()
mp.mp.dps=80
# P(y)=sum h_t y^t ; shift y=1+w
d=max(t for t in range(len(hist)) if hist[t]>0)
c=[sum(mp.mpf(float(hist[t]))*mp.binomial(t,i) for t in range(i,d+1)) for i in range(d+1)]
c=[x for x in c]; z=mp.polyroots(c[::-1],maxsteps=200000,extraprec=1000); zz=min(z,key=abs)
print(f"L={L} n={n} nearest zero |w|={mp.nstr(abs(zz),6)} w={mp.nstr(zz,5)} R/n={mp.nstr(abs(zz)/n,5)} R*L/n={mp.nstr(abs(zz)*L/n,5)}")
