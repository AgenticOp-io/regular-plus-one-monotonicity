# r13w3: refit c0 from r7+r13 data with larger n and higher-order 1/n polynomials; compare to exact formula (r12w3_exact.c0)
import numpy as np, collections, os, sys, glob
from r12w3_exact import c0, D
here=os.path.dirname(os.path.abspath(__file__)); N=os.path.join(here,'..','notes')
d=collections.defaultdict(dict)
for f in glob.glob(N+'/r7_data/d*.txt')+glob.glob(N+'/r13w3_data/d*.txt'):
    for l in open(f):
        t=l.split()
        if len(t)==5: d[(int(t[0]),t[1])][int(t[2])]=float(t[4])
def fit(v,nmin,deg):
    n=np.array([a for a in sorted(v) if a>=nmin],float)
    if len(n)<deg+2: return None
    y=np.array([v[int(a)] for a in n]); A=np.vstack([n**-i for i in range(deg+1)]).T
    return np.linalg.lstsq(A,y,rcond=None)[0][0]
for j,k in [(2,2),(3,3),(4,2),(4,4)]:
    f=c0(j,k)[2]
    for Dv in (5,6,7,8,9):
        v=d.get((Dv,f'S{j}_{k}_0'))
        if not v: continue
        row=[f'{float(f.subs(D,Dv)):.2f}',f'nmax={max(v)}']
        for nmin in (0,20,28,36,44,60):
            for deg in (2,3,4):
                r=fit(v,nmin,deg); row.append(f'm{nmin}d{deg}:{r:.2f}' if r is not None else '-')
        print(j,k,Dv,*row)
