class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both arguments must be numbers")
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both arguments must be numbers")
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both arguments must be numbers")
        self.result = a * b
        return self.result

    def divide(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both arguments must be numbers")
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        self.result = a / b
        return self.result

    def power(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both arguments must be numbers")
        self.result = a**b
        return self.result
