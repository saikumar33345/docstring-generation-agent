"""This module provides a Calculator class and functions for statistical calculations."""

import math
from typing import List

class Calculator:
    """A simple calculator class for basic arithmetic operations."""
    def __init__(self, precision=2):
        """Initializes the Calculator with a specified precision.

        Args:
            precision: The number of decimal places for results.
        """
        self.precision = precision

    def add(self, a, b):
        """Adds two numbers and returns the rounded sum.

        Args:
            a: The first number.
            b: The second number.

        Returns:
            The sum of a and b, rounded to the calculator's precision.
        """
        return round(a + b, self.precision)

    def subtract(self, a, b):
        """Subtracts the second number from the first and returns the rounded result.

        Args:
            a: The first number.
            b: The second number.

        Returns:
            The difference between a and b, rounded to the calculator's precision.
        """
        return round(a - b, self.precision)

    def multiply(self, a, b):
        """Multiplies two numbers and returns the rounded product.

        Args:
            a: The first number.
            b: The second number.

        Returns:
            The product of a and b, rounded to the calculator's precision.
        """
        return round(a * b, self.precision)

    def divide(self, a, b):
        """Divides the first number by the second and returns the rounded quotient.

        Args:
            a: The numerator.
            b: The denominator.

        Returns:
            The quotient of a divided by b, rounded to the calculator's precision.

        Raises:
            ValueError: If the denominator is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return round(a / b, self.precision)


def calculate_mean(numbers: List[float]) -> float:
    """Calculates the arithmetic mean of a list of numbers.

    Args:
        numbers: A list of floating-point numbers.

    Returns:
        The mean of the numbers.
    """
    return sum(numbers) / len(numbers)


def calculate_std(numbers: List[float]) -> float:
    """Calculates the standard deviation of a list of numbers.

    Args:
        numbers: A list of floating-point numbers.

    Returns:
        The standard deviation of the numbers.
    """
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)