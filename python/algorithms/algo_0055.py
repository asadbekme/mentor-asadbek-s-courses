from math import *

x, y = map(float, input().split())

if pow(x, 2) + pow(y, 2) <= 1:
    print("yes")
else:
    print("no")