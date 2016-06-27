from math import factorial

for t in range(int(raw_input())):
    digits = list("abcdefghijklm")
    res = []
    n = int(raw_input()) - 1
    for i in xrange(len(digits) - 1, -1, -1):
        index, n = divmod(n, factorial(i))
        res.append(digits.pop(index))
    print ''.join(str(i) for i in res)