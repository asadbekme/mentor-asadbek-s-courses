n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

sum, count = 0, 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] % m == 0:
            sum += matrix[i][j]
            count += 1

print("%.2f" % (sum / count))