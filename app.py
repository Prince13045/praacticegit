def addition(a, b):
    return a + b

def subtraction(a, b, c):
    return a - b -c

def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
