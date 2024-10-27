s = input()
words = s.split()
length = len(words[0])
longest_word = words[0]

for word in words:
    if len(word) > length:
        length = len(word)
        longest_word = word

print(longest_word)