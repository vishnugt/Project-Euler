n = int(raw_input())
sum = 0

def condition(i, n):
    sum = 0 
    list = map(int, str(i))
    for ele in list:
        sum = sum + (ele ** n)
    if (sum == i):
        return True
    return False
    
for i in range(10, 1000000):
    if(condition(i, n)):
        sum = sum + i
print sum