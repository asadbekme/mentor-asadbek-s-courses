s = input()
words = s.split()
l = 0

for word in words:
    if word[0].isupper():
        l += 1

print(l)