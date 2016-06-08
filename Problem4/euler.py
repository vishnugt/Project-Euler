def isprime(n):
    if(n==2 or n==3):
        return True
    else:
        for i in range(3, n, 2):
            if(n%i==0):
                return False
        return True

def highest_prime(n):
    highest = 2
    for i in range(n, 1, -1):
        if(n%i == 0):
            if(isprime(i)):
                if(highest<i):
                    highest = i
    return highest
    
    
for i in range(int(raw_input())):
    n = int(raw_input())
    print highest_prime(n)


    