x1, y1, x2, y2 = map(int, input().split())
distance_two_points = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("%.2f" % distance_two_points)