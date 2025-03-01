a, b, c = map(int, input().split())
max_value = max(a, b, c)
min_value = min(a, b, c)
average_arithmetic = (max_value + min_value) / 2
print("%.1f" % average_arithmetic)