# 9. Take two angles of a triangle and compute the third angle.

a1 = int(input("Enter Angle one: "))
a2 = int(input("Enter Angle two: "))

a3 = 180 - (a1+a2)

print(f"Third Angle is {a3}")