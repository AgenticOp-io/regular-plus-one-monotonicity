import sys; sys.path.insert(0,'v2/scripts')
from r6_tilt import *
hb,D=12,9; beta=D/((hb-D)*hb**2)
for ys,w in (([-1,0,1],[1,2,1]),([-2,-1,0,1,2],[1,4,6,4,1])):
    for n in (240,960,1920):
        tot=sum(w); cnt=[n*x//tot for x in w]; assert sum(cnt)==n
        sg=sum(c*y*y for c,y in zip(cnt,ys))/n; K=n*D*D*sg*sg/(2*9*hb**3)
        r=run(n,hb,D,ys,cnt,[0,-beta,-0.8*beta,-1.2*beta],N=2000)
        print(ys,"n",n,"sigma2 %.2f K %.2f"%(sg,K),[(round(t,4),round(float(v),3)) for t,v,_ in r],flush=True)
