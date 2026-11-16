import sys, collections, numpy as np
d=collections.defaultdict(list)
for f in sys.argv[1:]:
    for l in open(f):
        t=l.split()
        if len(t)==5: d[(int(t[0]),t[1])].append((int(t[2]),float(t[3]),float(t[4])))
for k in sorted(d,key=lambda k:(k[0],k[1])):
    v=sorted(d[k]); 
    if len(v)<3: continue
    n=np.array([x[0] for x in v],float); X=np.vstack([n**0,1/n,1/n**2]).T[:, :min(3,len(v))]
    c=[np.linalg.lstsq(X,np.array([x[i] for x in v]),rcond=None)[0] for i in (1,2)]
    print(f"D={k[0]} {k[1]:13s} nmax={int(n[-1])} prod c0={c[0][0]:7.3f} c1={c[0][1]:7.2f} | exp c0={c[1][0]:7.3f} c1={c[1][1]:7.2f}")
