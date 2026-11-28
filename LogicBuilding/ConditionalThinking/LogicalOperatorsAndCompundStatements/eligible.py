# 5. Take income and age, and check if eligible for tax (age > 18 and income > 5 L).

age = int(input("Enter your age: "))
income = int(input("Enter your income: "))

if age > 18 and income > 500000:
    print("You're eligible for tax!")
else:
    print("You're not eligible for tax!")