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

def rotate(i, j):
    temp1 = str(i)[:j]
    temp2 = str(i)[j:]
    temp = temp2 + temp1
    return int(temp)

sum = 0
for i in range(int(raw_input())):
    flag = 0
    if is_prime(i):
        if len(str(i)) == 1:
            sum = sum + i
        else:
            for j in range(len(str(i))-1):
                temp = (rotate(i, j+1))
                if is_prime(temp):
                    flag = flag + 1
            if flag == len(str(i)) -1:
                sum = sum + i

print sum