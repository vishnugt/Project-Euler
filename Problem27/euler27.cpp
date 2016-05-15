#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int isprime(int a)
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

int main()
 {
    int input, highn=0, higha=0, highb=0, a, b;
    cin>>input;
    //cout<<(int)sqrt(input);
    for (a = -1 * input; a <= input; a++) 
    {   
        for(b = 2; b <= input; b++)
        {
            int n = 0;
            while (isprime(n*n + a* n + b)==1)
            {
                n++;
                //cout<<n<<(n*n + a* n + b)<<endl;
            }
            if (n > highn)
            {
                //cout<<n<<"  "<<a<< "  " <<b<< "  "<<endl;
                higha = a;
                highb = b;
                highn = n;
            }
            n=0;
        }
    }
    cout<<higha<<" "<<highb;

    return 0;
}
