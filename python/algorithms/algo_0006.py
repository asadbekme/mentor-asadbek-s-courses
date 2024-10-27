# Natijani ikki kasr xonasigacha formatlab chop etish
# print(f"{20.256756:.2f}")
# print("%.2f" % 20.256756)
# print("%.4f" % 20.256756)

# x, y, z = 3, "Hello", 4.5
# print(x+z, y)

# Strings in Python
# first_name = "Asadbek"
# last_name = "Rakhimov"
# city = "Urgench"
# region = 'Khorezm'
# smile = "😁"
# hello = "Привет"
# text = "Men yangi 📱 sotib oldim"
# full_name = f"{first_name} {last_name}"

# print(f"{hello}. {first_name} is from {city}, {region}. {smile}")
# print(text)
# print(hello + " " + first_name)
# print(f"{hello} {first_name}. Cho' tam? {smile}")
# print(f"I am {first_name} {last_name}. I live in {city}, {region}. {smile}")
# print(full_name.upper())
# print(full_name.lower())
# print(full_name.title())
# print(full_name.capitalize())
# print(full_name)

ism = input("Ismingiz nima?\n>>>") # Foydalanuvchi ismini yangi qatordan kiritadi
print("Assalom alaykum, " + ism.title())
print(len(ism))
print(ism[0])
# Python'da satrlar (string) o'zgarmas tur (immutable) hisoblanadi, ya'ni ulardagi 
# belgilarni bevosita indeks orqali o'zgartirib bo'lmaydi. Ammo satrni yangidan 
# hosil qilib, kerakli o'zgarishlarni kiritish mumkin.
print("B" + ism[1:])