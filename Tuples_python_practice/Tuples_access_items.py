"""
                    ACCESTT TUPLE ITEMS USING DIFFRENT TECHNIQUES
"""
var_tuple_access=(2,3,5,"Apple",True,4.6)

#EXAMPLE 1: ACCESS TUPLE ITEMS USING THEIR INDEX NUMBER--POSITIVE INDEXING
#THE POSITIVE INDEXING IS USING WHOLE NUMBER DURING THE INDEXING SUCH AS 0,1,2,3 
#SYNTAX TO USE var_name [index number]. e.g. THE INDEX NUMBER OF THE FIRST ITEM IS [0], THE SECOND IS [1]...ETC
print("The tuple item in the third position is ",var_tuple_access[2])

#EXAMPLE 2: ACCESS TUPLE ITEM USING NEGATIVE INDEX NUMBER
#NOTE: USING NEGATIVE NUMBERS SUCH AS -1,-2 ETC IS LEGAL IN PYTHON DURING THE INDEXING A TUPLE ITEMS
# -1 MEANS YOU ARE INDEXING THE LAST ITEM IN THE TUPLE WHILE -2 AND -3 INDEX THE SECOND AND THIRD LAST ITEMS RESPECTIVELY
print("\nThe last item in the tuple is        :",var_tuple_access[-1])
print("\nThe second last item in the tuple is :",var_tuple_access[-2])
print("\nThe third last item in the tuple is  :",var_tuple_access[-3])

#EXAMPLE 3: ACCESS MULTIPLE ITEMS USING RANGE OF INDEX
#IT IS POSSIBLE TO DISPLAY MULTIPLE ITEMS FROM A TUPLE BY SPECIFYING A RANGE OF INDEX
#e.g. PRINT THE THE SECOND ITEM UPTO THE FIFTH ITEM AND SPECIFY THEIR RANGE OF INDEX
print("\nThe items ranging from the second to the fifth is ", var_tuple_access[1:5])
#ALTHOUGH THE 5 TH INDEX IS THE LAST INDEX, THE PYTHON IGNOR AND PRINT UNTILL THE 4 TH INDEX WHILE THE 1 ST INDEX INCLUDE THE RANGE
#Note: The search will start at index 2 (included) and end at index 5 (not included). [cite w3schools]

#                   DISCUSSING ABOUT HOW INDEX RANGING WORK IN PYTHON (SLICING)
"""
WHAT IF YOU DID NOT SPECIFY THE START INDEX AND ONLY PROVIDED THE LAST INDEX, THE START INDEX VALUE WILL BE 0 BY DEFAULT
SYNTAX: var_tuple_access[:index] IS ALSO SAME AS var_tuple_access[0:index].
AND IT WILL PRINT FROM THE FIRST ITEM UNTILL THE SPECIFIED ITEM
"""
print("\nStart from the first item to fourth item is : ",var_tuple_access[:5])#without start index specified
print("\nStart from the first item to fourth item is : ",var_tuple_access[0:5])#with start index specified as 0

"""
WHAT IF YOU DID NOT SPECIFY THE END INDEX AND ONLY PROVIDED THE START INDEX, THE END INDEX VALUE WILL BE THE LAST INDEX
OF YOUR LIST OR TUPLE 
SYNTAX: var_tuple_access[index:] IS ALSO SAME AS var_tuple_access[index:len(var_tuple_access)].
AND IT WILL PRINT STARING FROM THE SPECIFIED ITEM UNTILL THE LAST ITEM IN THE TUPLE OR LIST
"""
print("\nStart from the fourth item to fifth item (last) is : ",var_tuple_access[3:])#without end index specified
print("\nStart from the fourth item to fifth item (last) is : ",var_tuple_access[3:len(var_tuple_access)])#with end index specified as the last index
#NOTE: THE len(var_tuple_access) will return the number of items in the list which is 6, while there is no index 6. 
# the 6 will be excluded as usual since it is end index and it will be included the fifth one [ as they apply this formula [6-1=5]

"""
WHAT IF YOU DID NOT SPECIFY ANY OF THE INDEX RANGING VALUES, IT WILL BASICALLY RETURN A COPY OF THE ENTIRE ITEMS IN THE TUPLE
SYNTAX: var_tuple_access[:] IS ALSO SAME AS var_tuple_access[0:len(var_tuple_access)]
"""
print("\nStart from the first item to the last item is : ",var_tuple_access[:])#without end index specified
print("\nStart from the first item to the last item is : ",var_tuple_access[0:len(var_tuple_access)])#with end 

#
#EXAMPLE 4: ACCESS MULTIPLE ITEMS USING NEGATIVE RANGE OF INDEX -----SLICING WITH NEGATIVE BOUNDS IN PYTHON------
print("\nThe last items of the tuple to the last item !!! is : ",var_tuple_access[-1:])#IT START PRINTING FROM THE LAST ITEM WHEN GOES TO THE END ITEM IT WILL NOT SEE ANY FURTHER
print("\nThe last items of the tuple to the last item !!! is : ",var_tuple_access[-1:len(var_tuple_access)])#IT STARTS FROM THE LAST ITEM TO LAST ITEM AGAIN!!!
"""
the above two output is same which is like this
-------- The last items of the tuple to the last item !!! is :  (4.6,)-------
if you notice the returned value of 4.6 is concatinated comma (,) after it
this means we ask the tuple variable to return only the last value or item, therefore after returning one item the tuple
will not be a tuple and it is required multiple value to be stored, therefore comma is being added to show this is a tuple
"""

"""
WHAT IF YOU WANT TO START FROM LAST ITEM TO THIRD ITEM (FROM RIGHT TO LEFT)
"""
print("\nThe last items of the tuple to the third last is : ",var_tuple_access[-1:-4])
#THIS PRINTS EMPTY, BECOUSE IT SEEMS GOING FROM BIG VALUE TO SMALL VALUE, THIS MIGHT BE SIMILAR LIKE THIS
print("\nThe last items of the tuple to the third last is : ",var_tuple_access[5:1])
#INSTEAD DO LIKE THIS
print("\nThe last items of the tuple to the second last is : ",var_tuple_access[-4:-1])
#NOTE: THE END INDEX ALWAYS IS SUBTRACTED MINUS 1, BECOUSE IT WILL NOT INCLUDE THE DISPLAYING ITEM, 
# SO IF -1 SUBTRACTED 1 (-1-1)=-2 WHICH IS THE SECOND LAST ITEM INDEX AND IT WILL BE PRINTED ITS ITEM IN THE TUPLE
#This example returns the items from index -4 (included) to index -1 (excluded) [cite: w3schools]

"""
WHAT IF YOU DID NOT SPECIFY THE END INDEX VALUE AND ONLY SPECIFY THE START INDEX BUT AS NEGATIVE INDEX
"""
print("\nThe FOURTH last items of the tuple to the LAST ITEM is  : ",var_tuple_access[-4:])
print("\nThe FOURTH last items of the tuple to the LAST ITEM is  : ",var_tuple_access[-4:len(var_tuple_access)])
print("\nThe FOURTH last items of the tuple to the LAST ITEM is  : ",var_tuple_access[-4:len(var_tuple_access)])

#EXAMPLE 5: CHECK IF AN ITEM EXIST IN A TUPLE OR NOT IN PYTHON
#in keyword can be used during the looping and if statements. the following are both legal but not neccesary the second example
if 5 in var_tuple_access:
    print("\nYes the item 5 exist in the tuple")

for i in range(len(var_tuple_access)):
 if i==True:
    print("\nYes the item True exist in the tuple")




