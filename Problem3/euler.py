for t in range(int(raw_input())):
    n = int(raw_input())
    i = 2
    high = 1
    while(i*i <= n):
        while(n%i == 0 ):
            n = n/i
            high = i
        i += 1
    if n > 1 : print n
    else: print high