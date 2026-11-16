# https://github.com/shividoge/lab11-SA-NP
# Partner 1: Shivin Anand
# Partner 2: NP
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)


def hypotenuse(a, b):
    # squaring removes the sign, so negative side lengths still work
    return math.sqrt(a * a + b * b)


# First example
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def logarithm(a, b):
    # logarithm of b with base a
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Argument must be positive")
    return math.log(b, a)


def exponent(a, b):
    return a ** b
