from math import factorial
for t in range(int(raw_input())):
    m, n = map(int, raw_input().split(" "))
    print factorial(m+n)/(factorial(n)*factorial(m)) % (10**9 + 7)