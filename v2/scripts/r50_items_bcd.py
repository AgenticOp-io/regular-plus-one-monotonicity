"""r50 items B,C,D ((a) part A2 was run from r50_items.py and killed at timeout after L=12) L-scaling, (b) overlap fluctuations, (c) short cycles, (d) other y. Uses r50_cluster.ck (exact)."""
import numpy as np, sys
from r50_cluster import *
ns=[40,60,90,130]; M={40:[.9006,.01625,-2.656e-3,1.151e-4],60:[.947,9.849e-3,-1.185e-3,3.388e-5],90:[.9621,6.213e-3,-5.173e-4,9.754e-6],130:[.9758,4.161e-3,-2.444e-4,3.230e-6]}
print("A n-exponents (L=4,j=3,y=2, data from r50_cluster):",[round(np.polyfit(np.log(ns),np.log([abs(M[n][k]) for n in ns]),1)[0],2) for k in (1,2,3)])
print("== B fluctuations n=70,L=6,j=4,y=2: 40 samples")
r,ov=sample(70,6,4,2.0,25); print("mean",r.mean(0),"std",r.std(0),"overlap mean/std",ov.mean(),ov.std())
for k in (1,2,3): print(f"corr(c_{k+1},overlap)=",round(np.corrcoef(r[:,k],ov)[0,1],3))
print("== C short cycles n=70,L=6,j=4,y=2: random vs circulant (many triangles)")
r,_=sample(70,6,4,2.0,6); print("random",r.mean(0))
r,_=sample(70,6,4,2.0,1,mode="circ"); print("circulant",r[0])
print("== D y-dependence n=70,L=6,j=4")
for y in (0.5,1.5,2.0,3.0,5.0):
    r,_=sample(70,6,4,y,5); print(y,["%.3e"%x for x in r.mean(0)]); sys.stdout.flush()
