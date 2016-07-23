mod = 10 ** 9 + 7
for t in range(int(raw_input())):
    n = int(raw_input())
    ways = [1]  + [0] * n
    for i in range(1, n):
        for j in range(i, n + 1):
            ways[j] += ways[j - i] % mod
    print ways[-1] % mod