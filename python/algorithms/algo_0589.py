# * 1-st way
# from math import *
# n = int(input())

# def f(x):
#     return pow(-1, x) * x

# s = 0
# for i in range(1, n + 1):
#     s += f(i)

# print(int(s))

# * 2-nd way
n = int(input())

if n % 2 == 0: 
    print(n // 2)
else:
    print(-(n // 2 + 1))


