# Take two numbers and determine whether both are even, both are odd, or one is even and one is odd.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a%2 == 0 and b%2 == 0:
    print("Both numbers are even.")
elif a%2 != 0 and b%2 != 0:
    print("Both numbers are odd.")
else:
    print("One number is even and the other is odd.")