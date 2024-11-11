from math import pow, sqrt, exp

x, y, c, d = map(int, input().split())
s, p, sp, p1 = 0, 1, 0, 1

for k in range(1, x + 1):
    s += pow(k, 3) + exp(k)

for a in range(3, y + 1):
    p *= (a * x) / sqrt(pow(a, 2) + pow(x, 2)) 

for i in range(1, c + 1):
    for j in range(1, d + 1):
        p1 *= (i * x + pow(j, 2)) / sqrt(pow(i, 2) + j * y)
    
    sp += p1
    p1 = 1

print("%.2f %.2f %.2f" % (s, p, sp))  