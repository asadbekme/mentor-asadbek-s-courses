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

# * List operations
# * List is a collection of items in a particular order
ages = [12, 45, 89, 30, 26, 75, 62, 7]
cars = ["BMW", "Mercedes", "Volvo", "Audi", "Ford"]
nums = list(range(1, 8, 2))

min_age = min(ages)
max_age = max(ages)
average_age = sum(ages) / len(ages)
print(f"Minimum age: {min_age}")
print(f"Maximum age: {max_age}")
print(f"Average age: {average_age}")
print(f"Sorted ages: {sorted(ages, reverse=True)}")
print(f"Sorted cars: {sorted(cars)}")
print(f"Numbers: {nums}")

# * Slicing lists
print(f"First 3 cars: {cars[:3]}")
print(f"Last 3 cars: {cars[-3:]}")
print(f"Cars from index 2 to 4: {cars[2:5]}")
print(f"Cars from index 2 to the end: {cars[2:]}")
print(f"Cars from the beginning to index 3: {cars[:4]}")

# * List methods
cars.append("Tesla")
print(f"Cars after appending Tesla: {cars}")
cars.insert(2, "Toyota")
print(f"Cars after inserting Toyota at index 2: {cars}")
cars.remove("Audi")
print(f"Cars after removing Audi: {cars}")

# * Copying lists
cars_copy = cars[:]
print(f"Cars copy: {cars_copy}")

# * Checking if a list is empty
print(f"Is cars list empty? {not cars}")

# * Looping through lists
for car in cars:
    print(f"Car: {car}")

for i in range(len(cars)):
    print(f"Car at index {i}: {cars[i]}")

# * Tuple - immutable list, cannot be changed, used for fixed data, faster than list.
toys = ("car", "doll", "ball", "robot")
print(f"Toys: {toys}")
print(f"First toy: {toys[0]}")
print(f"Length of toys: {len(toys)}")

# * Looping through tuples
for toy in toys:
    print(f"Toy: {toy}")

for i in range(len(toys)):
    print(f"Toy at index {i}: {toys[i]}")
