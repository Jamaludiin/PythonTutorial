var_dictionary={
    "a":12,
    "b":123,
    "c":1234,
    "d":12345
}

#EXAMPLE 1: ASSIGN THE VALUES IN A DICTIONARY TO ANOTHER DICTIONARY 
# AND CHECK THIS IF IT WORKS OR NOT
var_dictionary2 = var_dictionary
print(var_dictionary2)
print(type(var_dictionary2))

print()
#EXAMPLE 2: COPY A DICTIONARY VALUES TO ANOTHER DICTIONARY USING COPY() METHOD IN PYTHON
var_dictionary3=var_dictionary.copy()
print(var_dictionary3)
print(type(var_dictionary3))


print()
#EXAMPLE 3: ALTERNATIVE WAY OF COPYING A DICTIONARY VALUES TO ANOTHER DICTIONARY USING BUILT-IN FUNCTION CALLED dict() METHOD IN PYTHON
var_dictionary4=dict(var_dictionary)
print(var_dictionary4)
print(type(var_dictionary4))
