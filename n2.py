marker = input("Enter marker: ")
thickness = int(input("Enter thickness: "))

for i in range(thickness):
    s = thickness - i
    print(" " * s + (i * marker) + marker + (i * marker))

for i in range(thickness + 1):
    s = thickness // 2 + 1
    print(" " * s + marker * thickness + " " * (thickness * 3) + marker * thickness)

for i in range(thickness // 2 + 1):
    s = thickness // 2 + 1
    print(" " * s + marker * (thickness * 5))

for i in range(thickness + 1):
    s = thickness // 2 + 1
    print(" " * s + marker * thickness + " " * (thickness * 3) + marker * thickness)

for i in range(thickness - 1, -1, -1):
    l = thickness * 4 + 1
    s = thickness - i - 1
    print(" " * l + " " * s + (i * marker) + marker + (i * marker))