"""
Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	                                                                        Example	Try it
in 	        Returns True if a sequence with the specified value is present in the object	    x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y

"""

#EXAMPLE 1: USE IN OPERATOR IF A SPECIFIC VALUE FROM ONE SET IS PRESENT IN ANOTHER SET VARIABLE USING PYTHON
var_set1 = ["Jamal","Abdi","James"]
var_set2 = ["James","Mike","Abdi"]

print("The James item can be found in this set : ","James" in var_set1)
#IT RETURN TRUE IF THE VALUE IS FOUND

print("")

#example 1.1: or you can do like this
var_check = "James" in var_set1
#we store the return value of the in operator in var_check var after it is checked
print("The James item can be found in this set : ",var_check)

print("")

#example 1.2: or you can do like this
if "James" in var_set1:
    print("USING IF STATEMENT: The James item can be found in this set : ",var_check)


print("")

#example 1.3: or you can do like this
if var_set2 in var_set1:
    print("USING IF STATEMENT: The set items of both variables can be found in each others set")
else:
    print("USING ELSE STATEMENT: The set items of both variables can not be found in each others set")

print("")

#or you can check like this
if "Jamal" in var_set1:
  print("True, 'Jamal' is in the list : ")

#or we can use like this

print("")

for i in var_set1:
  print("the i is : ",i)

print("")
print("the last item in i is : ",i)


print("")

#EXAMPLE 2: USE NOT IN OPERATOR IF A SPECIFIC VALUE FROM ONE SET IS PRESENT IN ANOTHER SET VARIABLE USING PYTHON
#not in	    Returns True if a sequence with the specified value is not present in the object	x not in y
var_set3 = ["Jamal","James","Mike"]
var_tuple = ("Jamal","James","Mike")

if var_set3 not in var_tuple:
    print("USING IF STATEMENT: The set and tuple items of both variables can be found in each others set")
else:
    print("USING ELSE STATEMENT: The set and tuple items of both variables can not be found in each others set")


print("")

#or we can use like this
var_check2 = var_tuple not in var_set3
print("The value of the var_check2 is :",var_check2)

#CHECK THE FOLLOWING IF WE CAN USE
#for var_set1 not in var_set2:
        #print("TRUE....")
 #THE OBOVE EXAMPLE IS NOT WORKING IF WE USE THE NOT IN OPERATOR IN THE FOR LOOP... WHY ..

"""It looks like you are confusing a couple of things. The for loop is used to iterate over sequences (lists, tuples, 
characters of a string, sets, etc). The not operator reverses boolean values. Some examples:""" #CITE stackoverflow
"""

This loops over everything in objects and only processes the ones that aren't in list. Note that this won't 
be very efficient; you could make a set out of list for efficient in checking:

s = set(list)
for object in objects:
    if object not in s:
        do_whatever_with(object)
""" #CITE stackoverflow