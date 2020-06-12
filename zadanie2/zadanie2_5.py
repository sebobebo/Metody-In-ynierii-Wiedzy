from math import sqrt


class Calculator:
    def add(self, a, b):
        return a + b

    def difference(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


class ScienceCalculator(Calculator):
    def pow(self, a, b):
        return a^b

    def sqrt(self, a):
        return sqrt(a)
