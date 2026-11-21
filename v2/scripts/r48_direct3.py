"""r48 step 3: direct k=3 term  Sum_j [lnZ3_j(y_j; m=0) - lnZ3_j(1; m=0)]  along the backward recursion (gamma2 only).
Scaling in n, L. Also the same for lnZ2 and for the m=0 value's m-slope contribution is in r48_gamma3.py."""
import mpmath as mp, sys, sympy as sp
sys.path.insert(0,'v2/scripts')
import r48_gamma3 as g
mp.mp.dps=60
F3=sp.lambdify((g.n,g.L,g.u,g.a),g.lnZ3.subs(g.m,0),'mpmath')
F2=sp.lambdify((g.n,g.L,g.u,g.a),g.lnZ2.subs(g.m,0),'mpmath')
f2=g.f2
def go(N,LL,x):
    ys=g.run(N,LL,x,[f2]); N=mp.mpf(N); LL_=mp.mpf(LL)
    s3=sum(F3(N,LL_,mp.mpf(j-1),ys[j-1]-1)-F3(N,LL_,mp.mpf(j-1),0) for j in range(1,LL+1))
    s2=sum(F2(N,LL_,mp.mpf(j-1),ys[j-1]-1)-F2(N,LL_,mp.mpf(j-1),0) for j in range(1,LL+1))
    return s3,s2
print("n L | S3 | S3 n^2/L^3 | S3 n^2/L^4 | S3 n^2/L^5 ; S2 for ref")
for N in (10**6,10**8):
    for LL in (10,30,100,300):
        if LL*LL>N/2: continue
        s3,s2=go(N,LL,2)
        print(N,LL,mp.nstr(s3,4),*[mp.nstr(s3*N**2/LL**p,4) for p in (3,4,5)],"| S2",mp.nstr(s2,5)); sys.stdout.flush()
