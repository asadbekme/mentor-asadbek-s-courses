from math import *

a = int(input())
x = - pi / 2
h = pi / 10
y = 0

while x <= pi:
    y += 2 * pow(a, sin(2 * x) / 3) + pow(x, 2) * cos(a * x)
    x += h

print("%.2f" % y)
