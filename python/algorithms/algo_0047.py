a = float(input())

if a <= 1:
    print("%.2f" % (abs(a)))
elif a > 1 and a <= 2:
    print("%.2f" % (1))
else:
    print("%.2f" % (-2 * a + 5))
