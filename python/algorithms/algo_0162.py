n = int(input())
s = input()
ss = ""

for i in s:
    if i == "$":
        ss += ""
    else:
        ss += i

print(ss)
