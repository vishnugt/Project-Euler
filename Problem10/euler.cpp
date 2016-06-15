#include <cmath>
#include <cstring>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
typedef unsigned long long int ll;
ll prime_sum[1000001];

bool isPrime(ll num) {
    if(num < 2) {
        return false;
    } else if(num < 4) {
        return true;
    } else if(num % 2 == 0 || num % 3 == 0) {
        return false;
    }
    for(int i = 3, max = sqrt(num); i <= max; i += 2) {
        if(num % i == 0) {
            return false;
        }
    }
    return true;
}

void find_all_sum()
{
    ll sum = 0;
    ll limit = 1000001;
    for(ll i=0; i < limit; i++)
    {
        if(isPrime(i))
        {
            sum += i;
        }
        prime_sum[i] = sum;
        //cout<<i<<" "<<prime_sum[i]<<endl;
    }
}

int main() {
    ll testcases, n;
    cin>>testcases;
    find_all_sum();
    while(testcases--)
    {
        cin>>n;
        cout<<prime_sum[n]<<endl;
    }
    return 0;
}