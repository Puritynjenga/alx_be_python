
import csv
import os
class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""
    all = []
    def __init__(self, type:str, number:float):
        self.type = type
        self.number = number
    @classmethod
    def instantiate_from_csv(cls):
        with open('numbers.csv', 'r') as f:
            reader = csv.DictReader(f)
            numbers = list(reader)
        for n in numbers:
            SimpleCalculator(
                 type=n.get('type'),
            number=n.get('number')
            )
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def add(self, a=None, b=None):
        """Return the addition of a and b, or self.a and self.b if not provided."""
        if a is None:
            a = self.a
        if b is None:
            b = self.b
        return a + b
    def subtract(self, a=None, b=None):
        """Return the subtraction of b from a, or self.a and self.b if not provided."""
        if a is None:
            a = self.a
        if b is None:
            b = self.b
        return a - b
    def multiply(self, a=None, b=None):
        """Return the multiplication of a and b, or self.a and self.b if not provided."""
        if a is None:
            a = self.a
        if b is None:
            b = self.b
        return a * b
    def divide(self, a=None, b=None):
        """Return the division of a by b, or self.a and self.b if not provided. Returns None if b is zero."""
        if a is None:
            a = self.a
        if b is None:
            b = self.b
        if b == 0:
            return ZeroDivisionError
        return a / b
SimpleCalculator.instantiate_from_csv()
print(os.getcwd())    