n = int(input())
array = list(map(int, input().split()))
even_counter, odd_counter = 0, 0

for element in array:
    if element % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1

print(even_counter)
print(odd_counter)