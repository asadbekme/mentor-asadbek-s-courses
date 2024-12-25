# * 1-st way:
# text = input()
# search_word = input()

# if search_word.lower() in text.lower():
#     print("Yes")
# else:
#     print("No")

# * 2-nd way:
text = input()
search_word = input()

if text.lower().find(search_word.lower()) != -1:
    print("Yes")
else:
    print("No")



