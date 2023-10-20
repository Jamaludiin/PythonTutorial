"""
format()	Formats specified values in a string
cite: w3schools.com

Definition and Usage
The format() method formats the specified value(s) and insert them inside the string's placeholder.

The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

The format() method returns the formatted string.
cite: w3schools.com

"""
print("")
var_string_fromat = 'The price of this course is {price:.3f} dollars!'
print(var_string_fromat.format(price = 49))

"""
            ----------------------------------------------------------
                        Syntax
                        string.format(value1, value2...)
            ===========================================================
Parameter Values
Parameter	Description
value1, value2...	Required. One or more values that should be formatted and inserted in the string.

The values are either a list of values separated by commas, a key=value list, or a combination of both.

The values can be of any data type.

The Placeholders
The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
"""

#before you use the format method, you must state your main string a place holder {}. 
# as mentioned above the place holder can have named as index, number as index or exmpty value

#=========================================================================================
#Accessing arguments by name:
#EXAMPLE 1: NAMED PLACEHOLDERS
#the followinh has named palceholder:  {provide a name of the placeholder}
print("")
var_string_fromat = "My name is {fname} I'm {age} years old, i live in {place}"
print(var_string_fromat.format(fname = "John", age = 36,place="Malaysia"))

#CAN YOU LIST THEM IN AN UNORDERED WAY DURING CALLING THESE NAMED PLACEHOLDERS
var_string_fromat = "My name is {fname} I'm {age} years old, i live in {place}"
print(var_string_fromat.format(place="Malaysia",  age = 36, fname = "John"))
#THIS IS WORKING AND THERE IS NO PROBLEM IF THEY ARE NOT ORDERED

#CAN YOU PROVIDE ONE PLACEHOLDER IN THE FORMAT METHOD MULTIPLE TIME
var_string_fromat = "My name is {fname} I'm {age} years old, i live in {place}"
#print(var_string_fromat.format(place="Malaysia"))
#THIS IS NOT WORKING AND YOU MUST MENTION THE THREE PLACEHOLDERS VALUE

#CAN YOU PROVIDE ONE PLACEHOLDER IN THE FORMAT METHOD
var_string_fromat = "My name is {fname} I'm {age} years old, i live in {place}"
#print(var_string_fromat.format(place="Malaysia",  place = 36, place = "John"))
#THIS IS NOT WORKING AND REPEATED ARGUMENT IS NOT ALLOWED


#CAN YOU GIVE SAME PLACE HOLDER NAME INTO TWO DIFFRENT PLACEHOLDERS
var_string_fromat = "My name is {fname} I'm {fname} years old, i live in {place}"
print(var_string_fromat.format(fname = "John", age = 36,place="Malaysia"))
#THIS IS WORKING AND THE AGE PLACEHOLDER WAS NOT EXECUTED INSTEAD fname WAS EXCUTED TWO TIMES

#CAN YOU LEAVE EMPT SOME OF THE PLACEHOLDER NAME 
var_string_fromat = "My name is {fname} I'm {fname} years old, i live in {}"
#print(var_string_fromat.format(fname = "John", age = 36,place="Malaysia"))
#NO YOU CANNOT LEAVE EMPTY SOME OF THE PLACEHOLDER WHILE OTHERS ARE NAMED

#=========================================================================================
#Accessing arguments by position:
#EXAMPLE 2: NUMERICAL PLACEHOLDERS
#the followinh has number value as palceholder:  {provide a number as a placeholder}
print("")
var_string_fromat1 = "My name is {0} I'm {1} years old and i live in {2}"
print(var_string_fromat1.format("Jamal Nuh",29,"Somalia"))

#what about if the number placeholder started a specific value such as 1 or 2 instead of 0
var_string_fromat1 = "My name is {1} I'm {2} years old and i live in {3}"
#print(var_string_fromat1.format("Jamal Nuh",29,"Somalia"))
#this has trigered an error

#what about if some of the number placeholder not specific such as
var_string_fromat1 = "My name is {0} I'm {1} years old and i live in {}"
#print(var_string_fromat1.format("Jamal Nuh",29,"Somalia"))
#this has trigered an error also

#what about if some of the number placeholder specific has negative value such as -1,-2 etc
var_string_fromat1 = "My name is {-1} I'm {1} years old and i live in {}"
#print(var_string_fromat1.format("Jamal Nuh",29,"Somalia"))
#this has trigered an error also and using negative value has even changed the format correctness

#THIS IS WORKING EXAMPLE
#what about if i give the number placeholder in a inverse way, starting 3,2,1,0 etc
var_string_fromat1 = "My name is {2} I'm {1} years old and i live in {0}"
print(var_string_fromat1.format("Jamal Nuh",29,"Somalia"))
#this has worked but the values will not be ordered in the way they supposed to be

#CAN YOU PROVIDE ONE INDEX VALUE MULTIPLE TIMES AND MENTION TWO DIFFRENT PLACEHOLDERS
var_string_fromat1 = "My name is {0} I'm {0} years old and i live in {2}"
print(var_string_fromat1.format("Jamal Nuh",29,"Somalia"))
#this has worked but SOME VALUES ARE DUPLICATE

#CAN YOU PERFORM COMPUATTION INSIDE THE NUMBER PLACEHOLDERS
var_string_fromat1 = "My name is {int(9.0)} I'm {1} years old and i live in {0}"
#print(var_string_fromat1.format("Jamal Nuh",29,"Somalia"))
#this has not worked and you cannot perform compuattions inside the placeholders

#WHAT WILL HAPPEN IF YOU PROVIDE EXTRA VALUE IN THE FORMAT METHOD
var_string_fromat1 = "My name is {0} I'm {1} years old and i live in {2}"
print(var_string_fromat1.format("Jamal Nuh",29,"Somalia","Haya"))
#IT WORKS BUT THE PYTHON WILL IGNORE IT THE FINAL EXTRA VALUE


#=========================================================================================
#EXAMPLE 3: EMPTY PLACEHOLDERS
#the followinh has empty value as palceholder:  {provide a empty value as a placeholder}
print("")
var_string_fromat2  = "My name is {} and I'm {} years old"
print(var_string_fromat2.format("David",43))

#WHAT WILL HAPPEN IF YOU PROVIDE EXTRA VALUE IN THE FORMAT METHOD
var_string_fromat2  = "My name is {} and I'm {} years old"
print(var_string_fromat2.format("David",43,34,"JAMAL"))
#IT WORKS BUT THE PYTHON WILL IGNORE IT THE FINAL EXTRA VALUE



#------------------=======================----------------------=======================
"""
Formatting Types
Inside the placeholders you can add a formatting type to format the result:

:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format

"""

#+=======================================================================================
#:<		Left aligns the result (within the available space)
print("")

var_string_formating="My name is {:<6}i am"
print(var_string_formating.format("Jamal"))
#My name is Jamal i am
#the jamal consists 5 letter or size and 6-5=1
var_string_formating="My name is {:<7}i am"
print(var_string_formating.format("Jamal"))
#My name is Jamal  i am
#the jamal consists 5 letter or size and 7-5=2 whitespaces will left added


var_string_formating ="My name is {:<6}i am {:<6}years old"
print("")
print(var_string_formating.format("Jamal",29))
#My name is Jamal i am 29    years old
#the first value has 6-5=1, and the second value is calculated as 6-2=4 whitespaces will be added
var_string_formating ="My name is {:<8}i am {:<6}years old"
print(var_string_formating.format("Jamal",29))
#My name is Jamal   i am 29    years old
#the first value has 8-5=3, and the second value is calculated as 6-2=4 whitespaces will be added

#+=======================================================================================
#:>		Right aligns the result (within the available space)
print("")
print("")

var_string_formating="My name is {:>6} i am"
print(var_string_formating.format("Jamal"))
#My name is  Jamal i am
#the jamal consists 5 letter or size and 6-5=1 whitespaces at front of jamal
var_string_formating="My name is {:>7} i am"
print(var_string_formating.format("Jamal"))
#My name is   Jamal i am
##the jamal consists 5 letter or size and 7-5=2 whitespaces at front of jamal


#+=======================================================================================
#:^		Center aligns the result (within the available space)
print("")
print("")

var_string_formating="My name is {:^6} i am"
print(var_string_formating.format("Jamal"))
#My name is Jamal  i am
#the jamal consists 5 letter or size and 6-5=1, whitespaces at right side of jamal becouse only 1 was the remaining
var_string_formating="My name is {:^7} i am"
print(var_string_formating.format("Jamal"))
#My name is  Jamal  i am
##the jamal consists 5 letter or size and 7-5=2 one whitespaces at the left and one at the right of jamal. this is how it was centered
#always after the calculation e.g. 7-5=2 the result is further divided into sides 2/2=1 so one at each side 
# and if there is reminder the right side will take the priority

ar_string_formating="My name is {:^8} i am"
print(var_string_formating.format("Jamal"))
#My name is  Jamal  i am
#8-5=3, therefore each side 1 was added while the reminder of was ignored, i dontknow why

ar_string_formating="My name is {:^9} i am"
print(var_string_formating.format("Jamal"))
#My name is  Jamal  i am
#9-5=4, therefore each side 1 was again added 1 while the reminder 2 of was ignored, 
# i dontknow why. one reason can be if there is already spaces in both isdes such spaces will also be considered

#remove spaces from here
ar_string_formating="My name is{:^9}i am"
print(var_string_formating.format("Jamal"))
#My name is  Jamal  i am
#9-5=4, therefore each side 2 was again added 2, i think beriveous spaces are counted during the formatting 

#remove spaces from here and increase the n value
ar_string_formating="My name is {:^122}."
print(var_string_formating.format("Jamal"))
#My name is  Jamal  i am
#9-5=4, therefore each side 2 was again added 2, again confusion about the center alignment

#NOW TEST BY REPLACING THE PREVIOUS VARIABLES AND THE WAY IT WAS DONE
a="jama"
b="my name is {:^10}.".format(a)
print(b)
#my name is    jama   .
#10-4=6. 3 in each side was added

myNum = -1234
myStr = "Center Aligned Number with length 10 is: {:^10}.".format(myNum)
print(myStr)
#cited from https://www.scaler.com/topics/python/string-formatting-in-python/#:~:text=To%20left%2Dalign%20a%20string,n%E2%80%9D%20symbol%20inside%20the%20placeholder.
#Center Aligned Number with length 10 is:   -1234   .

#+=======================================================================================
#:=		Places the sign to the left most position
print("")
print("")
#Use "=" to place the minus sign at the left most position:
myLoan = "My loan is {:=8} us dollar."
print(myLoan.format(-5))
#My loan is -      5 us dollar.
#8-2=6 WILL BE INSERTED BEFORE 5 AND ALIGN THE MINUS SYMPOL AT LEFT POSITION


#Use "=" to place the plus sign at the left most position:
myLoan = "My loan is {:=8} us dollar."
print(myLoan.format(+5))
#My loan is        5 us dollar.
#the plus sign was ignored, thus the formula goes diffrent
#8-1=7 WILL BE INSERTED BEFORE 5 AND ALIGN THE MINUS SYMPOL AT LEFT POSITION


#INSTEAD YOU CAN ISERT THE PLUS SIGN AT THE PLACEHOLDER LIKE THIS
#Use "=" to place the plus sign at the left most position:
myLoan = "My loan is {:=+8} us dollar."
print(myLoan.format(5))
#My loan is +      5 us dollar.
#the plus sign was ignored, thus the formula goes diffrent
#8-2=6 WILL BE INSERTED BEFORE 5 AND ALIGN THE PLUS SYMPOL AT LEFT POSITION


#BUT YOU CAN ALSO PUT MINUS SIGN AT THE PLACEHOLDER BUT IT WILL IGNORE DURING THE DISPLAY LIKE THIS
myLoan = "My loan is {:=-8} us dollar."
print(myLoan.format(5))
#My loan is        5 us dollar.

#+=======================================================================================
#:+		Use a plus sign to indicate if the result is positive or 
print("")
print("")
#Use "+" to always indicate if the number is positive or negative:
income_range = "My income is between {:+} and {:+} in this year."
print(income_range.format(-49, 90))
#My income is between -49 and +90 in this year.

#WHAT WILL HAPPEN IF YOU PUT BOTH THE MINUS AND SIGN AT THE PLACEHOLHER LIKE THIS
income_range = "My income is between {:-} and {:+} in this year."
print(income_range.format(49, 90))
#My income is between 49 and +90 in this year.
#THE MINUS INSERTED AT THE PLACEHOLDER WAS IGNORED WHILE THE PLUS WAS ACCEPTED. 
# THE PLUS ALSO IGNORED IF INSERTED INSIDE THE FORMAT METHOD


#+=======================================================================================
print("")
print("")
#:-		Use a minus sign for negative values only
#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):
income_range = "My income is between {:-} and {:-} in this year."
print(income_range.format(-49, 90))
#THE VALUES IN THE FORMAT METHOD HAS NEGATIVE AND POSITIVE NUMBER RESPECTIVELY, 
# AS USAUL THE PLUS SIGN WILL WORK OR DIPLAYED IF USED IN THE PLACE HOLDER WHILE THE MINUS DOES NOT
# AS USAUL THE MINUS SIGN WILL WORK OR DIPLAYED IF USED IN THE FORMAT METHOD WHILE THE PLUS DOES NOT

income_range = "My income is between {:-} and {:+} in this year."
print(income_range.format(49, 90))

income_range = "My income is between {:-} and {:-} in this year."
print(income_range.format(-49, +90))

#+=======================================================================================
print("")
print("")

#CONTINOUE ANOTHER DAYS THE REMAINING PRACTICES: 
# WEBSITE: https://www.w3schools.com/python/ref_string_format.asp