class Stack:
    def __init__(self):
        self.items = []  # empty array

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# instance
stack = Stack()  # object initialization

stack.push(2)
stack.push(4)
stack.push(9)

print(stack.peek())  # 9
# stack.pop()
# stack.pop()
# stack.pop()

for item in stack.items:
    print(item)
