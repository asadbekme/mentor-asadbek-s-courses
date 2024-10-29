from math import fabs
x, y = map(float, input().split())

if x < 0 and y < 0:
    x = fabs(x)
    y = fabs(y)
elif x < 0 or y < 0:
    x = x + 0.5
    y = y + 0.5
else:
    x = x
    y = y

print(x, y)
