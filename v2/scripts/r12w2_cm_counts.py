# r12w2: (a) check CM leading-order counts vs exact-uniform simple D-regular graphs (pairing+rejection), (b) rerun r11w3 c0 with corrected E(t)_2.
# usage: python r12w2_cm_counts.py mc | sym
import sys, numpy as np, itertools
def sample(n,D,rng):
    st=np.repeat(np.arange(n),D)
    while True:
        p=rng.permutation(st); a,b=p[0::2],p[1::2]
        if (a==b).any(): continue
        lo,hi=np.minimum(a,b),np.maximum(a,b); k=lo*n+hi
        if len(np.unique(k))<len(k): continue
        A=np.zeros((n,n),int); A[a,b]=1; A[b,a]=1; return A
def stats(A):
    n=len(A); D=A.sum(1)[0]; C=A@A; np.fill_diagonal(C,0)
    T=(A*C)                       # t(u,v) on edges
    t2=(T*(T-1)).sum()            # sum over directed edges (t)_2 = 4*diamonds
    tri=T.sum()/6
    # C4 (4-cycles): sum_{u<v} C(c,2) over all pairs /2
    c4=(C*(C-1)/2).sum()/4
    return tri,t2,c4
def mc(D,n,N,seed=1):
    rng=np.random.default_rng(seed); s=np.zeros(3)
    for _ in range(N): s+=stats(sample(n,D,rng))
    return s/N
if sys.argv[1]=='mc':
    for D in (3,4):
        for n in (16,32,64):
            N=3000 if D==4 else 6000
            tri,t2,c4=mc(D,n,N)
            # CM leading predictions
            ptri=(D-1)**3/6; pt2=(D-1)**4*(D-2)**2*n*D/(n*D)**0*1.0/(n*D)*n*D/ (D*D) *D/ D  # placeholder, replaced below
            pt2=n*D*((D-1)**2*(D-2)/(n*D))**2*1.0   # sum_dir (t)_2 = nD * E(t)_2 ; E(t)_2=(D-1)^4(D-2)^2/(nD)^2
            pt2_old=n*D*((D-1)**3/(n*D))**2
            pc4=(D-1)**4/8                           # 4-cycles in CM, O(1)
            print(f'D={D} n={n} N={N}: tri {tri:.3f} (pred {ptri:.3f}) | sum(t)_2 {t2:.4f} new {pt2:.4f} old {pt2_old:.4f} ratio_new {t2/pt2:.3f} | C4 {c4:.3f} (pred {pc4:.3f})',flush=True)
else:
    import sympy as sp
    n,D,x=sp.symbols('n D x',positive=True)
    ff=lambda a,m: sp.prod([a-i for i in range(m)]) if m>0 else sp.Integer(1)
    def c0(j,k,et2,r1=3*(D-1)/D):
        F=lambda t: sum(sp.binomial(j,c)*ff(t,c)*ff(D-1-t,j-c)*ff(D-1-c,k) for c in range(0,min(j,t)+1))
        F0,F1,F2=F(0),F(1)-F(0),F(2)-2*F(1)+F(0)
        Et=(D-1)**3/(n*D)*(1+r1/n)
        N2=n*D*(F0+F1*Et+F2*et2/2)
        g=lambda s: ff(D-s,k); gm=[sum((-1)**(m-i)*sp.binomial(m,i)*g(i) for i in range(m+1)) for m in range(3)]
        eL=sp.binomial(j,2)*(D-1)**2/(n*D)
        pairs=j*(D-j)*(D-1)**2/(n*D)+sp.binomial(j,2)*(D-1)**3/(n*D)
        N1=n*ff(D,j)*((n-1-j)*gm[0]+gm[1]*((j+1)*D-2*j-2*eL)+gm[2]*pairs)
        P=N2/N1; du,dv=D-j,D-k; leaves=[D-1]*(j+k)
        M=n*D-2*(j+k); M2=du*(du-1)+dv*(dv-1)+sum(d*(d-1) for d in leaves)+(n-2-len(leaves))*D*(D-1)
        A=M2**2/M**3+M2/M**2
        phi=-2*(du+dv)+2-j*(D-1)-k*(D-1)-(du+dv-2)*M2/M+du*dv
        err=(P/(du*dv/M*sp.exp(-A-phi/M))-1).subs(n,1/x)
        s=sp.series(err,x,0,3).removeO()
        return [sp.factor(sp.simplify(s.coeff(x,i))) for i in range(3)]
    old=((D-1)**3/(n*D))**2; new=((D-1)**2*(D-2)/(n*D))**2
    for j,k in [(2,2),(3,2),(3,3)]:
        a,b=c0(j,k,old),c0(j,k,new)
        print(j,k,'old',a[1:],'\n   new',b[1:],'\n   lim new',sp.limit(b[2],D,sp.oo),'vs',(j+k+1)**2/2,flush=True)
