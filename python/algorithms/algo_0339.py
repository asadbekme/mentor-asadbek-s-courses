m1, m2, m3 = map(int, input().split())
if m1 > m2 and m1 > m3:
    print(m1)
elif m2 > m1 and m2 > m3:
    print(m2)
else:
    print(m3)