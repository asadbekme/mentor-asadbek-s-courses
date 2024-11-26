from math import *
s, t = map(float, input().split())
def h(a, b):
    return a / (pow(b, 2) + 1) + b / (pow(a, 2) + 1) - pow(a - b, 3)

result = h(s, t) + max(h(s - t, s * t), h(s - t, s + t)) + h(1, 1)
print("%.2f" % result)