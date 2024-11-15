# * 1-st way
# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# k = int(input())

# new_matrix = []
# for i in range(n):
#     a = []
#     for j in range(m):
#         a.append(matrix[i][j])
#     if i == (k - 1):
#         continue
#     new_matrix.append(a)

# for i in range(n - 1):
#     for j in range(m):
#         print(new_matrix[i][j], end = " ")
#     print()

# * 2-nd way
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for i in range(n):
    if i == (k - 1):
        continue
    for j in range(m):
        print(matrix[i][j], end = " ")
    print()