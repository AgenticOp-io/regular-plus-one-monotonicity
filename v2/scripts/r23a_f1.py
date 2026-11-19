# test f1=2: n*(E q/((D-1)^4/8) -1) vs n, Richardson. usage D n1 n2 ...
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from r5w3_exact import make,contains
from r23a_counts import HOSTS,ncopies
sys.setrecursionlimit(100000)
D=int(sys.argv[1]); N=make(D); prev=None
for n in map(int,sys.argv[2:]):
    if n*D%2: continue
    tot=contains(N,n,D,[])
    Eq=contains(N,n,D,HOSTS['C4'])*ncopies(n,'C4')/tot; Et=contains(N,n,D,HOSTS['K3'])*ncopies(n,'K3')/tot
    a=n*(Eq*8/(D-1)**4-1); b=n*(Et*6/(D-1)**3-1)
    print(D,n,'f1~%.4f e1~%.4f'%(a,b),flush=True)
