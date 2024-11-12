from math import fabs
x, y = map(float, input().split())

if (y >= fabs(x) and y <= 1) or (y <= 1.5 and y >= 1 and x >= -2 and x <= 2):
    print("yes")
else:
    print("no")