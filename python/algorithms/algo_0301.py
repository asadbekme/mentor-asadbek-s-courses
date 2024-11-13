from math import pow, sqrt
x, y = map(int, input().split())

a = pow(y, x - 5)
b = pow((pow(x, y - 5) + pow(y + 5, x)), x - y)
c = pow(x + 1, y - 7) + x * y
W = (a + sqrt(b)) / c
print("%.2f" % W)  