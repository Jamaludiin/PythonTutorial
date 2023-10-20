"""
TO MODIFY A STRING PYTHON PROVIDES A SEVERAL BUILT IN FUNCTIONS THAT CAN PERFORM SUCH WORK


upper()         The upper() method returns the string in upper case:
lower()         The lower() method returns the string in lower case:
strip()         The method removes any whitespace from the beginning or the end:
eplace()        The replace() method replaces a string with another string:
split()         The split() method splits the string into substrings if it finds instances of the separator:

THE REMAINING ARE ALL THE BUILT-IN METHODS PYTHON HAS

CITE:W3SCHOOLS

Method	            Description
capitalize()	    Converts the first character to upper case
casefold()	        Converts string into lower case
center()	        Returns a centered string
count()	            Returns the number of times a specified value occurs in a string
encode()	        Returns an encoded version of the string
endswith()	        Returns true if the string ends with the specified value
expandtabs()	    Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()	        Formats specified values in a string
format_map()	    Formats specified values in a string
index()	            Searches the string for a specified value and returns the position of where it was found
isalnum()	        Returns True if all characters in the string are alphanumeric
isalpha()	        Returns True if all characters in the string are in the alphabet
isascii()	        Returns True if all characters in the string are ascii characters
isdecimal()	        Returns True if all characters in the string are decimals
isdigit()	        Returns True if all characters in the string are digits
isidentifier()	    Returns True if the string is an identifier
islower()	        Returns True if all characters in the string are lower case
isnumeric()	        Returns True if all characters in the string are numeric
isprintable()	    Returns True if all characters in the string are printable
isspace()	        Returns True if all characters in the string are whitespaces
istitle()	        Returns True if the string follows the rules of a title
isupper()	        Returns True if all characters in the string are upper case
join()	            Converts the elements of an iterable into a string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()	        Returns a left trim version of the string
maketrans()	        Returns a translation table to be used in translations
partition()	        Returns a tuple where the string is parted into three parts
replace()	        Returns a string where a specified value is replaced with a specified value
rfind()	            Searches the string for a specified value and returns the last position of where it was found
rindex()	        Searches the string for a specified value and returns the last position of where it was found
rjust()	            Returns a right justified version of the string
rpartition()	    Returns a tuple where the string is parted into three parts
rsplit()	        Splits the string at the specified separator, and returns a list
rstrip()	        Returns a right trim version of the string
split()	            Splits the string at the specified separator, and returns a list
splitlines()	    Splits the string at line breaks and returns a list
startswith()	    Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()	        Swaps cases, lower case becomes upper case and vice versa
title()	            Converts the first character of each word to upper case
translate()	        Returns a translated string
upper()	            Converts a string into upper case
zfill()	            Fills the string with a specified number of 0 values at the beginning
"""

#+++++++++++++++++  FORMATTING BASED METHODS FOR STRING +++++++++++++++++


#EXAMPLE 1: CAPITALIZE THE FIRST CHARECTER OF THE SECNTENCE ONLY USING capitalize() METHOD IN PYTHON
# capitalize()	    Converts the first character to upper case
#this method return a string with the first charecter converted into a upper case while the rest remain in lower case
#NOTE: if all were capital, this method converts all small except the firt charecter which will be in uppercase
# The capitalize() method returns a string where the first character is upper case, and the rest is lower case.

var_string = 'my name is jamal nuh'
print("")
print("The capilized firt charecter is :",var_string.capitalize())

#try with an example were all the string is capital and see what will happen
var_sring_all_capital ="JAMAL NUH"
print("The capilized firt charecter and the rest is small is :",var_sring_all_capital.capitalize())
#all the charecters are converted into lower case except the first charecter

#WHAT ABOUT IF THE FIRST CHARECTER IS A NUMBER CAN IT BE CONVERTED INTO CAPITAL
#note: you can use the capitalize() method at the same time you intialize the string variable
var_sring_all_capital ="12 JAMAL NUH".capitalize()
print("The capilized firt charecter is number and the rest remain small as :",var_sring_all_capital)

#NOTE: --------THE capitalize() HAS NO PARAMETER-------

print("")


#EXAMPLE 2: CONVERT UPERCASE OR CAPITALIZE ALL CHARECTERS OF THE SENTENCE USING upper() METHOD IN PYTHON
#upper()         The upper() method returns the string in upper case:
print("All are capitalized and is :",var_string.upper())

#NOTE: --------THE upper() HAS NO PARAMETER-------
print("")

#EXAMPLE 3: CHECK IF THE STRINGS CHARECTERS ARE IN UPERCASE FORMAT USING isupper() METHOD IN PYTHON
#isupper()	Returns True if all characters in the string are upper case
print("When checked if all the string charecters is upper case : ", var_string.isupper())
var_sring_all_capital ="JAMAL NUH".isupper()
# var_sring_all_capital ="JAMAL NUH".isupper ---this does not make error without () but why this output:  <built-in method isupper of str object at 0x101c09270>
print("When checked if all the string charecters is upper case : ", var_sring_all_capital)
#NOTE: --------THE isupper() HAS NO PARAMETER-------
print("")

#EXAMPLE 3.1 CHECK IF A FIRST AND SECOND NAME START AN UPPER CASE IN PYTHON
var_first_name = "Jamal"
var_second_name = "Nuh"
if var_first_name.isupper() and var_second_name.isupper():
    print("Both first and second name satarts with a capital letter : ",var_first_name.isupper() and var_second_name.isupper())
else:
    print("Both first and second name did not satarts with a capital letter : ",var_first_name.isupper() and var_second_name.isupper())

print("")

#EXAMPLE 4: CONVERT THE STRING CHARECTERS INTO LOWER CASE USING lower() METHOD IN PYTHON
#lower()	Converts a string into lower case
var_string_lower1 = "JAMAL A. NUH"
var_string_lower2 = "Jamal A. nuh"
var_string_lower3 = "jama A. nUH"

print("The string is converted into lower case is  :  ",var_string_lower1.lower())
print("The string is converted into lower case is  :  ",var_string_lower2.lower())
print("The string is converted into lower case is  :  ",var_string_lower3.lower())

#NOTE: --------THE lower() HAS NO PARAMETER-------
print("")

#EXAMPLE 5: CONVERT IF THE STRINGS CHARECTERS ARE IN lower case FORMAT USING casefold() METHOD IN PYTHON
var_string_casefold1 ="jamal nuh ali"
var_string_casefold2 ="Jamal Nuh Ali"
var_string_casefold3 ="jamAl NUH aLI"


#casefold()	Converts string into lower case
print("The string is converted into lower case is  :  ",var_string_casefold1.lower())
print("The string is converted into lower case is  :  ",var_string_casefold2.lower())
print("The string is converted into lower case is  :  ",var_string_casefold3.lower())


print("")

# lower() vs casefold(): both do the same job of converting strings into lower case 
# they say casefold() method is aggressive , means casefold() converts more charecters into lower case 
# compared the lower() method which does not convert some words into small letter 
var_casefold_vs_lower = "Straße" #german word of street or road

# convert the string to lowercase using casefold() method
print("CONVERT THE STRING TO LOER CASE USING  casefold() : ", var_casefold_vs_lower.casefold()) 

# convert the string to lowercase using lower() method
print("CONVERT THE STRING TO LOER CASE USING lower() : ", var_casefold_vs_lower.lower())


print("")

#EXAMPLE 6: CHECK IF THE STRINGS CHARECTERS ARE IN lower case FORMAT USING islower() METHOD IN PYTHON
var_string_islower1 ="jamal nuh ali"
var_string_islower2 ="jamAl nuh ali"
var_string_islower3 ="jamAl NUH aLI"


print("When checked if all the string charecters is lower case : ", var_string_islower1.islower())
print("When checked if all the string charecters is lower case : ", var_string_islower2.islower())
print("When checked if all the string charecters is lower case : ", var_string_islower3.islower())

#NOTE: --------THE islower() HAS NO PARAMETER-------
print("")


#EXAMPLE 6.1 CHECK IF A FIRST AND SECOND NAME IS LOWER CASE
#isupper()	        Returns True if all characters in the string are upper case
#islower()	        Returns True if all characters in the string are lower case

var_first_name = "JAMAL"
var_second_name = "NUH"
if not (var_first_name.islower() and not var_second_name.islower()):
    print("Both first and second name are in a capital form : ")
else:
    print("Both first and second name are in a lowecase form")

print("")
#also try like this
if not(var_first_name.isupper() and var_second_name.isupper()):
    print("Both first and second name are in a capital form : ")
else:
    print("Both first and second name are in a lowecase form")

#also try like this to check the display of such boolean value
print(not(var_first_name.isupper() and var_second_name.isupper()))
print(var_first_name.isupper() and var_second_name.isupper())

