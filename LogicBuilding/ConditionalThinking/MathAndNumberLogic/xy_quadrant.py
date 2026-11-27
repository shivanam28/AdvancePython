# 6. Take coordinates (x, y) and determine which quadrant the point lies in.

x = int(input("Enter x cordinate: "))
y = int(input("Enter y cordinate: "))

if (x==0 and y==0):
    print(f"{x},{y} coordnates lies on the origin.")
elif(x>0 and y>0):
    print(f"{x},{y} coordnates lies in 1st Quadrant.")
elif(x<0 and y>0):
    print(f"{x},{y} coordnates lies in 2nd Quadrant.")
elif(x<0 and y<0):
    print(f"{x},{y} coordnates lies in 3rd Quadrant.")
elif(x>0 and y<0):
    print(f"{x},{y} coordnates lies in 4th Quadrant.")
elif y == 0:
    print("X-axis")
else:
    print("Y-axis") 