# r9w3: cross-check of the E[T] reduction. r2(D) extracted from S1_1_1 data; predict c0 of S1_1_0 (path w-u-v-x) independently.
# Exact: P(uv|uw,vx)=[nD(D-1)^2-6E[T]]/[nD(nD-4D+2)]  (ordered 3-paths = 2e(D-1)^2-6T; disjoint directed edge pairs nD(nD-4D+2)).
import sympy as sp, numpy as np, os, collections
n,D,x,r1,r2=sp.symbols('n D x r1 r2')
def gao(dt):  # dt: dict u,v,... remaining degrees; same formula as r7_run.gao (W=0), leaves given as list
    pass
def c0_sym(j,k,w,PE):
    # PE(n,D,ET) -> exact P; ET = (D-1)^3/6*(1+r1 x+r2 x^2)
    du,dv=D-j,D-k; leaves=[D-2]*w+[D-1]*(j-w)+[D-1]*(k-w)
    M=n*D-(j+k+2*w+ (j-w)+(k-w) - 0)  # removed half-edges: j+k edges -> 2(j+k)... computed below
    M=n*D-2*(j+k)
    M2=du*(du-1)+dv*(dv-1)+sum(d*(d-1) for d in leaves)+(n-2-len(leaves))*D*(D-1)
    A=M2**2/M**3+M2/M**2
    su=(D-2)*w+(D-1)*(j-w); sv=(D-2)*w+(D-1)*(k-w)
    phi=-2*(du+dv)+2-su-sv-(du+dv-2)*M2/M+du*dv
    ET=(D-1)**3/6*(1+r1*x+r2*x**2)
    err=(PE(ET)/(du*dv/M*sp.exp(-A-B_(phi,M)))-1).subs(n,1/x); return err
def B_(phi,M): return phi/M
P111=lambda ET: 6*ET/(n*D*(D-1))
P110=lambda ET: (n*D*(D-1)**2-6*ET)/(n*D*(n*D-4*D+2))
r1v=3*(D-1)/D
out={}
for name,(j,k,w),PE in (('S1_1_1',(1,1,1),P111),('S1_1_0',(1,1,0),P110)):
    s=sp.series(c0_sym(j,k,w,PE),x,0,3).removeO()
    cs=[sp.simplify(s.coeff(x,i).subs(r1,r1v)) for i in range(3)]
    print(name,'n^0:',cs[0],' n^-1:',sp.factor(cs[1]),' c0(r2)=',sp.factor(cs[2])); out[name]=cs[2]
# data c0 via same fit as r8w3_extrap
base=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','notes','r7_data'); d=collections.defaultdict(list)
for Dv in range(3,11):
    for l in open(f'{base}/d{Dv}.txt'):
        t=l.split()
        if len(t)==5: d[(Dv,t[1])].append((int(t[2]),float(t[4])))
def c0d(Dv,h):
    v=sorted(d[(Dv,h)]); nn=np.array([a for a,_ in v],float); y=np.array([b for _,b in v])
    return np.linalg.lstsq(np.vstack([nn**0,1/nn,1/nn**2]).T,y,rcond=None)[0][0]
print('D  c0data(S111)  r2(D)   pred c0(S110)  data c0(S110)')
for Dv in range(4,11):
    c111=c0d(Dv,'S1_1_1'); r2v=sp.solve(sp.Eq(out['S1_1_1'].subs(D,Dv),c111),r2)[0]
    pred=float(out['S1_1_0'].subs({D:Dv,r2:r2v})); print(Dv,f"{c111:8.3f} {float(r2v):8.3f} {pred:10.3f} {c0d(Dv,'S1_1_0'):10.3f}")
# --- r2(D) shape: r2 = a + b/D + c/D^2 (D>=5) free vs a pinned at 25/2 (=c0 limit 8 + 9/2); and log-growth alternative
Ds=np.arange(5,11.); R=np.array([float(sp.solve(sp.Eq(out['S1_1_1'].subs(D,int(Dv)),c0d(int(Dv),'S1_1_1')),r2)[0]) for Dv in Ds])
X=np.vstack([Ds**0,1/Ds,1/Ds**2]).T; c=np.linalg.lstsq(X,R,rcond=None)[0]; print('r2 free poly(1/D): a,b,c=',c,'rms',np.sqrt(np.mean((X@c-R)**2)))
Xp=np.vstack([1/Ds,1/Ds**2]).T; cp=np.linalg.lstsq(Xp,R-12.5,rcond=None)[0]; print('pinned a=12.5: b,c=',cp,'rms',np.sqrt(np.mean((Xp@cp+12.5-R)**2)))
Xl=np.vstack([Ds**0,np.log(Ds),1/Ds]).T; cl=np.linalg.lstsq(Xl,R,rcond=None)[0]; print('a+b lnD+c/D:',cl,'rms',np.sqrt(np.mean((Xl@cl-R)**2)))
