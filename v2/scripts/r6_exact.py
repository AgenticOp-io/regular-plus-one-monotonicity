# r6: exact exp-form test, many hosts, parallel.  usage: python r6_exact.py D n1 n2 ... [-- host ...]
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from math import exp
from multiprocessing import Pool
from r5w3_exact import make, contains, gao

def clique(vs): return [(a,b) for i,a in enumerate(vs) for b in vs[i+1:]]
def hosts(D):
    H={'empty':[], 'match3':[(2,3),(4,5),(6,7)], 'match6':[(2+2*i,3+2*i) for i in range(6)],
     'path_uv':[(0,2),(2,3),(3,1)], 'common_nb':[(0,2),(1,2)], 'edge_at_u':[(0,2)], 'edge_at_both':[(0,2),(1,3)],
     'tri_far':clique([2,3,4]), 'K4_far':clique([2,3,4,5]), 'K23_far':[(a,b) for a in (2,3) for b in (4,5,6)],
     'path6_far':[(2+i,3+i) for i in range(6)], 'tri_at_u':[(0,2),(0,3),(2,3)],
     'mix':[(0,2),(0,3),(4,5),(5,6),(6,4),(1,7),(8,9)],
     'dstar':[(2,3+i) for i in range(D-1)]+[(0,3+D)],}   # far hub with D-1 leaves
    for j in range(1,D): H[f'star_u{j}']=[(0,2+i) for i in range(j)]
    for j in range(1,D): H[f'star_both{j}']=[(0,2+i) for i in range(j)]+[(1,2+j+i) for i in range(j)]
    for j in range(2,D+1): H[f'hub{j}']=[(2,3+i) for i in range(j)]   # far star, deg j hub
    return H
def run(a):
    D,name,ns=a; N=make(D); H=hosts(D)[name]; out=[]
    for n in ns:
        if n*D%2 or n<12+len(H): continue
        P=contains(N,n,D,H+[(0,1)])/contains(N,n,D,H)
        base,A,B=gao(n,D,H,0,1)
        P=float(P) if not hasattr(P,'numerator') else P
        out.append(f"{D} {name} {n} {(P/(base*(1-A)*(1-B))-1)*n*n:.5f} {(P/(base*exp(-A-B))-1)*n*n:.5f}")
    return "\n".join(out)
if __name__=='__main__':
    D=int(sys.argv[1]); r=sys.argv[2:]
    names=r[r.index('--')+1:] if '--' in r else list(hosts(D)); ns=[int(x) for x in (r[:r.index('--')] if '--' in r else r)]
    with Pool(8) as p:
        for s in p.imap_unordered(run,[(D,nm,ns) for nm in names]):
            print(s,flush=True)
