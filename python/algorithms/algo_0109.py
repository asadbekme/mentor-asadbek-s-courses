from math import log

n = int(input())
array = list(map(int, input().split()))
m = int(input())
p = 1

for element in array:
    if element > m:
        p *= element

print("%.2f" % log(p))