from math import sqrt
c = float(input())

a = c / 2
b = sqrt(3) * c / 2
p = a + b + c
s = a * b / 2
h = 2 * s / c
print("%.2f" % p, "%.2f" % h)
