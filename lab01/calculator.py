"""
A module for handling calculator operations
"""


class Calculator:
    """
    A simple calculator class that supports the four basic arithmetic
    operations.

    The calculator has four public methods: add, subtract, multiply, and
    divide. Each method takes two arguments and returns the result of the
    corresponding operation.
    """
    def add(self, a, b):
        """
        Return the sum of _a and b.

        :param a: The first operand.
        :param b: The second operand.
        :return: The sum of the two operands.
        """
        return a + b

    def subtract(self, a, b):

        """Return the difference of a _and b"""
        return a - b

    def multiply(self, a, b):
        """Return the product of _a _and b"""
        return a * b

    def divide(self, a, b):
        """Return the quotient of _a _and b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
