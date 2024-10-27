s = input()
words = s.split()
total = 0

for word in words:
    if word.startswith("a") and word.endswith("b"):
        total += 1

print(total)