n, a, b = map(int, raw_input().split(" "))
flag, x = 0, 1
tri, pent, hexa =[], [], []
while(flag==0):
    temp = x * (x + 1) / 2
    if temp < n:
        tri.append(temp)
        x = x + 1
    else:
        flag = 1

flag, x = 0, 1 
while(flag==0):
    temp = x * (3 * x - 1) / 2
    if temp < n:
        pent.append(temp)
        x = x + 1
    else:
        flag = 1

flag, x = 0, 1       
while(flag==0):
    temp = x * (2 * x - 1)
    if temp < n:
        hexa.append(temp)
        x = x + 1
    else:
        flag = 1

if a == 3 :
    tempset = set(tri).intersection(pent)
    for item in tempset:
        print item

if a == 5 :
    tempset = set(pent).intersection(hexa)
    for item in tempset:
        print item