# Dictionary Powers (Mutable, Unique Keys, Ordered, Heterogeneous)

# Before starting we need to understand some of the 
# terminology.- Dictionaries are mutable, meaning you can 
# change, add, or remove key-value pairs after creation- Keys must be unique, but you can have 
# duplicates in values- Dictionary follows insertion order– A dictionary can store different types of 
# keys and values, like integers, strings, lists, or even 
# another dictionary

# Student = {
#     "Name": "John Doe",
#     "Age": 20,
#     "Grade": "A"
# }



# Q1 - Write a Python script to merge two Python dictionaries

# fruits = {
#     'apple' : 2,
#     'banana' : 3
# }

# vegetables = {
#     'carrot' : 5,
#     'broccoli' : 4
# }

# cart = fruits | vegetables # Merging two dictionaries using the union operator
# cart = {**fruits, **vegetables} # Merging two dictionaries using dictionary unpacking
# fruits.update(vegetables) # Merging two dictionaries using the update() method  

# for i in cart:
#     print(i, ":", cart[i])



# Q2 - Write a Python program to sum all the values in a dictionary

# dict_values = {
#     'a' : 10,
#     'b' : 20
# }


# sum = 0
# for i in dict_values:
#     sum += dict_values[i]

# print("Sum:", sum)


# using built in function
# sum = sum(dict_values.values())


# another example 
# prices = {'apple': 2.5, 'banana': 1.2, 'orange': 3.0}

# expensive_total = sum(price for price in prices.values() if price > 2.0)
# print(expensive_total)

# Q3 - Count the frequency of each element

# fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# freq = {}
# for fruit in fruits:
#     freq[fruit] = freq.get(fruit, 0) + 1
# print(freq)


# Q4 - Write a Python program to combine two dictionary by adding 
# values for common keys

# dict1 = {'a': 100, 'b': 200, 'c':300}
# dict2 = {'a': 300, 'b': 200, 'd':400}     

# combined_dict = {}
# for key in set(dict1) | set(dict2):       #If dict1 = {'a': 1, 'b': 2} then set(dict1) becomes {'a', 'b'}.
#     combined_dict[key] = dict1.get(key, 0) + dict2.get(key, 0)

# print(combined_dict)