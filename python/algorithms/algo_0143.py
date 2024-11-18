# * 1-st way
# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]

# new_matrix = []
# for i in range(n):
#     a = []
#     for j in range(m):
#         a.append(matrix[i][j])
#         a.sort()
#     new_matrix.append(a)

# for i in range(n):
#     for j in range(m):
#         print(new_matrix[i][j], end = " ")
#     print()

# * 2-nd way
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for row in matrix:
    row.sort() 

for row in matrix:
    print(*row)


