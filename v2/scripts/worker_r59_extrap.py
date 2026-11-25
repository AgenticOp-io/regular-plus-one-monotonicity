# r59: Richardson extrapolation of c(D)=lim n^2*err/2 for B=2, exact DP (reuses r56_dp).
import sys, time
sys.setrecursionlimit(100000); import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r56_dp import lnP, G0
def err(n, D):
    d=[D]*n; x=d[:]; x[0]+=1; x[1]-=1
    return (lnP(x)-lnP(d))-(G0(x)-G0(d))
if __name__=="__main__":
    D=int(sys.argv[1])
    for n in map(int,sys.argv[2:]):
        if n*D%2: continue
        t=time.time(); e=err(n,D)
        print(n,D,repr(e),"n^2e/2=%.5f"%(e*n*n/2),"t=%.1f"%(time.time()-t),flush=True)
