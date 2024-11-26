from math import *
t, s = map(float, input().split())

def G(a, b):
    return (pow(a, 2) + pow(b, 2)) / (pow(a, 2) + 2 * a * b + 3 * pow(b, 2) + 4)

result = G(1.2, s) + G(t, s) + G(2 * s - 1, s * t)
print("%.2f" % result)