#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

//not working


int main() {
    int n;
    long long x, y, z, count, aa, bb, cc, j=0, a[100000];
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
        x=(a[i]-1)/3;
        y=(a[i]-1)/5;
        z=(a[i]-1)/15;
        count = 3*x*(x+1) + 5*y*(y+1) - 15*z*(z+1);
        cout<<count/2<<endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}