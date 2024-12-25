pascal_code = ""
while True:
    line = input()
    pascal_code += line + "\n"
    if line.strip().lower() == "end.":
        break

begin_count = pascal_code.lower().count("begin")
print(begin_count)