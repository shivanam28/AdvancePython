#  Take a 3-digit number and check if all digits are distinct.

a = int(input("Enter a 3-digit number: "))

if 100 <= a <= 999:
    first_digit = a//100
    second_digit = (a//10) % 10
    third_digit = a % 10

    if first_digit != second_digit and first_digit != third_digit and second_digit != third_digit:
        print("All digits are distinct.")
    else:
        print("Digits are not distinct.")

else:
     print("Invalid input. Please enter a three-digit number.")