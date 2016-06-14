def odddigits(n):
    for i in range(len(str(n))):
        temp = n%10
        if temp%2 == 0:
            return False
        else:
            n = int(n/10)
    return True
    
templist = []
for j in range(1000):
    templist.append(j + int(str(j)[::-1]))

print(max(templist))
dict = {}
count = 0
for i in range(0, 10**6):
    tempint = (int((str(i)[::-1])))
    if (i%2 == 0 and tempint % 2 == 0) or ( not(i%2==0) and not(tempint%2==0) ):
        dict[i] = count
        continue
    if not(len(str(i)) == len(str(tempint))):
        dict[i] = count
        continue
    if(odddigits(i + tempint)):
        count = count + 1
    dict[i] = count

for t in range(int(input())):
    n = int(input()) - 1
    print(dict[n])