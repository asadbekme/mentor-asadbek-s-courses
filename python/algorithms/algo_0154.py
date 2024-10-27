N = input()
numbers_list = list(N)
sum = 0

for number in numbers_list:
    if number.isdigit():
        sum += int(number)

print(sum)
