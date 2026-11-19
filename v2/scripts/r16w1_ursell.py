# r16w1: exact Ursell (connected log-cumulant) u_T of p_S=P(S subset G), G uniform D-regular on n vertices.
# u_T = sum_{U<=T} (-1)^{|T|-|U|} log p_U ; (B*) predicts u_T ~ c/n^{|T|-1} (fixed D). Prints n^{|T|-1} u_T.
import sys, os, itertools
from math import log
sys.path.insert(0, os.path.dirname(__file__))
from r5w3_exact import make, contains
D=int(sys.argv[1]); ns=[int(x) for x in sys.argv[2:]]
N=make(D); Z={}
shapes={'P2':[(0,1),(1,2)],'2e':[(0,1),(2,3)],'P3':[(0,1),(1,2),(2,3)],'K1,3':[(0,1),(0,2),(0,3)],'tri':[(0,1),(1,2),(2,0)],'P2+1':[(0,1),(1,2),(3,4)],'M3':[(0,1),(2,3),(4,5)],'P5':[(0,1),(1,2),(2,3),(3,4)],'M4':[(0,1),(2,3),(4,5),(6,7)],'C4':[(0,1),(1,2),(2,3),(3,0)],
 'tri+pend':[(0,1),(1,2),(2,0),(2,3)],'P3+2':[(0,1),(1,2),(3,4),(5,6)],'P4+1':[(0,1),(1,2),(2,3),(4,5)],
 'diamond-e':[(0,1),(1,2),(2,0),(3,4)]}
if D>=4: shapes['K1,4']=[(0,i) for i in range(1,5)]
if D>=3: shapes['K1,3+1']=[(0,1),(0,2),(0,3),(4,5)]
for n in ns:
    if n*D%2: continue
    tot=contains(N,n,D,[]) if False else None
    from r5w3_exact import Nseq
    tot=Nseq(N,D,[D]*n)
    lp=lambda U: log(contains(N,n,D,list(U))/tot) if U else 0.0
    for nm,S in shapes.items():
        u=sum((-1)**(len(S)-r)*lp(U) for r in range(len(S)+1) for U in itertools.combinations(S,r))
        print(D,nm,n,'u=%.4e'%u,'n^(k-1) u=%.4f'%(n**(len(S)-1)*u),'n^(k-2) u=%.4f'%(n**(len(S)-2)*u),flush=True)
