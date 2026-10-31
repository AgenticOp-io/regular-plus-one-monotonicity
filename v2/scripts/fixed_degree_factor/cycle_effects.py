# exact config-model cycle effect: E[Z * 1(C present)] / (E Z * P(C present)) for a fixed k-cycle C
from math import comb, lgamma, exp, log
def lM(N): return lgamma(N+1)-lgamma(N/2+1)-(N/2)*log(2)
def effect(n,d,m,k):
    # vertex weights by number j of the 2 cycle points chosen
    w=[(comb(d-2,m-j) if m-j>=0 else 0)/comb(d,m) for j in range(3)]
    tot=0.0
    for mask in range(1<<k):  # edge i in factor iff bit i
        s=bin(mask).count('1'); pr=1.0
        for v in range(k):
            j=((mask>>v)&1)+((mask>>((v-1)%k))&1); pr*=w[j]
        if pr==0: continue
        tot+=pr*exp(lM(m*n-2*s)+lM((d-m)*n-2*(k-s))-lM(m*n)-lM((d-m)*n)+lM(d*n)-lM(d*n-2*k))
    return tot-1
for d,m in [(4,1),(4,2),(6,2),(6,3),(7,3)]:
    print(d,m,[ (round(effect(200000,d,m,k),6), round((-1/(d-1))**k,6)) for k in (3,4,5)])
