#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int testcases, n, k, highest, temp;
    cin>>testcases;
    while(testcases--)
    {
        highest = -1;
        cin>>n;
        for(int i =1; i<n; i++)
            for(int j =i; j<n; j++)
            {
                k = n - i -j;
                if(k>j)
                {
                    if(i*i + j*j == k*k)
                    {
                        temp = i *j * k;
                        if(temp>highest)
                        {
                            highest = temp;
                        }
                    }
                }
            }
        cout<<highest<<endl;
    }
    return 0;
}
