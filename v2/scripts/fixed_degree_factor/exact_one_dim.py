import itertools, math
from fractions import Fraction as Fr
from math import comb

def pairings(pts):
    if not pts: yield []; return
    a=pts[0]
    for i in range(1,len(pts)):
        rest=pts[1:i]+pts[i+1:]
        for p in pairings(rest): yield [(a,pts[i])]+p

def brute(n,d,m):
    pts=list(range(n*d)); v=lambda x:x//d
    s1=s2=0; cnt=0
    for P in pairings(pts):
        cnt+=1; z=0; E=len(P)
        for mask in range(1<<E):
            deg=[0]*n
            for i in range(E):
                if mask>>i&1:
                    a,b=P[i]; deg[v(a)]+=1; deg[v(b)]+=1
            if all(x==m for x in deg): z+=1
        s1+=z; s2+=z*z
    return Fr(s2*cnt, s1*s1)

def M(N):
    if N<0 or N%2: return 0
    r=1
    for k in range(N-1,0,-2): r*=k
    return r

def formula(n,d,m):
    # pmf of S = sum of n hypergeometric(d,m,m)
    h=[Fr(comb(m,a)*comb(d-m,m-a),comb(d,m)) for a in range(m+1)]
    pmf=[Fr(1)]
    for _ in range(n):
        new=[Fr(0)]*(len(pmf)+m)
        for i,p in enumerate(pmf):
            for a,q in enumerate(h): new[i+a]+=p*q
        pmf=new
    num=sum(p*M(A)*M(m*n-A)**2*M((d-2*m)*n+A) for A,p in enumerate(pmf))
    return num*M(d*n)/Fr(M(m*n)*M((d-m)*n))**2

for (n,d,m) in [(4,3,1),(4,3,2),(6,2,1),(2,4,1),(2,4,2),(4,2,1)]:
    b=brute(n,d,m); f=formula(n,d,m)
    print(n,d,m,b,f,b==f)
