# 1. Create a lambda that converts Celsius to Fahrenheit.
celcius_to_fahrenheit = lambda c: (c * 9/5) + 32
print(celcius_to_fahrenheit(32))

# 2. Create a lambda that returns the larger of two numbers.
larger_number = lambda x,y: x if x>y else y
print(larger_number(10, 20))

# 3. Sort a list of words by their length using `key=lambda`.
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)