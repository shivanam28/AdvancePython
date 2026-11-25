# Take a 4-digit number and check if the first and last digits are equal.

a = int(input("Enter a 4-digit number: "))

if 1000 <= a <= 9999:
    first_digit = a//1000
    last_digit = a%10

    if first_digit == last_digit:
        print("The first and last digits are the same.")
    else:
        print("The first and last digits are not the same.")