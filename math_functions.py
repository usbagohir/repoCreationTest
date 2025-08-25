def add(int1=None, int2=None):
    try:
        int1 = float(int1)
        int2 = float(int2)
        return int1 + int2
    except(ValueError, TypeError):
        return "Numerical value not found"

def sub(int1: float, int2: float):
    return int1 - int2

def mul(int1: float, int2: float):
    return int1 * int2

def div(int1: float, int2: float):
    if int2 == 0:
        raise ZeroDivisionError("Division by zero")
    return int1 / int2