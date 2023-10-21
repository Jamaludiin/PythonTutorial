print("Example 0-------------------------------------------------------")
# -------------------
# string formatting
# Empty Placeholder
var_str = "My favorite programing language is : {}. I have {} years of experience. "
var_lan = "Python"
var_exp = 7

print(var_str.format(var_lan, var_exp))
print(var_str.format("Java", 8))

print("\nExample 1-------------------------------------------------------")

# Order of the argument
var_str = "My favorite programing language is : {}. I have {} years of experience."
var_lan = "Python"
var_exp = 7

print(var_str.format(var_exp, var_lan))

var_str = "My favorite programing language is : {}. I have {} years of experience. {}"

print(var_str.format(True, 5, "Java"))

print("\nExample 2-------------------------------------------------------")

# Over Specifying arguments on Empty Placeholders
var_str = "My favorite number is : {}, I have {} US Dollar and {} cents. "
var_num = 8
var_dollar = 7
var_cent = 0.8

print(var_str.format(var_num, var_dollar, var_cent, 8))
print(var_str.format(9, 8, 6, 9))
print(
    "Over Specifying the argument on empty placeholders WORKs as it IGNORES the ADITIONALS"
)

print("\nExample 3-------------------------------------------------------")

# Under_Specifying arguments on Empty Placeholders
var_str = "My favorite number is : {}, I have {} US Dollar and {} cents. "
var_num = 8
var_dollar = 7
var_cent = 0.8

# print(var_str.format(var_num,var_dollar))
# print(var_str.format(9,8))
print("Under Specifying the argument on empty placeholders will lead error")

print("\nExample 4-------------------------------------------------------")

# Combining string and numbers using format() method
# Named Placeholder
var_str = "My favorite programing language is : {language}. I have {experience} years of experience. "
var_lan = "Python"
var_exp = 7

print(var_str.format(language=var_lan, experience=var_exp))
print(var_str.format(language="C++", experience=9))
print(var_str.format(experience=3, language="PHP"))

print("\nExample 5-------------------------------------------------------")

var_str = (
    "Python is {int_num} easy to learn {float_num} and easy to understand {bool_num} "
)
var_int = 90
var_float = 89.67
var_bool = True

print(var_str.format(int_num=var_int, float_num=var_float, bool_num=var_bool))

print("\nExample 6-------------------------------------------------------")

# Over-specify the Number of Arguments Passed to the format() Method in Named Placeholders
var_str = (
    "Python is {int_num} easy to learn {float_num} and easy to understand {bool_num} "
)
var_int = 90
var_float = 89.67
var_bool = True

# print(var_str.format(int_num = var_int, float_num = var_float, bool_num = var_bool, float_num = 8.90))
# print(var_str.format(int_num = 87, float_num = 8.90, bool_num = False, float_num = 8.90, bool_num = False,))
print("Over Specifying the argument on named placeholders will lead error")

print("\nExample 7-------------------------------------------------------")

# Under-specify the Number of Arguments Passed to the format() Method using Named Placeholders
var_str = (
    "Python is {int_num} easy to learn {float_num} and easy to understand {bool_num} "
)
var_int = 90
var_float = 89.67
var_bool = True

# print(var_str.format(int_num = var_int,float_num = 8.90))
# print(var_str.format(int_num = 87, float_num = 8.90))
print("Under Specifying the argument on named placeholders will lead error")

print("\nExample 8-------------------------------------------------------")

# Numbered Placeholder (index placeholder/numbered indexes)
var_str = "This is int {0} this is float {1} this is bool {2} this is string {3}"
var_int = 90
var_float = 89.67
var_bool = True

print(var_str.format(var_int, var_float, var_bool, "Amazing"))

print("\nExample 9-------------------------------------------------------")

# The order of the Numbered Placeholder (index placeholder/numbered indexes)
var_str = "This is int {1} this is float {0} this is bool {3} this is string {2}"
var_int = 90
var_float = 89.67
var_bool = True

print(var_str.format(var_int, var_float, var_bool, "Amazing"))

print("\nExample 10-------------------------------------------------------")

# Do not skip index of the Numbered Placeholder (index placeholder/numbered indexes)
var_str = "This is int {1} this is float {4} this is bool {3} this is string {2}"
var_int = 90
var_float = 89.67
var_bool = True

# print(var_str.format(var_int, var_float, var_bool,"Amazing"))
print(
    "Do not skip index of the Numbered Placeholder (index placeholder/numbered indexes)"
)

print("\nExample 11-------------------------------------------------------")

# Over-specifying the Number of Arguments Passed to the format() Method using Numbered Placeholders
var_str = "Python is {0} easy to learn {1} and easy to understand {2} {3}"
var_int = 90
var_float = 89.67
var_bool = True

print(
    var_str.format(var_int, var_float, var_bool, 8.90, "Over=specifying", "Is allowed")
)

print("\nExample 12-------------------------------------------------------")

# Under-specifying the Number of Arguments Passed to the format() Method using Numbered Placeholders
var_str = "Python is {0} easy to learn {1} and easy to understand {2} {3}"
var_int = 90
var_float = 89.67
var_bool = True

# print(var_str.format(var_int, var_float, var_bool))
print("Under Specifying the argument on numbered placeholders will lead error")

# Formatting types
print("\nExample 13-------------------------------------------------------")

# Thousand Separators
# Use the :, to add a comma as a thousand separator
var_num = 637245566
var_output = "The number is formatted {:,}".format(var_num)
print(var_output)

# Use the :_ to add a underscore character as a thousand separator
var_output = "The number is formatted {:_}".format(var_num)
print(var_output)

var_output = "The number is formatted {:,}"
print(var_output.format(var_num))

print("\nExample 14-------------------------------------------------------")

# Number Formatting:
var_num = 6372455664.8976778

# :d Decimal format: is used to convert binary numbers, into decimal number format
var_output = "The Binary number is converted to integer number {0} is {0:d}".format(
    0b1110
)
print(var_output)

print("\nExample 15-------------------------------------------------------")

# :e Scientific number format: is used to convert the specified numbers into scientific number format
var_output = "The Scientific number formatted :e: {:e}".format(var_num)
print(var_output)
var_output = "The Scientific number formatted :e: {:e}".format(87)
print(var_output)
var_output = "The Scientific number formatted :e: {:e}".format(7654322)
print(var_output)

print("\nExample 16-------------------------------------------------------")

# :E Scientific format (must be upper case E) : is used to convert a number into scientific number format (with an upper-case E):
var_output = "The Scientific number formatted :E: {:E}".format(var_num)
print(var_output)
var_output = "The Scientific number formatted :E: {:E}".format(87)
print(var_output)
var_output = "The Scientific number formatted :E: {:E}".format(7654322)
print(var_output)

print("\nExample 17-------------------------------------------------------")

# :n Number format
var_output = "The number is formatted :n: {:n}".format(var_num)
print(var_output)
var_output = "The number is formatted :n: {0} is {0:.3n}".format(8566.76)
print(var_output)

print("\nExample 18-------------------------------------------------------")

# :g general format specifier: is used to automatically choose between fixed-point and exponential notation based on the magnitude of the number being formatted.
var_output = "The number is formatted :g: {:g}".format(58888888888)
print(var_output)
var_output = "The number is formatted :g: {:g}".format(78)
print(var_output)
var_output = "The number is formatted :g: {:g}".format(var_num)
print(var_output)

print("\nExample 19-------------------------------------------------------")

# :G General format is similar the :g and but uses uppercase exponent notation for large values.
var_output = "The number is formatted :G: {:G}".format(58888888888)
print(var_output)
var_output = "The number is formatted :G: {:G}".format(78)
print(var_output)
var_output = "The number is formatted :G: {:G}".format(var_num)
print(var_output)

print("\nExample 20-------------------------------------------------------")

# :f Fix point number format
# this is used to convert specified numbers into a fixed point number, by default it displays 6 decimal maximum.
# We have to use a period (.) followed by the number that specifies the number of decimals to be diplayed:
var_output = "The number is formatted :f: {:f}".format(
    var_num
)  # default it display 6 decimal maximum
print(var_output)
var_output = "The number is formatted :f: {:.3f}".format(var_num)
print(var_output)
var_output = "The number is formatted :f: {:.8f}".format(var_num)
print(var_output)
var_output = "The number is formatted :f: {0} in {0:f}".format(float("INF"))
print(var_output)
var_output = "The number is formatted :f: {0} in {0:f}".format(float("NAN"))
print(var_output)

print("\nExample 21-------------------------------------------------------")

# :F Fix point number format,is used to to convert a number into a fixed point number, but display inf and nan as INF and NAN
var_output = "The number is formatted :F: {0} in {0:F}".format(77)
print(var_output)
var_output = "The number is formatted :F: {0} in {0:F}".format(float("inf"))
print(var_output)
var_output = "The number is formatted :F: {0} in {0:F}".format(float("nan"))
print(var_output)

print("\nExample 22-------------------------------------------------------")

# :% Percentage format is used to convert the specified numbers into a percentage format
var_output = "The number is formatted :%: {:%}".format(var_num)
print(var_output)
var_output = "The number is formatted :%: {:%}".format(67)
print(var_output)
var_output = "The number is formatted :%: {:%}".format(0.2)
print(var_output)
var_output = "The number is formatted :%: {:.0%}".format(0.34)
print(var_output)
var_output = "The number is formatted :%: {:.1%}".format(0.66)
print(var_output)

print("\nExample 23-------------------------------------------------------")

# :o Octal format is used to convert the specified numbers into octal format
var_output = "The number is formatted :o: {:o}".format(90)
print(var_output)
var_output = "The number is formatted :o: {0} {0:o}".format(677)
print(var_output)

print("\nExample 24-------------------------------------------------------")

# :b Binary format is used to convert the specified numbers (must be integer) into binary format
var_output = "The number is formatted :b: {:b}".format(44)
print(var_output)
var_output = "The number is formatted :b: {0} in binary is {0:b}".format(899876)
print(var_output)

print("\nExample 25-------------------------------------------------------")

# :x Hex format (must be lower case) is used to convert the specified number (must be integer) into Hex format
var_output = "The number is formatted :x: {:x}".format(89)
print(var_output)
var_output = "The number is formatted :x: {0} in hex is {1:x}".format(255, 255)
print(var_output)

print("\nExample 26-------------------------------------------------------")

# :X Hex format (X must be upper case) to convert the specified number into upper-case Hex format:
var_output = "The number is formatted :X: {:X}".format(89)
print(var_output)
var_output = "The number is formatted :X: {0} in hex is {1:X}".format(255, 255)
print(var_output)

print("\nExample 27-------------------------------------------------------")

# Alignment and Sign
# :< Left aligns the result (within the available space)
txt = "I like {:<9} coding."
print("I like Python coding.")
print(txt.format("Python"))
print(txt.format("Pytho"))
print(txt.format("Pyth"))
print(txt.format("Pyt"))

print("The number of spaces added to align left is : ", 9 - len("Python"))
print("The number of spaces added to align left is : ", 9 - len("Pytho"))
print("The number of spaces added to align left is : ", 9 - len("Pyth"))
print("The number of spaces added to align left is : ", 9 - len("Pyt"))

print("\nExample 28-------------------------------------------------------")

# :- Use a minus sign for negative values only
txt = "This is a negative number {:-}."
print(txt.format(98))
print(txt.format(-45))

print("\nExample 29-------------------------------------------------------")

# investigate later
txt = "This is a negative number {:-9}."
print(txt.format(45))

print("\nExample 30-------------------------------------------------------")

# :^ The values (arguments) will be aligned center
txt = "I like {:^10} coding."
print("I like Python coding.")
print(txt.format("Python"))
print(txt.format("Pytho"))
print(txt.format("Pyth"))
print(txt.format("Pyt"))

print(
    "The value is centered and total spaces will be added at both side:",
    10 - len("Python"),
)
print(
    "The value is centered and total spaces will be added at both side:",
    10 - len("Pytho"),
)
print(
    "The value is centered and total spaces will be added at both side:",
    10 - len("Pyth"),
)
print(
    "The value is centered and total spaces will be added at both side:",
    10 - len("Pyt"),
)

print("\nExample 31-------------------------------------------------------")

# :> The values (arguments) will be right aligned based on the number of spaces specified.
txt = "I like {:>9} coding."
print("I like Python coding.")
print(txt.format("Python"))
print(txt.format("Pytho"))
print(txt.format("Pyth"))
print(txt.format("Pyt"))

print("The number of spaces added to align right is : ", 9 - len("Python"))
print("The number of spaces added to align right is : ", 9 - len("Pytho"))
print("The number of spaces added to align right is : ", 9 - len("Pyth"))
print("The number of spaces added to align right is : ", 9 - len("Pyt"))

print("\nExample 32-------------------------------------------------------")

# :+ We use a plus sign to show if the value is positive or negative
txt = "Is this a negative or possitive number {:+}."
print(txt.format(67))
print(txt.format(-89))

print("\nExample 33-------------------------------------------------------")

# : We use this format specifier (space) to insert an extra space before the numbers (both the positive and negative numbers)
txt = "Is this a negative or possitive number {:} and {:}."
print(txt.format(67, -34))
print(txt.format(-23, 55))

txt = "Is this a negative or possitive number {:5} and {:7}."
print(txt.format(67, -34))
print(txt.format(-23, 55))

print("\nExample 34-------------------------------------------------------")

# := Is used to places the sign (minus or plus) to the left most position.
txt = "The signs are left aligned {:=3} and {:=5}."
print(txt.format(+67, -34))
print(txt.format(-23, +55))

txt = "The signs are left aligned {:=5} and {:=7}."
print(txt.format(67, -34))
print(txt.format(-23, 55))

print("\nExample 35-------------------------------------------------------")

# :c This converts the assigned value into the corresponding Unicode character

txt = "The signs are left aligned {:c} and {:c}."
print(txt.format(67, 34))
print(txt.format(88, 90))

"""
Number Formatting:

n Number format
d Decimal format
e Scientific format, with a lower case e
g General format
G General format (using a upper case E for scientific notations)
f Fix point number format
E Scientific format, with an upper case E
% Percentage format
o Octal format
b Binary format
x Hex format, lower case
F Fix point number format, in uppercase format (show inf and nan as INF and NAN)

Alignment and Sign:

:< Left aligns the result (within the available space)
:- Use a minus sign for negative values only
:^ Center aligns the result (within the available space)
:> Right aligns the result (within the available space)
:+ Use a plus sign to indicate if the result is positive or negative
: Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:= Places the sign to the left most position

Thousand Separator:

:_ Use an underscore as a thousand separator
:, Use a comma as a thousand separator

Miscellaneous:

:c Converts the value into the corresponding Unicode character


"""
