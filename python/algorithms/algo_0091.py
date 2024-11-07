from math import *

a, b, c, d = map(int, input().split())

S, P = 0, 1
SP, PP = 0, 1
for m in range(1, a + 1):
    S += (3 * pow(m, 3) + 4 * m + 5) / (pow(m, 3) + log(m))

for k in range(1, b + 1):
    P *= k / (pow(k, 3) + 7 * k + 5)

for i in range(1, c + 1):
    for m in range(1, d + 1):
        PP *= (log(i) + pow(m, i)) / pow(m, i)
    SP += PP
    PP = 1

print("%.2f"% S , "%.2f"% P, "%.2f"% SP)