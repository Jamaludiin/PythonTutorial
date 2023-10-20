"""

Python Logical Operators
Logical operators are used to combine conditional statements:

Operator	Description	                                                Example	Try it
and 	    Returns True if both statements are true	                 x < 5 and  x < 10	
or	        Returns True if one of the statements is true	             x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true	     not(x < 5 and x < 10)

"""

#EXAMPLE 1: HOW TO USE LOGICAL OPERATOR AND TO CHECK MULTIPLE CONDITIONS IN PYTHON
var_int = 20

if var_int < 30 and var_int > 10:
    print("The value of var_int is between 20 and 30")
else:
    print("The value of var_int is not between 20 and 30")

#EXAMPLE 2: HOW TO USE LOGICAL OPERATOR OR TO CHECK MULTIPLE CONDITIONS IN PYTHON
print("")
if var_int > 30 or var_int > 10:
    print("ONE CONDITION MUST BE TRUE WHEN USED OR OPERATOR")

#EXAMPLE 2: HOW TO USE REVERSE LOGICAL OPERATOR TO REVERSE THE OBTAINED RESULT OF CONDITIONAL STATEMENTS IN PYTHON
print("")
if not(var_int > 30 and var_int > 10): 
# THE CONDITIONS IN THE BRACKET WAS EVALUETED AND BECOME FALSE AND THEN FALSE IS REVERSED TO MAKE IT TRUE AND PRINTS
    print("THE LOGIC RESULT BECOME FALSE AND WAS REVERSED TO BECOME TRUE")

print("")
if not(var_int < 30 and var_int > 10): 
# THE CONDITIONS IN THE BRACKET WAS EVALUETED AND BECOME TRUE AND THEN TRUE IS REVERSED TO MAKE IT FALSE 
# AND ELSE STATEMENT WILL BE PRINTED
    print("THE LOGIC RESULT BECOMES TRUE AND WAS REVERSED TO BECOME FALSE")
else:
    print("THE LOGIC RESULT WAS REVERSE AND BECOME FALSE SO ELSE STATEMENT IS CONSIDERED")
   