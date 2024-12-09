s = input()
vowel_letters = 'uioea'
letters = list(s.lower())
vowel_counter = 0

for letter in letters:
    if letter in vowel_letters:
        vowel_counter += 1

print(vowel_counter)
