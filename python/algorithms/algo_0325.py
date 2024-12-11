from math import pow, log
x, y, c, d = map(int, input().split())
s, p, sp, p1 = 0, 1, 0, 1
m = 1
while m <= x:
    s += (3 * pow(m, 3)) / (pow(m, 3) + log(m + 3))
    m += 1

k = 1
while k <= y:
    p *= (3 * k) / (pow(k, 3) + 7 * k)
    k += 1

i = 1
while i <= c:
    for j in range(1, d + 1):
        p1 *= (log(i) + pow(j, i)) / (pow(j, i) + pow(i, 2))
    sp += p1
    p1 = 1
    i += 1

print("%.2f %.2f %.2f" % (s, p, sp))

