# so know lets explain the diffrence between extend() and append() method
"""if you use append() method to add value from one element to another element
the provider list will only provide all its element as one element including square brakets
so append it is better to use when you want to add a single item or element is an existing list items
and better not to use to add the values of one list variable to another list variable
becouse the append() does not iterate the items.

while the extend() method can be used when you want to add a items from one list variable to another list variable. it has iterate feature
means it can add several items to other list variable by incrementing index"""

# example OF append()
# better to use the append() method when you want to add a single item to the end of an existing list.
var_list_animals = ["Ali", "A"]
var_list_animals.append("new appended")
# output: ['Lion', 'Giraf', 'Tiger', 'Trees', 'Herbs', 'new appended']
print(var_list_animals)
# the alternative way of how append() method works is like this
var_list_animals[len(var_list_animals) :] = ["appned slice"]
# output: ['Lion', 'Giraf', 'Tiger', 'Trees', 'Herbs', 'new appended', 'appned slice']
print(var_list_animals)
# The alternative way to append the list of items is as follows:

# For loop that is going to append the value# REPEAT THIS
listone = [1, 2, 3, 4]
listtwo = [5, 6, 7, 8]
for i in listtwo:
    listone.append(i)
print(listone)

listone.extend(listtwo)
print(listone)
"""better not to use the append() method when you want to add a list items from one list variable to the end of an existing list variable. example:  
var_list_animals.append(var_list_plants)-----"""
