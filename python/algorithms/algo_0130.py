n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

row_sums = []
max_value = matrix[0][0]
min_value = matrix[0][0]

for i in range(n):
    row_sum = 0
    for j in range(m):
        row_sum += matrix[i][j]
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
    
    row_sums.append(row_sum)

print(*row_sums)
print(max_value, min_value)