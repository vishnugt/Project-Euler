#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int hasSameDigits (int num1, int num2) {
    int digits[10], i;
    for (i = 0; i < 10; i++)      
        digits[i] = 0;
    while (num1 != 0)
    {          
        digits[num1%10]++;        
        num1 /= 10;               
    }
    while(num2 != 0) 
    {           
        digits[num2%10]--;
        num2 /= 10;
    }
    for (i = 0; i < 10; i++)
        if (digits[i] != 0)       
            return 0;
    return 1;                  
}

int main() {
    int n, k, flag;
    cin>>n>>k;
    for(int i = 1; i<=n; i++)
    {
        flag = 0;
        for(int j=2; j<=k; j++)
        {
            if(!hasSameDigits(i, j*i))
                break;
            else
                flag++;
        }
        if(flag == k-1)
        {
            for(int z = 1; z<=k; z++)
            {
               cout<<i*z<<" ";
            }
        cout<<endl;
        }
    }
    return 0;
}
