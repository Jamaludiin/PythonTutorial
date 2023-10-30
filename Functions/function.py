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


print(
    "\nKeyword argument in Python functions--------------------------------------------------------"
)


def fun_with_keyword_argument(fname, lname, age):
    print("The first name is: ", fname)
    print("The last name is: ", lname)
    print("The age is: ", age)


fun_with_keyword_argument(
    fname="Leyla",
    age=56,
    lname="Key",
)


print("\n some of the value in the variable can be list---------------------")
# some of the value in the variable can be list
fun_with_keyword_argument(fname=["Leyla", "Omar"], age=99, lname={"Laki", 55, "true"})
print(
    "\nFunction with default parameter--------------------------------------------------------"
)


def fun_with_default_parameter(animal="Lion"):
    print("the name of the animal is :", animal)


fun_with_default_parameter("Tiger")
fun_with_default_parameter("Goat")
fun_with_default_parameter()
fun_with_default_parameter("Cow")


print(
    "\nPassing a List as an Argument in Python functions--------------------------------------------------------"
)


def fun_with_list_argument(names):
    print("The first name is : ", names[0], "\n")
    for i in names:
        print(i + " ")


names_1 = ["Ali", "Key", "Kali", "Shik"]
fun_with_list_argument(names_1)


print(
    "\nReturn Values practice--------------------------------------------------------"
)


def fun_with_return():
    a = 10
    b = 20
    c = a + b
    return c


resut = fun_with_return()
print(resut)
