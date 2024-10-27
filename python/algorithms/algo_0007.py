import math as m

h, r = map(int, input().split())
v = m.pi * r * r * h / 3
print("%.2f" % v)