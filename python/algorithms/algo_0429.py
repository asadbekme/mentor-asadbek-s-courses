n, m = map(int, input().split())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# find index of max element in matrix
max_element = matrix[0][0]
max_row, max_col = 0, 0

for row in range(n):
    for col in range(m):
        if matrix[row][col] > max_element:
            max_element = matrix[row][col]
            max_row = row
            max_col = col

print(max_row + 1, max_col + 1)