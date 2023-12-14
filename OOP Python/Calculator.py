
class myCalculator:
   def __init__(self, operand1, operator, operand2):
      self.operand1 = operand1
      self.operand2 = operand2
      self.operator = operator
      self.result = self.calculate()
   
   """the __init__ method directly without using an additional function. However, the __init__ method in a class 
   is not meant to return values like a regular function. Instead, you can create a separate method for performing 
   the calculations. """
   def calculate(self):
        if self.operator == "+":
            return self.operand1 + self.operand2
        elif self.operator == "-":
            return self.operand1 - self.operand2
        elif self.operator == "*":
            return self.operand1 * self.operand2
        elif self.operator == "/":
            if self.operand2 != 0:  # Check for division by zero
                return self.operand1 / self.operand2
            else:
                return "Error: Division by zero"

# Example usage
result = myCalculator(20, "+", 5)
print(f"{result.operand1} {result.operator} {result.operand2} = {result.result}")

result = myCalculator(20, "-", 10)
print(f"{result.operand1} {result.operator} {result.operand2} = {result.result}")

result = myCalculator(5, "*", 5)
print(f"{result.operand1} {result.operator} {result.operand2} = {result.result}")

result = myCalculator(30, "/", 3)
print(f"{result.operand1} {result.operator} {result.operand2} = {result.result}")


print("\n")
