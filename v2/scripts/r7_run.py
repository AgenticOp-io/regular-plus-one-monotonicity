# r7 driver: python r7_run.py D n1 n2 ... -> lines "D name n prod_n2err exp_n2err" (star hosts at u,v; name=S{j}_{k}_{w}); uses ./r7_star
import sys, os, subprocess
from math import exp
from multiprocessing import Pool
def gao(n,D,j,k,w):
    dt=[D]*n; dt[0]-=j; dt[1]-=k   # u=0,v=1; leaves: w common (-2), j-w at u, k-w at v
    for i in range(w): dt[2+i]-=2
    for i in range(j-w): dt[2+w+i]-=1
    for i in range(k-w): dt[2+w+j-w+i]-=1
    M=sum(dt); M2=sum(x*(x-1) for x in dt)
    A=M2**2/M**3+M2/M**2   # W=0: every host edge touches u or v
    su=sum(dt[2+i] for i in range(j)); sv=sum(dt[2+i] for i in range(w))+sum(dt[2+j+i] for i in range(k-w))
    phi=-2*(dt[0]+dt[1])+2-su-sv-(dt[0]+dt[1]-2)*M2/M+dt[0]*dt[1]
    return dt[0]*dt[1]/M,A,phi/M
def run(a):
    D,n=a; out=[]
    exe=os.path.join(os.path.dirname(os.path.abspath(__file__)),'r7_star')
    for l in subprocess.run([exe,str(D),str(n)],capture_output=True,text=True).stdout.split('\n'):
        t=l.split()
        if len(t)!=6: continue
        j,k,w=map(int,t[2:5]);P=float(t[5]);base,A,B=gao(n,D,j,k,w)
        out.append(f"{D} S{j}_{k}_{w} {n} {(P/(base*(1-A)*(1-B))-1)*n*n:.5f} {(P/(base*exp(-A-B))-1)*n*n:.5f}")
    return "\n".join(out)
if __name__=='__main__':
    D=int(sys.argv[1]); ns=[int(x) for x in sys.argv[2:] if (int(x)*D)%2==0]
    with Pool(8) as p:
        for s in p.imap_unordered(run,[(D,n) for n in ns]): print(s,flush=True)
