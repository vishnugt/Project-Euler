from itertools import permutations

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

list1 = []
n = 10**8 - 1 #i am finiding digits only upto 10^8 coz the highest prime pandigital is 7652413
size = len(str(n))
while(size>0):
    list_a = range(1, size + 1)
    list_a.reverse()
    size = size - 1
    perms_a = permutations(list_a)
    for abc in perms_a:
        inta =  int(''.join(map(str, abc)))
        if inta <= n:
            if is_prime(inta):
                list1.append(inta)
for t in range(int(raw_input())):
    n = int(raw_input())
    greatest = -1
    for i in range(len(list1)):
        if list1[i] <= n:
            if list1[i] > greatest:
                greatest = list1[i]
    print greatest