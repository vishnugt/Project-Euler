list_inputs = []
for t in range(int(raw_input())):
    list_inputs.append(int(raw_input()))

limit = max(list_inputs)
list1, list2, list3, list4 =[], [], [], []
a, b, c, m, n = 0, 0, 0, 2, 1
while(c < limit):
    for n in range(1, m):
        a = m*m - n*n
        b = 2*m*n
        c = m*m + n*n
        if c > limit:
            break
        list1.append(a)
        list2.append(b)
        list3.append(c)
        list4.append(a+b+c)
    m = m + 1


for i in range(len(list_inputs)):
    highest = -1
    for ele in list4:
        if ele == list_inputs[i]:
            product = list1[i] * list2[i] * list3[i]
            if product > highest:
                highest = product
    print highest