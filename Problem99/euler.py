import math
list = []
dict = {}
for i in range(int(raw_input())):
    n, k = map(int, raw_input().split(" "))
    temp = (k * math.log10(n))
    list.append(temp)
    dict[temp] = str(n) +" " + str(k)
list.sort()
print dict[list[int(raw_input())-1]]
