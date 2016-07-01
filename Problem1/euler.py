def tria(n):
    return n * (n+1) / 2

for t in range(int(raw_input())):
    n = int(raw_input()) - 1
    print tria(n/3) * 3 + tria(n/5) * 5 - tria(n/15) * 15