# Before starting we need to understand some of the 
# terminology.- Mutability refers to whether an object's value 
# can be changed after creation. And List allows this- we know data structures are used to store 
# multiple values so duplicates means same value occuring 
# multiple time. List allows this- List maintains ordered data structure maintains 
# the sequence of elements as they were inserted. This 
# means you can access elements using their position 
# (index)- List have heterogenous nature that means 
# we can have multiple data types inside the list

# Q1 - Print positive and negative elements of an List

# values = list(map(int, input("Enter the list elements separated by space: ").split()))

# print("Positive elements:")
# for x in values:
#     if x > 0:
#         print(x, end=" ")
# print()
# print("Negative elements:")
# for x in values:
#     if x < 0:
#         print(x, end=" ")
# print()

# Q2 - Mean of List elements

# values = list(map(int, input("Enter values: ")).split())

# mean = sum(values) / len(values)
# print("Mean:", mean)    



# Q3 - Find the greatest element and print its index too

# values = list(map(int, input("Enter values: ").split()))

# max_value = max(values)
# max_index = values.index(max_value)
# print("Greatest element:", max_value)
# print("Index of greatest element:", max_index)



# Q4 - Find the second greatest element

# values = list(map(int, input("Enter values: ").split()))

# unique_values = list(set(values))
# unique_values.sort(reverse=True)
# if len(unique_values) >= 2:
#     print("Second greatest element:", unique_values[1])
# else:
#     print("Not enough unique elements") 


# Q5 - Check if List is sorted or not

# values = list(map(int, input("Enter values: ").split()))

# is_sorted = all(values[i] <= values[i + 1] for i in range(len(values) - 1))
# if is_sorted:
#     print("The list is sorted.")
# else:
#     print("The list is not sorted.")