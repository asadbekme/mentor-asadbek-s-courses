# 1. Ikkita string'dagi belgilarni ketma-ket birlashtiruvchi algoritm
def join_strings(s1, s2):
    result = ""
    max_length = max(len(s1), len(s2))

    for i in range(max_length):
        if i < len(s1):
            result += s1[i]
        if i < len(s2):
            result += s2[i]

    return result

print(join_strings("abc", "xyz"))  # axbycz
print(join_strings("Hello!", "guy"))  # Hgeulylo!