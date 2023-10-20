
#+++++++++++++++++  POSITION BASED METHODS FOR STRING +++++++++++++++++
var_string = 'my name is jamal nuh'

"""
Syntax
string.center(length, character) ---- the charecter is optional
"""
print("")
#center()	Returns a centered string
#EXAMPLE 7: FIND THE STRING IN THE CENTER USING center() METHOD IN PYTHON
var_str_position = "Jamal"
print("The charecter in the center is : ",var_str_position.center(30))
#The center() method will center align the string, using a specified character (space is default) as the fill character.
#means he put the specified charecter at the center of the specifed charecters (even using spaces)

#or you can do like this
print("The charecter in the center is : ",var_str_position.center(10,"+"))
#note: the total charecters in the returned string will be 10, although the jamal charcters is 5, 
# the additional 5 charecters of + will be introduced in the string while the jamal is centered 
# but the additional 5 must be inserted in both sides of the jamal string, so 5/2 2.5, thus, the least will be 
# inserted at the begining (2) while the remaining 3 will be inserted at end

#___________ BIG NOTE: IF THE SIZE OF THE LENGHT OF THE FIRST PARAMETER IS LESS THAN THE SIZE OF THE STRING TO BE CENTERED 
""" SUCH ARGUMENT WILL NOT WORK BECOUSE OF THIS SCENARIO
# STRING OF 'JAMAL' HAS 5 IN SIZE AND LENGHT PARAMETER IS 10, THIS WHAT WILL HAPEN
# THE 10 LENGTH WILL BE SUBTRACTED THE SIZE OF JAMAL WHICH IS 5 (10-5 = 5) SO THE JAMAL WILL BE SURROUNDED BY 5 CHARECTERS
# FROM LEFT TO RIGHT (2 AT THE LEFT AND 3 AT THE RIGHT SIDE)
# 
# """
print("")

#CHECK IF THE SIZE OF THE LENGHT PARAMETER IS EQUAL TO THE SIZE OF THE STRING TO BE CENTERED
print("The LENGHT PARAMETER HAS EQUAL TO THE charecter TO BE centerED is : ",var_str_position.center(5,"*")) #5-5 IS 0 SO WE EXPECT NOTHING TO HAPPEN
#check the the size or leng of the variable after you apply such scenario
temp = len(var_str_position.center(5,"*"))
print(temp)#we expect 5, becouse you cannot ceneter five in a five (the centered five is included criteria to the lenght parameter)


#CHECK IF THE SIZE OF THE LENGHT PARAMETER IS LESS THAN THE SIZE OF THE STRING TO BE CENTERED
"""
JAMAL IS 5 CHARECTER AND TRY LENGHT WHICH IS 4
"""
print("")

print("The LENGHT PARAMETER HAS LESS THAN THE charecter TO BE centerED is : ",var_str_position.center(4,"*")) #4-5 IS -1 SO WE EXPECT NOTHING TO HAPPEN
#check the the size or leng of the variable after you apply such scenario
temp = len(var_str_position.center(4,"*"))
print(temp)#we expect 5, becouse you cannot ceneter five in a four and they ignore such criteria (the centered five is included criteria to the lenght parameter)


#what about if you read the lenght parameter from the size of variable
print("")
print("the lenght size is read from same variable string to centered : ",var_str_position.center(len(var_str_position),"+"))
temp = len(var_str_position.center(len(var_str_position),"+"))
print(temp)
print("the lenght size is read from another  : ",var_str_position.center(len(var_string),"+"))
#this has greater lenght of 20, so 20-5=15 (7 goes left and 8 to the right, the left will take lower bound and right to the uperbound)
temp = len(var_str_position.center(len(var_string),"+"))
print(temp)


#more examples is here
print("")
#use int method after you perform mathematical operation
print("The charecter in the center is : ",var_str_position.center(int(len(var_string)),"+"))
print("The charecter in the center is : ",var_str_position.center(int(len(var_string)/2),"+"))
#len of var_string is 20 then divide into 2, it become 10 then 10-5 is 5, 
# we expect five to be surrounded by the centered charecter (2 to the left and 3 to the right)

print("The charecter in the center is : ",var_str_position.center(int(len(var_str_position)/2),"+"))
#this does not work since 5/2 is 2.5 and as integer is 2 and 2 is way less than the charecter to be centered

print("")
#use the center() method during the variable intialization and store such value to the variable as follows
var_str_position = "Jamal".center(20)#this stores the jamal value plust the number of specified spaces
print(var_str_position)
print("The number of charecters in this variable is : ",len(var_str_position))
#note the 20 lenght in the first parameter will be diducted the size of the value to be centered which is 5,
#so 15 will be surrounded white spacec (7 to the left and 8 to the right)
#while total size will be 15 + 5 (jamal) = 20, becouse after center() methof the effect or return value was stored

#with second parameter
var_str_position = "Jamal".center(10,"$")#this stores the jamal value plust the number of specified spaces
print(var_str_position)
print("The number of charecters in this variable is : ",len(var_str_position))