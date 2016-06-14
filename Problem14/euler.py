def findnext(i):
    if i%2 == 0:
        return i/2
    else:
        return 3 * i + 1

n = 10000
templist, masterlist, count = [], [], 0
for i in range(1, n):
    count = 0
    nextint = i
    while(True):
        if nextint == 1:
            break
        nextint = findnext(nextint)
        count = count + 1
    masterlist.append(count)
    templist.append(i)
for t in range(int(raw_input())):
    master = 0
    n = int(raw_input())
    for i in range(len(templist)+1):
        if n < templist[i]:
            break
        if n > templist[i]:
            temp = masterlist[i]
            if temp >= master:
                master = temp
                mastermaster = templist[i]
    print mastermaster