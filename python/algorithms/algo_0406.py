# * 1-st way:
# text = input()
# letter = input()
# words = text.split()
# for word in words:
#     if word.lower().startswith(letter.lower()):
#         print(word.lower(), end = " ")

# * 2-nd way:
text = input()
letter = input()
words = text.split()
for word in words:
    word = word.lower()
    if word[0] == letter.lower():
        print(word, end = " ")