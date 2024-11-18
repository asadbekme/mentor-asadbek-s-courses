n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

row_sums = []
for row in range(n):
    sum = 0
    for col in range(m):
        sum += matrix[row][col]
    row_sums.append(sum)

new_matrix = []
for row in range(n):
    a = []
    for col in range(m):
        a.append(matrix[row][col])
    a.append(row_sums[row])
    new_matrix.append(a)

for row in new_matrix:
    print(*row)