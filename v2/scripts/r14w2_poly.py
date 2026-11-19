# r14w2: final c0(j,k,D) as polynomial in y=1/D, and comparison with data fits (r7+r13 data, deg-3 fit, nmin=20)
import sympy as sp, numpy as np, os, glob, collections
from r12w3_exact import c0, D
y=sp.symbols('y'); here=os.path.dirname(os.path.abspath(__file__)); N=os.path.join(here,'..','notes')
d=collections.defaultdict(dict)
for f in glob.glob(N+'/r7_data/d*.txt')+glob.glob(N+'/r13w3_data/d*.txt'):
    for l in open(f):
        t=l.split()
        if len(t)==5: d[(int(t[0]),t[1])][int(t[2])]=float(t[4])
def fit(v,nmin=20,deg=3):
    n=np.array([a for a in sorted(v) if a>=nmin],float)
    if len(n)<deg+2: return float('nan')
    return np.linalg.lstsq(np.vstack([n**-i for i in range(deg+1)]).T,np.array([v[int(a)] for a in n]),rcond=None)[0][0]
for j,k in [(2,2),(3,1),(3,2),(3,3),(4,1),(4,2),(4,3),(4,4)]:
    c=c0(j,k); p=sp.expand(sp.simplify(c[2].subs(D,1/y)))
    print(f'({j},{k}) n^0,n^-1 coeffs={c[0]},{c[1]}  c0 = {p}   [(j+k+1)^2/2={sp.Rational((j+k+1)**2,2)}]')
    print('   D: formula/fit', ' '.join(f'{dv}:{float(c[2].subs(D,dv)):.2f}/{fit(d[(dv,f"S{j}_{k}_0")]):.2f}' for dv in (5,6,7) if d.get((dv,f'S{j}_{k}_0'))),flush=True)
