for t in range(int(raw_input())):
    n = int(raw_input())
    array = []
    for i in range(n):
        array.append(map(int, raw_input().split(" ")))
    for i in range(n):
        for j in range(i+1):
            if j == 0:
                pathleft = 0
            else:
                pathleft = array[i-1][j-1]
            if j == i:
                pathright = 0
            else:
                pathright = array[i-1][j]
            array[i][j] = array[i][j] + max(pathleft, pathright)
    print max(array[n-1])