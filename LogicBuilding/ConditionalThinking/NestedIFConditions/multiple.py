# Check if one of two given numbers is a multiple of the other.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a == 0 and b == 0:
    print("Both numbers are zero.")
elif (b != 0 and a % b == 0) or (a != 0 and b % a == 0):
    print("One number is a multiple of the other.")
else:
    print("Neither number is a multiple of the other.")
