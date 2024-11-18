n, m = map(int, input().split())
matrix = []
for row in range(n):
    matrix.append(list(map(int, input().split())))
x, y = map(int, input().split())

s, count = 0, 0
for row in range(n):
    for col in range(m):
        if matrix[row][col] >= x and matrix[row][col] <= y:
            s += matrix[row][col]
            count += 1

print("%.2f" % (s / count))