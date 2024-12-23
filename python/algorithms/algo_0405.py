text = input()
words = text.split()
counter = 0
for word in words:
    word = word.lower()
    reversed_word = word[::-1]
    if word == reversed_word:
        counter += 1

print(counter)
