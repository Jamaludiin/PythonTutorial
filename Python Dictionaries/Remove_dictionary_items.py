"""
in python there are several ways to remove a dictionary item(s)
for example removing one itme or multiple items or even the whole dictionary values
"""

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
for i in var_dictionaries:
  print("Before deleting it : ",i, " : ",var_dictionaries[i])

print("")

#EXAMPLE 1: DELETE DESIRED ITEM FROM A DICTIONARY USING POP METHOD IN PYTHON
#POP METHOD IN A PYTHON DICTIONARY
#pop() method delets the item that has the specified key name
var_dictionaries.pop("student")
for i in var_dictionaries:
  print("After deleting it : ",i, " : ",var_dictionaries[i])

print("")

#EXAMPLE 2: DELETE THE LAST ITEM INSERTED IN A DICTIONARY USING POPITEM METHOD IN PYTHON
var_dictionaries.popitem()
for i in var_dictionaries:
  print("After deleting the last item : ",i, " : ",var_dictionaries[i])

print("")

#EXAMPLE 3: DELETE DESIRED ITEM FROM A DICTIONARY USING DEL KEYWORD IN PYTHON
del var_dictionaries["race"]
for i in var_dictionaries:
  print("After deleting using del keyword : ",i, " : ",var_dictionaries[i])

print("")

#EXAMPLE 4: DELETE ALL ITEMS IN A DICTIONARY USING DEL KEYWORD IN PYTHON
del var_dictionaries #JUST DONT SPECIFY ANY ITEM KEY

#print("After deleting ALL using del keyword : ",var_dictionaries)
#THIS WILL TRIGER AN ERROR BECOUSE IT DOES NOT EXIST OR NOT DEFINED BECOUSE OF NO VALUES INSIDE. 
# IN VARIABLES ARE ONLY DEFINED WHEN THEY HAVE DEFINED WITH THEIR VALUE
print("")


#EXAMPLE 5: CLEAR ALL ITEMS IN A DICTIONARY USING CLEAR METHOD IN PYTHON
var_dictionaries = {
                        "name": "Jamal",
                        "race": "Somali",
                        "weight": 78.80,
                        "student": True,
                        "age": 38,
                        "foodlist": ["Rice","Fish","Burger","Fried eggs"],
                        "carlist": {"Toyoto","Mercedes","BMW","Honda","Volvo"}
                   }

var_dictionaries.clear()
print("This was cleared : ",var_dictionaries) 
#this will not triger an error similar to the del keyword



#EXAMPLE 6: DELETE DESIRED ITEMS (SPECIFYING MORE THAN ONE KEY NAME) FROM A DICTIONARY USING POP METHOD IN PYTHON
#POP METHOD IN A PYTHON DICTIONARY
#pop() method delets the item that has the specified key name

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
var_dictionaries.pop("name","race")
for i in var_dictionaries:
    print("After TRYING TO delete two items at the same time using pop method: ",i," : ",var_dictionaries[i])
#THIS ONLY DELETD THE FIRST ITEM SPECIFED AND HAS IGNORED THE SECOND ITEM "race" TO DELET

#delete a single value from a list in a dictionary 
#var_dictionaries.pop({"carlist":{"Volvo"}})
#it trigers an error saying : TypeError: unhashable type: 'dict'
print("")
for i in var_dictionaries:
    print("After TRYING TO delete a list items in the dictionary using pop method: ",i," : ",var_dictionaries[i])
#

#what about deleting a key name that does not exist in the dictionary
print("")
#var_dictionaries.pop("w")
#var_dictionaries.pop("")
#both will triger an error
