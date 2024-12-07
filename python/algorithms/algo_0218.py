# * 1-st solution:
# from math import *
# n = int(input())

# def is_square(number):
#     if number < 0:
#         return "No"
#     root = int(sqrt(number))
#     if root * root == number:
#         return "Yes"
#     return "No"

# print(is_square(n))

# * 2-nd solution:
from math import sqrt

n = int(input())
if n < 0:
    print("No")
else:
    root = sqrt(n)
    if root == int(root):
        print("Yes")
    else:
        print("No")

# print(4.0 % 1 == 0) # True
# print(12.77 % 1 == 0) # False