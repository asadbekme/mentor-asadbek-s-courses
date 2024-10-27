s = input()
words = s.split()

info_words = []

for word in words:
    if word.lower().find("info") != -1:
        info_words.append(word)

print(" ".join(info_words))