n = int(raw_input())
list = []
for i in range(n):
    list.append(raw_input())
list.sort()
for j in range( int(raw_input())):
    sum = 0
    temp = raw_input()
    for ch in temp:
        sum = sum + ord(ch) -64
    sum = sum * (list.index(temp)+1)
    print sum