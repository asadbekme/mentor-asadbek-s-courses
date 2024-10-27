s = input()
txt = ''

for i in s:
    if i.isupper():
        txt += i.lower()
    else:
        txt += i.upper()

print(txt)