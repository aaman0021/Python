X = float(input("Enter the First Number: "))
Y = float(input("Enter the Second Number: "))
Operation = input("Choose an Operator, (+, -, *, /): ")

if Operation == "+":
    print(f"Sum:", X + Y)

elif Operation == "-":
    print(f"Difference:", X - Y)

elif Operation == "*":
    print(f"Product:", X * Y)

elif Operation == "/":
    print(f"Quotient:", X / Y)

else:
    print("Invalid Operation")