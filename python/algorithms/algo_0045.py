a, b, c = map(int, input().split())
D = b * b - 4 * a * c
x1 = (-b + D ** 0.5) / (2 * a)
x2 = (-b - D ** 0.5) / (2 * a)

if D >= 0:
    print("%.2f %.2f" % (x1, x2))
else:
    print("NO")
