a, b, c = map(float, input().split())
result = (max(a, a + b) + max(a, b + c)) / (1 + max(a + b * c, 1.15))

print("%.2f" % result)