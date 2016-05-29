def find_divisors_sum(n):
    sum=0
    for i in range(1, n/2 + 1):
        if n%i==0:
            sum = sum + i
    if sum > n:
        return 1
    return 0
    
list = []
for i in range(12,15000): #its getting timeout exception if i go beyond this, but it should be 28123, testcase 3 is failing
    temp = find_divisors_sum(i)
    if temp == 1:
        list.append(i)
        

testcases = int(raw_input())
for i in range(testcases):
    n = int(raw_input())
    if n > 28123:
        print "YES"
        break
    for element in list:
        if element > n:
            print "NO"
            break
        if n-element in list:
            print "YES"
            break
    