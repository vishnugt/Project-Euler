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
    unsigned long long sum1=0, sum2=0, sum3=0, sum=0, mmod=1000000007, m;
    cin>>testcases;
    while(testcases--)
    {
        cin>>testcasevalue[i];
        n=(testcasevalue[i++]+1)/2;
        m=n;
        /*
        sum1 = (1+8*n*(n+1)*(2*n+1)/3)%mmod;
        sum2 = (2*(n)*(n+1))%mmod;
        sum3 = (4*n)%mmod;*/
        sum = ( (  (  (  ((16%mmod * m%mmod * m%mmod  * m%mmod)%mmod) %mmod -    ((18%mmod  * m%mmod * m%mmod) % mmod) %mmod        +       (14*m)%mmod        -       12%mmod      +       3%mmod)  %mmod ) %mmod  )/3)%mmod;
        cout<<sum%mmod<<endl;
    }
    return 0;
    
}


(16*(m*m*m)) = ((16%mmod * m%mmod * m%mmod  * mmmod)%mmod)
(18*(m*m)) = ((18%mmod  * m%mmod * m%mmod) % mmod)