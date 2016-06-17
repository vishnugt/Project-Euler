a = int(raw_input())
b = a
max_sum = 0
for i in range(a):
    for j in range(b):
        list1 = map(int, str(i**j))
        sum1 = sum(list1)
        if sum1 > max_sum:
            max_sum = sum1
print max_sum