#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int t,n,i,k,x,y;
    char no[1000];
    long long num,product,max;
        cin>>t;
    for(i=1;i<=t;i++)
        {
        cin>>n>>k;
        cin>>no;
        max=-1;
        for(x=0;x<n-k+1;x++)
            {
            product=1;
            for(y=x;y<x+k;y++)
              product = product * (no[y] - '0');
        if(product>max)
            max=product;
        }
        cout<<max<<endl;
    }
    return 0;
}