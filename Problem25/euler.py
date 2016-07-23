fib = [0 for i in range(5008)]
a1, a2 = 1, 1
temp = 1
while(len(str(a2)) < 5000 + 7):
    a1, a2 = a2, a1 + a2
    temp = temp + 1
    fib[len(str(a2))] = temp

for t in xrange(int(raw_input())):
    print fib[int(raw_input()) - 1] + 2