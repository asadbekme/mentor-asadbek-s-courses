def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0: 
        return f(n // 2)
    else: 
        return f(n // 2) + f(n // 2 + 1)

n = int(input())
print(f(n))
