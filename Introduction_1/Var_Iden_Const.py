# 4.4  Variables, Identifiers and Constants
"""Like all programming languages, a variable is a named storage location. A variable has a name (or identifier) and holds a value.

Like most of the scripting interpreted languages (such as JavaScript/Perl), Python is dynamically typed. You do NOT need to declare 
a variable before using it. A variables is created via the initial assignment. (Unlike traditional general-purpose static typed languages 
like C/C++/Java/C#, where you need to declare the name and type of the variable before using the variable.)

For example"""

"""this tutorial is all about variables, identifiers and constants
note: python is is dynamically typed which means you dont need to declare variable and leaf it without using. therefore 
in python you can declare a variable and initialize at the moment you want to use otherwise it will not be created.
but several other languages such as Java you can able to declare a variable with its datatype and do not assign a value (is option)
such variable is declared before it was used.

define a variable: is data storage container"""

# a is the variable name and 10 is the value (integer) the = sign is called assignment operator it assigns the value to variable and the rule is the value must be at right side and the name of the variable must be at the left side
a = 10
print(a)  # output : 10

# how to check the datatype of a variable in python
# use the type function and put the variable name as parameter like this
# type(a)
# to print the variable data type use the print() function and put the type(variable_name) function as follows
print(type(a))  # output : <class 'int'>

a = 10.9  # this re-assigns the variable a in a number with a decimal point. Note: python reads the last value assigned to variable and tell the computer the type of the variable based on the value charectersitics you assigned
print(type(a))  # output : <class 'float'>


"""DATA TYPES IN PYTHON WITH EXAMPLES 
this examples i will show you how many ways you can store a diffrent data in a variable """

var_int = 40  # stores a integer value
var_float = 40.40  # stores a float value
var_string = 'hello world'  # stores a string value
var_boolean = True  # stores a boolean value (true or false)

# stores multiple values in a variable (list stores collection of data value and uses square brackets)
"""list variable the items are displayed the way it is written (ordered) and if you add new item it will be added at the end but you can delete item
in a specified manner, you can change the values and allow duplicate value to be in the set. they are also indexible means the first item is in index [0]"""
var_list = ["Car", "Boat", "Plane", "Train"]
# stores a multiple value in a variable (tuple stores collection of data value and uses round brackets), is ordered and you can not change
var_tuple = ("Car", "Boat", "Plane", "Train")
# stores a multiple value in a variable (set stores collection of data value and uses curly brackets)
"""SET, is unordered (prints in a random order and diffrent runs might get diffrent orders, thus is difcult to index desired item), 
unchangeable once set variable is created (except that you can add and delete), ignores duplicate values(set does not allow to create same values in a set) 
and unindexed"""
var_set = {"Car", "Boat", "Plane", "Train"}
var_frozenset = frozenset({"Car", "Boat", "Plane", "Train"})
var_dictionary = {"name": "Car", "type": "Electric", "price": 50.000}

var_complex = 10j
var_bytes = b"MyCar"
var_memoryview = memoryview(bytes(2))
var_NoneType = None
