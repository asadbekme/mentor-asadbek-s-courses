from math import *

x, y, a, b = map(int, input().split())

s, p, sp = 0, 1, 0
for j in range(1, x + 1):
    s += (pow(j, 2) + 2 * j) / (pow(j, 3) + j * pow(cos(j), 2) + 1)

for i in range(1, y + 1):
    p *= (pow(i, 2) + 1) / (pow(i, 3 / i) + 2)


for i in range(1, a + 1):
    p1 = 1
    for k in range(1, b + 1):
        p1 *= log((pow(k, i) + pow(k, 1 / i)) / (pow(k, 3) + pow(i, 1 / k)))
    sp += p1
    
print("%.2f" % s, "%.2f" % p, "%.2f" % sp)
