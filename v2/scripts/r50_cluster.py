r"""r50: exact degree-k (k<=4) cumulants c_k of ln Z, Z=E_M prod_{e in M} f_e, M uniform perfect matching on n pts,
f=1+t*w: w=a (=y-1) on F minus U, w=-1 on U (so f=0), 0 else. c_k=[t^k] ln sum_k q_k m_k t^k, q_k=1/((n-1)(n-3)..(n-2k+1)).
F random L-regular (or circulant), U random (j-1)-regular. m_k exact weighted k-matching sums via r50_match.exe."""
import subprocess, os, sys, random, numpy as np, networkx as nx, mpmath as mp
mp.mp.dps=40; HERE=os.path.dirname(os.path.abspath(__file__))
def ck(n,Fe,Ue,a):
    U=set(Ue); edges=[(u,v,-1.0) for u,v in Ue]+[(u,v,a) for u,v in Fe if (u,v) not in U]
    inp=f"{n} {len(edges)}\n"+"\n".join(f"{u} {v} {w}" for u,v,w in edges)
    out=subprocess.run([os.path.join(HERE,"r50_match.exe")],input=inp,capture_output=True,text=True).stdout.split()
    m=[mp.mpf(1)]+[mp.mpf(s) for s in out]
    q=[mp.mpf(1)]
    for k in range(1,5): q.append(q[-1]/(n-2*k+1))
    # ln(1+s1 t+..): series coefficients
    s=[q[k]*m[k] for k in range(5)]
    c1=s[1]; c2=s[2]-s[1]**2/2; c3=s[3]-s[1]*s[2]+s[1]**3/3
    c4=s[4]-s[1]*s[3]-s[2]**2/2+s[1]**2*s[2]-s[1]**4/4
    return [float(x) for x in (c1,c2,c3,c4)]
def edges_of(G): return [tuple(sorted(e)) for e in G.edges()]
def rr(n,d,seed): return edges_of(nx.random_regular_graph(d,n,seed=seed))
def circ(n,d): return edges_of(nx.circulant_graph(n,list(range(1,d//2+1))))
def sample(n,L,j,y,reps,mode="rand",seed0=0):
    res=[];ov=[]
    for r in range(reps):
        Fe=rr(n,L,seed0+r) if mode=="rand" else circ(n,L)
        Ue=rr(n,j-1,1000+seed0+r) if mode=="rand" else circ(n,j-1)
        if mode=="circshift": pass
        res.append(ck(n,Fe,Ue,y-1)); ov.append(len(set(Fe)&set(Ue)))
    return np.array(res),np.array(ov)
if __name__=="__main__":
    random.seed(1)
    print("== A: n-scaling, L=4,j=3,y=2 (random), mean c_k and fitted exponent")
    ns=[40,60,90,130]; M={}
    for n in ns:
        r,_=sample(n,4,3,2.0,8); M[n]=r.mean(0); print(n,["%.3e"%x for x in M[n]]); sys.stdout.flush()
    for k in (1,2,3):
        sl=np.polyfit(np.log(ns),np.log([abs(M[n][k]) for n in ns]),1)[0]; print(f"c_{k+1} ~ n^{sl:.2f}")
    print("== B: L-scaling at n=120, j=L/2+1 (j even-ish), y=2")
    for L in (4,6,8,10):
        r,_=sample(120,L,L//2+1 if (L//2+1)>1 else 2,2.0,6); print(L,["%.3e"%x for x in r.mean(0)])
