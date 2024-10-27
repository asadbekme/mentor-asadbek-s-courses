s = input()
i, j = map(int, input().split())
words = s.split()

words[i - 1], words[j - 1] = words[j - 1], words[i - 1]

print(" ".join(words))
