n = int(input())
array = list(map(int, input().split()))

def is_prime(element):
    if element <= 1:
        return False
    if element <= 3:
        return True
    if element % 2 == 0 or element % 3 == 0:
        return False
    i = 5
    while i * i <= element:
        if element % i == 0 or element % (i + 2) == 0:
            return False
        i += 6
    return True

s = 0
for element in array:
    if is_prime(element):
        s += element
print(s)