"""
find()	Searches the string for a specified value and returns the position of where it was found
Cite: w3schools.com

the find() method returns the position of the SPECIFIED STRING AS A RESULT or charecter that was found at specified range positions


OTHER DEFINTIONS FROM W3SCHOOLS.COM
Definition and Usage
The find() method finds the first occurrence of the specified value.

The find() method returns -1 if the value is not found.

The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)
"""

#EXAMPLE 1: FIND THE LOCATION OR POSITION OF A DESIRED STRING AT PARTICULAR STRING 
# OR FIND WERE THE SPECIFIED TEXT WAS MENTIONED IN THE STRING
var_string = "My name is Jamal Nuh"
#find were the word 'Jamal' mentioned in the string
print("")
print("The word Jamal is metioned after position : ",var_string.find("Jamal"))
#result interortation 
"""
output: The word Jamal is metioned at position :  11
this means the count starts 1 until the word jamal is found, therefore jamal is found after 11 position
"""

#what is the search string is small case and the main string is upper case. like this
print("")
print("The word Jamal is metioned at position : ",var_string.find("jamal"))
#result interortation 
"""
output: The word Jamal is metioned at position :  -1
this means the text was not found and by default it will return -1 instead of trigering an error
"""

"""
            ----------------------------------------------------------
                        Syntax
                        string.find(value, start, end)
            ===========================================================
Parameter Values
Parameter	Description
value	Required. The value to search for
start	Optional. Where to start the search. Default is 0
end	Optional. Where to end the search. Default is to the end of the string

"""

#EXAMPLE 2: FIND THE LOCATION OF SPECIFIC STRING OR CHARECTER AT SPECIFIED LOCATION
var_string = "My name is Jamal Nuh"
#find were the word 'Jamal' mentioned in the string BUT START THE SEARCHING AT CENTER OF THE MAIN STRING
print("")
print("The word Jamal is metioned after position : ",var_string.find("Jamal",int(len(var_string)/2)))

#other options of start position of the search include by specifying the int value directly
print("The charecter a is metioned after position : ",var_string.find("a",5))
#INTIALLY IF YOU DID NOT SPECIFY THE SECOND PARAMETER, THE SEARCH WILL BE STARTED AT THE FIRST INDEX 0 UNTILL THE LAST INDEX OF THE STRING
#AND IF YOU ONLY SPECIFY THE START ONLY, THE END PARAMETER WILL OUTOMATICALLY BE THE FINAL INDEX OF THE MAIN STRING 
# WHICH MEANS THE SEARCH WILL CONTINOU UNTILL THE END OF THE STRING

print()
#EXAMPLE 3: FIND THE LOCATION OF SPECIFIC STRING OR CHARECTER AT SPECIFIED RANGES
print("The charecter a is metioned after position : ",var_string.find("a",13,22))
#YOU CAN SPECIFY THE FINAL USING len method
print("The charecter a is metioned after position : ",var_string.find("a",13,len(var_string)))


print()
#USING NEGATIVE VALUES AT THE SECOND OR THIRSD PARAMETER OF THE find() METHOD IN PYTHON
#EXAMPLE 4: FIND THE LOCATION OF SPECIFIC STRING OR CHARECTER AT SPECIFIED RANGES using negative values
print("The charecter a is metioned after position : ",var_string.find("a",-6,22))
#THE RULE OF THE START AND THIRD PARAMETERS IS 
# THE VALUE OF THE FIRST PARAMETER MUST ALWAYS GREATER THAN THE VALUE OF THE SECOND PARAMETER 
# NO MATTER WHETHER IT IS BEGATIVE OR POSITIVE VALUES



print("")
#THE DIFFRENCE BETWEEN THE find() and index() METHOD
print("The charecter a is metioned after position : ",var_string.find("a",-6,22))
print("The charecter a is metioned after position : ",var_string.index("a",-6,22))

#the index method: Searches the string for a specified value and returns the position of where it was found
#the find method : Searches the string for a specified value and returns the position of where it was found
#and the only diffrence is the index method if you specified a value that does not exist it will triger error 
# while the find method does not triger error instead it will return -1
