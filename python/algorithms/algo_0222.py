from math import *

n = int(input())
count = 0

# Kvadrat ildizgacha bo'luvchilarni tekshirish
for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        # Agar `i` bo'luvchisi bo'lsa, ikkita bo'luvchini hisobga olish kerak
        count += 1
        if i != n // i:  # `i` va `n//i` bir xil bo'lmasa, juft bo'luvchini qo'shish
            count += 1

print(count)
