s = input()
l, r = map(int, input().split())

if l > r:
    letters = list(s[r - 1:l])
    letters.reverse()
    print("".join(letters))
else:
    print(s[l - 1:r])
