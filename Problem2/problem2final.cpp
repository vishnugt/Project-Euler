#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    unsigned long long int a[100000], x, y, z, n, count=0;
    int i,j;
    cin>>n;
    for(i=0;i<n;i++)
    {
         x=1;
         y=2;
        cin>>a[i];
        for(z=3;z<a[i];z=x+y)
        {
            if(z%2==0)
            {
                count = count +z;
               // cout<<z<<endl;
            }
            x=y;
            y=z;
        }
        cout<<count+2<<endl;
        count=0;
    }
    return 0;
}