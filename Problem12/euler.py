def num_of_div(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count = count + 2
    if n**0.5 == int(n**0.5):
        count = count - 1
    return count
    

trian = [1]
divi = [1]

for i in range(2, 41041):
    temp =  i * (i+1) / 2 
    trian.append(temp)
    if(i%2==0):
        divi.append(num_of_div(i/2) * num_of_div(i+1))
    else:
        divi.append(num_of_div(i) * num_of_div((i+1)/2))

for t in range(int(raw_input())):
    n = int(raw_input())
    for i in range(len(trian)):
        if n < divi[i]:
            print trian[i]
            break