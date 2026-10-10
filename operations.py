import math

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return None
    return a // b
def mod(a, b):
    if b == 0:
        return None
    return a % b
def sin_deg(x):
    return math.sin(math.radians(x))
def cos_deg(x):
    return math.cos(math.radians(x))
def power(a, b):
    return a ** b
def sqrt(x):
    if x < 0:
        return "Ошибка"
    return math.sqrt(x)
def floor_value(x):
    return math.floor(x)
def ceil_value(x):
    return math.ceil(x)
