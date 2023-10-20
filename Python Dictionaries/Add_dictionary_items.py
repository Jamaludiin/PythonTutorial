"""
Adding an item to the dictionary is done by using a new index key and assigning a value to it:
source: w3schools.com
"""

var_dictionary = {
    "name":"Jamal",
    "age":38,
    "nationality": "Somali",
    "has_car": False
}

#before it has been added to a new item to the dictionary
print(var_dictionary)
print("")
#EXAMPLE 1: ADD A NEW ITEM IN A DICTIONARY, BOTH A KEY AND VALUE IN PYTHON
var_dictionary["job"] = "Student"
#after it has been added a new item to the dictionary
print(var_dictionary)


#EXAMPLE 2: CHANGE THE PREVIOUS AGE VALUE IN THE DICTIONARY IN PYTHON
var_dictionary["age"]=30 #the only diffrence is that this only adds new value and replaces the previous one in the age keys
#while the above statement insert new key and its value, becouse such does not existed before and it will be considered to create new one
print("")
print(var_dictionary)


#UPDATE METHOD IN PYTHON
#THIS METHOD ALO ADDS IF THE SPECIFIED ITESM DOES NOT EXIST BEFORE, 
# BUT IF HAS EXISTED THE NEW ADDED VALUE WILL BE CONSIDERED IF THEY ARE DIFFRENT FROM THE PREVIOUS ONE

"""
The update() method will update the dictionary with the items from a given argument. 
If the item does not exist, the item will be added.
The argument must be a dictionary, or an iterable object with key:value pairs.
"""
#EXAMPLE 3: add a new item (key and value) in the dictioanry 
#the syntax of update is litel bit diffrent from the previous methods used
var_dictionary.update({"laptop":"MacBook"})
print("")
print(var_dictionary)
#change the previous age number
var_dictionary.update({"age":40})
print("")
print(var_dictionary)

#what about inserting a list of values and access in one key
var_dictionary.update({"carsowned": {"Toyoto","Mercedes","BMW","Honda","Volvo"}})

#tyou can insert list inside another list {it will not work the way we think it will be. check at the next call}
var_dictionary.update({"carsowned": {"Toyoto","Mercedes","BMW","Honda","Volvo"},"VolvoTypes":{"Volvo1","Volvo2"}})

print("")
print(var_dictionary)

#call only the carsowned kist
print("")
print(var_dictionary["carsowned"])
#it only calls the carsowned values while the volvotypes was considered seperate list item

#what about inserting a single item to an existing list of values and access in one key
#we also learn here, if we update the carowned it will not effect the volvotypes key item
var_dictionary.update({"carsowned": "vos"})
print("")
print(var_dictionary)
#failed and it erases the previous list items ans insert the single new item