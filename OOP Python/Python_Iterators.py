# normally tuple, sets, lists and disctionaries are all iteratable also string are iteratable 
# example 

var_tupel = ("Java", "Python", "C sharp")
var_iter = iter(var_tupel)

print(next(var_iter))
print(next(var_iter))
print(next(var_iter))

print("\n")
# string iterables 
var_str = "Musics"
var_it = iter(var_str)

print(next(var_it))
print(next(var_it))
print(next(var_it))
print(next(var_it))
print(next(var_it))
print(next(var_it))

print("\n")

# Iterator looping
var_tupel_1 = ("Java", "Python", "C sharp", "HTML")

for i in var_tupel_1:
  print(i)

# Itorating string through loop
var_str_1 = "Language"

for i in var_str_1:
  print(i)

# Create an object/class as an iterator
# use the methods __iter__() and __next__() to your object.
print("\nDeclared iterator in class")

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# IELTS Marking scheme
class marks:
    def __iter__(self): 
        self.score = 11
        return self
  
    def __next__(self):
        if self.score in range (9,13):
            outcome = self.score 
            self.score += 1
            return outcome 
            # return 4
        elif self.score in range (13,16):
            outcome = self.score 
            self.score += 0.2
            return outcome 
            # return 4.5
        elif self.score in range (16,20):
            outcome = self.score 
            self.score += 0.3
            return outcome
            # return 5
        elif self.score in range (20,23):
            outcome = self.score 
            self.score += 0.4
            return outcome 
            # return 5.5
        elif self.score in range (23,27):
            outcome = self.score 
            self.score += 0.5
            return outcome 
            #return 6
        elif self.score in range (27,30):
            outcome = self.score 
            self.score += 0.6
            return outcome
            #return 6.5
        elif self.score in range (30,33):
            outcome = self.score 
            self.score += 0.7
            return outcome 
            #return 7
        elif self.score in range (33,35):
            outcome = self.score 
            self.score += 0.8
            return outcome 
            #return 7.5
        elif self.score in range (35,37):
            outcome = self.score 
            self.score += 0.9
            return outcome 
            #return 8
        elif self.score in range (37,39):
            outcome = self.score 
            self.score += 0.10
            return outcome 
            #return 8.5
        elif self.score in range (39,41):
            outcome = self.score 
            self.score += 0.11
            return outcome 
            #return 9
        else:
            return "Unknown Results"

print("\nSome Ielts marks DUMP")    
marks_obj = marks()
myiter = iter(marks_obj)
print("Before increment happen ", next(myiter))
print("After increment happen ",next(myiter))

