from math import cos, pow, sqrt

x, y, c, d = map(int, input().split())

s, p, sp, p1 = 0, 1, 0, 0

for a in range(1, x + 1):
    s += pow(2 * a + cos(a), 2)

for a in range(1, y + 1):
    p *= (a + 6) / sqrt(pow(a, 2) + 2)

for k in range(1, c + 1):
    for y in range(1, d + 1):
        p1 += (pow(k, 2) + y) / sqrt(pow(k, 2) + pow(y, 2))
    sp += p1
    p1 = 0

print("%.2f %.2f %.2f" % (s, p, sp))