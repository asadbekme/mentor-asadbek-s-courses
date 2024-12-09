# * 1-st way
# from math import *
# n = int(input())
# x = list(map(int, input().split()))
# k, m = map(int, input().split())

# s1, s2, s3, s4 = 0, 0, 0, 0
# for index in range(m - k):
#     s1 += x[index]

# for index in range(k):
#     s2 += x[index]

# for index in range(m):
#     s3 += x[index]

# for index in range(4):
#     s4 += x[index]

# result = (s1 + s2) / pow(s3 - s4, 2)
# print("%.2f" % result)

# * 2-nd way 
# * using function 
from math import *
n = int(input())
x = list(map(int, input().split()))
k, m = map(int, input().split())

def sum_of_array(array, start, end):
    sum = 0
    for index in range(start, end):
        sum += array[index]
    return sum

s1 = sum_of_array(x, 0, m - k)
s2 = sum_of_array(x, 0, k)
s3 = sum_of_array(x, 0, m)
s4 = sum_of_array(x, 0, 4)

result = (s1 + s2) / pow(s3 - s4, 2)
print("%.2f" % result)