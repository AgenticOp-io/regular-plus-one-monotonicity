from math import comb, log, exp
def xlogx(x): return 0.0 if x<=0 else x*log(x)
worst=(1e9,None)
for d in range(3,81):
    for m in range(1,d):
        lo=max(0,2*m-d); a0=m*m/d
        lh=[log(comb(m,a)*comb(d-m,m-a)/comb(d,m)) if comb(m,a)*comb(d-m,m-a)>0 else None for a in range(m+1)]
        sup=[a for a in range(m+1) if lh[a] is not None]
        def Lam(t):
            mx=max(lh[a]+t*a for a in sup); return mx+log(sum(exp(lh[a]+t*a-mx) for a in sup))
        def mean(t):
            mx=max(lh[a]+t*a for a in sup); w=[exp(lh[a]+t*a-mx) for a in sup]
            return sum(a*x for a,x in zip(sup,w))/sum(w)
        psi=lambda al: 0.5*(xlogx(al)+2*xlogx(m-al)+xlogx(d-2*m+al))-0.5*(2*xlogx(m)+2*xlogx(d-m)-xlogx(d))
        N=200
        for i in range(1,N):
            al=lo+(m-lo)*i/N
            if abs(al-a0)<1e-12: continue
            a,b=-200.0,200.0
            for _ in range(200):
                c=(a+b)/2
                if mean(c)<al: a=c
                else: b=c
            t=(a+b)/2; I=t*al-Lam(t)
            g=(I-psi(al))/(al-a0)**2
            if g<worst[0]: worst=(g,(d,m,al))
print("min (I-psi)/(al-a0)^2:",worst)
