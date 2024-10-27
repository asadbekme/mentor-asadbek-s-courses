s = input()
words = s.split()
l1, l2 = 0, 0

for word in words:
    if len(word) % 2 == 0:
        l1 += 1
    else:
        l2 += 1

print(l1 * l2)