# Q1 - Separate each digit of a number and print it on the new line

# digit = int(input("Enter a number: "))
# while digit > 0:
#     print(digit % 10)
#     digit //= 10            



# Q2 - Accept a number and print its reverse

# digit = int(input("Enter a number: "))
# reverse = 0

# while digit > 0:
#     remainder = digit % 10
#     reverse = (reverse * 10) + remainder
#     digit //= 10


# Q3 - Accept a number and check if it is a pallindromic number (If 
# number and its reverse are equal

# digit = int(input("Enter a number:"))
# org = digit
# rev = 0

# while digit > 0:
#     rem = digit % 10
#     rev = (rev *10) + rem
#     digit //=10

# if rev == org:
#     print("Pallindromic number")


# Q4 - Create a random number guessing game with python
# import random
# random = random.randint(1,100)
# guess = None

# while guess != random:
#     guess = int(input("Enter your guess between 1-100: "))

#     if guess < random:
#         print("Too Low! Try again.")
#     elif guess > random:
#         print("Too High! Try again.")
#     else:
#         print("Congratulations! You guessed the number.")