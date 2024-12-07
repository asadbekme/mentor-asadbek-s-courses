a, b, c = sorted(map(int, input().split()))

if (a ** 2 + b ** 2 == c ** 2):
    print(1)
elif (a == b and b == c and a == c):
    print(3)
elif (a == b or a == c or b == c):
    print(2)
else:
    print(4)