# Polymorphism is an is often used in Class methods, where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():

"""The word "polymorphism" means "many forms", and in programming it refers 
to methods/functions/operators with the same name that can be executed on many objects or classes."""
# len() methods can be used in the list, tuple, set, dictionary, string etc

# Cars (Drive), Planes (Fly), Boats (Sail) all move, so they share this method or charecteristics, this example gives each class move method but diffrent task
print("\n")

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

# all classes use the same method during call, but when it goes back it behaves diffrently
for x in (car1, boat1, plane1):
  x.move()



# Inheritance Class Polymorphism
"""What about classes with child classes with the same name? Can we use polymorphism there?
-----Answer
Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, 
Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:"""
print("\n")

# Parent class
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle): # this is child class and it inherits the parent
  pass

class Boat(Vehicle): # this is child class and it inherits the parent
  def move(self): # it override the parent method
    print("Sail!")

class Plane(Vehicle): # this is child class and it inherits the parent
  def move(self): # it override the parent method
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()