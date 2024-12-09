s = input()
letters = list(s)
upper_letters = ""

for letter in letters:
    if letter.isupper():
        upper_letters += letter

# if len(upper_letters) > 0:
#     print(upper_letters)
# else:
#     print(-1)

# using ternary operator
print(upper_letters if len(upper_letters) > 0 else -1)