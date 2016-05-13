#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

unsigned long long fibonacci[1000000], number_of_digits_array[1000000];
    
void create_fibonacci()
{
    int iter=2;
    fibonacci[0]=1;
    fibonacci[1]=1;
    int times=1000000;
    while(times--)
    {
        fibonacci[iter]=fibonacci[iter-1] + fibonacci[iter-2];
        //cout<<fibonacci[iter++]<<endl;
        iter++;
    }
    
}

int find_no_of_digits(unsigned long long a)
{
    int jter=0;
    while(a>0)
    {
        a/=10;
        jter++;
    }
    return jter;
}

void create_digits_array()
{
    for(int j=0; j<10000; j++)
    {
        number_of_digits_array[j] = find_no_of_digits(fibonacci[j]);
        //cout<<number_of_digits_array[j]<<" "<<fibonacci[j]<<endl;
    }
}
int main() 
{
    int testcases, testcase_values[1000000], i=0;
    create_fibonacci();
    create_digits_array();
    //cout<<find_no_of_digits(123456789);
    cin>>testcases;
    while(testcases--)
    {
        cin>>testcase_values[i];
        for(int k=0; k<1000000; k++)
        {
            if(number_of_digits_array[k]==testcase_values[i])
            {
                cout<<++k<<endl;
                break;
            }
        }
    }
    
    return 0;
}
