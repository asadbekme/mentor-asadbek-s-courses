from math import pow, log, fabs, cos
x, y, c, d = map(int, input().split())

s, p, sp, p1 = 0, 1, 0, 1

a = 1
while a <= x:
    s += (4 * a + 6 * log(a)) / (pow(a, 2) + a)
    a += 1

b = 1
while b <= y:
    p *= fabs(b - 6 * cos(b)) / (pow(b, 2) + pow(b, log(b)))
    b += 1

k = 1
while k <= c:
    a = 1
    while a <= d:
        p1 *= (a * k + x) / (pow(k, 2) + pow(y, 2))
        a += 1

    sp += p1
    p1 = 1
    k += 1

print("%.2f %.2f %.2f" % (s, p, sp)) 