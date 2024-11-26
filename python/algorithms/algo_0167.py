from math import *
y = float(input())

def calculate_t(x):
    s1, s2 = 0, 0
    k = 0
    while k <= 10:
        s1 += pow(x, 2 * k + 1) / factorial(2 * k + 1)
        s2 += pow(x, 2 * k) / factorial(2 * k)
        k += 1
    
    return s1 / s2

result = (1.7 * calculate_t(0.25) + 2 * calculate_t(y + 1)) / (6 - calculate_t(pow(y, 2) - 1))
print("%.2f" % result)