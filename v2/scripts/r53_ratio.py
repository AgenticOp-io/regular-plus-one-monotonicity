# exact N(d) = #labelled simple graphs with degree seq d, via edge-DP; test dlnP vs dG0 (G0=-s2/2s1-s2^2/4s1^2)
import sys, itertools, math
from collections import defaultdict
def count(d):
    n=len(d); st={tuple([0]*n):1}
    for i,j in itertools.combinations(range(n),2):
        new=defaultdict(int)
        for s,c in st.items():
            new[s]+=c
            if s[i]<d[i] and s[j]<d[j]:
                t=list(s);t[i]+=1;t[j]+=1;new[tuple(t)]+=c
        st=new
    return st.get(tuple(d),0)
def pairings(d):
    m=sum(d);r=math.factorial(m)//(2**(m//2)*math.factorial(m//2))
    return r//math.prod(math.factorial(x) for x in d)*math.prod(math.factorial(x) for x in d)//1 if False else r
def lnP(d):  # P(simple)=N*prod d! / (m-1)!!
    m=sum(d);df=math.prod(range(m-1,0,-2))
    return math.log(count(d)*math.prod(math.factorial(x) for x in d)/df)
def G0(d):
    s1=sum(d);s2=sum(x*(x-1) for x in d);return -s2/(2*s1)-s2**2/(4*s1**2)
n=int(sys.argv[1]);D=int(sys.argv[2])
d=[D]*n;d2=d[:];d2[0]+=1;d2[1]-=1;d3=d[:];d3[0]+=1;d3[1]-=1;d3[2]+=1;d3[3]-=1
b=lnP(d)
for name,x in(("B=2",d2),("B=4",d3)):
    a=lnP(x)-b;g=G0(x)-G0(d);print(n,D,name,"dlnP=%.5f dG0=%.5f err=%.5f err*n^2/(B(D+B))=%.3f"%(a,g,a-g,(a-g)*n*n/(int(name[2])*(D+int(name[2])))))
