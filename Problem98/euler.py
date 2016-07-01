n= int(raw_input())
start = (10 ** (n-1)) ** 0.5 - 5 
end = (10 ** n) ** 0.5 + 5
lista, listcount, listgreatest = [], [], []
for j in range(int(start), int(end)):
    i = j * j
    if i ** 0.5  == int(i ** 0.5):
        temp  = map(int, str(i))
        temp.sort()
        if temp in lista:
            index = lista.index(temp)
            listcount[index] = listcount[index] + 1
            if listgreatest[index] < i:
                listgreatest[index] = i
        else:
            lista.append(temp)
            listcount.append(1)
            listgreatest.append(i)


index = listcount.index(max(listcount))
print listgreatest[index]