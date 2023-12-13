
class myCalculator:
   def __init__(self, operand1, operator, operand2):
      self.operand1 = operand1
      self.operand2 = operand2
      self.operator = operator
      self.result = self.calculate()
   
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
result = myCalculator(10, "+", 20)
print(f"{result.operand1} {result.operator} {result.operand2} = {result.result}")

result = myCalculator(10, "-", 20)
print(f"{result.operand1} {result.operator} {result.operand2} = {result.result}")

result = myCalculator(10, "*", 20)
print(f"{result.operand1} {result.operator} {result.operand2} = {result.result}")

result = myCalculator(10, "/", 20)
print(f"{result.operand1} {result.operator} {result.operand2} = {result.result}")