n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_value = matrix[0][0]
min_value = matrix[0][0]
for row in range(n):
    for col in range(m):
        if matrix[row][col] > max_value:
            max_value = matrix[row][col]
        if matrix[row][col] < min_value:
            min_value = matrix[row][col]
    
s = 0
for row in range(n):
    for col in range(m):
        if matrix[row][col] == max_value or matrix[row][col] == min_value:
            s += matrix[row][col]

print(s)