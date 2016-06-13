for testcases in range(int(raw_input())):
    highest = -1
    n = int(raw_input())
    for i in range(1, n/3):
        for j in range(i, n/2):
            k = n - i - j
            if k > j:
                if i**2 + j**2 == k**2:
                    temp = i*j*k
                    if temp > highest:
                        highest = temp
    print highest