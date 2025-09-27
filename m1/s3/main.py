from string import printable
from types import LambdaType


print("1. Define a function and call the functions")


def greet():
    print("Hello, James!")


greet()
print("------------------------------")

print("2. Create a function with Parameters and Arguments")


def add_numbers(a: int, b: int):
    return a + b


result = add_numbers(3, 5)
print(f"The result of the calculation is {result}")  # 8
print("------------------------------")


print("3. Create a function with Default Arguments")


def greet_with_default(name: str = "Guest"):
    print(f"Hello, {name}!")


greet_with_default()  # Hello, Guest!
greet_with_default("Bob")  # Hello, Bob!

print("------------------------------")


print("4. Create a function to return a values")


def return_value():
    return "Hello, World!"


print(return_value())  # Hello, World!
print("------------------------------")


print("5. Variable scope")


def variable_scope():
    x: int = 10
    print(x)  # 10


variable_scope()  # 10
print("------------------------------")


print("6. Create a lambda function and call the lambda function.")
lambda_func: LambdaType = lambda x, y: x + y
print(lambda_func(3, 5))  # 8

print("------------------------------")


print("7. Create a function as First-Class Objects")


# Ex: 1
def first_class_function(func):
    return func(2, 3)


print(first_class_function(lambda x, y: x * y))  # 6


# Ex: 2
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def speak(func, msg):
    print(func(msg))


speak(shout, "hello")  # HELLO
speak(whisper, "HELLO")  # hello
