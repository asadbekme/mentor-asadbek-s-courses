n, m = map(int, input().split())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for row in range(n):
    for col in range(m):
        if matrix[row][col] < 0:
            matrix[row][col] = abs(matrix[row][col])

for row in matrix:
    print(*row)