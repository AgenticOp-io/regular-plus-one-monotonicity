# r10w3: (1) r2(D) of triangle count from S1_1_1 data, shape tests incl. 1/D^3 and hold-out D=3,4, window-bias;
# (2) does c0 -> (j+k+w+1)^2/2 hold for ALL star hosts in r7_data (free vs pinned fit)?
import numpy as np, collections, os, re
base=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','notes','r7_data'); d=collections.defaultdict(list)
for Dv in range(3,11):
    for l in open(f'{base}/d{Dv}.txt'):
        t=l.split()
        if len(t)==5: d[(Dv,t[1])].append((int(t[2]),float(t[4])))
def c0d(Dv,h,drop=0):
    v=sorted(d[(Dv,h)]); v=v[drop:]; nn=np.array([a for a,_ in v],float); y=np.array([b for _,b in v])
    return np.linalg.lstsq(np.vstack([nn**0,1/nn,1/nn**2]).T,y,rcond=None)[0][0]
r2=lambda c,D:(2*D*D*c+9*D*D+30*D-67)/(2*D*D)   # exact inversion of c0(S1_1_1) (r9w3_tri)
print('r2(D) vs fit-window drop (drop smallest n points):')
for Dv in range(3,11): print(Dv,[round(r2(c0d(Dv,'S1_1_1',k),Dv),3) for k in (0,2,4)])
Ds=np.arange(5,11.); R=np.array([r2(c0d(int(x),'S1_1_1'),x) for x in Ds])
for deg in (2,3):
    X=np.vstack([Ds**-i for i in range(deg+1)]).T; c=np.linalg.lstsq(X,R,rcond=None)[0]
    Dh=np.array([3.,4.]); Xh=np.vstack([Dh**-i for i in range(deg+1)]).T
    print('deg',deg,'free coef',c.round(3),'rms',np.sqrt(np.mean((X@c-R)**2)).round(4),'holdout D=3,4 pred',(Xh@c).round(2),'data',[round(r2(c0d(int(x),'S1_1_1'),x),2) for x in Dh])
print('\nall star hosts: D>=5 free a+b/D+c/D^2 limit vs L=(j+k+w+1)^2/2, pinned rms')
hosts=sorted({h for (_,h) in d}); 
for h in hosts:
    j,k,w=map(int,re.findall(r'\d+',h)); 
    if j==0 and k==0: continue
    Dv=[x for x in range(5,11) if len(d[(x,h)])>=4 and x>=max(j,k)+1]
    if len(Dv)<4: continue
    y=np.array([c0d(x,h) for x in Dv]); Dv=np.array(Dv,float); L=(j+k+w+1)**2/2
    X=np.vstack([Dv**0,1/Dv,1/Dv**2]).T; c=np.linalg.lstsq(X,y,rcond=None)[0]
    Xp=X[:,1:]; cp=np.linalg.lstsq(Xp,y-L,rcond=None)[0]
    print(f'{h:8s} nD={len(Dv)} free a={c[0]:7.2f} L={L:6.2f} rms={np.sqrt(np.mean((X@c-y)**2)):.3f} pinned rms={np.sqrt(np.mean((Xp@cp+L-y)**2)):.3f}')
