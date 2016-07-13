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

prime_list = []
for i in range(3163):
    if is_prime(i):
        prime_list.append(i)

length = len(prime_list)
master_list = []

for i in range(length):
    for j in range(47):
        for k in range(16):
            temp = prime_list[i] ** 2 + prime_list[j] ** 3 + prime_list[k] ** 4
            if temp > 10000001:
                continue
            master_list.append(temp)
ms = sorted((set(master_list)))
countl = []
temp = 0
itera = 0
for i in range(10000001):
    if itera == len(ms):
        countl.append(temp)
        continue
    if i == ms[itera]:
        temp = temp + 1
        itera = itera + 1
        countl.append(temp)
    else:
        countl.append(temp)
    
for t in range(int(input())):
    print(countl[int(input())])