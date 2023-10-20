"""
                    ACCESTT TUPLE ITEMS USING DIFFRENT BUILTIN METHODS
"""

#EXAMPLE 1: COUNT THE NUMBER OF TIMES AN ITEM MENTIONED IN A TUPLE USING A COUNT METHOD IN PYTHON
var_tuple_access=(1,2,2,3,4)
count=var_tuple_access.count(2)#you have to store into a second variable to the return count number
print("\nThe number of times an element 2 is specified is : ",count)

#alternative way of ucounting the number of times an item is mentioned in a tuple using for loop is 
# How to count the number of times an item appeared in the list using for loop
loop_cout=0
for i in range(len(var_tuple_access)):
    if var_tuple_access[i]==2:
      loop_cout+=1
print("\nThe item 2 appears ",loop_cout," times in the tuple")

#EXAMPLE 2: FINDING THE INDEX NUMBER OF A SPECIFIED TUPLE ITEM USING INDEX METHOD IN PYTHON
#How to know the index number of a specified value in a tuple
print("\nThe index value of ELEMENT 1 is : ", var_tuple_access.index(1))

#How to know the index number of a specified duplicate value in a tuple
print("\nThe index value of ELEMENT 2 is : ", var_tuple_access.index(2))
#since the element 2 is mentioned 2 times, the index() method only return the index number of the first mentioned elemet

#EXAMPLE 3: FIND THE INDEX NUMBERS OF ALL THE TUPLE ITEMS
for i in range(len(var_tuple_access)):
    print("\nThe index number of item: ", var_tuple_access[i]," is : ",i)

#the two methods used the tuple variable directly is the count and index methods

#use the assignment operator to copy a tuple value to another tuple variable
