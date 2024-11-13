from math import factorial, pow
n, x = map(int, input().split())

s, i = 0, 1
while i <= n:
    s += pow(x, i) * factorial(i + 1) / factorial(i)
    i += 1
print(int(s))