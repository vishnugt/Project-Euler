def col_greatest(row):
    prod_col = 1
    for i in range(17):
        temp = list[i][row] * list[i+1][row] * list[i+2][row] * list[i+3][row]
        if temp > prod_col:
            prod_col = temp
    return prod_col

def row_greatest(col):
    prod_col = 1
    for k in range(17):
        temp = list[col][k] * list[col][k+1] * list[col][k+2] * list[col][k+3]
        if temp > prod_col:
            prod_col = temp
    return prod_col

def right_diag(i, j):
    prod_col = 1
    temp = list[i][j] * list[i+1][j+1] * list[i+2][j+2] * list[i+3][j+3]
    if temp > prod_col:
        prod_col = temp
    return prod_col

def left_diag(i, j):
    prod_col = 1
    temp = list[i][j] * list[i-1][j+1] * list[i-2][j+2] * list[i-3][j+3]
    if temp > prod_col:
        prod_col = temp
    return prod_col


list = []
prod = 1

for i in range(20):
    list.append([int(k) for k in raw_input().split()])

for i in range(20):
    prod_temp = col_greatest(i)
    if prod_temp > prod:
        prod = prod_temp
        
for j in range(20):
    prod_temp = row_greatest(j)
    if prod_temp > prod:
        prod = prod_temp

for i in range(17):
    for j in range(17):
        prod_temp = right_diag(i, j)
        if prod_temp > prod:
            prod = prod_temp
            
for i in range(3,20):
    for j in range(17):
        prod_temp = left_diag(i, j)
        if prod_temp > prod:
            prod = prod_temp
print prod