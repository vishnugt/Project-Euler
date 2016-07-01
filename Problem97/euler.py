t_sum = 0
for t in range(int(raw_input())):
    a, b, c, d = map(int, raw_input().split(" "))
    tempbc = pow(b, c, 10**12)
    tempstr =  a * tempbc + d
    t_sum = t_sum + tempstr
while(len(str(t_sum)) < 12):
        t_sum = "0" + str(t_sum)
print str(t_sum)[-12:]