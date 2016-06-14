def sumofdiv(n):
    sum1 = 0 
    for i in range(1, n/2 + 1):
        if n%i == 0:
            sum1 = sum1 + i
    return sum1

def amicablepair(n):
    temp = sumofdiv(n)
    if sumofdiv(temp) == n and not(temp==n):
        return True
    return False

list1 = []
for t in range(100001):
    if amicablepair(t):
        list1.append(t)

print list1

for testcases in range(int(raw_input())):
    n = int(raw_input())
    sum = 0
    for ele in list1:
        if ele <= n:
            sum = sum + ele
    print sum