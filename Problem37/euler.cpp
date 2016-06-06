#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int prime(long long n)
{
    if(n<2)
        return 0;
    for(int i=2;i<=sqrt(n);i++)
    {
        if(n%i==0)
            return 0;
    }
    return 1;
}

int noofdigits(long long n)
{
    int count=0;
    while(n!=0)
    {
        count++;
        n=n/10;
    }
    return count;
}

int reverse_number(long long n) 
{
    long long reverse = 0;
    while(n != 0) {
        int remainder = n%10;
        reverse = reverse*10 + remainder;
        n/=10;
    }
   return reverse;
}

int main() 
{
    long long n,i,p,sum=0, temp1, temp2, reversed_number;
    int k,d,j;
    cin>>n;
    for(i=11;i<n;i++)
    {
        k=0;
        if(prime(i))
        {
            
            reversed_number = reverse_number(i);
            temp1 = i;
            temp2 = reversed_number;
            k=1;
            d=noofdigits(i);
            for(j=1;j<d;j++)
            {
                if(  !(prime(temp1/10) &&  prime(reverse_number(temp2/10))) )
                    k=0;
                temp1 = temp1/10;
                temp2 = temp2/10;
                
            }
        }
        if(k==1)
        {
            sum = sum + i;
        }
            
    }
    cout<<sum<<endl;
    return 0;
}

