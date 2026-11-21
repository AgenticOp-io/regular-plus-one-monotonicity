// reads n E then E lines "u v w"; prints weighted k-matching sums m1..m4 (long double)
#include <stdio.h>
#include <stdlib.h>
int n,E,*U,*V; long double *W; char *used; long double m[5];
static void rec(int start,int k,long double w){ m[k]+=w; if(k==4)return;
 for(int e=start;e<E;e++){ if(used[U[e]]||used[V[e]])continue; used[U[e]]=used[V[e]]=1; rec(e+1,k+1,w*W[e]); used[U[e]]=used[V[e]]=0; } }
int main(){ scanf("%d %d",&n,&E); U=malloc(4*E);V=malloc(4*E);W=malloc(sizeof(long double)*E);used=calloc(n,1);
 for(int i=0;i<E;i++){double w;scanf("%d %d %lf",&U[i],&V[i],&w);W[i]=w;}
 rec(0,0,1.0L); for(int k=1;k<=4;k++)printf("%.18Le\n",m[k]); }
