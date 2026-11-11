def average_marks(args):
    total_marks = sum(args)
    total = len(args)
    print(total_marks/total)

def product_details(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

def student_details(name, age, **kwargs):
    print(f'Name: {name}')
    print(f'Age: {age}')
    for key, value in kwargs.items():
        print(f'{key}: {value}')

def student_hobbies(name, *hobbies):
    print(f"{name}'s hobbies:")
    for hobby in hobbies:
        print(f" - {hobby}")

average_marks((90, 80, 70, 60, 50))
product_details(name="Laptop", price=1000, brand="Dell")
student_details(name="Alice", age=20, grade="A", major="Computer Science")
student_hobbies("Alice", "Reading", "Swimming", "Coding")