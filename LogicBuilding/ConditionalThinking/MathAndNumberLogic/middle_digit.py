# Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither.

a = int(input("Enter a three-digit number: "))

if 100 <= a <= 999:
    first_digit = a//100
    second_digit = (a//10) % 10
    third_digit = a % 10

    if second_digit > third_digit and second_digit > first_digit:
        print("The middle digit is the largest digit.")
    elif second_digit < third_digit and second_digit < first_digit:
        print("The middle digit is the smallest digit.")
    else:
        print("The middle digit is neither the largest nor the smallest digit.")