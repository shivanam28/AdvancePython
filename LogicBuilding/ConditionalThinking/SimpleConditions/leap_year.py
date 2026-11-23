# Check if a given year is a leap year.

# It is divisible by 4, AND NOT divisible by 100.
# OR it is divisible by 400.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")  


# A leap year is a calendar year that has 366 days instead of the usual 365, with an extra day—February 29 (known as leap day)—added to keep our calendar aligned with Earth's orbit around the Sun.