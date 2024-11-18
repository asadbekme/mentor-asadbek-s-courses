n = int(input())
matrix1 = [list(map(int, input().split())) for _ in range(n)]
matrix2 = [list(map(int, input().split())) for _ in range(n)]

matrix = []
for row in range(n):
    a = []
    for col in range(n):
        a.append(matrix1[row][col])
    for col in range(n):
        a.append(matrix2[row][col])
    matrix.append(a)

for row in matrix:
    print(*row)