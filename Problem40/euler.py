def digit_at(n):
    digits = 1
    n = n - 1
    while True:
        numbers = 9 * pow(10, digits-1) * digits
        if n > numbers: n = n - numbers
        else: break
        digits = digits + 1
    num = n / digits + pow(10, digits-1)
    return int(str(num)[n % digits])

for t in range(int(input())):
    ans = 1
    list_inputs = []
    list_inputs = list(map(int, input().split(" ")))
    for i in range(7):
        ans = ans * digit_at(list_inputs[i])
    print(ans)