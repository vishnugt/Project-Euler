#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin>>n;
    int a[100], count;
    for(int i=0;i<n;i++){
        cin>>a[i];
    count=0;
    for(int j=0; j <a[i] ;j++)
    {
        if(j%3==0 )
        {
            count =count + j;
        }
        if(j%5==0)
        {
            count = count +j;
        }
        if(j%15==0)
        {
            count = count -j;
        }
    }
        cout<<count<<endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
