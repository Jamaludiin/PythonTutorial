# Create class using the class keyword:


class myFirtsClass:
    print("Hello Class")


class mySecondClass:
    a = 10
    b = 20


# Create Object variable
obj = mySecondClass()
print(obj.a, " ", obj.b)


# Using init function
class Person:
  def __init__(self, fname, lname, age):
    self.fname = fname
    self.lname = lname
    self.age = age

p1 = Person("Alice", "Mike", 36)

print(p1.fname, p1.lname, p1.age)


# --------------------------------------------------------------------------------------
# Class with return value
class myReturnClass:
   def __init__(self, name, age, phone):
      self.name = name 
      self.age = age
      self.phone = phone
      self.result = self.funcReturnInfor()

   def funcReturnInfor(self):
         if self.age > 18:
            return "You are Mature Person"
         elif self.age < 18:
            print("Thank you")
            return "You are Not Mature Person"

print("\n")
# Example usage
result = myReturnClass("Nuh", 26, 683342782)
print(f"{result.name} {result.age} {result.phone} = {result.result}")

print("\n")
# Example usage
result = myReturnClass("Nuh", 17, 683342782)
print(f"{result.name} {result.age} {result.phone} = {result.result}")