import math
from typing import List

class Calculator:
    def __init__(self, precision=2):
        self.precision = precision

    def add(self, a, b):
        return round(a + b, self.precision)

    def subtract(self, a, b):
        return round(a - b, self.precision)

    def multiply(self, a, b):
        return round(a * b, self.precision)

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return round(a / b, self.precision)


def calculate_mean(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)


def calculate_std(numbers: List[float]) -> float:
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)
