#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
unsigned long long power(int a,int b)
    {
    unsigned long long f=1;
    for(int i=1;i<=b;i++)
        f=f*a;
    return f;
}
int noofdigits(unsigned long long n)
    {
    int count=0;
    while(n>0)
        {
        count++;
        n=n/10;
    }
    return count;
}
int main() {
    int n,i;
    unsigned long long h1,h2,num;
    cin>>n;
    h1=power(10,n);
    h2=power(10,n-1);
    for(i=1; i<h2 && num<h1;i++)
        {
        //cout<<i<<"*"<<n<<endl;
        num=power(i,n);
        if(noofdigits(num)==n)
            cout<<num<<endl;
    }
    return 0;
}