from itertools import permutations

def checkvalidity(sudoku):
    sudoku = list(sudoku)
    for i in range(9):
        templist = sudoku[i][:]
        templist.sort()
        if not(templist == oneto9):
            return False
    for i in range(9):
        templist = [row[i] for row in sudoku][:]
        templist.sort()
        if not(templist == oneto9):
            return False
    return True

def findnext(m, n, sudoku):
    for i in range(m, 9):
        for j in range(9):
            if i == m and j > n:
                if sudoku[i][j] == 0:
                    return i, j
            if i > m:
                if sudoku[i][j] == 0:
                    return i, j
    return 10, 10

def printa(sudoku):
    for i in range(9):
        tempstr = ""
        for j in range(9):
            tempstr = tempstr + str(sudoku[i][j])
        print tempstr

def solve(i, j, sudoku):
    sudoku = list(sudoku)
    if i == 10:
        if checkvalidity(sudoku):
            printa(sudoku)
            return False, True
        return False, False
    sudoku = list(sudoku)
    oneto9c = list(oneto9)
    for item in sudoku[i]:
        if not(item==0):
            oneto9c.remove(item)
    f = False
    perms = list(permutations(oneto9c))
    for item in perms:
        oneto9c = list(item)
        z = 0
        for m in range(9):
            if sudoku[i][m] == 0 or sudoku[i][m] in oneto9c:
                sudoku[i][m] = oneto9c[z]
                z = z + 1
        flag = True
        while(flag):
            m, n = findnext(i, j, sudoku)
            flag, f = solve(m, n, sudoku)
        if f :
            return False, True
            break
    return True, False

oneto9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku = []
for i in range(9):
    sudoku.append(map(int, raw_input()))
i, j = findnext(0, 0, sudoku)
solve(i, j, sudoku)