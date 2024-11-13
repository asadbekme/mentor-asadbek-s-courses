
from math import pow
a, b, c = map(int, input().split())

result = (a + b + c) / 3 * pow(a * b * c, 1 / 3)
print("%.1f" % result)  