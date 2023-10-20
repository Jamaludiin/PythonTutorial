"""
                    WE CAN USE A LOOP CONCEPT TO DEAL WITH TUPLE VARIABLES
"""

#EXAMPLE 1: PRINT OR DISPLAY ALL TUPLE ITEMS ONE BY ONE USING FOR LOOP IN PYTHON
# : we use for loop
var_tuple_for_loop=1,2,3,5,7,9,8,
for i in var_tuple_for_loop:
   print("\nThe tuple variable item : ", i)

#EXAMPLE 2: DISPLAY THE TUPLE ITEMS THROUGH LOOPING THEIR INDEX NUMBER
# : we use for loop
for i in range(len(var_tuple_for_loop)):
   print("\nThe tuple variable item using their index using for loop : ", var_tuple_for_loop[i])

#EXAMPLE 3: DISPLAY THE TUPLE ITEMS THROUGH LOOPING THEIR INDEX NUMBER
# : we use while loop
i=0
while i < len(var_tuple_for_loop):
   print("\nThe tuple variable item using their index using while loop : ", var_tuple_for_loop[i])
   i=i+1

#EXAMPLE 4: DISPLAY THE TUPLE ITEMS WITH THE ODD INDEX VALUE USING FOR LOOP IN PYTHON
#odd numbers are 1,3,5,7,9,11,13,etc
j=1
k=len(var_tuple_for_loop)
for i in range(len(var_tuple_for_loop)):
   if j<k:
     print("\nThe tuple item with odd index number using for loop is : ",var_tuple_for_loop[j]," j value is : ",j)
     j=j+2

#EXAMPLE 5: DISPLAY THE TUPLE ITEMS WITH THE ODD INDEX VALUE USING WHILE LOOP IN PYTHON
#odd numbers are 1,3,5,7,9,11,13,etc
j=1
k=len(var_tuple_for_loop)
while j < k:
     print("\nThe tuple item with odd index number using while loop is : ",var_tuple_for_loop[j]," j value is : ",j)
     j=j+2

#EXAMPLE 6: FIND AND DISPLAY TUPLE ITEMS IN REVERSE ONE BY ONE USING FOR LOOP IN PYTHON
print("\nThe original value of the tuple is :", var_tuple_for_loop,"\n")
k=len(var_tuple_for_loop)
m=len(var_tuple_for_loop)
for i in range(len(var_tuple_for_loop)):
    k=k-1
    print("The item ",m,"in the tuple using for loop is: ", var_tuple_for_loop[k]," IT HAS THIS INDEX ",k)
    m=m-1

#EXAMPLE 7: FIND AND DISPLAY TUPLE ITEMS IN REVERSE ONE BY ONE USING WHILE LOOP IN PYTHON
print("\nThe original value of the tuple is :", var_tuple_for_loop,"\n")
k=len(var_tuple_for_loop)
m=len(var_tuple_for_loop)
while k > 0 and k != 0:
    k=k-1
    print("The item ",m,"in the tuple using while loop is: ", var_tuple_for_loop[k]," IT HAS THIS INDEX ",k)
    m=m-1

#alternative way of reversing a tuple items without using loops such as for or while loop
print("\nThe reversed item in the tuple is  :",var_tuple_for_loop[::-1],"\n")

#EXAMPLE 7: DISPLAY THE LAST HALF ITEMS OF A TUPLE USING FOR LOOP IN PYTHON
k=int(len(var_tuple_for_loop)/2)
for i in var_tuple_for_loop:
    if i==var_tuple_for_loop[k]:
      print("The last half items in the tuple using for loop is : ",var_tuple_for_loop[k])
      k=k+1

#this is an alternative way of slicing the last half tuple items without using for loop
print("\nThe last half item in the tuple is  :",var_tuple_for_loop[int(len(var_tuple_for_loop)/2):len(var_tuple_for_loop)])

print("\n")
#EXAMPLE 8: DISPLAY THE FIRST HALF ITEMS OF A TUPLE USING FOR LOOP IN PYTHON
k=0
for i in var_tuple_for_loop:
    if i == var_tuple_for_loop[k] and k <= int(len(var_tuple_for_loop)/2):
      print("The FIRST half items in the tuple using for loop is : ",var_tuple_for_loop[k])
      k=k+1

#this is an alternative way of slicing the first half tuple items without using for loop
print("\nThe first half item in the tuple is  :",var_tuple_for_loop[0:int(len(var_tuple_for_loop)/2)])
#the above statement ignores the last index to include the output, the following we add plus one to make it inclusive
print("\nThe first half item in the tuple after inclusive applied is  :",var_tuple_for_loop[0:int(len(var_tuple_for_loop)/2)+1])

#EXAMPLE 9: DISPLAY THE LAST HALF ITEMS OF A TUPLE USING WHILE LOOP IN PYTHON
print("\n")
k=int(len(var_tuple_for_loop)/2)
while k <= len(var_tuple_for_loop)-1:
  print("The last half items in the tuple using WHILE loop is : ",var_tuple_for_loop[k])
  k=k+1

#EXAMPLE 10: DISPLAY THE FIRST HALF ITEMS OF A TUPLE USING WHILE LOOP IN PYTHON
print("\n")
k=0
while k <= len(var_tuple_for_loop)/2:
  print("The FIRST half items in the tuple using WHILE loop is : ",var_tuple_for_loop[k])
  k=k+1
#EXAMPLE 11: DISPLAY THE REVERSED FIRST HALF ITEMS OF A TUPLE USING WHILE LOOP IN PYTHON
print("\n")
k=0
m=int(len(var_tuple_for_loop)/2)
while k <= int(len(var_tuple_for_loop)/2):
  print("The REVERSED FIRST half items in the tuple using WHILE loop is : ",var_tuple_for_loop[m])
  k=k+1
  m=m-1

#EXAMPLE 12
# : DISPLAY THE REVERSED LAST HALF ITEMS OF A TUPLE USING WHILE LOOP IN PYTHON
print("\n")
k=len(var_tuple_for_loop)-1
while k >= int(len(var_tuple_for_loop)/2):#use int other wise it will return float of 3.5
  print("THE REVERSED LAST HALF ITEMS OF A TUPLE USING WHILE is : ",var_tuple_for_loop[k])
  k=k-1

print("\nThe original value of the tuple is :", var_tuple_for_loop,"\n")