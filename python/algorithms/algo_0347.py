n, m = map(int, input().split())
matrix = []
for row in range(n):
    matrix.append(list(map(int, input().split())))

s = 0
for row in range(n):
    for col in range(m):
        s += matrix[row][col]

average_value = s / (n * m)
print("%.2f" % average_value)