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

list = []

list.append(2)
for k in range(3, 1000001, 2):
    if is_prime(k):
        list.append(k)

for i in range(int(raw_input())):
    n = int(raw_input())
    i, sum =0, 0
    while(True):
        if list[i] < n+1:
            sum = sum + list[i]
            i = i + 1
        else:
            break
    print sum