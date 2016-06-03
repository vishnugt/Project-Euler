for i in range(int(raw_input())):
    n = int(raw_input())
    sum1, sum2 = 0, 0
    for j in range(1, n+1):
        sum1 = sum1 + j*j
        sum2 = sum2 + j
    sum2 = sum2**2
    print str(sum2 - sum1)