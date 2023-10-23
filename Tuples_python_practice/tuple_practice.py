"""Tuple variable is used to store multiple items
although Python does not have arrays support instead it has four built-in data types that support collection which means
you can store multiple values. these include

List--------- it can be stored multiple values, the stored items are ordered (the way you set can be displayed), 
              they can also be ordered in the way you want, they can also changeable (delete, add, change) and finaly 
              acepts duplicates
Tuple-------- it can be stored multiple values, the stored items are ordered (the way you set can be displayed), 
              they can also be ordered in the way you want, they  unchangeable (cannot delete, add or change) and 
              finaly acepts duplicates
Set---------- TODO
Dictionary---TODO

"""

# How to declare a tuple variable and store value
var_tuple_num = (1, 2, 3, 4, 6, 5, 7, 88, 5)
# syntax of tuple: the items of the tuple they are wirten inside a round brackets varname = (item1,item2,...etc)
print(
    "The Tuple value is :", var_tuple_num
)  # output: The Tuple value is : (1, 2, 3, 4, 6, 5, 7, 88, 5)
# the above outcome shows that the tuple items are ordered, and they accept duplicate values

# The Following example i will show you that the tuple values can be indexed .e.g. the first item has [0] index etc
print(
    "this is the first value of a tuple : ", var_tuple_num[0]
)  # output: this is the first value of a tuple :  1

# How to display all the items in the tuple one by one by indexing
# this example will show you how to display the tuple items from left to right and print in new line after each loop

for i in range(0, len(var_tuple_num)):
    print("the item : ", i, "in the list is : ", var_tuple_num[i])

print("\n")

# Alternative two of the above loop is also like this
k = 1
for x in var_tuple_num:
    print("the item : ", k, "in the list is : ", x)
    k = k + 1


print("\n")

# TODO ---discuss thsi--
"""the in Keyword in Python:
is mainly used for two reason
Reason 1: to check if a particular value is present in a sequence such as list, tuple, string etc
Reason 2: to iterate the sequnce in the for loop or even the if statements when checking is such value is in the tuple etc
"""

print("the current x value of ", x, "is available in the tuple : ", x in var_tuple_num)

if 1 in var_tuple_num:
    print("1 is present in the tuple")

var_tuple_fruits = ("apple", "Orange", "Lime")

if "apple" in var_tuple_fruits:
    print("Yes apple is available")


# Can you store multiple value with diffrent dataypes in a tuple variable
# for example you want to store number, string, float all in one tuple variable
var_tuple_num = ("Ali", 22, 1.5, "Morocan")
# it is also legal to use both single or double quatation during the string specification
print("\nIt is legal to store multiple diffrent data types in a tuple")

print("\n")

# How to check the lengeth of the tuple in python
# we use the len() method to return the total items stored in our list
print("The total number of items stored in the tuple is :", len(var_tuple_num))

# What will happen if you store one value item in a tuple
# lets check the output
var_tuple_onevalue = "one value"
print("\nthe tuple is stored one value and it is : ", var_tuple_onevalue)

# lets check if such tuple is a ctually a tuple
print("\nIs this variable a tuple : ", type(var_tuple_onevalue))
# However, if you store a tuple only one value such variable will not recognized as a tuple but
# other data types depends on the stored value e.g. if the value is string it will string
# Note, according to Python concept, tuples are defined as objects with the data type 'tuple':

# How to declare a tuple using tuple constructor or tuple() method
var_tuple_constructor = tuple(
    ("Apple", "Sumsung", "Nokia", "Redmi")
)  # note the double round-brackets
print("\nThis is used tuple constructor and items is :", var_tuple_constructor)

# How to count the number of times a tuple item appears in the tuple.
# How many times an a tuple item is duplicated inside the tuple
# we use count() method to count the number of times an item appears in a tuple
var_tuple_count = (1, 2, 3, 44, 44, 55, 44, 3, 2, 1, 1, 2, 44, 55, 8)
print("the item 44 appears ", var_tuple_count.count(44), " times in the tuple")

# alternative of the above using long route
# How to count the number of times an item appeared in the list using for loop
loop_cout = 0
for i in range(0, len(var_tuple_count)):
    if var_tuple_count[i] == 44:
        loop_cout = loop_cout + 1
print("\nthe item 44 appears ", loop_cout, " times in the tuple")

# How to know the index number of a specified value in a tuple
print("\nthe index value of 8 is :", var_tuple_count.index(8))
# what about if we have duplicate items in a tuple and you want to find the index of them
# using only index() method will only return the index number of the first item of the duplicates
print("\nthe index value of 44 is :", var_tuple_count.index(44))
# you can also specify the position of the item you want for example i want to get the index number of the second 44
print("\nthe index value of 44 after the first 44 is :", var_tuple_count.index(44, 4))
# You can also find the index value of a tuple in a specified range
# example you want to find the index number of item 3 after the 3 thrd position till 9 th position
print(
    "\nthe index value of 3 after the 3 thrd position and before the  th position is is :",
    var_tuple_count.index(3, 3, 9),
)
# if the specified item does not occur or lie inside the range you specied an error will be thrown. e.g.
# the following code shows that to find a the index valu of item 3 in the range of after the third self to 6 th shelf and there is no 3 item in the range
"""
print("\nthe index value of 3 after the 3 thrd position and before the  th position is is :", var_tuple_count.index(3,3,6))
"""
print("\n")
# How to find the last index value of a duplicate item in a tuple in python
# this example you can print the last index number of a duplicate tuple item through iteration
# and it will stop the loop when reached the last item specified and store its index value in a variable
k = 0
for i in range(0, len(var_tuple_count)):
    if var_tuple_count[i] == 44:
        k = i
print("the index value of the last 44 is : ", k)

# find all the duplicate items of 44 and their index value
print("\n")
k = 1
for i in range(0, len(var_tuple_count)):
    if var_tuple_count[i] == 44:
        print("the index value of the ", k, "44 is : ", i)
        k = k + 1
# can we use append() method to add an item in an existing tuple
# although we define tuple cannot be changed after it has been created
"""
var_tuple_count.append("A")
this will give you an error saying:
AttributeError: 'tuple' object has no attribute 'append'
"""
# can we also use insert() method to insert a value in a specified position in the tuple
# similar to append() method python does not suuport to provide attribute insert to the tuple which means tuples are unchangeble
"""
var_tuple_count.insert(1,"White")
this will give you an error saying:
AttributeError: 'tuple' object has no attribute 'insert'
"""
# can we also remove an item in a specified position from a tuple using pop() method
# similar to append() method python does not support to provide attribute insert to the tuple which means tuples are unchangeble
"""
var_tuple_count.pop(1)
this will give you an error saying:
AttributeError: 'tuple' object has no attribute 'pop'
"""
# can we also remove an item from a tuple using remove() mthod
# remove method() deletes the specified item from a list...if they are duplicate the first one will be removed
# similar to the above mthods, tuple items cannot be removed or added once they are created
"""
var_tuple_count.remove(44)
this will give you an error saying:
AttributeError: 'tuple' object has no attribute 'remove'
"""

# how to reverse a tuple items using a method called reverse()
# the reverse() method reverses the order of the tuple
# although the reverse method is not adding or removing anything in the tuple
# the python will trigger an for using this method. becouse when the reverse happen the order of the items will be re-arranged
# and stored again to the variable which will appear as it is new values.
# Note this does not mean the tuple is not ordered or unindexible
"""
var_tuple_count.reverse()
print("after reversed all the items in tuple using reverse method is:  ",var_tuple_count)
this will give you an error saying:
AttributeError: 'tuple' object has no attribute 'reverse'
"""
# you can reverse a tuple using a slicing technique this is TODO list in the future

# or you can reverse a tuple items by converting to list an then reversing
list(var_tuple_count).reverse()
print(
    "\nthe type of the variable is a tuple :", type(var_tuple_count)
)  # the reverset items of the tuple is : (1, 2, 3, 44, 44, 55, 44, 3, 2, 1, 1, 2, 44, 55, 8)
print("\nthe reverset items of the tuple is :", var_tuple_count)
# the above result has failed to reverse as we, we should investigate later

# You cannot also sort the tuple items using sort() method

# but we can you this technique by converting the tuple into kist and then sort the items. BUT IT IS NOT WORKING
list(var_tuple_count).sort(reverse=False)
print(
    "\nthe type of the variable is a tuple :", type(var_tuple_count)
)  # the reverset items of the tuple is : (1, 2, 3, 44, 44, 55, 44, 3, 2, 1, 1, 2, 44, 55, 8)
print("\nthe sorted items of the tuple is :", var_tuple_count)
# the above result has failed to sort as we tried, we should investigate later
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.[CITE: W3SCHOOLS]
