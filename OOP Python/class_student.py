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
