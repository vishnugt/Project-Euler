import math

sum1 = 0
n = int(raw_input())
temp1 = 10**11
for i in range(1, n+1):
    temp = pow(i, i, temp1)
    temp = temp % temp1
    sum1 = sum1 + temp
str1 = str(sum1)
print int(str1[len(str1)-10:len(str1)])