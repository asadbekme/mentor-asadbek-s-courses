n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

x, y = 0, 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] < 0:
            x, y = i, j

for i in range(n):
    for j in range(m):
        if i != x and j != y:
            print(matrix[i][j], end=" ")
    if i != x:
        print()