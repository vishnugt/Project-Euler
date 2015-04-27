#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    long double n, count=0;
    int i,j;
    long long int f[400000], a[100000];
    f[0]=1;
    f[1]=2;
    cin>>n;
    for(i=0;i<n;i++)
    {
        count=0;
        cin>>a[i];
    for(j=2;j<a[i];j++)
    {
        f[j]=f[j-1]+f[j-2];
       // cout<<f[j]<<endl;
        if(f[j]>a[i])
            break;
        if((j-1)%3==0)
        {
            count = count + f[j];
            //cout<<f[j]<<endl;
        }
    }
        cout<<count+2<<endl;
        count=0;
    }
    return 0;
}