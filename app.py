def add(a, b):
    return a + b

def multipy(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by ZERO")
    return a / b