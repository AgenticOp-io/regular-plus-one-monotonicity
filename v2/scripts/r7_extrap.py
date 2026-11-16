# r7: D-extrapolation of c0(D), D=5..10: model L: a+b ln D  vs  model R: a+b*D/(D+s) (best s on grid). Reports rms and R-limit a+b.
import numpy as np
D=np.arange(5,11.)
data={'S1_0_0':[.64,.83,.98,1.09,1.19,1.26],'S1_1_1':[.09,.89,1.58,2.15,2.65,3.11],'S2_2_0':[-.90,.64,1.91,2.92,3.71,4.33],'S3_3_3':[-7.90,-4.79,-1.47,1.85,5.25,9.04]}
for k,y in data.items():
    y=np.array(y); X=np.vstack([D**0,np.log(D)]).T; c=np.linalg.lstsq(X,y,rcond=None)[0]; rl=np.sqrt(np.mean((X@c-y)**2))
    best=min(((np.sqrt(np.mean((np.vstack([D**0,D/(D+s)]).T@np.linalg.lstsq(np.vstack([D**0,D/(D+s)]).T,y,rcond=None)[0]-y)**2)),s) for s in np.arange(0.5,200,.5)))
    s=best[1]; q=np.linalg.lstsq(np.vstack([D**0,D/(D+s)]).T,y,rcond=None)[0]
    print(f"{k}: log fit rms={rl:.3f} (b={c[1]:.2f}); rational rms={best[0]:.3f} s={s} limit={q[0]+q[1]:.2f}")
