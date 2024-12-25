n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

for col in range(m):
    even_counter = 0
    for row in range(n):
        if matrix[row][col] % 2 == 0:
            even_counter += 1
    print(even_counter, end = ' ')