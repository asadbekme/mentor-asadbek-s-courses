# Read the dimensions of the matrix
N, M = map(int, input().split())

# Initialize the matrix
matrix = []

# Read the matrix elements
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

# Initialize a list to store the maximums of even columns
max_even_columns = []

# Iterate through each even column
for j in range(1, M, 2):
    max_value = -101  # Initialize to a value less than the minimum possible element
    for i in range(N):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
    max_even_columns.append(max_value)

# Print the maximums of even columns in a single row
print(*max_even_columns)