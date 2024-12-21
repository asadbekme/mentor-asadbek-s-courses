n = int(input())
array = list(map(int, input().split()))
max_element = array[0]

for index in range(1, n):
    if (index - 1) % 2 == 1 and array[index] % 2 == 0 and array[index] > max_element:
        max_element = array[index]  

print(max_element)