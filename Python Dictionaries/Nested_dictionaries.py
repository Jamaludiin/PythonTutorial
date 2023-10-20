"""
Nested Dictionaries is called a dictionaries within a dictionary
"""

computer_courses = {
                        "course_one" : {
                            "name" : "Concept of programming",
                            "credit" : 4
                        },
                        "course_two" : {
                            "name" : "Object oriented paradigm",
                            "credit" : 3
                        },
                        "course_three" : {
                            "name" : "Calculus",
                            "credit" : 6
                        },
                        "course_four" : {
                            "mame" : "Software architecture",
                            "credit" : 3
                        }
}

#NOTE A DCITIONARY THAT CONTAINS A LIST IS DIFFRENT A DICTIONARY WITHIN A DICTIONARY
var_dictionaries = {
                        "name": "Jamal",
                        "race": "Somali",
                        "weight": 78.80,
                        "student": True,
                        "age": 38,
                        "foodlist": ["Rice","Fish","Burger","Fried eggs"],
                        "carlist": {"Toyoto","Mercedes","BMW","Honda","Volvo"}
                   }
#===============================================================================================================
#PRINT THE COMPUTER_FAMILY WHICH IS A DICTIONARY WITHIN A DICTIONARIES
print()
print("ALL THE KEY NAMES (DICTIONARY NAMES) OF THE DICTIONARY WITHIN DICTIONARIES")
for i in computer_courses:
 print(i)# THIS WILL PRINT ALL THE DICTIONARY NAMES INSIDE THE MAIN DICTIONARY (COMPUTER_FAMILY), THIS REPRESENT


#PRINT THE var_dictionaries WHICH IS A NORMAL DICTIONARY BUT CONTAINS A LIST
print()
print("ALL THE KEY NAMES OF THE NORMAL DICTIONARY")
for i in var_dictionaries:
 print(i)# THIS WILL PRINT ALL THE KEY NAMES INSIDE THE MAIN DICTIONARY (var_dictionaries)


#===============================================================================================================
#PRINT ALL THE COMPUTER_FAMILY KEY NAMES AND VALUES WHICH IS A DICTIONARY WITHIN A DICTIONARIES
print()
print("ALL THE KEY NAMES and values (DICTIONARY NAMES) OF THE DICTIONARY WITHIN DICTIONARIES")
for i in computer_courses:
 print(i,":", computer_courses[i])


#PRINT THE var_dictionaries WHICH IS A NORMAL DICTIONARY BUT CONTAINS A LIST
print()
print("ALL THE KEY NAMES AND VALUES OF THE NORMAL DICTIONARY")
for i in var_dictionaries:
 print(i, ":", var_dictionaries[i])# THIS WILL PRINT ALL THE KEY NAMES INSIDE THE MAIN DICTIONARY (var_dictionaries)


#alternative way of displaying the details of the dictioonary within a dictionaries using nested for loops

#use the get() method
#it requires to pass string which the key name
print("")
print(computer_courses.get("course_one"))
#===============================================================================================================

#use the keys() method
#it does noy require to pass any value  
print("")
print(computer_courses.keys())
print()
print("print all keys in one by one using fro loop")
#or you can print all in one by one using for loop
for i in computer_courses.keys():
    print(i)
#===============================================================================================================

#use the values() method
print()
print("values option one")
print("using the value method")
print(computer_courses.values())
print()
print("values option two")
print("print all values in one by one using fro loop")
#or you can print all in one by one using for loop
for i in computer_courses.values():
    print(i)

#also same like this to the above
print()
print("values option three")
for i in computer_courses:
    print(computer_courses.get(i))

#or you can print all in one by one using for loop
print()
print("values option four")
for i in computer_courses.values():
    for j in i:
     print(j, ":",i[j])

#or you can print all in one by one using for loop
print()
print("values option five")
for i in computer_courses.values():
    for j in i:
     print(j, ":",i.get(j))
#===============================================================================================================
#use the items() method
print()
print("items option one")
print("print all the items of the computer course")
print(computer_courses.items())

print()
print("items option two")
for i in computer_courses.items():
    print(i)

print()
print("items option three")
for i, j in computer_courses.items():
    print(i," ",j)

print()
print("items option four")
for i, j in computer_courses.items():
    print(i)
    for k in j:
     print("  ",k, ":",j[k])
#===============================================================================================================

#PRINT ALL THE COMPUTER_FAMILY KEY NAMES AND VALUES WHICH IS A DICTIONARY WITHIN A DICTIONARIES
print()
print("ALL THE KEY NAMES and values (DICTIONARY NAMES) OF THE DICTIONARY WITHIN DICTIONARIES")
for i in computer_courses:
      print(i,":", computer_courses[i])

#try this way
print()
for i in computer_courses.keys():
      print(i, ":",computer_courses.get(i))


#===============================================================================================================
#SUMMARY
#ACCESSING THE SUB DICTIONARY VALUES USING LOOPS

print()
print("ACCESSING THE SUB DICTIONARY VALUES USING LOOPS--- ITEMS-- OPTION ONE")
for i, j in computer_courses.items():
    print(i)
    for k in j:
     print("  ",k, ":",j[k])
     #print("  ",k, ":",j.get(k)) . #this is also optional since j is dictionalry



print("ACCESSING THE SUB DICTIONARY VALUES USING LOOPS--- VALUES-- OPTION TWO")
#or you can print all in one by one using for loop
print()
for i in computer_courses.values():
    for j in i:
     print(j, ":",i[j])


print("ACCESSING THE SUB DICTIONARY VALUES USING LOOPS--- VALUES, GET -- OPTION THREE")
#or you can print all in one by one using for loop
print()
for i in computer_courses.values():
    for j in i:
     print(j, ":",i.get(j))


#===============================================================================================================
#ALTERNATIVE WAY OF NESTING THE DICTIONARIES
#ADD DICTIONARIES TO A NEW DICTIONARY
#Create FOROUR SEPERATE DICTIONARIES, THEN PUT THEM INTO A NEW DICTIONARY


course_one = {
         "name" : "Concept of programming",
         "credit" : 4
                }
course_two  = {
          "name" : "Object oriented paradigm",
          "credit" : 3
                      }
course_three = {
         "name" : "Calculus",
         "credit" : 6
                   },
course_four = {
        "mame" : "Software architecture",
        "credit" : 3
                 }
computer_course ={
    course_one,
    course_two,
    course_three,
    course_four
}