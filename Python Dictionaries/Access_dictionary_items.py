"""
You can access the items of a dictionary by referring to its key name, inside square brackets:
CITE:SOURCE W3SCHOOLS.COM
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

#print the weight value in the dictionary by reffering the weight key
print("My weight is : ",var_dictionaries["weight"], " KG")

#alternative option can be as follows
#retrieve the weight value in the disctionary and store in another variable
weight=var_dictionaries["weight"]
print("")
print("My weight is : ",weight, " KG")

#another alternative method is to use get method
print("")
print("My weight is : ",var_dictionaries.get("weight"), " KG")



#EXAMPLE 2: GET ALL THE KEYS IN THE DICTIONARY
#the key method will return all the key names in the dictionary
print("")
print("All the keys in the dictionary is : ",var_dictionaries.keys())

#print all the key names in a dictionary in one by one with a new line
print("")
for i in var_dictionaries.keys():
    print("     : ",i)
#using the loop and without loop, the result are slidely diffrent, see their output


print("")

#this also can do the same
for i in var_dictionaries:
       print("    : ",i)

print("")


#EXAMPLE 3: GET ALL VALUES IN THE DICTIONARY 
#The value method is used which returns the list of the values stored in the dictionary variable
print(var_dictionaries.values())

#print all the values in a dictionary in one by one with a new line
print("")
for i in var_dictionaries.values():
    print(i, "         : ")
#using the loop and without loop, the result are slidely diffrent, see their output

print("")

#can we print both keys and values using loop
print("can we print both keys and values using loop")
for i in var_dictionaries.keys():
    print(i,"  :  ", var_dictionaries[i])

print("")

#EXAMPLE 4: print all items in a dictionary  using the item method
print(var_dictionaries.items())

#print all items in a dictionary in one by one with a new line using the item method
print("")

for i in var_dictionaries.items():
       print(i)

print("")


#EXAMPLE 5: CHECK IF AN ITEM KEY IS EXIST IN THE DICTIONARY OR NOT
if "age" in var_dictionaries:
    print("the age key is found in the dictionary")
#this can also be wriiten like this
if "age" in var_dictionaries.keys():
    print("the age key is found in the dictionary")

print("")
#EXAMPLE 5: CHECK IF AN ITEM VALUE IS EXIST IN THE DICTIONARY OR NOT
if "Jamal" in var_dictionaries:
    print("the jamal value is found in the dictionary")

#although jamal name is exist in the dictionary and this will be FALSE and it will not be printed 
# becouse the values in the dictionary variable should be accessed through their keys but the way we stated checks 
# this as key item and there is not keys called jamal.

#what about if we find using the value method
if "Jamal" in var_dictionaries.values():
    print("the jamal value is found in the dictionary")
#this works becouse we check it while using the value method and it is iteratable
#what about if we find using the value method
if "Jamal" in var_dictionaries.items():
    print("the jamal value is found in the dictionary")
#this will not work also