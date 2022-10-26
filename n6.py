value = int(input("Enter value: "))
product = 1

while value > 0:
    tmp = value % 10
    if tmp > 0:
        product *= tmp
    value //= 10

print(f"Произведение равно: {product}")