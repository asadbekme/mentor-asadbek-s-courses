n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

column_sums, max_value, min_value = [], matrix[0][0], matrix[0][0] 
for j in range(m):
    column_sum = 0
    for i in range(n):
        column_sum += matrix[i][j]
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
    
    column_sums.append(column_sum)

print(*column_sums)
print(max_value, min_value)

