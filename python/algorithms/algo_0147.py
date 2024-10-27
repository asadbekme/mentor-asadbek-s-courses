s = str(input())
l1, l2 = 0, 0

for i in range(len(s)):
    if s[i] == "A":
        l1 += 1
    if s[i] == "Y":
        l2 += 1

print(l1)
print(l2)