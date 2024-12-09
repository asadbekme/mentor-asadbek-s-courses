n, m = map(int, input().split())
matrix = []
for row in range(n):
    matrix.append(list(map(int, input().split())))

positive_elements_sum, negative_elements_sum = 0, 0
for row in range(n):
    for col in range(m):
        if matrix[row][col] > 0:
            positive_elements_sum += matrix[row][col]
        else:
            negative_elements_sum += matrix[row][col]

print("%.2f" % (positive_elements_sum / negative_elements_sum))