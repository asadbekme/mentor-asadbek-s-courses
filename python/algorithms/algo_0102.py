n = int(input())
array = list(map(int, input().split()))
a, b = map(int, input().split())

min_value = min(array)
new_array = []

for i in range(n):
    if i >= a - 1 and i <= b - 1:
        new_array.append("%.1f" % (array[i] / min_value))
    else:
        new_array.append("%.1f" % array[i])

print(* new_array)