/*input
100
*/
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int isprime(long long int a)
{
    if(a<2)
        return 0;
    else if(a==2)
        return 1;
    else if(a%2==0) 
        return 0;
    else
    {
        for(int i=2; i<(int)sqrt(a) + 1; i++)
            if(a%i==0)
                return 0;
        return 1;
    }
}



int hasSameDigits (long long int num1, long long int num2) {
    int digits[10];
    int i;

    for (i = 0; i < 10; i++)      // Init all counts to zero.
        digits[i] = 0;

    while (num1 != 0) {           // Process all digits.
        digits[num1%10]++;        // Increment for least significant digit.
        num1 /= 10;               // Get next digit in sequence.
    }

    while (num2 != 0) {           // Same for num2 except decrement.
        digits[num2%10]--;
        num2 /= 10;
    }

    for (i = 0; i < 10; i++)
        if (digits[i] != 0)       // Any count different, not a permutation.
            return false;

    return true;                  // All count identical, was a permutation.
}

int main() 
{
    double ratio, bestratio=10000000;
    long long int testcase, n=0, phi=0, bestn=0;
    cin>>testcase;
    //cout<<testcase;
    long long int testcase_sqrt =  sqrt(testcase);
    //cout<<testcase_sqrt<<" "<<testcase;
    for(int i=0; i<testcase_sqrt; i++)
    {
        for(int j=i+1; j < testcase_sqrt;j++)
        {
            if(isprime(i)==1 && isprime(j)==1)
            {
                //cout<<"a"<<i<<j<<endl;
                n=i*j;
                if(testcase >= n)
                {
                    //cout<<"passed"<<endl;
                    phi = (i-1) * (j-1); // gt doesnt understand y this is, some math shit
                    ratio = (i*j)/phi;
                    //cout<<phi<< "   "<<n<<endl;
                    //check whether they are same permutation
                    if(ratio < bestratio  && hasSameDigits(phi, i*j))
                    {
                        //cout<<ratio;
                        bestn = i*j;
                        bestratio = ratio ;
                    }   
                }
                
            }
        }
    }
    cout<<bestn;
    return 0;
}
