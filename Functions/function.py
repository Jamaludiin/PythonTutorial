# Declaring a Python Function


def my_function():
    print("This is a function")


# Calling a function
my_function()


# Function with Arguments
def fun_with_argument(name):
    print("My name is :", name)


# Calling the function
fun_with_argument("Michael")
# The problem is it can take anything you pass no matter which datatype is
fun_with_argument(78)


# Function with more than one argument
def fun_with_more_argument(fname, lname, age):
    print("My First Name: ", fname, "Lat Name: ", lname, "My Age: ", age)


# Call the function
fun_with_more_argument("Ali", "Kruskul", 67)
