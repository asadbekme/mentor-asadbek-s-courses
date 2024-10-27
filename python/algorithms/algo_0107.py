n = int(input())
array = list(map(int, input().split()))

# * 1-st way
# higest_element = max(array)

# * 2-nd way
higest_element = array[0]
for i in range(n):
    if array[i] > higest_element:
        higest_element = array[i]
# print(higest_element)

for i in range(n):
    print("%.2f" % (array[i] / higest_element), end=" ")