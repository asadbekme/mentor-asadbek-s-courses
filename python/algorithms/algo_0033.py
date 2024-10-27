x, y, z = map(int, input().split())
a = max(x + y + z, x, y, z)
b = min(x + y / 2, x, y, z) ** 2

print("%.2f" % a, "%.2f" % b)