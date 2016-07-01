#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;
typedef unsigned long ul;

bool is_palindrome(ul num)
{
    ul numcopy = num;
    ul rev = 0, dig = 0;
    while (num > 0)
    {
        dig = num % 10;
        rev = rev * 10 + dig;
        num = num / 10;
     }
     if (numcopy == rev)
        return true;
    else
        return false;
}

ul reverse_num(ul num)
{
    ul rev = 0, dig = 0;
    while (num > 0)
    {
        dig = num % 10;
        rev = rev * 10 + dig;
        num = num / 10;
     }
    return rev;
}

int main() {
    map<ul, ul> mymap;
    map<ul,ul>::iterator it = mymap.begin();
    ul n;
    cin>>n;
    ul temp = 0;
    for (ul i = 1; i <= n; i++)
        for (int j = 0; j < 60; j++)
        {
        if(j==0)
            temp = i;
        if(is_palindrome(temp))
        {
            it = mymap.find(temp);
            if(it == mymap.end())
            {
                mymap.insert(pair<ul, ul>(temp, 1));
            }
            else
            {
                mymap[temp]++; 
            }
            break;
        }
        temp = temp + reverse_num(temp);
    }
    ul greatest_num = 0, greatest_count = 0;
    for(it=mymap.begin(); it!=mymap.end(); it++)
    {
        if(it->second >= greatest_count)
        {
            greatest_count = it -> second;
            greatest_num = it -> first;
        }
    }
    cout<<greatest_num<<" "<<greatest_count;
    return 0;
}
