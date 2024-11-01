# * Bir o`lchamli sonli massivni max elementi bilan k-elementini o`rnini almashtiring. max elementidan bir necha bo`lishi mumkin
n = int(input())
array = list(map(int, input().split()))
k = int(input())

max_element = max(array)
new_array = []

for element in array:
    if element != max_element:
        new_array.append(element)
    else:
        new_array.append(array[k - 1])

new_array[k - 1] = max_element
print(*new_array)
