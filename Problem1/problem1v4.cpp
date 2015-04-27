#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

//not working


int main() {
    int n;
    int j=0;
    cin>>n;
    int a[100], count;
    for(int i=0;i<n;i++){
        cin>>a[i];
    count=0;
    while(j<a[i]/3)
    {
        j=3;
        count = count+j;
        j = j+3;
    } 
        j=0;
        while(j<a[i]/5)
    {
        j=5;
        count = count+j;
        j = j+5;
    }
        j=0;
        while(j<a[i]/15)
    {
        j=15;
        count = count-j;
        j = j+15;
    }
        cout<<count<<endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
