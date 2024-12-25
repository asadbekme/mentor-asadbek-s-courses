n, m = map(int, input().split())
matrix = []
for row in range(n):
    matrix.append(list(map(int, input().split())))

array = []
for row in range(n):
    odd_counter = 0
    for col in range(m):
        if matrix[row][col] % 2 == 1:
            odd_counter += 1
    array.append(odd_counter)

print(*array)
        