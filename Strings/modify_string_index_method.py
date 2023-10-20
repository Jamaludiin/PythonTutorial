"""
find()	Searches the string for a specified value and returns the position of where it was found
cite: w3schools.com

#we use index() method to return the index number of the item specified, if the items are duplicate the first item index is returned
#the index() method requires a parameter which the item you are searching his index.
#the value of the parameter can be any data type such as string, intiger, float even list
#the index() method has the follwoing format style list_var.index(item, start_index_of_sublist, end_index_of_sublist)
"""

var_string = "My name is Jamal Nuh"
#find were the word 'Jamal' mentioned in the string
print("")
print("The word Jamal is metioned after position (or at index) : ",var_string.index("Jamal"))
#The word Jamal is metioned after position (or at index) :  11
"""
            ----------------------------------------------------------
                        Syntax
                        string.index(value, start, end)
            ===========================================================
Parameter Values
Parameter	Description
value	Required. The value to search for
start	Optional. Where to start the search. Default is 0
end	Optional. Where to end the search. Default is to the end of the string

"""

#EXAMPLE 1: FIND WERE A SPECIFIC TEXT WERE MENTIONED IN THE MAIN STRING USING INDEX METHOD IN PYTHON
var_string = "My name is Jamal Nuh"
#find were the word 'ma' mentioned in the string
print("")
print("The word ma is metioned after position (or at index) : ",var_string.index("ma"))
#The word Jamal is metioned after position (or at index) :  13
#NOTE THE COUNTING YOU CAN START FROM ZERO, THUS, THE 13 WILL BE m, but if you start from 1 it will be before m

print("")
print("The word ma is metioned after position (or at index) : ",var_string.index("ma",4,len(var_string)))
#the bellow line is erorr becouse the start value must not be greater then the end value
#print("The word ma is metioned after position (or at index) : ",var_string.index("ma",4,0))
#if we use the find it will not triger an error but there is no result
#print("The word ma is metioned after position (or at index) : ",var_string.find("ma",4,0))


