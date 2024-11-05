from math import *

a, b, c = map(int, input().split())
x, h, y = -pi, pi/10, 0

while x <= pi:
    y += (log(pow(a, 2 * sin(x))) + exp(2 * x)) / (atan(x) + b) + c
    x += h

print(f"{y:.2f}")
