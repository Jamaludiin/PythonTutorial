"""
INITIALLY WE SAID TUPLE ITEMS CANNOT BE CHANGED, REMOVED, OR ADDED. BUT THERE ARE SOME WAYS TO BREAK SUCH RULES BY 
FOLLOWING SOME CONVERTION RULES SUCH AS CONVERTING THE TUPLE TO LIST DURING THE MANIPULATION.

The following steps is all about using tuple variables then converting to a list, manipulate the list items 
and then convert back to a tuple
"""

#EXAMPLE 1: CREATE A TUPLE VARIABLE AND STORE MULTIPLE DIFFRENT ITEMS OR VALUES IN PYTHON
var_tuple_update=("C++","Java","Python",4.5,2.3,True,7)

#EXAMPLE 2: CHECK THE TYPE OF THE TUPLE VARIABLE IN PYTHON
print("\nThis is a TUPLE VARIABLE : ",type(var_tuple_update))

#EXAMPLE 3: CONVERT A TUPLE VARIABLE TO A LIST 
#we use list() method that is used to create a list object
#the following example what it will do is to store all the tuple items to a list variable
var_list=list(var_tuple_update)
print("\nThis is a TUPLE VARIABLE : ",type(var_tuple_update))
print("This is a LIST VARIABLE : ",type(var_list))

#EXAMPLE 4: CHANGE THE LAST ITEM OF THE TUPLE USING INDEX
#this is imposible, but we access the items using the list as we converted the tuple into list at example 3
var_list[len(var_list)-1]=8 #if you dont know the last index number you can subtract the leng of the variable to 1
#this is also writen like this... var_list[6]=8 
#print both the list variable value and tuple variable. note the tuple variable still not converted
print("\nThe tuple variable items not modified yet : ",var_tuple_update)
print("\nThe list variable items are modified      : ",var_list)
#converted the list items back to the tuple variable
var_tuple_update=tuple(var_list)
print("\nThe tuple variable items are modified now : ",var_tuple_update)

#EXAMPLE 5:ADD A NEW ITEM TO A TUPLE USING APPEND() METHOD
#similar to the previous step we need to convert the tuple variable and their items to a list variable 
# and then after adding a new item convert the list variable and its items back to a tuple
#since we already converted, we continou by directly using the append() method
var_list.append("Visual Basic")
var_tuple_update=tuple(var_list)
print("\nThe tuple variable was added a new item : ",var_tuple_update)

#LESSON LEARNED FROM EXAMPLE 4 N 5 
"""
WE LEARNED HOW TO ADD ALL THE TUPLE ITEMS TO A LIST VARIABLE 
WE ALSO LEARNED HOW TO ADD ALL THE LIST ITEMS TO TUPLE VARIABLE
NOTE: DIRECT CONVERTION IS NOT ALLOWED BUT WE USED TUPLE() METHOD AND LIST() METHOD TO ASSIT SURING THE CONVERTION PROCESS
LIST() METHOD ALLOWS YOU TO CONVERT A TUPLE OBJECT TO LIST OBJECT AND VISE VERSE TO THE TUPLE() METHOD. 
THESE METHODS NOT ONLY USED STRICLY FROM TUPLE TO LIST OR LIST TO A TUPLE BUT ALSO OTHER SEQUENCES.

WE ALSO LEARN THAT WHEN YOU CONVERT FROM A LIST TO A TUPLE MEANS YOU STORE THE VALUE FROM RIGHT TO THE LEFT VARIABLE
E.G.       VAR1_IS_TUPLE=TUPLE(VAR2_IS_LIST)   
THIS MEANS THE RIGHT VARIABLE ARE NOT CONVERTED DIRECTLY TO A TUPLE BUT HIS VALUE ARE CONVERTED TO A TUPLE AND THEN STORED
INTO A TUPLE VARIABLE. SAME GOES TO A LIST VARIABLE.

THE QUESTION IS CAN YOU COMBINE THE ITEMS OF TWO TUPLE VARIABLES INTO ONE TUPLE VARIABLE, THE ANSWER IS YES SINCE THEY
ARE COMPATIBLE AND THE ABOVE EXAMPLES SAYS IT ALL. AND THE FOLLOWING EXAMPLES WE PROVE THIS                            
"""
#EXAMPLE 6: COMBINE THE ITEMS FROM ONE TUPLE VARIABLE TO ANOTHER TUPLE VARIABLE
var_tuple_one=(1,2,3,4,5,7,6)
var_tuple_two=var_tuple_one
print("\nThe value of tuple one is : ",var_tuple_one)
print("\nThe value of tuple two is : ",var_tuple_two)

#EXAMPLE 7: COMBINE THE ITEMS OF TWO TUPLE VARIABLE TO ANOTHER TUPLE VARIABLE
var_tuple_three=("Cars","MotoBike","Trucks","Plane")
var_tuple_four=var_tuple_one+var_tuple_three
print("\nThe value of tuple one and two is stored in tuple four varaible : ",var_tuple_four)

#EXAMPLE 8: COMBINE THE ITEMS OF A TUPLE VARIABLE TO THE SAME TUPLE VARIABLE
#this cpoies the tuple items of variable one two times and then stores the same variable
#the means the previous value erases and recieved the items two variables combined
var_tuple_one=var_tuple_one+var_tuple_one
# this is also written like this   -----  var_tuple_one=+var_tuple_one -------
print("\nThe value of tuple one is stored in tuple one again : ",var_tuple_one)

#EXAMPLE 9: CREATE A TUPLE WITH ONE ITEM IN PYTHON
#TO CREATE A TUPLE WITH ONE ITEM AS A VALUE YOU HAVE TO AS FOLLOWS
var_tuple_with_one_item =("Banana",)
print("\nThis is a one value tuple and it has type of : ", type(var_tuple_with_one_item))
#you have to add comma (,) after the item specified otherwise 
# python will recognize it as string variable since it has string value
#Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple. [cite: w3schools]

#EXAMPLE 10: REMOVE AN ITEM FROM A TUPLE IN PYTHON
#as we know it is not allowed to remove an item from a tuple but what we do it is to convert the tuple items to a list
#so we can remove an item from a list and then convert back to the tuple
#to remove a specified item from a list we use a remove() method
print("\nBefore a tuple item was removed is : ",var_tuple_update)
var_list=list(var_tuple_update)
var_list.remove("Visual Basic")
var_tuple_update=tuple(var_list)
print("\nAfter a tuple item is removed using a remove method is : ",var_tuple_update)

#EXAMPLE 11: REMOVES AN ITEM FROM A TUPLE AT A SPECIFIED POSITION USING POP() METHOD IN PYTHON
#as we know it is not allowed to remove an item at a specified location from a tuple 
# but what we do it is to convert the tuple items to a list so we can remove an item from a list and then convert back to the tuple
#to remove a specified item at a specied location from a list we use a pop() method
var_list=list(var_tuple_update)
var_list.pop(len(var_tuple_update)-1)
var_tuple_update=tuple(var_list)
print("\nAfter a tuple item is removed using pop method is  :",var_tuple_update)

#EXAMPLE 12: INSERT AN ITEM INTO A TUPLE USING PYTHON
#since python tuple is unchangeable or immutable, it will be impossible to insert an item at specified location
#so we have to convert the tuple items to list and then insert the item to the list and convert back the list items 
# to a tuple as we didi previous examples
var_list=list(var_tuple_update)
var_list.insert(len(var_tuple_update),"Visual Studio")#insert item at the last index position
var_tuple_update=tuple(var_list)
print("\nAfter a tuple item is inserted  using insert method is  : ",var_tuple_update)

#EXAMPLE 13: ADD AN ITEM AT THE END OF A TUPLE USING APPEND METHOD IN PYTHON
var_list=list(var_tuple_update)
var_list.append(8)
var_tuple_update=tuple(var_list)
print("\nAfter a tuple item is added at the end using append method  is  : ",var_tuple_update)
#YOU CAN ALSO COMBINE A TUPLE ITEMS TO ANOTHER TUPLE ITEMS USING APPEND METHOD IN PYTHON
var_tuple_1=(1,2,3)
var_tuple_2=(4,5,6)
var_list_3=list(var_tuple_1)
var_list_3.append(list(var_tuple_2))
var_tuple_1=tuple(var_list_3)
print("\nThis is a list combined two tuple items ",var_list_3)
#YOU CAN ALSO COMBINE A TUPLE ITEMS TO ANOTHER TUPLE ITEMS USING APPEND METHOD IN PYTHON
var_tuple_4=("A","B","C")
var_tuple_5=("D","E","F")
var_tuple_4=var_tuple_4+var_tuple_5 #ALSO WRITTEN LIKE THIS ----  var_tuple_4+=var_tuple_5
print("\nThis is a two tuples combined without any method : ",var_tuple_4)

#EXAMPLE 14: CLEAR ALL ITEMS IN A TUPLE USING PYTHON
#we use clear method to clear all the items in a list, remeber we should convert the tuple into a list
var_list_4=list(var_tuple_4)
var_list_4.clear()
var_tuple_4=tuple(var_list_4)
print("\nAll the tuple items was cleared : ",var_tuple_4)

#EXAMPLE 15: DETELTE A TUBLE VARIABLE AND ITS ITEMS COMPLETELY
# IN THIS CASE WE USE THE del KEYWORD TO DELETE THE TUPLE 
del var_list_4
print("\nThe tuple variable was deleted completely : ",var_tuple_4)
