# 1. Use `map()` to convert a list of temperatures from Celsius to Fahrenheit.
temp = [32,35,38]
fahrenheit = list(map(lambda c: c *9/5 + 32, temp))
print(fahrenheit)


# 2. Use `filter()` to select words longer than five characters.
fruits = ['apple', 'banana', 'cherry', 'date']
Long_fruits = list(filter(lambda fruit: len(fruit) > 5, fruits))
print(Long_fruits)

# 3. Use `zip()` to combine employee names and IDs into a dictionary.
emp_id = [101, 102, 103]
emp_name = ['Alice', 'Bob', 'Charlie']
emp_dict = dict(zip(emp_id, emp_name))
print(emp_dict)