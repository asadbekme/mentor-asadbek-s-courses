from math import fabs

a, b, c = map(int, input().split())

if c <= b <= a:
    a = 2 * a
    b = 2 * b
    c = 2 * c
else:
    a = int(fabs(a))
    b = int(fabs(b))
    c = int(fabs(c))

print(a, b, c)


