"""
Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.
cite: w3schools.com

python has number of built-in methods that can be used on dictionaries. 
these methods are used to perform various number of operations, including copying the dictionary items to another and many more

"""
var_dic ={
    "name":"Jamaal",
    "age":28,
    "degree":"PhD"
}

#==========================================================================================================
#EXAMPLE 1: COPY A DICTIONARY VALUE AND STORE IT INTO ANOTHER VARIABLE USING COPY() METHOD IN PYTHON

var_dict2=var_dic.copy()
print(var_dict2)
"""
#the DEFINTION AND USAGE OF COPY() METHOD 
This method return a copy of the specified dectionary and you can further store it into another variable

Synatx: name_of_the_dictionary.copy()
Parameters required: no parameter value is required to use this method
"""
#==========================================================================================================
#EXAMPLE 2: Create a dictionary that has four keys, and assign a same value

x=("key_name1","key_name2","key_name3","key_name4")
y="Jamal"

var_dic3=dict.fromkeys(x,y)
print()
print(var_dic3)

"""
#fromkeys()	Returns a dictionary with the specified keys and value

Definition and Usage
The fromkeys() method returns a dictionary with the specified keys and the specified value.

Syntax
dict.fromkeys(keys, value)
Parameter Values
Parameter	Description
keys	Required. An iterable specifying the keys of the new dictionary
value	Optional. The value for all keys. Default value is None

CITE: W3SCHOOLS
"""

#EXAMPLE 2.1 : Create a dictionary that has four keys, and do not assign value
x=("key_name1","key_name2","key_name3","key_name4")

var_dic3=dict.fromkeys(x)
print()
print(var_dic3)

#EXAMPLE 2.2 : Create a dictionary that has four keys, and assign same and multiple values in each key
x=("key_name1","key_name2","key_name3","key_name4")
y=("Jamal","Nuh","Ali","PhD") #it will provide each set to each key_name
#y=["Jamal","Nuh","Ali","PhD"]
y="Jamal","Nuh","Ali","PhD"
#y="Jamal","Nuh","Ali","PhD"

var_dic3=dict.fromkeys(x,y)
print()
print(var_dic3)

#EXAMPLE 2.3 : Create a dictionary that has four keys, and assign diffrent values in each key
#TODO

#==========================================================================================================
#EXAMPLE 3 : DISPLAY THE DICTIONARY VALUE USING SPECIFIED KEY NAME USING GET() METHOD IN PYTHON
#get()	Returns the value of the specified key
print()
print(var_dic.get("name"))

"""
Definition and Usage
The get() method returns the value of the item with the specified key.

Syntax
dictionary.get(keyname, value)
Parameter Values
Parameter	Description
keyname	Required. The keyname of the item you want to return the value from
value	Optional. A value to return if the specified key does not exist.
Default value None

CITE: W3SCHOOLS
"""

#YOU CAN EVEN SPECIFY A KEY NAME THATS WAS NOT SPECIFIED AT THE DICTIONARY AND ALSO 
# YOU CAN SPECIFY THE VALUE YOU WANT TO BE RETURNED
print()
print(var_dic.get("year"))#it will return none
print(var_dic.get("year",2023))#it will return 2023

#==========================================================================================================

#EXAMPLE 4 : Display all the key name and values in a dictionary in pairs using items() method
#items()	Returns a list containing a tuple for each key value pair
print()
print(var_dic.items())
"""
Definition and Usage
The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.

The view object will reflect any changes done to the dictionary, see example below.

Syntax
dictionary.items()
Parameter Values
No parameters
"""

#display all the key names and values in a dictionary pair by pair
for i in var_dic.items():
    print(i)
#==========================================================================================================

#EXAMPLE 5 : RETURN ALL THE KEY NAMES IN A DCITIONARY USING KEYS() METHOD IN PYTHON
#keys()	Returns a list containing the dictionary's keys
print()
print(var_dic.keys())

#display all the key names of a dictionary one by one
print()
for i in var_dic:
    print(i)

"""
Definition and Usage
The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.

The view object will reflect any changes done to the dictionary, see example below.

Syntax
dictionary.keys()
Parameter Values
No parameters
"""
#==========================================================================================================
#EXAMPLE 6 : DISPLAY ALL THE VALUES IN A DICTIONARY USING VALUES() METHOD IN PYTHON
#values()	Returns a list of all the values in the dictionary
print()
print(var_dic.values())

#display all the values in a dictionary one by one
print()
for i in var_dic.values():
    print(i)

"""
Definition and Usage
The values() method returns a view object. The view object contains the values of the dictionary, as a list.

The view object will reflect any changes done to the dictionary, see example below.

Syntax
dictionary.values()
Parameter Values
No parameters
"""
#==========================================================================================================

#pop()	Removes the element with the specified key