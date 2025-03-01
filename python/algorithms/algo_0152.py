# * 1-way:
# s = input()
# reversed_string = s[::-1]
# print(reversed_string)

# * 2-way:
# s = input()
# letters = list(s)
# letters.reverse()
# reversed_string = "".join(letters)

# print(reversed_string)

# * 3-way:
s = input()
reversed_string = ""

for character in s:
    reversed_string = character + reversed_string
    # x += a is equivalent to x = x + a

print(reversed_string)