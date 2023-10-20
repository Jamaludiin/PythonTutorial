"""
Tuples   ----is used to store multiple items or elements in a single variable called tuple
Tuples   ----ORDERED-- means they have defined order and everytime you run you will se the same order 
                    unless you change the order
Tuples   ----UNCHANGABLE-- means the items in the tuple cannot be deleted, inserted or modified after the tuple is created
Tuples   ----ALLOW DUPPLICATE-- means similar itesm can be stored in the same tuple variable. becouse each will get 
                                unique index or can be diffrentiated with index values
"""

"""
                                    The syntax of Tuples
name_of_the_variable = (list items)-------- you use round brackets to create a tuple variable
"""

#EXAMPLE 1: CREATE A TUPLE VARIABLE AND STORE DIFFRENT ITEMS WITH DIFFRENT DATA TYPES IN PYTHON
var_tuple_items =(1,4,"Ali",22.5,True)
#it is legal to specify diffrent types of data inside one single tuple variable

#EXAMPLE 2: PRINT OR DISPLAY ALL THE ITEMS IN THE TUPLE VARIABLE
print("All the items in the tuple variable is :",var_tuple_items)

#EXAMPLE 3: INDEX TUPLE ITEMS IN PYTHON
index_one=var_tuple_items[0]
print("\nThe first item of the tuple is :", index_one)
#the tuple items can be indexed and the first index number starts 0 ---n, where n is the total length of the tuple minus one

#EXAMPLE 4: PRINT OR DISPLAY THE LAST ITEM OF THE TUPLE USING HIS INDEX
print("\nThe last item of the tuple is :",var_tuple_items[4])

#EXAMPLE 5: HOW TO KNOW THE LAST INDEX NUMBER OF A TUPLE
print("\nThe last index number of the tuple is :",len(var_tuple_items)-1)
#Hint the index number of the last item of the tuple can be found by subtracting the size or length of the tuple by one. 
# e.g the tuple size is 5 which means it has five items stored in the tuple, so 5-1 is 4

#EXAMPLE 6: THE len() METHOD IS USED TO KNOW THE LENGTH OF THE TUPLE OR THE NUMBER OF ITEMS STORED IN THE TUPLE
print("\nThe number of items stored in the tuple is :", len(var_tuple_items))

#EXAMPLE 7: STORE DUPLICATE ITEMS INSIDE A TUPLE VARIABLE
var_tuple_check_duplicate =("Alpha","Beta","Alpha","Beta","Zscore")
print("\nThis tuple has duplicate items : ",var_tuple_check_duplicate)

#EXAMPLE 8: STORE SINGLE ITEM INSIDE A TUPLE VARIABLE
var_tuple_single_item = (6)
print("\nThis tuple have been stored in a single item :",var_tuple_single_item)

#EXAMPLE 9: CHECK THE TYPE OF A TUPLE IN PYTHON
print("\nThis is a tuple or not a tuple :",type(var_tuple_check_duplicate))
#OUTPUT OF THE ABOVE IS TUPLE, SINCE IT HAS MULTIPLE ITEMS PYTHON CONSIDERS AS A TUPLE. PYTHON REFERS THE TUPLE AS AN OBJECT WITH A TUPLE DATA TYPE
print("\nThis is a tuple or not a tuple :",type(var_tuple_single_item))
#THE OUTPUT OF THIS IS int
#THIS IS NOT A TUPLE, ALTHOUGH IT HAS BEEN DECLARED USING THE SYNTAX OF A TUPLE, BUT HAVING ONLY ONE ITEM INSIDE 
# THE PYTHON WILL NOT CONSIDER AS A TUPLE

#EXAMPLE 10: CREATE A TUPLE VARIABLE WITH ONE VALUE IN PYTHON
#RULE IS TO ADD COMMA AFTER THE ITEM IS SPECIFED OTHERWISE PYTHON WILL NOT RECOGNIZE AS A TUPLE DATA TYPE
var_tuple_single_value=(3,)
print("\nThis is a tuple or not a tuple :",type(var_tuple_single_value))

#EXAMPLE 11: CREATE A TUPLE VARIAVLE WITHOUT ROUND BRACKETS OR PARENTHESES
var_tuple_no_pracket = 1,5,8,9
print("\nThe type of this variable is : ",type(var_tuple_no_pracket))

#EXAMPLE 11: REPEAT THE TUPLE ITEM MULTIPLE TIMES IN PYTHON
var_tuple_single_item_repeat =1,   #this is a single item tuple without using a round bracket
var_tuple_single_item_repeat=var_tuple_single_item_repeat*5
print("\nThe tuple items is repeated 5 times and is ",var_tuple_single_item_repeat)

#EXAMPLE 12: HOW TO CONCATENATE TUPLES USING AUGMENTED ASSIGNEMENTS SUCH AS (*=, +=):
#THIS IS ALSO CALLED ADDING A TUPLE VALUE TO ANOTHER TUPLE
var_tuple_single_item_repeat+=var_tuple_single_item_repeat
print("\nThe tuple items is concatinated by itself += and is ",var_tuple_single_item_repeat)

var_tuple_single_item_repeat*=2
print("\nThe tuple items is concatinated by itself using *= and is ",var_tuple_single_item_repeat)

# .      var_tuple_single_item_repeat+=2 .  this is error unless you put bracket to the right value
var_tuple_single_item_repeat+=(2,)
print("\nThe tuple items is concatinated by a new item and is ",var_tuple_single_item_repeat)