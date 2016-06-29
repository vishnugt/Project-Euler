////////////// 2 cases time out

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
import math

sum1 = 0
n = int(raw_input())
temp1 = 10**11
for i in range(1, n+1):
    temp = pow(i, i, temp1)
    temp = temp % temp1
    sum1 = sum1 + temp
str1 = str(sum1)
print int(str1[len(str1)-10:len(str1)])
*/

typedef unsigned long long int ull;
ull temp1 = pow(10, 10);    

ull powergt(ull a, ull b, ull c)
{
    ull product = 1;
    for(ull i =0; i < b; i++)
    {
        product *= a;
        if (product > temp1)
            product %= temp1;
    }
 return product;   
}

int main() {
    ull sum1 = 0, n, i, temp;
    cin>>n;
    for(i = 1; i < n+1; i++)
    {
        temp = powergt(i, i, temp1);
        temp = temp % temp1;
        sum1 = sum1 + temp;
    }
    cout<<(sum1 % temp1) ;
    return 0;
}
