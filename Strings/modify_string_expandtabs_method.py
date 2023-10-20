"""
expandtabs()	    Sets the tab size of the string

The expandtabs() method sets the tab size to the specified number of whitespaces.
cite:w3shools.com

MYOWN
the expandtabs() is used to set a tap size in a given string,
The expandtabs() is used to set the desired tapsize or the number of whitespaces in a given string at a specified positions.
Initially, you can specify the positions to be inserted the whitespaces using tap charecter '\t'
By default, using the tap charecter '\t' it will automatically insert a tapsize of 8.
Therefore, the expandtabs() method is used to specify your desired tapsize instead of using the default tapsize 

"""
#EXAMPLE 1: INSERT A TAP SPACE IN STRING USING \t TAP CHARECTERS IN PYTHON
var_string_tabs = "\tMy name is Jamal Nuh"
print(var_string_tabs)
#        My name is Jamal Nuh
"""
The tap charecter of \t used in the above string inserted 8 whitespaces in front of the string.
as shown in the output.
The tap charecter or the expandtabs() method both keep track the cursor position, 
for example the bove tap charecter \t used is at the front which means the count will start from index 0 untill 7 (which is 8 in total)

Imagine, you specify anothor tap charecter \t some were in the string. as shwon at the following example.

NOTE: the counting is based on sets, each set has 8 charecters or white spaces or both. for example you have
a text that consisits of 20 charecters including white spaces like this "My name is Jamal Nuh"
this string has 2 sets and 4 charecter. lets say every 8 sequenced charecters is a complete set.
and when you count the above example you will found it 8+8+4 =20 (including whitespaces). 
having this concept in mind, whenever the \t charecter found, the python should be dealt with the set they occur.

first \t was found at the first set, especially at the first position which is 0, 
thus the 8 white spaces that supposed to be inserted in front of the main text will be decided using the following formula
8 (the tap size, now is 8 by default since we did not specify any value) minus the \t charecter psoition in the set which 0
= 8-0 =8, therefore 8 white spaces should be inserted.
"""

var_string_tabs = "\tMy name is \tJamal Nuh"
print(var_string_tabs)
#        My name is      Jamal Nuh
#the first tap charecter has inserted 8 whitespace at front of the main text becouse the initial position found the tap charecter was position 0.
#and applying the formula 8-0 is 8 as shown at the above.
#while the second tap charecter specified at set two (the second eight charecter groups) especially after 3 positions
# thus, lets apply the formula 8-3=5, the number of white spaces to beinserted is 5 in the second set, especially the place specified the tap charecter

print("")

#WHAT ABOUT IF TWO tap charecters \t was found in the second set
var_string_tabs_2 = "\tMy name is \tJama\tl Nuh"
print(var_string_tabs_2)
#        My name is      Jama    l Nuh
print(len(var_string_tabs_2))
#the lenth of the string is 23 becouse when the len method counting the lengeth of the string will not count 
# the whitespaces they are puting becouse, the tap charecter will not return anyvalue to this method, 
#while in python this tap charecter is considered one charecter each although it consists two charecters which \ and t
var_tapcharecter ="\t\t\t"
print(len(var_tapcharecter))
print("")
#the first set is inserted 8 whitespace at front
#while the second set has two tap charecters after position 3 and after position 7, 
# it is true the first charecter lies before position 3, and it will add 5 whitespaces 
# by applying the previous formula, the first tap charecter is 8-3 = 5, therefore five whitespaces are inserted 

# BUT the count postions in set two will be changed at this time especially for the second tap charecter.
# therefore, the new count in set two will start after the first tap charecter in set two, start 'jama' utill 
# the second tap charecter, thus 8-4 = 4 , four whitespaces will be added.
#


#EXAMPLE 2: MAKE  WHITESPACE IN STRING USING expandtabs() METHOD IN PYTHON

#to make tabs work you have to add the \t syntax inside the place you want to insert white spaces
var_string_tabs = "My name is \tJamal \tNuh"
#\t normally provides whitespace with 8 tapsize by default (maximum) but you can reduce or expand the default whitespace made by the \t
#the formula: the first set does not have any tap charecter. 
# the second tap charecter is in the second set and starts after psoition 3, thus 8-3=5 (5 whitespaces will be added)
#the second tap charcter is also at the second set, though two tap charecters mention. 
# the second tap charecter counting will start after the first tap charecter in set two, which is 8-6=2 whitespaces will be added
print(var_string_tabs)
#My name is      Jamal   Nuh
print("The expandtabs is used fron now")

print(var_string_tabs.expandtabs())
#the above two lines display same result and the default parameter of tapsize is 8
"""
                    ----------------------------------------------------------
                      Syntax
                      string.expandtabs(tabsize)
                    ==========================================================

Parameter Values
Parameter	Description
tabsize	Optional. A number specifying the tabsize. Default tabsize is 8
"""
#EXAMPLE 3: REDUCE OR INCREASE THE AMOUNT OF WHITESPACE IN STRING USING expandtabs() METHOD IN PYTHON
print("")
#provide the optional parameter to make the default whitespace to appear smaller or reduced
var_string_tabs = "My name is \tJamal \tNuh"
print("bellow output has 1 tapsize")
print(var_string_tabs.expandtabs(1))
#My name is  Jamal  Nuh
print("")

#EXAMPLE 3: CAN NEGATIVE NUMBERS AND ZERO BE INSERTED IN THE expandtabs() method TO REDUCE THE AMOUNT OF WHITESPACE IN STRING IN PYTHON

var_string_tabs1 ="My name is Jamal Nuh"
print("bellow output has not tapsize and no tap charecter was specified at the text")
print(var_string_tabs1)
var_string_tabs1 ="My name is \tJamal Nuh"
print("")
print("bellow output has no tapsize")
print(var_string_tabs1.expandtabs())
#My name is      Jamal Nuh
#Note: the negative numbers and zero will disable the functionality of the \t tap charecters 
# as shown in the following example
print("")
print("bellow output has negative and zero tapsize")
print(var_string_tabs1.expandtabs(-6))
print(var_string_tabs1.expandtabs(0))

#what about if you use floating number in the parameter
print("")
print("bellow output has floating number  tapsize")
#print(var_string_tabs1.expandtabs(2.4))
#this has triggered an error: TypeError: 'float' object cannot be interpreted as an integer


#you can specify the parameter of expandtabs method through calculation or you pass integer value from a variable
print("")
var_string_tabs1 ="My name is \tJamal Nuh"
print("tapsize of the following output has been decoded through calculation ")
print(var_string_tabs1.expandtabs(int(len(var_string_tabs)/3)))
#My name is    Jamal Nuh
#the formula applied the above example is this: the tapsize passed is 7, the \t was specified after position 3 in the second set
#thus 7-3=4, 4 whitespaces should be inserted. BUT THIS DOES NOT SEEM IT. INVESTIGATE AGAIN
"""
KNOW WE KNOW NEW CONCEPT: BEFORE THE SETS WERE CONSIST 8, NOW THE SETS CONSIST 7, SO THE SBOVE EXAMPLE IS TRUE
BECOUSETHE SECOND SET STARTS ' is \tJama' WHICH MEANS THE \t WAS MENTION BEFORE PSOITION 4
SO 7-4=3, THEREFORE 3 WHITESPACES SHOULD BE INSERTED
"""

#TRY THIS EXAMPLE AGAIN
var_string_tabs1 ="My name is \tJamal \tNuh"
print("tapsize of the following output has been decoded through calculation ")
print(var_string_tabs1.expandtabs(7))
"""
this will be 7-6=1
My name is    Jamal  Nuh
although the second tapsize is not in the second set
but the counting of the second \t will start after the previous \t which is "jamal "
"""
print(int(len(var_string_tabs)/3))

#see this again
print("")
print("see this again")
var_string_tabs1 ="My name is \tJamal Nuh"
print(var_string_tabs1.expandtabs(7))
#7-3=4     THIS IS SEEMS also 7 set based as discussed above
#My name is    Jamal Nuh

#see this again
print("")
print("see this again")
var_string_tabs1 ="My \tname is Jamal Nuh"
print(var_string_tabs1.expandtabs(int(len(var_string_tabs)/3)))
#7-3=4     THIS IS SEEMS GOOD
#My     name is Jamal Nuh




#see this example as well
var_string_tabs1 ="\tMy name is Jamal Nuh"
print("tapsize of the following output has been decoded through calculation ")
print(var_string_tabs1.expandtabs(int(len(var_string_tabs)/3)))
#       My name is Jamal Nuh
print(int(len(var_string_tabs)/3))


print("")
#what happen if the tapsize equal to the position specified the tapsize like this
var_string_tabs1 ="My \tname is Jamal Nuh"
print("tapsize of the following output has been same to postion specified ")
print(var_string_tabs1.expandtabs(3))
#My    name is Jamal Nuh
#3-3=0, thus it will go back to the default which is 3 as mentioned 
# or we can say the first tapcharceter was specified after position three, note the sets are made in 3 pair
#therefore it starts at first set in psoition 0, therefore 3-0=3

#see this example as well
#what happen if the tapsize is 2
var_string_tabs1 ="My \tname is Jamal Nuh"
print("tapsize of the following output has 2 value of tapsize ")
print(var_string_tabs1.expandtabs(2))
#My  name is Jamal Nuh
#2-3=-1, convert to 1, thus it will insert 1 whitespace
#or we can say the sets are made in pairs (2 charecters in each set), thus, 
# the first tap charecter is mentioned at second set after the first position, therefore 2-1=1, is also same the previous formula

#see this example as well
#what happen if the tapsize is more than 10, 
# the grouping will be done in 12 pairs
var_string_tabs1 ="My \tname is Jamal Nuh"
print("")
print("bellow output has 12 tapsize")
print(var_string_tabs1.expandtabs(12))
#My          name is Jamal Nuh
#12-3=9, thus it will insert 9 whitespace

#see this example as well
#what happen if the tapsize is more than the lenght of the string
# the grouping will be done in 12 pairs
var_string_tabs1 ="My \tname is Jamal Nuh"
print(len(var_string_tabs1))
print("")
print("bellow output has more than the lenghth of the string 22 tapsize")
print(var_string_tabs1.expandtabs(22))
#My                    name is Jamal Nuh
#22-3=19, thus it will insert 19 whitespace

