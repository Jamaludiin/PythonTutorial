class transportSystem:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Transport System!")

class Car(transportSystem):
  def move(self):
    print("Drive!")

class Boat(transportSystem):
  def move(self):
    print("Sail!")

class Plane(transportSystem):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

# all classes use the same method during call, but when it goes back it behaves diffrently
for x in (car1, boat1, plane1):
  x.move()