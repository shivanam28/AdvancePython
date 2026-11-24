# Check voting eligibility for a given age (18+).

age = int(input("Enter your age: "))

if age < 18 and age > 0:
    print("You are not eligible to vote.")
elif age >= 18 and age <= 100:
    print("You are eligible to vote.")
else:   
    print("Invalid age entered. Please enter a valid age between 1 and 100.")