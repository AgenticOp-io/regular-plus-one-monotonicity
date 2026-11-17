# r11w2: fit R_n-1 = r1/n + r2/n^2 + ... from exact DP data (files D n R); prints r1 (check 3(D-1)/D) and r2 for several orders/windows.
import sys, numpy as np
from mpmath import mp, matrix, lu_solve, mpf
mp.dps=30
for f in sys.argv[1:]:
    t=[l.split() for l in open(f) if len(l.split())==3 and l.split()[2]!='None']
    D=int(t[0][0]); pts=sorted((int(a[1]),mpf(a[2])) for a in t)
    print(f'D={D} npts={len(pts)} n in [{pts[0][0]},{pts[-1][0]}]  3(D-1)/D={3*(D-1)/D:.6f}')
    for K in (4,5,6,7,8):
        for lo in (0,2):
            P=pts[lo:][-K:] if lo==0 else pts[lo:lo+K] # lo=0: largest-n K pts; lo=2: K pts skipping 2 smallest
            if len(P)<K: continue
            A=matrix(K,K); b=matrix(K,1)
            for i,(n,R) in enumerate(P):
                for k in range(K): A[i,k]=mpf(1)/n**(k+2)
                b[i]=R-1-(mpf(3*(D-1))/D)/n  # r1 fixed (verified free fit to 1e-5)
            c=lu_solve(A,b); print(f'  K={K} {"top" if lo==0 else "skip2"}: r2={float(c[0]):.6f} r3={float(c[1]):.4f} r4={float(c[2]):.3f}')
