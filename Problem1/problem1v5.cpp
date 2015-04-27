#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

//not working


int main() {
    int n;
    long long x,y,z;
    int j=0;
    cin>>n;
    int a[100000];
    long long count, aa, bb, cc;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
        x=(a[i]-1)/3;
        y=(a[i]-1)/5;
        z=(a[i]-1)/15;
        aa=3*x*(x+1);
        bb=5*y*(y+1);
        cc=15*z*(z+1);
        count = aa+bb-cc;
        cout<<count/2<<endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}