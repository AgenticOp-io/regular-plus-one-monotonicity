# r8w3: c0(D) for all r7 star hosts (fit n^2*err_exp = c0+c1/n+c2/n^2, same as r6_fit), then fit c0 = poly_deg(1/D) on D>=5 and print D->inf limit
import sys,collections,numpy as np,os
base=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','notes','r7_data')
d=collections.defaultdict(list)
for D in range(3,11):
    for l in open(f'{base}/d{D}.txt'):
        t=l.split()
        if len(t)==5: d[(D,t[1])].append((int(t[2]),float(t[4])))
c0={}
for k,v in d.items():
    v=sorted(v); 
    if len(v)<3: continue
    n=np.array([x[0] for x in v],float); y=np.array([x[1] for x in v])
    c0[k]=np.linalg.lstsq(np.vstack([n**0,1/n,1/n**2]).T,y,rcond=None)[0][0]
hosts=sorted({k[1] for k in c0})
for h in hosts:
    Ds=[D for D in range(3,11) if (D,h) in c0]
    if len(Ds)<6: continue
    y=np.array([c0[(D,h)] for D in Ds]); D=np.array(Ds,float)
    out=[]
    for deg in (2,3,4):
        m=D>=4; X=np.vstack([D[m]**-i for i in range(deg+1)]).T
        c=np.linalg.lstsq(X,y[m],rcond=None)[0]; out.append(f"deg{deg}: lim={c[0]:6.2f} rms={np.sqrt(np.mean((X@c-y[m])**2)):.3f}")
    print(f"{h:8s} c0(D=10)={y[-1]:6.2f}  "+"  ".join(out))
# --- conjecture test: c0(D->inf) = (j+k+w+1)^2/2.  Fit c0 = L + b/D + c/D^2 (limit pinned) vs free a+b/D+c/D^2, D>=5; compare rms.
print("\nconj L=(j+k+w+1)^2/2 pinned (2 free params) vs free limit (3 params), D=5..10; rms of fit")
for h in hosts:
    j,k,w=map(int,h[1:].split('_'))
    if j<k or (j,k,w)==(0,0,0) or len([D for D in range(3,11) if (D,h) in c0])<8: continue
    D=np.arange(5,11.); y=np.array([c0[(int(d),h)] for d in D]); L=(j+k+w+1)**2/2
    X=np.vstack([D**-1,D**-2]).T; c=np.linalg.lstsq(X,y-L,rcond=None)[0]; rp=np.sqrt(np.mean((X@c+L-y)**2))
    X3=np.vstack([D**0,D**-1,D**-2]).T; c3=np.linalg.lstsq(X3,y,rcond=None)[0]; rf=np.sqrt(np.mean((X3@c3-y)**2))
    print(f"{h:8s} L={L:6.1f} pinned rms={rp:.3f} | free lim={c3[0]:6.2f} rms={rf:.3f}")
