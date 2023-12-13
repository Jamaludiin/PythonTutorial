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

print(p1.fname)
print(p1.lname)
print(p1.age)