n = int(input())
letters = input()

a = letters.count("A")
s = letters.count("S")
l = letters.count("L")
o = letters.count("O")
m = letters.count("M")

if a >= 2 and s >= 2 and l >= 1 and o >= 1 and m >= 1:
    print("YES")
else:
    print("NO")

