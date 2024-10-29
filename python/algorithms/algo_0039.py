x, y = map(int, input().split())
a = (x + y) / 2
b = 2 * x * 2 * y

if x > y:
    y = a
    x = b
else:
    x = a
    y = b

print("%.1f" % x, "%.1f" % y)