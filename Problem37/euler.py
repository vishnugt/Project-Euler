def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True 

def lefttoright(n):
    flag = 0
    temp = n
    #print n
    for i in range(len(str(n))):
        temp = temp/10
        #print temp
        if(is_prime(temp)):
            flag = flag +1
    if flag == len(str(n)) - 1:
        return True
    return False

def righttoleft(n):
    temp1 = int(str(n)[::-1])
    flag = 0
    #print n
    for i in range(len(str(n))):
        temp1 = temp1/10
        temp2 =  int(str(temp1)[::-1])
        #print temp
        if(is_prime(temp2)):
            flag = flag +1
    if flag == len(str(n)) - 1:
        return True
    return False

sum = 0
n =  int(raw_input())
for i in range(10, n, 1):
    if(is_prime(i)):
        if lefttoright(i) and righttoleft(i):
            sum = sum + i
print sum
            