# Barvinok test: is Z(y)=sum_G prod_{e in G} y_e zero-free on polydisc |y_e-1|<=rho ?  Random + local minimisation of |Z|/Z(1).
import itertools, numpy as np, sys
sys.path.insert(0,'.')
from r47_leeyang import regs
n,D=int(sys.argv[1]),int(sys.argv[2])
E=list(itertools.combinations(range(n),2)); G=regs(n,D)
A=np.zeros((len(G),len(E)))
idx={e:i for i,e in enumerate(E)}
for r,g in enumerate(G):
    for e in g:A[r,idx[e]]=1
Z1=len(G); rng=np.random.default_rng(0)
def f(th,rho):
    y=1+rho*np.exp(1j*th); return abs(np.exp(A@np.log(y)).sum())/Z1
for rho in [0.3,0.5,0.7,0.9,1.0]:
    best=1e9
    for t in range(6):
        th=rng.uniform(0,2*np.pi,len(E)); v=f(th,rho); s=1.0
        for it in range(3000):  # random hill-climb
            t2=th+s*rng.normal(size=len(E))*(rng.random(len(E))<0.2); v2=f(t2,rho)
            if v2<v: th,v=t2,v2
            elif it%300==299: s*=0.5
        best=min(best,v)
    print("n,D",n,D,"rho",rho,"min|Z|/Z(1)",round(best,5),flush=True)
