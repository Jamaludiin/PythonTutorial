"""

Python Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, 
with the same memory location:

Operator	        Description	                                                Example	Try it
is 	                Returns True if both variables are the same object	        x is y	
is not	            Returns True if both variables are not the same object	    x is not y

"""

#EXAMPLE 1: USE IDENTITY OPERATOR IS IF TWO OBJECTS ARE SAME OBJECT USING PYTHON
print("")

var_int1 = 10
var_int2 = 10

if var_int1 is var_int2:
    print("BOTH OBJECTS ARE SAME")
else:
    print("BOTH OBJECTS ARE NOT SAME")

print("")
var_set1 =["JAMAL","ALI","ABDI"]
var_set2 =["JAMAL","ALI","ABDI"]

if var_set1 is var_set2:
    print("BOTH OBJECTS ARE SAME")
else:
    print("BOTH OBJECTS ARE NOT SAME")

print("")
var_set3 = var_set1

if var_set1 is var_set3:
    print("BOTH OBJECTS ARE SAME")
else:
    print("BOTH OBJECTS ARE NOT SAME")


#examples below are from w3schools
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


#EXAMPLE 2: USE IDENTITY OPERATOR IS NOT IF TWO OBJECTS ARE NOT SAME OBJECT USING PYTHON
print("")

var_int1 = 10
var_int2 = 10

if var_int1 is not var_int2:
    print("BOTH OBJECTS NOT ARE SAME")
else:
    print("BOTH OBJECTS ARE SAME")


print("")

if var_set1 is not var_set2:
    print("BOTH OBJECTS ARE NOT SAME")
else:
    print("BOTH OBJECTS ARE  SAME")