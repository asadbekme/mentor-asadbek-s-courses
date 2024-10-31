n = int(input())
array = list(map(int, input().split()))

s1 = 0
s2 = sum(array)
for element in array:
    s1 += pow(element, 2)

print(s1)
print("%.2f" % (s2 / len(array)))
