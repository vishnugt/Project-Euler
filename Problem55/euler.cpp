/*def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

palindrome_num, palindrome_count = [], []

n = int(raw_input())
for i in range(1, n+1):
    for j in range(60):
        if j == 0:
            temp = i
        if is_palindrome(temp):
            if temp in palindrome_num:
                index = palindrome_num.index(temp)
                palindrome_count[index] = palindrome_count[index] + 1
            else:
                palindrome_num.append(temp)
                palindrome_count.append(1)
            break
        temp = temp + int(str(temp)[::-1])
        
greatest_count = max(palindrome_count)
greatest = palindrome_num[palindrome_count.index(greatest_count)]
print greatest, greatest_count
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

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

int main() {
    vector<ul> p_num; 
    return 0;
}
