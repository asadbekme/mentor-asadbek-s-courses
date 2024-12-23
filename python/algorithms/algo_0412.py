# * 1-st way: best way to find the nth Fibonacci number
n = int(input())
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Example usage:
print(fibonacci(n))  # Output: 34

# * 2-nd way: time complexity is O(2^n)
# n = int(input())
# def fibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(n))  