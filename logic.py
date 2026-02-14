import math

def add(a,b):
    result = a+b
    return result

def subtract(a,b):
    result = a-b
    return result

def multiply(a,b):
    result = a*b
    return result

def divide(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        return None


