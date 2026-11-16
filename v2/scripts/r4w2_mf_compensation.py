"""Mean-field test: does the McKay exponent Phi(b;y) cancel the pairing-level y-dependence?
total(S) = log pi(S) + log f(S) + Phi_MF(S); log E-ratio ~ logsumexp_S total(S) - (first-moment McKay exponent)*2.
Phi_MF uses class vector b_v = tilted-mean of the cell overlap law (class sums at means, pairing sums at means)."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('scripts',1)[0]+'scripts')
from r4w2_pairing_shift import ldf, hyp_pmf

def cells(h, D):
    r = h - D
    return [(np.arange(max(0,2*rv-hv), rv+1), hyp_pmf(np.arange(max(0,2*rv-hv), rv+1), hv, rv, rv)) for hv,rv in zip(h,r)]

def tilt_means(C, theta):
    out=[]
    for ks,p in C:
        w=p*np.exp(theta*(ks-ks.mean())); w/=w.sum(); out.append((w*ks).sum())
    return np.array(out)

lam = lambda g: (g*(g-1)).sum()/(2*g.sum())
def pm(u, w):   # pairing sum mean: (sum c w)^2 / (2 sum c) with class sizes u
    return (u*w).sum()**2/(2*u.sum())

def Phi(h, D, b):
    r = h - D; c = r - b; s = h - 2*r + b
    Eb = -lam(b)-lam(b)**2
    E1 = -lam(c)-lam(c)**2 - pm(b,c)/c.sum()
    E2 = -lam(c)-lam(c)**2 - (pm(b,c)+pm(c,c))/c.sum()
    E4 = -lam(s)-lam(s)**2 - (pm(b,s)+2*pm(c,s))/s.sum()
    return Eb+E1+E2+E4

def first(h, D):   # E[Z 1_S]/E[Z] exponent
    r = h - D; Dv = np.full(len(h), float(D))
    return -lam(r)-lam(r)**2 - lam(Dv)-lam(Dv)**2 - pm(r, Dv)/Dv.sum()

def total(h, D, grid=None):
    C = cells(h, D); n=len(h)
    pmf=np.array([1.0])
    for ks,p in C: pmf=np.convolve(pmf,p) if ks[0]==0 else np.convolve(pmf, np.concatenate([np.zeros(0),p]))
    # offset-safe convolution
    off=sum(ks[0] for ks,_ in C); pmf=np.array([1.0])
    for ks,p in C: pmf=np.convolve(pmf,p)
    Sv=np.arange(len(pmf))+off
    r=h-D; th=h.sum(); tr=r.sum(); tD=D*len(h)
    best=[]
    mu=(Sv*pmf).sum(); sd=np.sqrt(((Sv-mu)**2*pmf).sum())
    for S in Sv:
        if S%2 or pmf[S-off]<=0 or abs(S-mu)>8*sd+60*abs(0): continue
        lo,hi=-0.5,0.5
        # find theta with sum tilt means = S (bisection on wide bracket)
        a,bb=-3.0,3.0
        for _ in range(60):
            m=(a+bb)/2
            if tilt_means(C,m).sum()<S: a=m
            else: bb=m
        b=tilt_means(C,(a+bb)/2)
        M1=(tr-S)/2; Ms=(tD-tr+S)/2
        lf=ldf(th/2)+ldf(S/2)+2*ldf(M1)+ldf(Ms)-2*ldf(tr/2)-2*ldf(tD/2)
        best.append((S, np.log(pmf[S-off])+lf, Phi(h.astype(float),D,b)))
    best=np.array(best); tot=best[:,1]+best[:,2]
    m=tot.max(); return m+np.log(np.exp(tot-m).sum()) - 2*first(h.astype(float),D), best

if __name__=="__main__":
    rng=np.random.default_rng(1)
    for n,hb,D in [(60,12,9),(120,12,9),(240,12,9)]:
        y=rng.integers(-1,2,n); y[:n//2]=np.abs(y[:n//2]); y[n//2:]=-y[:n//2]
        h0=np.full(n,hb); h1=hb+y
        v0,_=total(h0,D); v1,bst=total(h1,D)
        print(f"n={n} h={hb} D={D}: MF log-ratio incl Phi: regular {v0:.3f}  nonregular {v1:.3f}  (var y {y.var():.2f})")
