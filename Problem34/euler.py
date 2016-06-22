def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

outside_sum = 0
n = int(raw_input())
for i in range(18, n):
    sum = 0
    l1 = []
    l1 = map(int, str(i))
    for ele in l1:
        sum = sum + fact(ele)
    if sum % i == 0:
        outside_sum = outside_sum + i
print outside_sum