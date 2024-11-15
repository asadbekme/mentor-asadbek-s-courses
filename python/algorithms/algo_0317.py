from math import pow, fabs
x, y = map(float, input().split())

try:
    b = x + 2 * y
    c = pow(y, 2) + fabs((pow(y, 2) + 2) / (x + 1))
    d = 2 * x - y
    a = b / c + d 
    print("%.2f" % a) 
except:
    print("-3.00")