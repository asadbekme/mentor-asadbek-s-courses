from math import *

x, y = map(float, input().split())

if y >= 0 and pow(x, 2) + pow(y, 2) >= 1 and pow(x, 2) + pow(y, 2) <= 4:
    print("yes")
else:
    print("no")