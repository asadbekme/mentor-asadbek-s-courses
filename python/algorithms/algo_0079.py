from math import *

a = float(input())
y = 0
x = -(pi / 2)
h = pi / 19
while x <= pi:
    y += pow(a, a / 3) + pow(x, 2) * cos(a * x)
    x += h

print("%.2f" % y)
