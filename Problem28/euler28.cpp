/*input
1
5
*/
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    unsigned long long testcases=0, testcasevalue[100000], i=0, n;
    unsigned long long sum1=0, sum2=0, sum3=0, mmod=1000000007;
    cin>>testcases;
    while(testcases--)
    {
        cin>>testcasevalue[i];
        n=testcasevalue[i++]/2;
        sum1 = (1+8*n*(n+1)*(2*n+1)/3)%mmod;
        sum2 = (2*(n)*(n+1))%mmod;
        sum3 = (4*n)%mmod;
        cout<<((( sum1 + sum2)%mmod +( sum3 + sum2)%mmod +( sum1 + sum3)%mmod)/2)%mmod<<endl;
    }
    return 0;
    
}
