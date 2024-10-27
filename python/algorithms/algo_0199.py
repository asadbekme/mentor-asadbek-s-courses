# Lotin alfavitining kichik harflaridan iborat bo’lgan satr berilgan. Unda uchta undosh harf ketma-ket kelmaganligini aniqlash lozim. 
# Agar satrda hech qanday uchta unli harf ketma-ket kelmagan bo’lsa "YES", aks holda "NO" so’zini chiqaring.

s = input()
vowels = "aiueo"
count = 0
    
for char in s:
    if char not in vowels:
        count += 1
    else:
        count = 0
    
    if count == 3:
        print("NO")
        break
else:
    print("YES")

    



