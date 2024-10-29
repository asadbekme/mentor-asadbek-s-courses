a, b, c, d = map(float, input().split())
max_value = max(a, b, c, d)
min_value = min(a, b, c, d)

if a <= b and b <= c and c <= d:
    a = b = c = d = max_value
else:
    a = b = c = d = min_value

print(a, b, c, d)
