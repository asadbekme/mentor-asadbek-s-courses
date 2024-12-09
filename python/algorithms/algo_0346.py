n, m = map(int, input().split())
matrix = []
for row in range(n):
    matrix.append(list(map(int, input().split())))

for row in range(n - 1, -1, -1):
    for col in range(m - 1, -1, -1):
        print(matrix[row][col], end = " ")
    print()
