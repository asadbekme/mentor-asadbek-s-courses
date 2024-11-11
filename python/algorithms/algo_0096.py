
from math import pow, log, fabs
x, y, c, d = map(int, input().split())

s, p, sp, p1 = 0, 1, 1, 0

k = 1
while k <= x:
    s += (pow(-1, k) * (k + 1)) / (pow(k, 3) + pow(k, 2) + 1)
    k += 1

i = 1
while i <= y:
    p *= (pow(i, 3) + fabs(i - 9)) / (log(i) + 7 * i)
    i += 1

n = 1
while n <= c:
    m = 1
    while m <= d:
        p1 += pow(-1, m) * (log(m + 5)) / (pow(m, n + 3) + n * m)
        m += 1

    sp *= p1
    p1 = 0
    n += 1

print("%.2f %.2f %.2f" % (s, p, sp))