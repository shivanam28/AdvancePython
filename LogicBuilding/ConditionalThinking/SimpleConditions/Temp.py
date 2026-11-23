temp = int(input("Enter temperature in Celsius: "))

if temp < 15:
    print("It's a Cold day.")
elif temp > 15 and temp < 40:
    print("It's a Warm day.")
else:
    print("It's a Hot day.")