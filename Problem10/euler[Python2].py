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

dir = {}
sum = 0

for k in range(3, 1000001, 2):
    if is_prime(k):
        sum = sum + k
        dir[k] = sum

for i in range(int(raw_input())):
    n = int(raw_input())
    i, sum =0, 0
    for z in range(n, 0, -1):
        if is_prime(z):
            small_prime = z
            break
    print dir[small_prime] + 2