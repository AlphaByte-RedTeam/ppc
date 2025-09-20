# as is
# def main():
#     print("Hello from s1!")

# to be
def f(x: int):
    print(x*2)

# new function
def myAge(age: int): # int = integer -> for whole number
    print(age)

def myName(name: str): # str = string
    print(name)

# def greet(name, age):
#     print(f"Hello, my name is {myName(name)}, and my age is {myAge(age)}") # string interpolation
def greet(name: str, age: int):
    print(f"Hello, my name is {name}, and my age is {age}")


if __name__ == "__main__":
    # f(1)
    greet("James", 24)


# f(x: int) => x*2 (mathematical equation)
# f(9) = 18
