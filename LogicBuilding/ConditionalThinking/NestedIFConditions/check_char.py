# Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’.

char = input("Enter a character: ")

if char < 'a' or char > 'm':
    print(f"{char} is inside a and m range.")
elif char < 'n' or char > 'z':
    print(f"{char} is inside n and z range.")
else:
    print(f"{char} is not in any of the specified ranges.")