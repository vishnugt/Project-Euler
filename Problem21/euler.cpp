#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int array[1000];
//array = [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368, 10744, 10856, 12285, 14595, 17296, 18416, 63020, 66928, 66992, 67095, 69615, 71145, 76084, 79750, 87633, 88730]

int sumofdiv(int n)
{
    int sum1 = 0 ;
    for (int i=1; i<n/2 + 1; i++)
    {
        if(n%i==0)
        {
            sum1 = sum1 + i;
        }
    }
    return sum1;
}

int amicable_pair(int n)
{
    int temp = sumofdiv(n);
    if(sumofdiv(temp) == n && not(temp==n))
    {
        return 1;
    }
    return 0;
}


int main() {
    int j=0;
    for(int i=0; i<100001; i++)
    {
        if(amicable_pair(i)==1)
        {
           array[j++] = i; 
        }
    }
    return 0;
}
