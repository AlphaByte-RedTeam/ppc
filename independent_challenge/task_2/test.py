# a = "5"
# b = "10"
# print (type(int(a)))
# print (type(int(b)))


# def print(val: str):
#     return val


def s(a: int, b: int):
    return a + b


def d(a: int, b: int):
    return a - b


total1 = s(1, 2)  # returns a value back to the caller
total2 = d(3, 4)
print(total1, total2)
