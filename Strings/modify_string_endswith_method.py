"""
endswith()	        Returns True value if the target string ends with a certain specified string value (it can be char, string) otherwise returns false value

"""

#EXAMPLE 1: HOW TO CHECK IF A CERTAIN STRING END WITH A CERTAIN CHARECTER OR STRING IN PYTHON
#THE endwith() is method that is used to check if a certain string end with a certain specified value (it can be charecter, or string)

#check if the string value in this variable ends with 'h' or 'Nuh'
var_string = "My name is Jamal Nuh"
#we use to check only single charecter
print("Is this ends with 'h' or not? : ",var_string.endswith('h'))
#we use to check multiple charecters
print("Is this ends with 'Nuh' or not? : ",var_string.endswith('Nuh'))
#we use to check only single charecter that does not exist in the string value
print("Is this ends with 'k' or not? : ",var_string.endswith('k'))

print("")

#EXAMPLE 2: HOW TO CHECK IF A CERTAIN STRING END WITH A CERTAIN CHARECTER OR STRING USING IF ELSE STATEMENT AND endwith() METHOD IN PYTHON 
if var_string.endswith('h'):
    print("It ends with a 'h : ",var_string.endswith('h'))
else:
    print("It does not end with 'h' : ",var_string.endswith('h'))

#can we use endwith() method to non-string values such as int values etc
#EXAMPLE 3: CHECK IF CERTAIN NUMBERS ENDS WITH A CERTAIN SPECIFIED NUMBER USING endwith() METHOD IN PYTHON
var_int = 1234
#----------------- print("Does the integer values of 1234 ends with 4 or not : ",var_int.endwith(4)) -----------------
#the above result is not valid becouse endwith() method cannot be used in int variable and is only be used string variable


"""
            ----------------------------------------------------------
                        Syntax
                        string.endswith(value, start, end)
            ===========================================================

Parameter Values
Parameter	Description
value	Required. The value to check if the string ends with
start	Optional. An Integer specifying at which position to start the search
end	Optional. An Integer specifying at which position to end the search

"""
print("")
#EXAMPLE 4: CHECK IF A SET OF CERTAIN STRINGS ENDS WITH A CERTAIN CHARECTER(S) BY SPECIFYING THE START POSITION OF THE SEARCH USING endwith() METHOD IN PYTHON
var_string = "My name is Jamal Nuh"
print("Does my last name of Nuh ends with h : ? ",var_string.endswith("h",17))
#USING NEGATIVE NUMBERS TO THE SECOND PARAMETER OF THE endwith() method BY STARTING THE SEARCH POSITION FROM BACKWARD
print("Does my last name of Nuh ends with h : ? ",var_string.endswith("h",-4))

print("")
#EXAMPLE 5: CHECK IF A SET OF CERTAIN STRINGS ENDS WITH A CERTAIN CHARECTER(S) BY SPECIFYING THE START AND END POSITION OF THE SEARCH USING endwith() METHOD IN PYTHON
var_string = "My name is Jamal Nuh"
print("Does my last name of Nuh ends with h : ? ",var_string.endswith("h",17,20))
#this can also be written since counting manually is tedious and error prone
print("Does my last name of Nuh ends with h : ? ",var_string.endswith("h",17,len(var_string)))
#if you leave empty the second parameter is also same output since it will search ends to the last string value
print("Does my last name of Nuh ends with h : ? ",var_string.endswith("h",17))
print("")

#the total lenght is 20, though the string charecters is counted by index and index counting always starts 0, thus,
#the counting starts from 0-19 which is also like this 1-20, therefore, the final parameter of endwith was used as 20
#and 20 is exlusive since the counting is index based (starts 0-19),

#if you use the 19 as the end of the string, this applies exlusive rule and the search stops untill 18, thus, there is no h ending in 18sth index
print("Does my last name of Nuh ends with h : ? ",var_string.endswith("h",17,19))
print("")


var_string = "My name is Jamal Nuh"
#USING NEGATIVE NUMBERS TO THE SECOND PARAMETER OF THE endwith() method BY STARTING THE SEARCH POSITION FROM BACKWARD
print("Does my last name of Nuh ends with h : ? ",var_string.endswith("h",-4))

print("")
var_string = "My name is Jamal Nuh .."
#you can use a negative number for the last two parameters of the endwith() method, 
# but the rule is, the start parameter value (wether is negative or positive) must be greater than the end parameter value 
# otherwise it will not return a value. lets practice for these cenarios

print("Does my last name of Nuh ends with h : ? ",var_string.endswith("h",-4,-10))
#the start is greater than the the end parameter which is not valid, but still returning false or 0, which is converted to False

print("Does my last name of Nuh ends with h : ? ",var_string.endswith("h",-10,-3))
print("Does my last name of Nuh ends with h : ? ",var_string.endswith("h",-10,-5))
#this examples ((-10,-3), (-10,-5)) is ok since the end is greater than the start value
print("")

#you can also use both negative and positive numbers in the parameters but the rule still applies (start must not be greater than the end)
var_string = "My name is Jamal Nuh"
print("Does my last name of Nuh ends with h : ? ",var_string.endswith("h",-1,))
#the end parameter was not specififed although by default is the end of the string, this is also wirtten like this
print("Does my last name of Nuh ends with h : ? ",var_string.endswith("h",-1,len(var_string)))

print("")
print("Does the specified range ends with N : ? ",var_string.endswith("N",17,-2))
print("Does the specified range ends with N : ? ",var_string.endswith("N",17,18))






