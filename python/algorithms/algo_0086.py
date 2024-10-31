from math import *

a, b, c = map(int, input().split())

x, h, y = c, 0.25, 0

while x <= b:
    y += pow(a, 2) * cos(x) + sin(x) / 2 + b * pow(x, 2)
    x += h

print("%.2f" % y)
