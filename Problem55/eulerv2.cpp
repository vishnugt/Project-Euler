#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
typedef unsigned long long ull;
ull nos[100000];
ull acount[100000];
ull reverse(ull n)
    {
    ull rev=0;
        while(n!=0)
        {
        rev=rev*10+n%10;
            n=n/10;
        }
    return rev;
}
ull palindrome(ull n)
    {
    ull rev=reverse(n);
    if(rev==n)
        return 1;
    else
        return 0;
}
void maxPalindrome(ull n)
    {
    static int i=0;
    int k = 0;
    if(i==0)
        {
        nos[i]=n;
        acount[i] = 1;
        i++;
        }
    else
        {
        for(ull j=0;j<i;j++)
            {
            if(nos[j]==n)
                {
                k=1;
                acount[j]++;
                }
           }
        if(k==0)
            {
            nos[i]=n;
            acount[i] = 1;
            i++;
            }
        }
}
int main() {
    ull n,i,j,sum,k,palin,max=0;
        cin>>n;
    for(i=1;i<=n;i++)
        {
         for(j=1;j<=60;j++)
            {
            if(j==1)sum=i;
            k=palindrome(sum);
            if(k)
                {
                maxPalindrome(sum);
                break;
               }
            sum=sum+reverse(sum);
           }
       }
    for(i=0;i<1000;i++)
        {
        if(acount[i]>max)
            {
            palin=nos[i];
            max=acount[i];
           }
       }
    cout<<palin<<" "<<max<<endl;
    return 0;
}