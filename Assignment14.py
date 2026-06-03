from addition import add
from subtract import subtract
# from multiplication import multiply
# from division import divide
# from power import power
# from modulus import modulus
# from floor import floor_divide

print("Calculator Operations")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Modulus")
print("7. Floor Division")

choice = int(input("Enter your choice: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print("Result:", add(a, b))

elif choice == 2:
    print("Result:", subtract(a, b))

# elif choice == 3:
#     print("Result:", multiply(a, b))

# elif choice == 4:
#     print("Result:", divide(a, b))

# elif choice == 5:
#     print("Result:", power(a, b))

# elif choice == 6:
#     print("Result:", modulus(a, b))

# elif choice == 7:
#     print("Result:", floor_divide(a, b))

else:
    print("Invalid Choice")