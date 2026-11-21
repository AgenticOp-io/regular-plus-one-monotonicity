# r49: read r49_enum output on stdin, report roots of P_H(z)=sum N_j z^j (exact via mpmath 50 digits if present)
import sys, mpmath as mp
mp.mp.dps=50
hdr=sys.stdin.readline(); print(hdr.strip()); worst=(-1e9,None); nearest=(1e9,None); minz=None
for line in sys.stdin:
    t=line.split(); name=t[0]; c=[int(x) for x in t[1:]]
    while c and c[-1]==0: c.pop()
    if len(c)<2: continue
    lo=0
    while c[lo]==0: lo+=1   # root at 0 with multiplicity lo
    r=mp.polyroots(c[lo:][::-1],maxsteps=500,extraprec=200) if len(c)-lo>1 else []
    mr=max([x.real for x in r]+[mp.mpf(0)]) if r else mp.mpf(0)
    d1=min([abs(x-1) for x in r]) if r else mp.inf
    mi=max([abs(x.imag) for x in r]+[0])
    print(f"{name:7s} deg{len(c)-1} zeroMult{lo} maxRe(nonzero roots) {mp.nstr(max([x.real for x in r]),6) if r else '-'} maxIm {mp.nstr(mi,4)} dist_to_1 {mp.nstr(d1,5)} maxRe_over_|root| {mp.nstr(max([x.real/abs(x) for x in r]),4) if r else '-'}")
    if r:
        m=max(x.real for x in r)
        if m>worst[0]: worst=(m,name)
        if d1<nearest[0]: nearest=(d1,name)
print("WORST maxRe",mp.nstr(worst[0],8),worst[1],"| NEAREST to 1",mp.nstr(nearest[0],8),nearest[1])
