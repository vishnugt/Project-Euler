n = int(raw_input())
a1 = []
a2 = []
ten = 10 ** 10
for i in range(n):
    a1.append(map(int, raw_input().split(" ")))
    a2.append(a1[i])
for i in range(n):
    for j in range(n):
        if i == 0:
            if j == 0: 
                a2[i][j] = a1[i][j]
            else:
                a2[i][j] = a1[i][j] + a1[i][j-1]
            continue
        else:
            if j == 0:
                a2[i][j] = a2[i-1][j] + a1[i][j]
                continue
            else:
                a2[i][j] = a1[i][j] + min(a2[i-1][j], a2[i][j-1])
            
print a2[n-1][n-1]