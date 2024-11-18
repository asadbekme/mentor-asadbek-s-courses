n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for j in range(m):
    column = [matrix[i][j] for i in range(n)]
    column.sort(reverse=True)
    for i in range(n):
        matrix[i][j] = column[i] 

for row in matrix:
    print(*row)
