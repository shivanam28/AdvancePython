# Q1 - Accept an integer and Print hello world n times

# hello_num = int(input("Enter num: "))
# for i in range(hello_num):
#     print("Hello World")
    

# Q2 -Print natural number up to n

# n = int(input("Enter n: "))
# for i in range(1, n):
#     print(i+1)


# Q3 - Reverse for loop. Print n to 1

# n = int(input("Enter n: "))
# for i in range(n, 0, -1):
#     print(i)



# Q4 - Take a number as input and print its table

# n = int(input("Enter n: "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n*i}")


# Q5 - Sum up to n terms

# n = int(input("Enter n: "))
# sum = 0
# for i in range (1, n+1):
#     sum+=i
# print("Sum: ", sum)


# Q6 - Factorial of a number

# n = int(input("Enter n: "))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print("Factorial: ", factorial)

# Q7 - Print the sum of all even & odd numbers in a range 

# n = int(input("Enter n: "))
# even_sum = 0
# odd_sum = 0

# for i in range(1, n+1):
#     if(i%2 ==0):
#         even_sum += i
#     else:
#         odd_sum += i

# print("Even Sum: ", even_sum)
# print("Odd Sum: ", odd_sum)



# Q8 - Print all the factors of a number

# n = int(input("Enter n: "))

# for i in range(1, n+1):
#     if(n%i ==0):
#         print(i)


# Q9 - Accept a number and check if it a perfect number or not. 
# A number whose sum of factors is equal to the number itself 
# Ex -  6 = 1, 2, 3 = 

# n = int(input("Enter n: "))
# factor_sum = 0
# for i in range(1, n):
#     if(n%i == 0):
#         factor_sum += i
# print("Sum of factors: ", factor_sum)
# if factor_sum == n:
#     print(f"{n} is a perfect number")



# Q10 - Check whether the number is prime or not

# n = int(input("Enter n: "))

# is_prime = True
# for i in range(2, n):
#     if(n%i == 0):           
#         is_prime = False
#         break
# print(f"{n} is prime: {is_prime}")


# Q11 - Reverse a string without using in build functions.

# a = input("Enter string: ")

# for char in range(len(a)-1, -1, -1):
#     print(a[char], end="")



# Q12 - Check string is Pallindrome or not

# a = input("Enter string: ")
# is_pallindrome = True

# for i in range(len(a)//2):
#     if(a[i] != a[len(a)-1-i]):
#         is_pallindrome = False
#         break

# print(f"Is palindrome: {is_pallindrome}")



# Q13 - Count all letters, digits, and special symbols from a given 
# string 
# Given: str1 = "P@#yn26at^&i5ve" 
# Expected Outcome: 
# Total counts of chars, digits, and symbols 
# Chars = 8 
# Digits = 3 
# Symbol = 4

# str1 = "P@#yn26at^&i5ve" 
# char_count = 0
# digit_count = 0
# symbol_count = 0

# for i in str1:
#     if i.isalpha():
#         char_count += 1
#     elif i.isdigit():
#         digit_count += 1
#     else:
#         symbol_count += 1

# print(f"Chars = {char_count}")  
# print(f"Digits = {digit_count}")  
# print(f"Symbol = {symbol_count}")
