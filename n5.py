height = int(input("Enter height: "))
width = height * 3

for i in range(1):
    print("|" * width)

for i in range(1, height - 2, 2):
    print("|" + ("\\/" * i).center(width - 2, "-") + "|")

print("|" + "HELLO".center(width - 2, "-") + "|")

for i in range(height - 4, 0, -2):
    print("|" + ("/\\" * i).center(width - 2, "-") + "|")

for i in range(1):
    print("|" * width)