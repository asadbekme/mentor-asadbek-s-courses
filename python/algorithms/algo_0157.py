s = input()
i = int(input())
words = s.split()
words[i-1] = "TATU"

print(" ".join(words))