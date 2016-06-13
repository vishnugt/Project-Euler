for testcases in range(int(raw_input())):
    n, k = map(int, raw_input().split(" "))
    value = int(raw_input())
    list = [int(i) for i in str(value)]
    highest_product = -1
    temp = n-k+1
    i = 0
    while(temp>0):
        product = 1
        for j in range(i, i+k):
            product = product * list[j]
        #print product, highest_product, i, k
        i = i + 1
        temp = temp - 1
        if product > highest_product:
            highest_product = product
    print highest_product