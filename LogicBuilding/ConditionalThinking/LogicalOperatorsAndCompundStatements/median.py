# 3. Take three numbers and print the median value (neither maximum nor minimum).

a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))

if a1 <= a2 <= a3 and a3 <= a2 <= a1:
    print(f"{a2} is median!")
elif a2 <= a1 <= a3 and a3 <= a1 <= a2:
    print(f"{a1} is median!")
else:
    print(f"{a3} is median!")

