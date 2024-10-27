import math as m

r1, r2, r3 = map(int, input().split())
s1 = m.pi * r1 * r1
s2 = m.pi * r2 * r2
s3 = m.pi * r3 * r3
print("%.2f" % s1, "%.2f" % s2, "%.2f" % s3)
