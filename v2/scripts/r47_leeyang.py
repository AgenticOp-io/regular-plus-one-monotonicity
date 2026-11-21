# Lee-Yang test: P_H(z)=sum_{G simple D-regular on [n]} z^{|E(G)∩H|}, H = k-cycle/path host. Are roots real/negative?
import itertools, numpy as np, sys
def regs(n,D):
    E=list(itertools.combinations(range(n),2)); out=[]
    deg=[0]*n; cur=[]
    def rec(i):
        if i==len(E):
            if all(d==D for d in deg): out.append(frozenset(cur))
            return
        u,v=E[i]
        # prune: vertex u finished after its last edge (u,n-1)
        rem_u=n-1-v; 
        if deg[u]<D and deg[v]<D:
            deg[u]+=1;deg[v]+=1;cur.append(E[i]);rec(i+1);cur.pop();deg[u]-=1;deg[v]-=1
        if v==n-1 and deg[u]!=D: return
        if deg[u]+ (n-1-v) >= D:
            rec(i+1)
    rec(0); return out
if __name__=="__main__":
  for n,D in [(8,3),(8,4),(7,4)]:
      G=regs(n,D); print("n,D,#",n,D,len(G))
      for k,cyc in [(3,1),(4,1),(5,1),(6,1),(8,1),(7,0),(5,0)]:
          H={tuple(sorted((i,(i+1)%k))) for i in range(k)} if cyc else {(i,i+1) for i in range(k)}
          c=np.zeros(len(H)+1)
          for g in G: c[len(g&H)]+=1
          while c[-1]==0: c=c[:-1]
          r=np.roots(c[::-1]) if len(c)>1 else []
          print(" k",k,"cyc" if cyc else "path","N_j",c.astype(int).tolist(),"maxImag",float(np.max(abs(np.imag(r)))) if len(r) else 0,"maxRe",float(np.max(np.real(r))) if len(r) else 0)
