# 1-usul:
# s = input()
# words = s.split()

# na_words = [word for word in words if word.endswith("NA")]

# print(len(na_words))
# print(" ".join(na_words))

# 2-usul:
# s = input()
# words = s.split()
# na_words = []

# for word in words:
#     if word.endswith("NA"):
#         na_words.append(word)

# print(len(na_words))
# print(" ".join(na_words))

# 3-usul:
s = input()
words = s.split()
na_words = []

for word in words:
    if word[len(word) - 2] == "N" and word[len(word) - 1] == "A":
        na_words.append(word)

print(len(na_words))
print(" ".join(na_words))