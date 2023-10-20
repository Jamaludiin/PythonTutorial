print("Example 0-------------------------------------------------------")
# How to Display a Value of a Variable in Python
a = 20
b = 8

print("This is a text display")  # display only text
print(a)  # display only one variable
print(a, b)  # display multiple variables
print("The value of a is:", a, "The value of b is:", b)  # display only text

print("Example 1-------------------------------------------------------")

distance = 25  # declare variable and assign int value
print(distance)  # print the value in the variable

distance = 5.30  # reassign float value to declared variable
print(distance)  # print the value in the variable

print("Example 2-------------------------------------------------------")

"""
type casting
"""

name = str("Gilbert")  # defined as str
age = int(25)  # defined as int
slary = float(35.60)  # defined as float
is_maried = bool(True)  # defined as bool"""

print("Example 3-------------------------------------------------------")

"""
CHECK THE TYPE OF VARIABLE
"""
name = "Gilbert"
age = 25
salary = 35.60
is_maried = True

print(type(name))  # checks the type of name
print(type(age))  # checks the type of age
print(type(salary))  # checks the type of salary
print(type(is_maried))  # checks the type of is_maried

print("Example 4-------------------------------------------------------")

a = 30  # global scope variable

# declare a function


def my_fun():
    b = 20  # local scope variable
    print(b)
    print(a)


# call the function
my_fun()
print(a)

# this trigers an error becouse it is local scope variable
# print(b)

# How to use the global keyword in Python
a = 55  # global scope variable

# declare a function


def my_fun():
    global b  # global scope variable
    b = 30


# call the function
my_fun()
print(a)
print(b)

print("Example 5-------------------------------------------------------")

# How to declare and assign value to global variable in one line


def my_fun():
    global b
    b = 30  # global scope variable


# call the function
my_fun()
print(b)

print("Example 6-------------------------------------------------------")

"""naming conventions"""

# Snake Case
student_first_name = "Abraham"
student_second_name = "Lincoln"
student_age = 26
student_cgpa = 3.5

# print their values
print(student_first_name, student_second_name)
print(student_age)
print(student_cgpa)

print("Example 7-------------------------------------------------------")

# Camel Case
studentFirstName = "Susan"
studentSecondName = "Connor"
studentAge = 22
studentCgpa = 4.0

# print their values
print(studentFirstName, studentSecondName)
print(studentAge)
print(studentCgpa)

print("Example 8-------------------------------------------------------")

# Pascal Case
StudentFirstName = "Ali"
StudentSecondName = "Sharif"
StudentAge = 25
StudentCgpa = 3.8

# print their values
print(StudentFirstName, StudentSecondName)
print(StudentAge)
print(StudentCgpa)

print("Example 9-------------------------------------------------------")

# How to Assign Multiple Variables to Multiple Values in Python
first_level, second_level, third_level = "Beginner", "Intermediate", "Advanced"

# print the three levels of programming skills
print(first_level)
print(second_level)
print(third_level)

print("Example 10-------------------------------------------------------")

# How to Assign Multiple Variables to Multiple Values in Python
# the following line can produce eror
# student_name, student_age, student_cgpa, student_status = "Khan", 12, 4.1
student_name, student_age, student_cgpa, student_status = "Khan", 12, 4.1, "Active"

# print the three levels of programming skills
print(student_name)
print(student_age)
print(student_cgpa)

print("Example 11-------------------------------------------------------")

# How to Assign Multiple Variables to Single Value in Python
num_one = num_two = num_three = 5

# print their values
print(num_one)
print(num_two)
print(num_three)
