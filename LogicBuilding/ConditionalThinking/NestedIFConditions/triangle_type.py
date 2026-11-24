# If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene.

a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))

# equilateral triangle: all sides are equal
if a == b and b == c:
    print("The triangle is equilateral.")

# isosceles triangle: two sides are equal
elif a == b or b == c or a == c:
    print("The triangle is isosceles.")

# scalene triangle: all sides are different
else:
    print("The triangle is scalene.")
