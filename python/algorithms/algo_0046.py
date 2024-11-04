from math import pow

a = float(input())
if a <= -1:
    print("%.2f" % (1 / (pow(a, 2))))
elif a >= -1 and a < 2:
    print("%.2f" % (pow(a, 2)))
else:
    print("%.2f" % 4)
