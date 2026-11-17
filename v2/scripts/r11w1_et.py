# writes+compiles the C++ exact DP, runs D=3 (n<=400) and D=4 (n<=160), saves r11w1_d{3,4}.txt next to r11w1_fit.py (needs g++)
import subprocess,os
h=os.path.dirname(os.path.abspath(__file__))
SRC=r'''// Exact E[#triangles] in uniform random D-regular graph on n vertices. g++ -O2 r11w1_et.cpp -o et ; ./et D nmax
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <array>
#include <unordered_map>
#include <functional>
#include <algorithm>
using namespace std; struct LD{ double m; int e; LD(double v=0):m(v),e(0){nm();} LD(double a,int b):m(a),e(b){nm();}
 void nm(){ if(m==0){e=0;return;} int k; m=frexp(m,&k); e+=k; }
 LD operator*(const LD&o)const{return LD(m*o.m,e+o.e);} LD&operator+=(const LD&o){ if(o.m==0)return *this; if(m==0){*this=o;return *this;} if(e>=o.e){ m+=ldexp(o.m,o.e-e);} else {m=o.m+ldexp(m,e-o.e);e=o.e;} nm(); return *this;}
 LD operator+(const LD&o)const{LD r=*this;r+=o;return r;} LD operator/(const LD&o)const{return LD(m/o.m,e-o.e);} double dbl()const{return ldexp(m,e);} }; typedef unsigned long long u64;
int D; unordered_map<u64,LD> memo; LD C[450][450];
LD N(array<int,5> c){ // c[j]=#vertices with residual j (j=1..D)
  int k=0; for(int j=D;j>=1;j--) if(c[j]){k=j;break;}
  if(!k) return LD(1.0);
  u64 key=0; for(int j=1;j<=D;j++) key=key<<16|c[j];
  auto it=memo.find(key); if(it!=memo.end()) return it->second;
  c[k]--; LD tot(0.0);
  function<void(int,int,array<int,5>,LD)> rec=[&](int j,int left,array<int,5> cur,LD w){
    if(j==0){ if(!left) tot+=w*N(cur); return;}
    for(int a=0;a<=min(left,c[j]);a++){ auto nw=cur; nw[j]-=a; if(j>=2) nw[j-1]+=a; rec(j-1,left-a,nw,w*C[c[j]][a]); }
  };
  rec(D,k,c,1); memo[key]=tot; return tot;
}
int main(int argc,char**argv){ D=atoi(argv[1]); int nmax=atoi(argv[2]);
  for(int i=0;i<450;i++){C[i][0]=LD(1.0);for(int j=1;j<=i;j++)C[i][j]=C[i-1][j-1]+(j<i?C[i-1][j]:LD(0.0));}
  for(int n=D+2;n<=nmax;n++){ if((n*D)%2) continue;
    array<int,5> c{}; c[D]=n; LD tot=N(c);
    int m=n-3; LD tri(0.0); int x[8];
    // enumerate column-type counts x[1..7]; row i (bit i) sum = D-2
    function<void(int,int*)> en=[&](int s,int*rows){
      if(s==8){ if(rows[0]!=D-2||rows[1]!=D-2||rows[2]!=D-2) return;
        int used=0; for(int t=1;t<8;t++) used+=x[t]; if(used>m) return;
        array<int,5> cc{}; cc[D]=0; LD w(1.0); int rem=m;
        for(int t=1;t<8;t++){ w=w*C[rem][x[t]]; rem-=x[t]; int pc=__builtin_popcount(t); int r=D-pc; if(r>=1&&x[t]) cc[r]+=x[t]; else if(r<0&&x[t]) return; }
        cc[D]+=rem; tri+=w*N(cc); return; }
      for(int v=0;v<=D-2;v++){ int r2[3]; bool ok=true; for(int i=0;i<3;i++){ r2[i]=rows[i]+((s>>i&1)?v:0); if(r2[i]>D-2) ok=false;}
        if(!ok) break; x[s]=v; en(s+1,r2); }
    };
    int r0[3]={0,0,0}; en(1,r0);
    LD ET=C[n][3]*tri/tot; printf("%d %.17g\n",n,ET.dbl()/((D-1.0)*(D-1)*(D-1)/6)); fflush(stdout);}
}

'''
open(h+'/r11w1_et.cpp','w').write(SRC)
subprocess.check_call(['g++','-O2',h+'/r11w1_et.cpp','-o',h+'/et.exe'])
for D,nm in ((3,400),(4,160)):
    open(f'{h}/r11w1_d{D}.txt','w').write(subprocess.check_output([h+'/et.exe',str(D),str(nm)],text=True))
