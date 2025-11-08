def is_balanced(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

# Test
expr1 = "(a + b) * (c + d)"
expr2 = "((a + b) * (c + d)"
print(expr1, "->", is_balanced(expr1))
print(expr2, "->", is_balanced(expr2))

