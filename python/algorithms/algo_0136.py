n, m = map(int, input().split()) 
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
k = int(input())

for i in range(n):
    for j in range(m):
        if j == (k - 1):
            continue
        print(matrix[i][j], end = " ")
    print()
