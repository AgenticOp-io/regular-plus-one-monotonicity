# u = D2 log P(e,f in G) (graph-level, P=g/Z) vs c=D2 log Q; shows what each equals at D=3
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from math import log
from r5w3_exact import make,contains
D=int(sys.argv[1]);N=make(D)
for n in map(int,sys.argv[2:]):
    g=lambda H:log(contains(N,n,D,H))
    u=g([(0,1),(1,2)])-2*g([(0,1)])+g([])
    print(D,n,'u=%.6f n*u=%.4f'%(u,n*u))
