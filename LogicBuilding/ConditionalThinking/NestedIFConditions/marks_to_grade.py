# Take marks (0–100) and print the corresponding grade (A/B/C/D/F).

marks = int(input("Enter the marks obtained: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else: 
    print("Grade: D")