"""
                    PACKING TUPLE IS CREATING AND ASSIGNING INTO A VALUE IS CALLED TUPLE PACKING

                    UNPACKING TUPLE IS EXTRACTING THE ITEMS BACK FROM TUPLE IS CALLED TUPLE UNPACKING
"""

#EXAMPLE 1: TUPLE PACKING CREATING A TUPLE AND ASSIGNING A NEW VALUES IS CALLED TUPLE PACKING
var_tuple_packing =1,2,
var_tuple_packing_mix =("Apple","Banana","Mengo",True, 2.89)
print("\nTuple variables was created/PACKED : ",var_tuple_packing,var_tuple_packing_mix)

#EXAMPLE 2: UNPACKING A TUPLE VARIABLE: EXTRACTING A TUPLE ITEMS AND STORE THEM IN TO A NOTHER VARIABLES
(Apple,Banana,Mengo,Boolean,Decimal)=var_tuple_packing_mix
print("\nThe value of Apple is : ",Apple)
print("\nThe value of Banana is : ",Banana)
print("\nThe value of Mengo is : ",Mengo)
print("\nThe value of Bool is : ",Boolean)
print("\nThe value of Decimal is : ",Decimal)

#WHAT WILL HAPPEN IF THE NUMBER OF VALUE IN THE TUPLE VARIABLE MISMATCH THE NUMBER OF VARIABLES
#THE ABOVE EXAMPLE THEY MATCH AS THEY ARE FIVE TUPLE VALUE ASSIGNED INTO FIVE VARIABLES
"""(Apple,Banana,Mengo,Boolean)=var_tuple_packing_mix
print("\nThe value of Apple is : ",Apple)
print("\nThe value of Banana is : ",Banana)
print("\nThe value of Mengo is : ",Mengo)
print("\nThe value of Bool is : ",Boolean)

THE ABOVE EXAMPLE OSS TRIGERED AN ERROR WHICH IS :
ValueError: too many values to unpack (expected 4)
"""
#EXAMPLE 3: UNPACKING MISMATCHED VARIBALES AND TUPLE ITEMS USING ASTERISK* IN PYTHON
#we use astrick to assign all the remaining value items to the last variable, thus the last variable will become a list
(Apple,Banana,*Mengo)=var_tuple_packing_mix
print("\nThe value of Apple is : ",Apple)
print("\nThe value of Banana is : ",Banana)
print("\nThe value of Mengo is : ",Mengo)
print("\nThe TYPE OF LAST VARIABLE WITH * is : ",type(Mengo))

#EXAMPLE 4: UNPACKING MISMATCHED VARIBALES AND TUPLE ITEMS USING ASTERISK* IN PYTHON
#assume if we give the astrik * sympol to another variable which is not the last variable
#the python will assign all the value except the first one and the last one 
# (only if you have three variable and the second one taken the astrik)
(Apple,*Banana,Mengo)=var_tuple_packing_mix
print("\nThe value of Apple is : ",Apple)
print("\nThe value of Banana is : ",Banana)
print("\nThe value of Mengo is : ",Mengo)