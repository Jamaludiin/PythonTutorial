"""
Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

NOTE: As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
CITE:SOURCE W3SCHOOLS.COM
"""

var_dictionaries = {
                        "name": "Jamal",
                        "job": "Student",
                        "race": "Somali",
                        "age": 29
                   }
#the above has key names such as name, job, race etc and value, such as jamal, student etc
print(var_dictionaries)

#dictionary key without a name
var_dictionaries = {
                        "name": "Jamal",
                        "job": "Student",
                        "race": "Somali",
                        "age": 29,
                        "": 11569571
                   }

print("")
#you can print a single value by reffering its key. such as to print jamal you have to call the name key as follows
#after calling the variable you must use Square [] brackets
print(var_dictionaries["name"])

#call multiple keys 
#TODO: print(var_dictionaries["name"])

#DUPLICATES ARE NOT ALLOWED. BUT IT WILL NOT TRIGER AND ERROR INSTEAD IT WILL CONSIDER THE FINAL VALUE OF THE DUPLICATE 
# ELEMNTS AND OVERWRITE THE EXIRSITING ONE

var_dictionaries = {
                        "name": "Jamal",
                        "job": "Student",
                        "race": "Somali",
                        "age": 29,
                        "age": 38,
                        "": 11569571
                   }
print("")
print(var_dictionaries)

#IN DICTIONARY VARIABLE YOU CAN STORE ANY DATAT TYPES SUCH AS INT, STRING, BOLLEAN, LIST DATA ETC
var_dictionaries = {
                        "name": "Jamal",
                        "race": "Somali",
                        "weight": 78.80,
                        "student": True,
                        "age": 38,
                        "foodlist": ["Rice","Fish","Burger","Fried eggs"],
                        "carlist": {"Toyoto","Mercedes","BMW","Honda","Volvo"}
                   }

print("")
print(var_dictionaries)

#print the list values by calling its key in the dictionary
print("")
print(var_dictionaries["foodlist"])
print(var_dictionaries["carlist"])

