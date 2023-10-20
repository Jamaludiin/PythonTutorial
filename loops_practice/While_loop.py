"""
            Python Loops is used to iterate sequences such as list items, tuple items, dictionary items, etc.
"""
#WHILE LOOPS CONTINOUSLY EXECUTE A BLOCK OF CODE AS LONG AS THE CONDITION SPECIFIED IS TRUE

var_set_while_loop =[1,2,3,4,9,8,7,6,5]
#EXAMPLE 1: PRINT ALL ITEMS IN A SET ONE BY ONE IN REVERSE USING WHILE LOOP IN PYTHON
i=len(var_set_while_loop)-1
while i <= len(var_set_while_loop) and i !=0:
    print("The items of the set is : ",var_set_while_loop[i]," The value of i is : ",i)
    i=i-1


#EXAMPLE 2: USE BREAK STATEMENT AND PRINT ALL ITEMS IN A SET ONE BY ONE IN REVERSE USING WHILE LOOP IN PYTHON
print("")
i=len(var_set_while_loop)-1
while i <= len(var_set_while_loop):
    print("The items of the set is : ",var_set_while_loop[i]," The value of i is : ",i)
    i=i-1
    if i ==0:
        break
#EXAMPLE 3: PRINT 1-6 USING WHILE LOOP IN PYTHON
print("")
num = 1
while num < 7:
  print("The iteration number is : ",num)
  num += 1

#EXAMPLE 4: WITHOUT NEW LINE PRINT 0-5 USING WHILE LOOP IN PYTHON
print("")
num2=0
while num2 < 6:
  print("The iteration number is : ",num2, end=" ")
  num2=num2+1

#LETS USE BREAK STATEMENT DURING WHILE LOOP TO STOP AND EXIT THE LOOP WHEN CERTAIN CONDITIONS BECOMES TRUE
#EXAMPLE 5: STOP THE WHILE LOOP IN THE MIDLE OF THE PROCESS
print("")

i=1
while i < 6:
    print("I is less than 5 and I is : ",i)
    i = i+1
    if i > int(6/2):
        break

#LETS USE CONTINOUE STATEMENT DURING WHILE LOOP TO STOP AND CONTINPUE WITH THE NEXT LOOP WHEN CERTAIN CONDITIONS BECOMES TRUE
#EXAMPLE 6: STOP AND CONTINOUE WHEN THE WHILE LOOP REACH IN THE MIDLE OF THE PROCESS
print("")

i=0
while i < 6:
    i = i+1
    if i == int(6/2):#Note that number 3 is missing in the result
        continue
    print("I is less than 5 and I is : ",i)

#WE USE THE ELSE STATEMENT WHEN THE LOOP CONDITION IS NO LONGER TRUE
#EXAMPLE 7: PRINT GOOD WHEN THE WHILE LOOP FINSIHED IN PYTHON
print("")

i=6
while i >= 0:
   print("I is greater than 0 and I is : ",i)
   i=i-1
else:
    print("GOOD")


