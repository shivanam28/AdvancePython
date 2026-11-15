# Create a decorator that prints a welcome message before a function runs.
# from functools import wraps
# def my_decorator(func):
#     @wraps(func)
#     def wrapper():
#         print(f"Calling >>> {func.__name__}()")
#         func()
#         print(f"Finished >>> {func.__name__}()")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()



# Create a decorator that measures how long a function takes.
# import time
# def calculate_time(func):
#     def wrapper(*args):
#         st = time.time()
#         result = func(*args)
#         et = time.time()
#         print(f"Execution time: {et-st} seconds")
#         return result
#     return wrapper

# @calculate_time
# def add(*args):
#     return sum(args)

# print(add(1,2,3,4,5))


# Create a decorator that checks whether a user is logged in before showing a dashboard.
# def check_login(func):
#     def wrapper():
#         if loggedin():
#             print("User is logged in.")
#             return func()
#         else:
#             print("User is not logged in.")
#     return wrapper



# def loggedin():
#     return True # Simulate a login check

# @check_login
# def show_dashboard():
#     print("Welcome to the dashboard!")

# show_dashboard()
