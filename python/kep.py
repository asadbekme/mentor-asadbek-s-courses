# * 56. add function
# def add(a, b):
#     return a + b

# add(2, 2)
# add(3, 5)

# * 57. sum_digits function
# def sum_digits(n):   
#     sum = 0
#     for digit in str(n):
#         sum += int(digit)
#     return sum

# sum_digits(2)
# sum_digits(123)

# * 58. filter_list function
# def filter_list(l, n):
#     if n == 0:
#         return [x for x in l if x % 2 != 0]
#     else:
#         return [x for x in l if x % 2 == 0]


# filter_list([1, 2, 3, 4, 5, 6], 0) # [1, 3, 5]
# filter_list([3, 5, 3, 6], 1) # [6]


import datetime

# Bugungi sanani olamiz
today = datetime.datetime.today()

# Yakshanba 6-indexda joylashgan (0 - Dushanba, 6 - Yakshanba)
yakshanba_kuni = 6

# Bugungi hafta kunini olamiz
bugungi_hafta_kuni = today.weekday()

# Bugungi kunga qadar nechta kun qolgani hisoblaymiz
kun_qoldi = (yakshanba_kuni - bugungi_hafta_kuni) % 7

# Agar bugun yakshanba bo'lsa, kelasi yakshanbagacha 7 kun qoldi
if kun_qoldi == 0:
    kun_qoldi = 7

# Natijani chop etamiz
print(kun_qoldi)
