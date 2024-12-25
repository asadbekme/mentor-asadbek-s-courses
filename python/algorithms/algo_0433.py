operator_types = {
    "cin": "kiritish operatori",
    "cout": "chiqarish operatori",
    "for": "sikl operatori",
    "if": "shart operatori",
    "{": "boshlash",
    "}": "tugash",
    "int": "butun tip",
    "double": "haqiqiy tip"
}

inputs = []
while True:
    line = input()
    if not line.strip():
        break
    inputs.append(line.strip())

for operator in inputs:
    if operator in operator_types:
        print(operator_types[operator])