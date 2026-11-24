# Take a month number (1–12) and print the number of days in that month (ignore leap years).

month_num = int(input("Enter a number(1-12) to represent a month of the year: "))

if month_num == 2:
    print("February has 28 days, ignoring leap years.")
elif month_num in [4, 6, 9, 11]:
    print("The month has 30 days.")
elif month_num in [1, 3, 5, 7, 8, 10, 12]:
    print("The month has 31 days.")
else:
    print("Invalid input. Please enter a number between 1 and 12.") 
