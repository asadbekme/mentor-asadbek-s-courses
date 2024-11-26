a, b = map(float, input().split())
def min_func(x, y):
    if x < y:
        return x
    else:
        return y

def max_func(x, y):
    if x > y:
        return x
    else:
        return y
    
u = min_func(a, b)
v = min_func(a * b, max_func(a, b))
s = min_func(u + v, 3.14)

print("%.2f %.2f %.2f" % (u, v, s))

