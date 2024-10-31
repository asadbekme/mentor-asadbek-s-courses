a, b, c = map(int, input().split())

x, h, y = 1, 5, 0

while x <= 20:
    y += (a * pow(x, 2) + b * x + c) / (pow(a, 2) + pow(b, 2) + pow(x, 2))
    x += h

print("%.2f" % y)
