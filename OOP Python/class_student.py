# class for student
class Student:
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade


# another class for courses
class Course:
    def __init__(self, name, max_students):
        self.name = name 
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)



# objects for Student class
obj_s1 = Student("Nuh",20,89)
obj_s2 = Student("Ley",22,88)
obj_s3 = Student("Yuh",19,76)

    
# objects for Course class
course = Course("Math", 2)
course.add_student(obj_s1)
course.add_student(obj_s2)
course.add_student(obj_s3)# it will not be added

# print student list property in the course class
print(course.students[0].name)

print(course.get_average_grade())    



# ANOTHER ONE EXAMPLES
# IELTS Marking scheme
class marks:
  def __init__(self, score):# score ranges 0-40
     self.score = score
     print("\nIELTS Score of ", self.score, "is:")


  """def __iter__(self,score): 
    self.score = score
    return score"""
  
  def outcome(self):
    if self.score in range (9,13): # range is 9 to 12, 13 is not inclusive 
       return 4
    elif self.score in range (13,16):
      return 4.5
    elif self.score in range (16,20):
      return 5
    elif self.score in range (20,23):
      return 5.5
    elif self.score in range (23,27):
      return 6
    elif self.score in range (27,30):
      return 6.5
    elif self.score in range (30,33):
      return 7
    elif self.score in range (33,35):
      return 7.5
    elif self.score in range (35,37):
      return 8
    elif self.score in range (37,39):
      return 8.5
    elif self.score in range (39,41):
      return 9
    else:
      return "Unknown Results"
    
marks_obj = marks(12) # why
print(marks_obj.outcome())
marks_obj = marks(37)
print(marks_obj.outcome())
marks_obj = marks(3)
print(marks_obj.outcome())