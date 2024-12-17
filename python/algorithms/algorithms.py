# 1. Ikkita string'dagi belgilarni ketma-ket birlashtiruvchi algoritm
# def join_strings(s1, s2):
#     result = ""
#     max_length = max(len(s1), len(s2))

#     for i in range(max_length):
#         if i < len(s1):
#             result += s1[i]
#         if i < len(s2):
#             result += s2[i]

#     return result

# print(join_strings("abc", "xyz"))  # axbycz
# print(join_strings("Hello!", "guy"))  # Hgeulylo!

# 2. Bir nechta butun sonlarning eng katta qiymatini 0 ga almashtiruvchi algoritm
# * 1-st way:
# def replace_max_with_zero(array):
#     max_value = max(array)
#     new_array = []

#     for element in array:
#         if element == max_value:
#             new_array.append(0)
#         else:
#             new_array.append(element)

#     return new_array

# n = int(input())
# array = list(map(int, input().split()))

# result = replace_max_with_zero(array)
# print(*result)
    
# * 2-nd way:
n = int(input())
array = list(map(int, input().split()))

max_value = max(array)
for index in range(n):
    if array[index] == max_value:
        array[index] = 0

print(*array)

