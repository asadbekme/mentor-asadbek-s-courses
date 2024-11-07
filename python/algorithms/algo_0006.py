from math import pi, sqrt, pow
    
a, b, h = map(int, input().split())

S = pi * (a + b) / 2 * sqrt(pow(h, 2) + pow((a - b) / 2, 2)) + pi * (pow(a, 2) + pow(b, 2)) / 4

print("%.2f" % S)