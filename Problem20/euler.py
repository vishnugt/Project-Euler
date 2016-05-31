def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)
for i in range(int(raw_input())):
    print sum(map(int, str(fact(int(raw_input())))))
