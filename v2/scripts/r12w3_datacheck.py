# compare r11w3 exact c0 (w=0 two-sided) with fitted r7 data c0 (3-param fit in 1/n, as r9w3_cross)
import numpy as np, collections, os, sympy as sp
from r12w3_exact import c0, D
base=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','notes','r7_data'); d=collections.defaultdict(list)
for Dv in range(4,11):
    for l in open(f'{base}/d{Dv}.txt'):
        t=l.split()
        if len(t)==5: d[(Dv,t[1])].append((int(t[2]),float(t[4])))
for j,k in [(2,2),(3,2),(3,3),(4,1),(4,2),(4,3),(4,4)]:
    f=c0(j,k)[2]; print(j,k,'D:exact/fit',end=' ')
    for Dv in range(5,11):
        v=sorted(d[(Dv,f'S{j}_{k}_0')])
        if len(v)<4: continue
        nn=np.array([a for a,_ in v],float); y=np.array([b for _,b in v])
        fit=np.linalg.lstsq(np.vstack([nn**0,1/nn,1/nn**2]).T,y,rcond=None)[0][0]; print(f'{Dv}:{float(f.subs(D,Dv)):.2f}/{fit:.2f}',end=' ')
    print()
