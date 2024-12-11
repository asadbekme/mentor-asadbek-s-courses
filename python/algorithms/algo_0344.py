# * 1-st way:
# s = input()
# l, r = map(int, input().split())

# if l > r:
#     letters = list(s[r - 1:l])
#     letters.reverse()
#     print("".join(letters))
# else:
#     print(s[l - 1:r])

# * 2-nd way:
s = input()
l, r = map(int, input().split())

def slicing_string_by_range(s, l, r):
    if l > r:
        letters = list(s[r - 1 : l])
        letters.reverse()
        print("".join(letters))
    else:
        print(s[l - 1 : r])

slicing_string_by_range(s, l, r)
