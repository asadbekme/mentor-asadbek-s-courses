from math import *

a = float(input())
if a <= 0:
    y = fabs(a + 1)
else:
    y = fabs(a - 1)
print("%.2f" % y)
