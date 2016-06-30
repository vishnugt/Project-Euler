def is_palindrome(n):
    if n == int(str(n)[::-1]):
        return True
    return False

list_palindrome = []
for i in range(100, 1000):
    for j in range(100, 1000):
        temp = i * j
        if is_palindrome(temp):
            list_palindrome.append(temp)
list_palindrome.sort()

for t in range(int(raw_input())):
    n  = int(raw_input())
    for i in range(len(list_palindrome)):
        if list_palindrome[i] >= n:
            print list_palindrome[i-1]
            break