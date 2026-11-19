# P(H in G) predicted from E[t],E[q] (counts affine in t,q) vs exact DP contains().  usage: D n
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from r5w3_exact import make,contains
from r23a_counts import formulas,HOSTS,ncopies
D,n=int(sys.argv[1]),int(sys.argv[2]); N=make(D); sys.setrecursionlimit(100000)
tot=contains(N,n,D,[])
P=lambda H:Fr(contains(N,n,D,H),tot)
from math import comb
Et=P(HOSTS['K3'])*ncopies(n,'K3'); Eq=P(HOSTS['C4'])*ncopies(n,'C4')
F=formulas(n,D,Et,Eq); bad=0
for k,h in HOSTS.items():
    pred=Fr(F[k])/ncopies(n,k) if k in F else None
    if pred is None: continue
    ex=P(h); 
    if pred!=ex: bad+=1; print('MISMATCH',k,float(pred),float(ex))
print(D,n,'checked',len(F),'bad',bad,'Et=%.5f Eq=%.5f'%(Et,Eq))
