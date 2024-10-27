from math import *

a, x, y = map(eval, input().split())
b = sqrt(exp(x) + a / (pow(x, 2) + 2))
c = pow(cos(x), 2) / sin(pow(x, 2))
d = sqrt(pow(y, 2) + exp(x) + b + c)
t = d + pow(cos(x), 3)

print("%.2f" % t)