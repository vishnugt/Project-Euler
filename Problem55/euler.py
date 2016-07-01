def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

palindrome_num, palindrome_count = [], []

n = int(raw_input())
for i in range(1, n+1):
    for j in range(60):
        if j == 0:
            temp = i
        if is_palindrome(temp):
            if temp in palindrome_num:
                index = palindrome_num.index(temp)
                palindrome_count[index] = palindrome_count[index] + 1
            else:
                palindrome_num.append(temp)
                palindrome_count.append(1)
            break
        temp = temp + int(str(temp)[::-1])
        
greatest_count = max(palindrome_count)
greatest = palindrome_num[palindrome_count.index(greatest_count)]
print greatest, greatest_count