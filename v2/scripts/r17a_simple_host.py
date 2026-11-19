# Exact Delta(H)=log Q(H)-log Q(empty), Q(H)=P(pairing simple | fixed point-level host H).
# Q(H)=g(H)*prod(D-h_v)!/(N-2L-1)!!, g(H)=#simple D-regular graphs containing H (r16w1_cluster.count).
import sys; from math import log, lgamma, factorial
from r16w1_cluster import count
def lf2(m):  # log (m)!! for odd m
    return sum(log(k) for k in range(m,0,-2))
def logQ(n,D,H,Z):
    N=n*D; L=len(H); h=[0]*n
    for a,b in H: h[a]+=1; h[b]+=1
    g=count(n,D,H)
    return log(g)+sum(log(factorial(D-x)) for x in h)-lf2(N-2*L-1)
shapes={'e':[(0,1)],'P3':[(0,1),(1,2)],'2e':[(0,1),(2,3)],'tri':[(0,1),(1,2),(0,2)],'P4':[(0,1),(1,2),(2,3)],'3e':[(0,1),(2,3),(4,5)]}
if __name__=='__main__':
    D=int(sys.argv[1])
    for n in map(int,sys.argv[2:]):
        Z=count(n,D,[]); base=log(Z)+n*log(factorial(D))-lf2(n*D-1)
        # sanity: Q(empty) must be a probability
        assert base<0
        print('D',D,'n',n,'logQ0 %.5f'%base,{k:'%.6e'%(logQ(n,D,H,Z)-base) for k,H in shapes.items()},flush=True)
