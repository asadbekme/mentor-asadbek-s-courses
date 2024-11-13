from math import exp, pow, log
x = float(input())

S = exp(2) + exp(x) / 12 + pow(2, x + 1) + log(pow(x, x + 20), x)
print("%.2f" % S)   