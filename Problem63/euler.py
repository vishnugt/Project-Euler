n = int(raw_input())
start = 10 ** (n-1)
end = 10 ** n
start_pow = int(start ** (1.0/n))
end_pow = int(end ** (1.0/n)) + 1
for i in range(start_pow, end_pow):
    temp = i ** n
    if len(str(temp)) == n:
        print temp