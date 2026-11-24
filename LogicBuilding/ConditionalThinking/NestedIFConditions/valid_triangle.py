# Take three sides and check if they form a valid triangle.

a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))

if a + b > c and a + c > b and b + c > a:
    print("The given lengths can form a valid triangle.")
else:   
    print("The given lengths cannot form a valid triangle.")

