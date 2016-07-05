#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int t, a[15][15];
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        for(int i = 0; i < n; i++)
            for(int j = 0; j <= i; j++)
                cin>>a[i][j];
        int sum = 0;
        for (int i = 0; i < n; i ++)
            for(int j = 0; j <= i; j++)
        {
            int pathleft = j == 0 ? 0 : a[i-1][j-1];
            int pathright = j == i ? 0 : a[i-1][j];
            a[i][j] += pathleft > pathright ? pathleft : pathright;  
        }
        int max = 0;
        for (int j =0; j < n; j++)
            if(max < a[n-1][j])
                max = a[n-1][j];
        cout<<max<<endl;
    }
    return 0;
}
