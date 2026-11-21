# Pairing relvar vs predicted (1-x)^(-1/2)-1, x=1/(d-1); n-correction n*(relvar-lim) across m incl. band m~d/2.
from r54_pairing_relvar import relvar
for d in (6,12,24,40):
    x=1/(d-1); lim=(1-x)**-.5-1
    for m in sorted({1,2,d//4,d//2-1,d//2,d//2+1,3*d//4}):
        if not 1<=m<d: continue
        r=[relvar(n,d,m) for n in (400,1600)]
        print(d,m,f"rel.err@1600={(r[1]/lim-1):+.2e}",f"n*(rv-lim)@400={400*(r[0]-lim):+.4f}",f"@1600={1600*(r[1]-lim):+.4f}",f"coef/d^2={1600*(r[1]-lim)/d**2:+.4f}")
