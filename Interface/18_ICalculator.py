#importing the abstractmethod from abc module
from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self, a, b):
        pass
    
    @abstractmethod
    def subtract(self, a, b):
        pass
    
    @abstractmethod
    def multiply(self, a, b):
        pass
    
    @abstractmethod
    def divide(self, a, b):
        pass

class BasicCalculator(ICalculator):
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

calc = BasicCalculator()

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(f"Addition: {calc.add(a, b)}")
print(f"Subtraction: {calc.subtract(a, b)}")
print(f"Multiplication: {calc.multiply(a, b)}")
print(f"Division: {calc.divide(a, b)}")
