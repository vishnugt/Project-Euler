#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int gcd(int a, int b)
{
    for (;;)
    {
        if (a == 0) return b;
        b %= a;
        if (b == 0) return a;
        a %= b;
    }
}

int lcm(int a, int b)
{
    int temp = gcd(a, b);

    return temp ? (a / temp * b) : 0;
}


int main() {
    int testcases, n, ans=1;
    cin>>testcases;
    while(testcases--)
    {
        //cout<<"a";
        cin>>n;
        for(int i=n;i>0;i--)
        {
            ans = lcm(ans, i);
            //cout<<ans<<"A"<<endl;
        }
        cout<<ans<<endl;
        ans=1;
    }
    return 0;
}
