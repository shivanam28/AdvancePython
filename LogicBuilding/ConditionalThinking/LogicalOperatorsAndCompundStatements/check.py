# 1. Take a character and check if it is a letter, a digit, or neither.

char = input("Enter a value: ")

if char.isalpha():
    print("Entered value is a letter.")
elif char.isdigit():
    print("Entered value is a digit")
else:
    print("It's neither digit nor a letter.")