# r7: fit n^2*err_exp = c0 + c1/n + c2/n^2 using only n>=nmin..nmax window; usage r7_fit.py nmax_cut files...  (shows fit-window bias)
import sys, collections, numpy as np
cut=int(sys.argv[1]); d=collections.defaultdict(list)
for f in sys.argv[2:]:
    for l in open(f):
        t=l.split()
        if len(t)==5 and int(t[2])<=cut: d[(int(t[0]),t[1])].append((int(t[2]),float(t[4])))
for k in sorted(d):
    v=sorted(d[k])
    if len(v)<3: continue
    n=np.array([x[0] for x in v],float); y=np.array([x[1] for x in v])
    c=np.linalg.lstsq(np.vstack([n**0,1/n,1/n**2]).T,y,rcond=None)[0]
    print(k[0],k[1],int(n[-1]),f"{c[0]:.3f}")
