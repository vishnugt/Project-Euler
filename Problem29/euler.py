### version 1: 9 testcases passed
## just bruteforce
n, l  = int(raw_input()), []
for i in range(2,n+1):
    for j in range(2,n+1):
        l.append(i**j)
print len((list(set(l))))

### version 2: 7 testcases passed
## little optimized, saving i * j to use in i* j+1
n, l = int(raw_input()), []
for i in range(2,n+1):
    for j in range(2,n+1):
        temp1 = i
        for k in range(2,j+1):
            temp1 = temp1 * i
        l.append(temp1)
print len((list(set(l))))


### version 3 - 6 testcases passed
## but this is supposed to be the most optimised one :( 
#Sad Life, Meliodas
dict = {}
n, l = int(raw_input()), []
for i in range(2,n+1):
    for j in range(2,n+1):
        temp1 = i
        for k in range(2,j+1):
            if (str(i) + "**" + str(k)) in dict:
                temp1 = dict[str(i) + "**" + str(k)]
            else:
                temp1 = temp1 * i
                dict[str(i) + "**" + str(k)] = temp1
        l.append(temp1)
print len((list(set(l))))