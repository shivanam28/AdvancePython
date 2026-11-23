char = input("Enter a character: ")

if char.isalpha():
    if char.isupper():
        print("The character is an uppercase letter.")
    else:
        print("The character is a lowercase letter.")
elif char.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")

