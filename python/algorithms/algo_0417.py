n = int(input())
matrix = []

for row in range(n):
    matrix.append([])  # Har bir qator uchun bo'sh ro'yxat qo'shamiz
    for col in range(n):
        if (row + col) % 2 == 0:
            matrix[row].append(0)  # Juft o'rin uchun 0 qo'shamiz
        else:
            matrix[row].append(1)  # Toq o'rin uchun 1 qo'shamiz

for row in range(n):
    for col in range(n):
        print(matrix[row][col], end = " ")
    print()