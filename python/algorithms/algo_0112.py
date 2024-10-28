n = int(input())
array = list(map(int, input().split()))
s, p = 0, 1

# * 1-st way
# for i in range(n):
#     if i % 2 == 0:
#         p *= array[i]
#     else:
#         s += array[i]

# * 2-nd way
for i in range(1, n + 1):
    if i % 2 == 1:
        p *= array[i - 1]
    else:
        s += array[i - 1]

print("%.2f" % (p / s))