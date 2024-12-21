n = int(input())
array = list(map(int, input().split()))

# Massivni o'sish tartibida saralash
array.sort()

# Eng katta ko'paytmani topish uchun ikkita variantni tekshirish kerak:
# 1. Uchta eng katta musbat sonlarning ko'paytmasi
# 2. Ikki eng kichik manfiy son va eng katta musbat sonning ko'paytmasi
max_product = max(array[-1] * array[-2] * array[-3], array[0] * array[1] * array[-1])

print(max_product)