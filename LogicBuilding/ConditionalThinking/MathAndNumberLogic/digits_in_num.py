# Check whether a given integer is single-digit, double-digit, or multi-digit.

a = int(input("Enter a number: "))

if a // 10 == 0:
    print("The number has 1 digit.")
elif a // 100 == 0:
    print("The number has 2 digits.")
else:
    print("The number has multi digits.")