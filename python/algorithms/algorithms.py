# * 1-algorithm. Ikkita string'dagi belgilarni ketma-ket birlashtiruvchi algoritm
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

# * 2-algorithm. Bir nechta butun sonlarning eng katta qiymatini 0 ga almashtiruvchi algoritm
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
# n = int(input())
# array = list(map(int, input().split()))

# max_value = max(array)
# for index in range(n):
#     if array[index] == max_value:
#         array[index] = 0

# print(*array)

# * 3-algorithm. Find second largest element in the list
# * 1-st way: best solution
def find_second_largest(nums):
    if len(nums) < 2:
        return None
    
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    
    return second

# Example usage
nums = [10, 20, 4, 45, 99, 99]
print(find_second_largest(nums))  # Output: 45

# * 2-nd way:
# n = int(input())
# array = list(map(int, input().split()))
# if len(array) < 2:
#     print(None)
# else:
#     max_value = max(array)
#     new_array = []
#     for element in array:
#         if element != max_value:
#             new_array.append(element)
#     print(max(new_array))  

# * new knowledges
# * Practice in Python
# 1. slicing list
x = [1, 2, 3, 4]
print(x[2:]) # [3, 4]
print(x[4:]) # []
print(x[-3:-1]) # [2, 3] 
# 2. pow function => pow(base: int, exp: int, mod: int) -> return int type
print(pow(2, 5, 20)) # return 12 => 1. 2 ** 5 = 32; 2. 32 % 20 = 12
print(pow(3, 4, 7)) # return 4 => 1. 3 ** 4 = 81; 2. 81 % 7 = 4
# 3. list comprehension
z = [1, 2, 3]
y = z # but this way is not copy, it's reference
y.append(4)
print(z) # [1, 2, 3, 4]
# data types
a = {} # empty dictionary
b = set() # empty set
c = [] # empty list
d = () # empty tuple
print(type(a)) # <class 'dict'>
print(type(b)) # <class 'set'>
print(type(c)) # <class 'list'>
print(type(d)) # <class 'tuple'>
# bool function
print(bool(0)) # False
print(bool(1)) # True
print(bool(c)) # False
print(bool('')) # False
# for loop
s = 0
for i in range(8, 0, -2):
    # i = 8, 6, 4, 2
    s += (i - 3) ** 2

print(s) # 36

# function
# * recursive function - it's a function that calls itself
def f(x):
    if x < 3: return x
    return 3 * f(x - 1) - 2 * f(x - 2) + f(x - 3)

print(f(7)) # 114
print(f(6))
# * explanation
# f(7) = 3 * f(6) - 2 * f(5) + f(4) = 3 * 49 - 2 * 21 + 9 = 147 - 42 + 9 = 114
# f(6) = 3 * f(5) - 2 * f(4) + f(3) = 3 * 21 - 2 * 9 + 4 = 63 - 18 + 4 = 49
# f(5) = 3 * f(4) - 2 * f(3) + f(2) = 3 * 9 - 2 * 4 + 2 = 27 - 8 + 2 = 21
# f(4) = 3 * f(3) - 2 * f(2) + f(1) = 3 * 4 - 2 * 2 + 1 = 12 - 4 + 1 = 9
# f(3) = 3 * f(2) - 2 * f(1) + f(0) = 3 * 2 - 2 * 1 + 0 = 6 - 2 = 4
# f(2) = 2
# f(1) = 1
# f(0) = 0
# * 4-algorithm. Find the sum of the numbers in the list that are greater than the previous one
# * Bubble sort:
def bubbleSort(array):
    n = len(array)
    if n == 1:
        print("There is nothing to sort")
        return 1
    else:
        for i in range(n):
            for j in range(n - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1]= array[j + 1], array[j]

array = [1, 2, 0, 41, -42, 2847, -5238, -32578421, 4132787848, 43, 876, -87, 6, -1, 0]

if not array:
    print("List is empty")
    
bubbleSort(array)
print(array)