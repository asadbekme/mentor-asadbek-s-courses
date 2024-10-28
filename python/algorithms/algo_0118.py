n = int(input())
array = list(map(int, input().split()))

total_sum, odd_count = 0, 0

for element in array:
    if element % 2 == 1:
        odd_count += 1
        total_sum += element

if odd_count == 0:
    print("0.00")
else:
    average = total_sum / odd_count
    print(f"{average:.2f}")
