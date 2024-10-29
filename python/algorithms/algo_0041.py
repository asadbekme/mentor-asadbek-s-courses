# * 1-st way
# x, y, z = map(float, input().split())
# min_value = min(x, y, z)

# if (x < 1 and y < 1 and z < 1):
#     if min_value == x:
#         x = (y + z) / 2
#     elif min_value == y:
#         y = (x + z) / 2
#     else:
#         z = (x + y) / 2

# print(x, y, z)

# * 2-nd way
x, y, z = map(float, input().split())

if x < 1 and y < 1 and z < 1:
    if x < y and x < z:
        x = (y + z) / 2
    elif y < x and y < z:
        y = (x + z) / 2
    else:
        z = (x + y) / 2
    print(x, y, z)
else:
    print(x, y, z)
