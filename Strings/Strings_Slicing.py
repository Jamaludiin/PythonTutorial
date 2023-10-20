"""
STRING SLICING
this is used to index a specified range of charecters using slice syntax
the syntax has a start and end index seperated by colon
"""
print("")

var_str = 'My name is Jamal Nuh'
#the index of the first charecter starts at 0 

#EXAMPLE 1: SELECT THE STRING CHARECTERS RANGING FROM 11 TO 16 USING STRING SLICING IN PYTHON
print("The value ranging from 11 to 16 index is : ",var_str[11:16])
#the retrieval start from 11 th position till 15 (included) while the specified 16 is execluded

#SLICE FROM THE START
#EXAMPLE 2: NOT SPECIFIED THE START INDEX DURING THE STRING SLYCING IN PYTHING
#IF YOU DID NOT SPECIFY THE START POINT OF THE INDEX, IT MEANS IT WILL AUTOMATICALLY BE STARTED FROM THE FIRST INDEX
#WHICH IS ZERO
print("")
print("The value ranging from UNSPECIFIED FIRST INDEX to 16 th index is : ",var_str[:16])
#it is also similar like this
# ...  print("The value ranging from UNSPECIFIED INDEX to 16 th index is : ",var_str[0:16])


#SLICE TO THE END
#EXAMPLE 3: NOT SPECIFIED THE LAST INDEX DURING THE STRING SLYCING IN PYTHING
#IF YOU DID NOT SPECIFY THE LAST POINT OF THE INDEX, IT MEANS IT WILL AUTOMATICALLY BE ENDED UPTO THE LAST INDEX
#WHICH IS n-1, where n is the lenght of the string (total string including spaces)
print("")
print("The value ranging from UNSPECIFIED LAST INDEX starting from 11 th index is : ",var_str[11:])
#it is also similar like this
# ...  print("The value ranging from UNSPECIFIED LAST INDEX starting from 11 th index is : ",var_str[11:0])


#NEGATIVE INDEXING
#EXAMPLE 4: USING NEGATIVE INDEXING DURING THE STRING SLICING IN PYTHON 
# FOR EXAMPLE YOU WANT TO STATE A NEGATIVE NUMBER AT BEGINING OF THE SLICING MEANS STARTING FROM THE END OF THE STRING
print("")
print("The last charecter of the string is :",var_str[-1:])
print("The last charecter of the string is :",var_str[-1:len(var_str)])

#note: i did not mentioned the last index becouse the start index is already pointing at last charecter 
#if you leave empty at the last index, by default the range will go to the end:
# while the last index is the n-1, but n-1 is not inclusive, so n only will be ok to get inclusiveness


print("")
#EXAMPLE 5: DISPLAY THE LAST THREE CHARECTERS OF THE STRING IN PYTHON USING STRING SLYCING IN PYTHON
print("The last charecter of the string is :",var_str[-3:len(var_str)])

print("")

#EXAMPLE 6: DISPLAY ALL THE STRING CHARECTERS EXCEPT FOR THE LAST CHARECTER USING STRING SLYCING IN PYTHON
print("All charecters of the string except for the last charecter is :",var_str[0:-1])
print("All charecters of the string except for the last charecter is :",var_str[:len(var_str)-1])
print("All charecters of the string except for the last charecter is :",var_str[:19])




print("",len(var_str))

print("")

#EXAMPLE 7: DISPLAY THE LAST 9 CHARECTERS USING STRING SLYCING IN PYTHON
print("The last 9 charecter of the string is :",var_str[-9:])

