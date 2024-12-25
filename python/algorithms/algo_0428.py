n, m = map(int, input().split())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

max_element = matrix[0][0]
for row in range(n):
    for col in range(m):
        if matrix[row][col] > max_element:
            max_element = matrix[row][col]

for row in range(n):
    for col in range(m):
        if matrix[row][col] > 0:
            matrix[row][col] = matrix[row][col] / max_element
            print("%.2f" % matrix[row][col], end = ' ')
        else:
            print("%.2f" % matrix[row][col], end = ' ')
    print()

# for row in range(n):
#     for col in range(m):
#         print("%.2f" % matrix[row][col], end = ' ')
#     print()