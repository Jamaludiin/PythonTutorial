# Declaring a Python Function

print(
    "Function without parameter--------------------------------------------------------"
)


def my_function():
    print("This is a function")


# Calling a function
my_function()

print(
    "\nFunction with one parameter--------------------------------------------------------"
)


# Function with Arguments
def fun_with_argument(name):
    print("My name is :", name)


# Calling the function
fun_with_argument("Michael")
# The problem is it can take anything you pass no matter which datatype is
fun_with_argument(78)

print(
    "\nFunction with more parameters--------------------------------------------------------"
)


# Function with more than one argument
def fun_with_more_argument(fname, lname, age):
    print("My First Name: ", fname, "Lat Name: ", lname, "My Age: ", age)


# Call the function
fun_with_more_argument("Ali", "Kruskul", 67)

print(
    "\nFunction with under specified arguments--------------------------------------------------------"
)


def fun_with_underspecied_argument(fname, lname):
    print(fname + " " + lname)


# my_function("Ali")
print(
    "this will print an erro if the Function has under specified arguments--------------------------------------------------------"
)

print(
    "\nIf you want to pass more argument in your Function just add * before the parameter name--------------------------------------------------------"
)


def fun_with_arbitery_argument(*names):
    print("The first argument is " + names[0])
    print("All the arguments list is: ")
    j = 0
    for i in names:
        print(j, "--------", i)
        j = j + 1


fun_with_arbitery_argument("Leli", "Tedros", "Kali", "45")