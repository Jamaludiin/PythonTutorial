var_dictionary = {
"a":"Jamal",
"b":"mmm",
"c":"Ali",
"d":"Hassan",
"e":"Ahmed",
"f":"Hussein",
"g":"Sadaq",
"h":"Mohamed",
"i":"Sade",
"j":"Khalid",
"k":"A.wahab"
}

#EXAMPLE 1: CHECK IF CERTAIN VALUES IS IN THE DICTIONARY OR NOT USING IF STATEMENT IN PYTHON
if "Jamal" in var_dictionary.values():
    print("Jamal was found in the dictionary")

#EXAMPLE 2: CHECK IF CERTAIN KEY NAME IS IN THE DICTIONARY OR NOT USING IF STATEMENT IN PYTHON
print()
if "a" in var_dictionary.keys():
    print("a key name was found in the dictionary")

#EXAMPLE 3: CHECK IF CERTAIN KEY NAME AND VALUE IS IN THE DICTIONARY USING IF STATEMENT IN PYTHON
print()
for i,j in var_dictionary.items():#j is item value and i is key name
  if j =="mmm" and i =="b":
    pass
    #print(i,j)
  else:
   print(i,j)


