def ncr(n, r):
    return list_fact[n]/(list_fact[r] * list_fact[n-r])
list_fact = [1]

temp = 1
for i in range(1, 1005):
    temp = temp * i
    list_fact.append(temp)

n, k = map(int, raw_input().split(" "))
count = 0
for i in range(n+1):
    for j in range(i+1):
        if ncr(i, j) > k:
            count = count + 1
print count