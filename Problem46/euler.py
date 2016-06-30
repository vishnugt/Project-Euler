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

list_primes = []
for i in range(500001):
    if is_prime(i):
        list_primes.append(i)

for t in range(int(raw_input())):
    ways = 0
    n = int(raw_input())
    for item in list_primes:
        if item > n:
            print ways
            break
        temp = n - item
        if temp%2==0:
            x = (temp/2) ** 0.5
            if int(x) == x:
                ways = ways + 1