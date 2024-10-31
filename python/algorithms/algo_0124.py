# * Bir o`lchamli sonli massivni max elementi bilan k-elementini o`rnini almashtiring. max elementidan bir necha bo`lishi mumkin
n = int(input())
array = list(map(int, input().split()))
k = int(input())

max_element = max(array)

for index in range(n):
    if array[index] == max_element:
        array[index], array[k - 1] = array[k - 1], max_element

print(*array)
