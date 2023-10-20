var_dict={
    "name": "Jamal",
    "age": 45,
    "city": "Mog",
    "color": "Blck",
    "origin": "Somali",
    "religion": "Islam",
    "colors":{"red","yellow","marron","green"}
}

#EXAMPLE 1: PRINT ALL KEY NAMES OF A PYTHON DICTIONARY USING FOR LOOP
#USING KEYS() METHOD
print("")
print("Key names using keys() method are:")
for i in var_dict.keys():
    print(i)

#USING ITEMS() METHOD
print("")
print("Key names using items() method are:")
for i in var_dict.items():
    print(i)

#ALTERNATIVE OF THE ABOVE WITHOUT USING ANY METHOD
print()
print("Key names without using any method are:")
for i in var_dict:
    print(i)


#EXAMPLE 2: PRINT ALL VALUES OF A PYTHON DICTIONARY USING FOR LOOP
print("")
print("Value items using values() method are:")
for i in var_dict.values():
    print(i)


#YOU CAN ALSO PRINT ALL THE VALUES IN THE DICTIONARY USING INDEXING
print("")
print("Value items using indexing technique")
for i in var_dict:
    print(var_dict[i])

#YOU CAN ALSO PRINT ALL THE VALUES IN THE DICTIONARY USING KEYS() METHOD
print("")
print("Value items using keys method and ndexing technique")
for i in var_dict.keys():
    print(var_dict[i])

#EXAMPLE 3. PRINT ALL KEYS AND VALUES IN THE DICTIONARY USING FOR LOOP
#YOU CAN ALSO PRINT ALL THE KEY NAMES AND VALUES IN THE DICTIONARY USING ITEMS() METHOD
print("")
print("Value items using items method and ndexing technique")
for i in var_dict.items():
    print(i)

#ALTERNATIVELY, YOU CAN ALSO PRINT ALL THE KEY NAMES AND VALUES IN THE DICTIONARY USING ITEMS() METHOD
print("")
print("Value items using items method and ndexing technique")
for i,j in var_dict.items():
    print(i,j)
#note: the above two practices, their result are some what diffrent, just check


#MORE PRACTICE: DO IF STATEMENT IN DICTIONARIES