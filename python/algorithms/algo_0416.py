text = input()

for index in range(len(text)):
    character = text[index]
    if character == "a" or character == "A":
        print(index + 1, end = " ")