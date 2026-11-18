# fit r2(D) from exact E[T] data (r13w1_d{D}.txt from r13w1_et.exe; D=3 from r11w1_d3.txt); r1=3(D-1)/D fixed
import numpy as np, os
from fractions import Fraction
h=os.path.dirname(os.path.abspath(__file__))
for D,f in ((3,'r11w1_d3.txt'),(4,'r13w1_d4.txt'),(5,'r13w1_d5.txt'),(6,'r13w1_d6.txt')):
    a=np.loadtxt(f'{h}/{f}'); n=a[:,0]; y=n**2*(a[:,1]-1-3*(D-1)/D/n)
    for nmin in (30,45):
      for deg in (4,5,6):
        m=n>=nmin; X=np.vstack([n[m]**-i for i in range(deg+1)]).T
        c=np.linalg.lstsq(X,y[m],rcond=None)[0]
        print(D,nmin,deg,'r2=%.6f r3=%.4f'%(c[0],c[1]), Fraction(c[0]).limit_denominator(200))
