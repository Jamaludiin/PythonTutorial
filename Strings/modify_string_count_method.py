"""
count()	            Returns the number of times a specified value occurs in a string or in a list or tuple etc.

for exampe  you want to know the number of times a specific value (can be int, float string etc) a peared in a string variable
or in alist etc.
lets say we want to know how many times the word "Python" apeared in a string variable 
if you use the count() method it returns such number of times such value appeared
"""

print("")
#EXAMPLE 1: CHECK NUMBER OF TIMES A SPECIFIC WORD APEARED IN STRING USING count() METHOD IN PYTHON
var_word_count = "I love writing Python code"
print("The word Python appeared ",var_word_count.count("Python")," times")

#EXAMPLE 1.1 COUNT THE NUMBER OF TIMES A SINGLE CHARECTER APEARED IN A STRING USING count() METHOD IN PYTHON
#WHAT ABOUT IF WANT TO CHECK A SINGLE CHARECTER ONLY
print("")
#Try counting the I in capital case how many times appeared
print("The word I appeared ",var_word_count.count("I")," times")
#Try counting the i in small case how many times appeared
print("The word i appeared ",var_word_count.count("i")," times")
#Note capital case and small case are diffrent since they have diffrent ASCI code

#EXAMPLE 2: CHECK NUMBER OF TIMES A SPECIFIC INT VALUE APEARED IN A LIST USING count() METHOD IN PYTHON
print("")
#can we use count method to count the number of times an item appears in a list
var_list_count=[1,2,3,4,44,55,44,33,44,33,2,2,8]
print("the item 44 appeared in the list ",var_list_count.count(44)," times")


"""
            ----------------------------------------------------------- 
                    Syntax
                    string.count(value, start, end)
            =========================================================== 

Parameters and their Values Explained 

Parameter	Description
value	Required. A String. The string to value to search for
start	Optional. An Integer. The position to start the search. Default is 0
end	Optional. An Integer. The position to end the search. Default is the end of the string

cite [w3schools.com]
"""

print("")
#EXAMPLE 3: COUNT THE NUMBER OF TIMES A SPECIFIED CHARECTER MENTIONED IN A STRING IN A SPECIFIED POSITIONS USING count() METHOD IN PYTHON
var_word_count1 = "My Passion is Python code writing"
#ony use the first two parameters of count() method by specifying the values to search and start postion to start the search
print("The charecter i is mentioned ",var_word_count1.count("i",7)," times after position 7")
#althought the end position is not specified, the default will be the end of the string, and the above example also written like this
print("The charecter i is mentioned ",var_word_count1.count("i",7,len(var_word_count1))," times after position 7")


#use all the parameters of count() method by specifying the values to search and start postion to start the search and end position
print("The charecter i is mentioned ",var_word_count1.count("i",7,15)," times after position 7 and before position 15")

#automate the last two parametrs using some operations
print("The charecter i is mentioned ",var_word_count1.count("i",int(len(var_word_count1)/3),int(len(var_word_count1)/2))," times after position ",int(len(var_word_count1)/3)," and before position ",int(len(var_word_count1)/2))
#use int method otherwise it will triger error after the division result becomes float

print("")
#USING NEGATIVE NUMBERS FOR THE START AND END PARAMETERS OF count() METHOD IN PYTHON

#if you use negtive intiger at the start postion means the counting will be started from the end of the string (or right to left)
#but the end position by default will be the end of the string
print("The charecter n is mentioned ",var_word_count1.count("n",-7)," times after position -7")
#this example can also be written like this if you want to specify the end position as the end of the string 
print("The charecter n is mentioned ",var_word_count1.count("n",-7,len(var_word_count1))," times after position -7 and before position ",len(var_word_count1))

print("")
#use negative number at the end position when using count() methos to search the number of times a word specified
print("The charecter n is mentioned ",var_word_count1.count("n",-7,-15)," times after position -7 and before position -15")
#the rsult of the above line will be 0 becouse the start is -7 the end is -15 which is less than -7, 
# this logic is reversing the string which will be extra functionality and it will not work

# becouse the value is like this  "My Passion is Python code writing", the start is -7 
# and it starts the 'w' at the word 'writing' while the end parameter suposed to be end of the string 
# in onther word the the end value must be greater than the start value always no mater whether is positive int or negative int

print("The charecter n is mentioned ",var_word_count1.count("n",-15,-7)," times after position -15 and before position -7")

print("")
#what about this example: take this as a quiz, note we have discussed such concept in above
print("The charecter n is mentioned ",var_word_count1.count("n",-15,2)," times after position -15 and before position 2")
print("The charecter n is mentioned ",var_word_count1.count("n",-15,15)," times after position -15 and before position 15")

#this is legal: answe why
print("")
print("The charecter n is mentioned ",var_word_count1.count("n",2,-7)," times after position -15 and before position -7")
