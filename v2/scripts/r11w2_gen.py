# r11w2: large-n exact E[T] ratio R_n=E[T]/((D-1)^3/6)=P*n*D/(D-1)^2 from the r7_star DP (host S1_1_1). usage: r11w2_gen.py BIN D n1 n2 ... -> lines "D n R"
import sys, subprocess
from multiprocessing import Pool
def run(a):
    b,D,n=a
    for l in subprocess.run([b,str(D),str(n)],capture_output=True,text=True).stdout.split('\n'):
        t=l.split()
        if len(t)==6 and t[2:5]==['1','1','1']: return f"{D} {n} {float(t[5])*n*D/(D-1)**2:.15f}"
if __name__=='__main__':
    b,D=sys.argv[1],int(sys.argv[2]); ns=[int(x) for x in sys.argv[3:] if int(x)*D%2==0]
    with Pool(6) as p:
        for s in p.imap_unordered(run,[(b,D,n) for n in ns]): print(s,flush=True)
