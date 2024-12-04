n = int(input())
array = list(map(int, input().split()))

def is_arithmetic_progression(arr):
    # Massiv uzunligi 2 yoki undan kam bo'lsa, bu progressiya
    if len(arr) <= 2:
        return "yes"
    
    # Dastlabki ikki element o'rtasidagi farq
    diff = arr[1] - arr[0]
    
    # Har bir ketma-ket elementlar farqini tekshirish
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != diff:
            return "no"
    
    return "yes"

print(is_arithmetic_progression(array))