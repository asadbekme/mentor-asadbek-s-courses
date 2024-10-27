s = input()
count = 0
vowels = "AaOoIiUuEe"

for char in s:
    if char in vowels:
        count += 1

print(count)