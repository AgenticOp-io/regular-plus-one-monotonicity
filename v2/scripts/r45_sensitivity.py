"""r45: test r43 gap-3 claim. Backward recursion y_L=x, y_j = x exp(sum_{k>j} gamma_k(y_k)),
gamma_k(y) = -(y-1)/(n-1) (r36 s3 leading form). Measures (a) Lipschitz const of the map y->G(y) (sup-norm,
row-sum), (b) response of y_j and S=sum_j j*(y_j-1) [f_j' ~ j, since kappa1 ~ L^2/2] to perturbation delta
in every gamma_k (delta = 1e-3*L^3/n^2 scaled, linear regime). Claim: (a)~O(L^2/n)."""
import numpy as np
def run(n,L,x,delta=None):
    d=np.zeros(L+1) if delta is None else delta
    y=np.zeros(L+2); y[L]=x; acc=0.0
    for j in range(L-1,0,-1):
        k=j+1; acc+=-(y[k]-1)/(n-1)+d[k]; y[j]=x*np.exp(acc)
    return y[1:L+1]
def lip(n,L,x):
    # exact Jacobian of G(y)_j wrt y_k (k>j): -y_j/(n-1)  (y fixed point approx) -> row sums
    y=run(n,L,x); J=np.array([(L-j)*y[j-1]/(n-1) for j in range(1,L)])
    return J.max()
for x in (2.0,):
  print("n L  L^2/n  Lip(a)  Lip/(L^2/n)  max|dy|/delta/L  dS/delta/L^2  (x=2)")
  for n in (10**4,10**6):
    for L in (10,30,100,300):
      if L*L>n/2: continue
      base=run(n,L,x); S0=sum(j*(base[j-1]-1) for j in range(1,L+1))
      delta=1e-6*L**3/n**2*1.0; rng=np.random.default_rng(0)
      d=delta*np.sign(rng.standard_normal(L+1)+1e-9)  # worst-ish sign pattern: all +
      d=np.abs(d)
      p=run(n,L,x,d); dy=np.abs(p-base).max()/delta
      dS=abs(sum(j*(p[j-1]-1) for j in range(1,L+1))-S0)/delta
      print(n,L,"%.2e %.2e %.3f %.3f %.3f"%(L*L/n,lip(n,L,x),lip(n,L,x)/(L*L/n),dy/L,dS/L**2))
