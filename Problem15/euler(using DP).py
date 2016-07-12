testcases = int(raw_input())
for i in range(testcases):
	string = raw_input()
	m,n = int(string.split(" ")[0]), int(string.split(" ")[1])
	array =[[0 for j in range(n+1)] for i in range(m+1)]
	for i in range(m):
		array[i][n] = 1
	for j in range(n):
		array[m][j] = 1
	for i in range(m-1, -1, -1):
		for j in range(n-1, -1, -1):
			array[i][j] = array[i+1][j] + array[i][j+1]
	print array[0][0]