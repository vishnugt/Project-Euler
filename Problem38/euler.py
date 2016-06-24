n, k = map(int, raw_input().split(" "))
list_s = []
list_2 = []
for i in range(1, k+1):
    list_s.append(i)
set_s = set(list_s)
for i in range(2, n + 1):
    list_2 = []
    for m in range(1, 9):
        for ch in str( i * m ):
            list_2.append(int(ch))
        if len(list_2) > k or len(list_2) < k:
            continue
        else:
            #print i, list_2
            if set_s == set(list_2):
                print i