# Nearest zero R of P(y)=E y^T via r14w3_gen.exe (C, exact integer histogram) + companion-matrix eig (as r13w2).
# Usage: r14w3_zeros.py L n [dps]   (n<=11)
import sys, subprocess, mpmath as mp
from math import comb
L,n=int(sys.argv[1]),int(sys.argv[2]); dps=int(sys.argv[3]) if len(sys.argv)>3 else 100
out=subprocess.run([__file__.replace("zeros.py","gen.exe"),str(L),str(n)],capture_output=True,text=True).stdout.split("\n")
hd=out[0].split(); N,NF,NB=int(hd[1]),int(hd[3]),int(hd[5]); M=n*(n-1)//2
hist=[0]*(M+1)
for ln in out[1:]:
    if ln.startswith("B"):
        f=list(map(int,ln.split()[1:])); w=f[0]
        for t,v in enumerate(f[1:]): hist[t]+=w*v
assert sum(hist)==NF*N
if hist[0]==0: print(f"L={L} n={n} N={N} classes={NB} DEGENERATE P(0)=0 (R=1)"); sys.exit()
d=max(t for t in range(M+1) if hist[t])
c=[sum(hist[t]*comb(t,i) for t in range(i,d+1)) for i in range(d+1)]
mp.mp.dps=dps; a=[mp.mpf(x) for x in c]; k=d
C=mp.zeros(k,k)
for i in range(1,k): C[i,i-1]=1
for i in range(k): C[i,k-1]=-a[i]/a[k]
z=mp.eig(C,left=False,right=False); zz=min(z,key=abs); R=abs(zz)
res=abs(mp.polyval(a[::-1],zz))/sum(abs(a[i])*R**i for i in range(d+1))
print(f"L={L} n={n} N={N} classes={NB} deg={d} R={mp.nstr(R,8)} w={mp.nstr(zz,6)} R*L/n={mp.nstr(R*L/n,6)} relres={mp.nstr(res,2)}")
