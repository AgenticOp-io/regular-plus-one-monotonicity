// Host: u~X (|X|=j), v~Z (|Z|=k), |X&Z|=w, uv not in H.  Remove u,v -> near-regular sequence (defects 0,1,2) on m=n-2 vertices,
// counted by the class-count DP (positive terms only -> doubles are safe).  N~ = N/(M-1)!! keeps values in (0,1].
// usage: r7_star D n   -> lines "D n j k w P"
#include <cstdio>
#include <cstdint>
#include <cmath>
#include <vector>
#include <array>
#include <unordered_map>
#include <functional>
#include <algorithm>
#include <cstdlib>
using namespace std;
typedef unsigned __int128 K; int D; 
struct H{size_t operator()(const K&k)const{uint64_t a=(uint64_t)k,b=(uint64_t)(k>>64);a^=b*0x9E3779B97F4A7C15ULL;a^=a>>29;a*=0xBF58476D1CE4E5B9ULL;a^=a>>32;return a;}};
unordered_map<K,double,H> memo; double Cb[130][130];
double solve(array<int,16>&c);
static inline K pack(const array<int,16>&c){K k=0;for(int j=0;j<D;j++)k|=(K)c[j]<<(8*j);return k;}
double solve(array<int,16>&c){
  int k=0;for(int j=D;j>=1;j--)if(c[j-1]){k=j;break;}
  if(!k)return 1.0;
  K key=pack(c);auto it=memo.find(key);if(it!=memo.end())return it->second;
  long M=0;for(int j=1;j<=D;j++)M+=(long)j*c[j-1];
  array<int,16> b=c;b[k-1]--;double tot=0;
  function<void(int,int,array<int,16>&,double)> rec=[&](int j,int left,array<int,16>&cur,double w){
    if(j==0){ if(left==0) tot+=w*solve(cur); return;}
    int mx=min(left,b[j-1]);
    for(int a=0;a<=mx;a++){ // a vertices of class j lose one degree
      array<int,16> nw=cur; nw[j-1]-=a; if(j>=2)nw[j-2]+=a;
      rec(j-1,left-a,nw,w*Cb[b[j-1]][a]);
    }
  };
  // note: vertices moved from class j to j-1 must not be re-chosen; rec goes j=D..1 so class j-1 is visited later with b (original) counts -> use b for choice counts, cur for result
  array<int,16> cur=b; rec(D,k,cur,1.0);
  double den=1;for(int i=0;i<k;i++)den*=(M-1-2*i);
  double r=den>0?tot/den:0; memo[key]=r;return r;
}
int main(int argc,char**argv){
  D=atoi(argv[1]);int n=atoi(argv[2]);int m=n-2;
  for(int i=0;i<130;i++){Cb[i][0]=1;for(int j=1;j<=i;j++)Cb[i][j]=Cb[i-1][j-1]+(j<=i-1?Cb[i-1][j]:0);}
  auto lC=[&](int a,int b)->double{return (b<0||b>a)?-1e300:log(Cb[a][b]);};
  auto lfd=[&](long M)->double{return lgamma(M+1.0)-(M/2)*log(2.0)-lgamma(M/2+1.0);}; // log (M-1)!!, M even
  for(int j=0;j<D;j++)for(int k=0;k<D;k++)for(int w=0;w<=min(j,k);w++){
    if(j+k-w>m)continue;
    double L[2];
    for(int e=0;e<2;e++){
      int ru=D-j-e,rv=D-k-e,r0=m-j-k+w;vector<double> t;
      for(int y1=0;y1<=min(k-w,ru);y1++){int y0=ru-y1;if(y0>r0)continue;
       for(int z1=0;z1<=min(j-w,rv);z1++){int z0=rv-z1;if(z0>r0)continue;
        for(int tt=0;tt<=min(y0,z0);tt++){
          if(z0-tt>r0-y0)continue;
          int a2=w+z1+y1+tt,a1=(j-w-z1)+(k-w-y1)+(y0+z0-2*tt);
          double lw=lC(k-w,y1)+lC(r0,y0)+lC(j-w,z1)+lC(y0,tt)+lC(r0-y0,z0-tt);
          long Mm=(long)D*m-a1-2*a2; if(Mm&1)continue;
          array<int,16> c{};c[D-1]=m-a1-a2;c[D-2]=a1;if(D>=3)c[D-3]=a2;
          double v=solve(c); if(v<=0)continue;
          t.push_back(lw+log(v)+lfd(Mm));
        }}}
      double mx=-1e300;for(double x:t)mx=max(mx,x);double s=0;for(double x:t)s+=exp(x-mx);
      L[e]=t.empty()?-1e300:mx+log(s);
    }
    double P=1/(1+exp(L[0]-L[1]));
    printf("%d %d %d %d %d %.15g\n",D,n,j,k,w,P);
  }
}
