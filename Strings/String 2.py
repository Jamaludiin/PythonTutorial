# Create String Variable and Assign Value
print("Example 0 ------------------------------------------------------")
# Create Python variable and store with string value
# Use double quate
var_str1 = "This is a String used with double quotation"
# Use single quate
var_str2 = "This is a String used with single quotation"


# Display the string literals using print() function in python

print(var_str1)
print(var_str2)
print("I like Python Strings")

print("\nExample 1 ------------------------------------------------------")

# Singleline String Value

# Multiline String Value
# ------------------------
# Create a variable and assign a multiline string value in Python
# We use triple double qoatation
var_multiline_str1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print("\nExample 2 ------------------------------------------------------")

# you can also use a triple single quates
var_multiline_str2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# the above string was surrounded by  three quotes otherwise it will not accept
""" normally strings are surrounded with single and double quatation, however, strings can grow beyond few words
and might become multiline, tabs and with other special charecters inside.
therefore, trible quatations will be used to support string with such carecteristics.
Note: triple quatations can be single (use three single quatations) or double quates (three double quatations)
"""
print(var_multiline_str1)
print("")
print(var_multiline_str2)

print("\nExample 3 ------------------------------------------------------")

# Access String Items

# ---------------
# String Indexing
# Acess string items using their index (Positive Indexing) in Python
var_str = "Strings are Object"
print(var_str[0])
print(var_str[3])
var_bool = True
print(var_str[var_bool])
print(var_str[0:8])

print("\nExample 4 ------------------------------------------------------")

# -----
# String Indexing
# Acess string items using their index (Negative Indexing) in Python
var_str = "Strings are Object"
print(var_str[-4])
print(var_str[-3])
print(var_str[-1 : len(var_str)])
print(var_str[-6:])
print(var_str[: len(var_str) - 1])

print("\nExample 5 ------------------------------------------------------")

# ---------------
# String Looping
# Access string items using for loop in Python
var_str = "This is Python String"
for i in var_str:
    print("The string items of :", i)

print("\nExample 5 ------------------------------------------------------")

# ---------------
# We can also use the range() function during the loop process
var_str = "Python is AMAZING"

for i in range(len(var_str)):
    print("The string items of :", var_str[i])

print("\nExample 6 ------------------------------------------------------")

# ----------------
# Perform Operations on Strings
var_str1 = "90"
var_str2 = "10.90"

var_str = var_str1 + var_str2
print(var_str)
print("Use + Operator" + "to Combine Strings")
print(var_str1 + " + " + var_str2 + " =", int(var_str1) + float(var_str2))

print("\nExample 7 ------------------------------------------------------")

# --------------------
# Combine two Strings
var_str1 = "I love "
var_str2 = "Python"

var_str = var_str1 + var_str2
print(var_str)
print("Use + Operator" + "to Combine Strings")
print(var_str + " " + var_str)

print("\nExample 8 ------------------------------------------------------")

# ----------------
# Compare two Strings
var_str1 = "Python is a programming language "
var_str2 = "Python is a coding language"

var_str = var_str1 == var_str2
print(var_str)
print("Python is a good language" == "Python is a good language")

print("\nExample 9 ------------------------------------------------------")

# String Length
var_str = "We must learn Python programming language"

# Use the len() function to get the length of a string
var_len = len(var_str)

print(var_len)
print(len("This is my length"))

print("\nExample 10 ------------------------------------------------------")

# ---------------
# Check String
var_str = "We must learn Python programming language"

# Use the in keyword to check if a certain word, phrase or character is present in a string
var_check = "Python" in var_str

print(var_check)
print("language" in var_str)
print("website" in var_str)

print("\nExample 11 ------------------------------------------------------")

# -------------------
# Check String
# Use NOT IN Keyword to Check String
var_str = "We must learn Python programming language"

# Use the not in keywords to check if a certain word, phrase or character is not present in a string
var_check = "Python" not in var_str

print(var_check)
print("language" not in var_str)
print("website" not in var_str)

print("\nExample 12 ------------------------------------------------------")

# -------------------
# Check String
# Use IF and IN Keyword to Check String
var_str = "We must learn Python programming language"
var_check = None

# Use the if and in keywords to check if a certain word, phrase or character is present in a string
if "Python" in var_str:
    var_check = True
    print(var_check, ":" + "The Python word is present in the main text")

if "Java" in var_str:
    var_check = True
    print(var_check, ":" + "The Java word is present in the main text")

print("\nExample 13 ------------------------------------------------------")

# -------------------
# Check String
# Use IF and NOT IN Keywords to Check String
var_str = "We must learn Python programming language"
var_check = None

# Use the if and not in keywords to check if a certain word, phrase or character is not present in a string
if "Python" not in var_str:
    var_check = True
    print(var_check, ":" + "The Java word is not present in the main text")

if "Java" not in var_str:
    var_check = True
    print(var_check, ":" + "The Java word is not present in the main text")
