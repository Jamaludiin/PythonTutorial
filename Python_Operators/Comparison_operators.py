"""
Python Comparison Operators
Comparison operators are used to compare two values:

Operator	    Name	                    Example	Try it
==	            Equal	                    x == y	
!=	            Not equal	                x != y	
>	            Greater than	            x > y	
<	            Less than	                x < y	
>=	            Greater than or equal to	x >= y	
<=	            Less than or equal to	    x <= y

"""

#COMPARE WHTHER TWO STRINGS ARE EQUAL OR NOT USING IF STATEMENT IN PYTHON
var_str1 = "KAMAL"
var_str2 = "JAMAL"

if var_str1 == var_str2:
    print("BOTH STRINGS ARE EQUAL")
else:
    print("BOTH STRINGS ARE NOT EQUAL")

print("")
#EXAMPLE 2: COMPARE WHTHER TWO STRINGS ARE NOT EQUAL OR NOT USING IF STATEMENT IN PYTHON

if var_str1 != var_str2:
    print("BOTH STRINGS ARE NOT EQUAL")
else:
    print("BOTH STRINGS ARE EQUAL")


print("")
#EXAMPLE 3: COMPARE WHTHER ONE STRINGS IS GREATER THAN OTHE OTHER USING IF STATEMENT IN PYTHON
"""
NOTE:
IN PYTHON STRINGS ARE COMPARED ONE BY ONE, AND THOSE WITH DIFFRENT CHARRECTERS, THEIR UNICODE POINTS ARE COMPARED.
THEREFORE,THE SMALLER UNICODE POINTS ARE SAID TO BE SMALLER THAN THE ONE WITH THE HIGHER UNICODE POINTS.

A Unicode string is a sequence of zero or more code points.
"""

if var_str1 > var_str2:
#if "JAMAL" > "JAMAL":
    print("STRING ONE IS GREATER THAN STRINGS TWO")
else:
    print("STRING ONE IS NOT GREATER THA STRINGS TWO")



print("")
#EXAMPLE 4: COMPARE WHTHER ONE STRINGS IS LESS THAN OTHE OTHER USING IF STATEMENT IN PYTHON

if var_str1 < var_str2:
   print("STRING ONE IS LESS THAN STRINGS TWO")
else:
    print("STRING ONE IS NOT LESS THA STRINGS TWO")

