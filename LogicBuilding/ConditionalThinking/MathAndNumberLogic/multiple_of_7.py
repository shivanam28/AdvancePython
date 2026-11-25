# Check if a number is a multiple of 7 and ends with 7.

a = int(input("Enter a number: "))

if a % 7 == 0 and a % 10 == 7:
    print(f"{a} is a multiple of 7 and ends with 7.")
else:
    print(f"{a} is not a multiple of 7 and does not end with 7.")
