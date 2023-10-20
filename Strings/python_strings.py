"""
String are set of elemenets surrounded by single or double quataion marks
"""

# EXAMPLE 1: CREATE PYTHON VARIABLE AND STORE WITH A STRING VALUE
# Assign python string to a variable
var_str = "My name is Jamal"

# DISPLAY THE STRING LITERALS USING PRINT FUNCTION IN PYTHON]

print(var_str)
# or you can use like this
print("My name jamal")

print("")
# EXAMPLE 2: CREATE A VARIABLE AND ASSIGN A MULTILINE STRING VALUE USING PYTHON
var_multiline_str = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# you can also do like this with triple single quates
var_multiline_str2 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
# the above string was surrounded by  three quotes otherwise it will not accept
""" normally strings are surrounded with single and double quatation, however, strings can grow beyond few words
and might become multiline, tabs and with other special charecters inside.
therefore, trible quatations will be used to support string with such carecteristics.
Note: triple quatations can be single (use three single quatations) or double quates (three double quatations)
"""
print(var_multiline_str)


"""
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string. cite: w3schools
"""

# STRING INDEXING
print("")
# EXAMPLE 3: ACCESS STRING ITEMS USING THEIR INDEX IN PYTHON
var_str2 = "The string is an object"
print("The second items of the variable is : ", var_str2[1])
"""the string elements can be indexed using their index value (staring from zero to n-1. where n is the total number of string elements)
"""
# EXAMPLE 3: ACCESS STRING ITEMS USING FOR LOOP IN PYTHON
# although strings elements can be indexed, we can use loopthrough all the elements or charecters using for loop
for i in var_str2:
    print("The string items of ", i)

print("")
# or you can do like this by using their index numbers
i = len(var_str2)
for j in range(i):  # or you do like this ... range(len(var_str2)):
    print("The string items of : ", var_str2[j])

print("")

# EXAMPLE 4: SHOW THE LENTH OF A STRING USING len() METHOD PYTHON
print("The length of this variable is : ", len(var_str2))

# EXAMPLE 5: CHECK IF CERTAIN KEYWORD IS PRESENT IN OR NOT IN THE STRING OR THE ARRAYS USING IN OPERATOR
var_str_name = "My name is Jamal Nuh"
print("")
print("The word jamal is not found in the array : ",
      'jamal' in var_str_name)  # uses small letter j
print("Again The word Jamal is found in the array using in operator : ",
      'Jamal' in var_str_name)  # uses capital letter J

# USE NOT IN OPERATOR
print("The word jamal is not found in the array using not in operator : ",
      'Jamal' not in var_str_name)  # uses small letter J


# EXAMPLE 6: CHECK IF CERTAIN KEYWORD IS PRESENT IN THE STRING OR THE ARRAYS USING IN OPERATOR AND IF STATEMENT
var_str_name = "My name is Jamal Nuh"
print("")
if 'Jamal' in var_str_name:
    # uses capital letter J
    print("The word Jamal is found in the array using IF and IN operator")

# or use if not in.    like this
print("")
if 'jamal' not in var_str_name:
    # uses capital letter J
    print("The word jamal is not found in the array using IF and NOT IN operator")
