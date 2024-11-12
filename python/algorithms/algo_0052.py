x, y = map(float, input().split())

if (y <= 2 * x + 3 and y >= x - 1 and y <= 0) or (y <= 2 * x + 3 and y <= -x and y >= 0):
    print ("yes")
else:
    print ("no")