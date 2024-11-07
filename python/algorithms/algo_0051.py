x, y = map(float, input().split())

if (y >= -2 and x >= -1 and x <= 1 and y <= 0) or (x >= -1 and x <= 1 and y <= abs(x)):
    print("yes")
else:
    print("no")