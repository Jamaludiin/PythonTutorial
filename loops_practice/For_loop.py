"""
            Python Loops is used to iterate sequences such as list items, tuple items, dictionary items, etc.
"""
var_set=["A","B","C","D","E"]
#EXAMPLE 1: PRINT ALL ITEMS IN A SET ONE BY ONE USING FOR LOOP IN PYTHON
for i in var_set:
    print("The items of the set are : ",i)

print("\n")
#EXAMPLE 2: LOOP STRING ITEMS IN STRING VARIABLE USING FOR LOOP IN PYTHON
         #: LOOP THROUGH THE LETTERS IN THE WORD "SOFTWARE"
var_string="SOFTWARE"
for i in var_string:
    print("The combonents of the string is : ",i)


"""
          BREAK STATEMENT:
          WE USE BREAK STATEMENT TO STOP THE LOOP BEFORE IT HAS LOOPED THROUGH ALL THE ITEMS:
"""
print("\n")
#EXAMPLE 3: STOP AND EXIT THE FOR LOOP WHEN THE I IS "D" USING BREAK STATEMENT IN PYTHON
        #NOTE: THE D STATEMENT WILL BE PRINTED (INCLUDED), BECOUSE THE I WILL BE PRINTED BEFORE THE BREAK STATEMENT
for i in var_set:
    print("USING BREAK STATEMENT The items of the set are : ",i)
    if i =="D":
        break
#NOTE: THE D STATEMENT WILL NOT BE PRINTED (EXCLUDED), BECOUSE THE PRINT STATEMENT WAS PUT AFTER BREAK
print("\n")
for i in var_set:
    if i =="D":
        break
    print("USING BREAK STATEMENT The items of the set are : ",i)

"""
          CONTINUE STATEMENT:
          WE USE CONTINUE STATEMENT TO STOP A CURRENT ITERATION AND CONTINOU WITH NEXT ITERATION
"""
#EXAMPLE 4: USE CONTINUE STATEMENT TO SKIP WHEN A SPECIFIED CONDITION BECOME TRUE USING FOR LOOP IN PYTHON
print("\n")
for i in var_set:
    if i =="D":
        continue
    print("USING CONTINOU STATEMENT The items of the set are : ",i)

"""
             THE RANGE() FUNCTION
IF WE WANT TO ITERATE A SET OF CODE IN A SPECIFIED NUMBER OF TIMES, WE USE THE RANGE() METHOD
THIS METHOD RETURNS A SEQUENCE OF NUMBERS, AND THE RANGE STARTS 0 (BY DEFAULT) AND INCREMENT 1 AT EVERYTIME EXECUTION 
HAPPENS UNTILL THE SPECIFIED NUMBER ACHIEVED
"""

#RNAGE WITH ONE PARAMETERS

print("\n")
#EXAMPLE 5: RUN A CODE LOOP THAT RUNS 5 TIMES (STARTING FROM ZERO) USING FOR LOOP AND RANGE METHOD IN PYTHON
#if you did not specify the start point of the range, by default it will start from 0, so 0-4 (it is 5 iteration)
for i in range(5):
    print("The loop is run 5 times : ",i)

print("\n")
#EXAMPLE 6: RUN A CODE LOOP THAT RUNS 4 TIMES (STARTING FROM 1) USING FOR LOOP AND RANGE METHOD IN PYTHON
for i in range(1,5):        #5 is excluded
    print("The loop is run 4 times : ",i)

print("\n")
#EXAMPLE 7: LOOP A SET OF ITEMS IN A SPECIFIED TIMES USING FOR LOOP AND RANGE METHOD IN PYTHON
var_set_range=["Python","Java","C++","C","Pascal",1,2,3,4]
for i in range(len(var_set_range)):
    print("The set item of : ",var_set_range[i],"      has index of : ",i)

#RNAGE WITH TWO PARAMETERS

print("\n")
#EXAMPLE 8: LOOP A SET OF ITEMS STARTING FROM ONE IN A SPECIFIED TIMES USING FOR LOOP AND RANGE METHOD IN PYTHON
for i in range(1,len(var_set_range)):
    print("The set item of : ",var_set_range[i],"      has index of : ",i)

print("\n")
#EXAMPLE 9: PRINT THE FIRST HALF ITEMS OF S SET USING FOR LOOP AND RANGE METHOD IN PYTHON
# the set has 9 items, so 9/2 = 4.5, then convert to int which is 4, the following will print the first four items
for i in range(0,int(len(var_set_range)/2)):
    print("The first half item of the set starts from : ",var_set_range[i],"      has index of : ",i)

print("\n")
#EXAMPLE 10: PRINT THE LAST HALF ITEMS OF S SET USING FOR LOOP AND RANGE METHOD IN PYTHON
# the set has 9 items, so 9/2 = 4.5, then convert to int which is 4, 
# the following loop will start from 4 untill the final index which is 9, so from 4 till 9 is 5
# print the last four items
for i in range(int(len(var_set_range)/2),len(var_set_range)):
    print("The last half item of the set starts from : ",var_set_range[i],"      has index of : ",i)

#RNAGE WITH THREE PARAMETERS
"""
THE RANGE METHOD NORMALLY INCREMENT 1 BY DEFAULT, THEREFORE YOU CAN DECIDE THE NUMBER OF INCREMENT AT THE THIRD PARAMETER
range(0, 20, 2):
"""
print("\n")
#EXAMPLE 11: LOOP THE SPECIFIED CODE AT SPECIFIED SET BY INCREMENTING 2 EACH TIME USING FOR LOOP AND RANGE METHOD IN PYTHON
for i in range(0,20,2):
    print("The loop has increment of 2 : ",i)

print("\n")
#EXAMPLE 12: LOOP AND INCRIMENT 2 USING FOR LOOP AND RANGE METHOD IN PYTHON
for i in range(1,20,2):
    print("The ODD NUMBERS OF A loop has increment of 2 : ",i)

print("\n")
#EXAMPLE 13: DSIPLAY BY LOOPING AND INCRIMENTING 2 AT THE INDEX NUMBERS IN THE SET USING FOR LOOP AND RANGE METHOD IN PYTHON
for i in range(0,len(var_set_range),2):
     print("The set items incrimented their index by 2  : ",var_set_range[i],"      has index of : ",i)

"""
THE ELSE KEYWORD IN THE FOR LOOP
WE USE ELSE STATEMENT TO SPECIFY A CODE THAT TO BE EXECUTED WHEN A PARTICULAR LOOP IS FINISHED
"""
print("\n")
#EXAMPLE 14: USE ELSE KEYWORD AFTER LOOP IF FINISHED USING FOR LOOP IN PYTHON
for i in range(5):
    print("The loop is at : ",i)
else:
    print("The loop is finished")

print("\n")
#EXAMPLE 15: USE ELSE KEYWORD AFTER BREAK IF FINISHED USING FOR LOOP IN PYTHON
#The else block will NOT be executed if the loop is stopped by a break statement. [CITE: W3SCHOOLS]
for i in range(5):
  if i == 4: 
    break
    print("The loop is at : ",i)
else:
  print("Finally finished!")

#NESTED LOOPS
#EXAMPLE 15: USE NESTED FOR LOOP IN PYTHON
print("\n")

var_set_strik1 =["*","***","****","*****"]
var_set_strik2 =["*****","****","***","**","*"]
for i in var_set_strik1:
    print(i)
    for x in var_set_strik2:
        print(x)


"""
THE PASS STATEMENT
IN FOR LOOP IT WILL BE AN ERROR IF CANNOT BE EMPTY, BUT IF YOU WANT A FOR LOOP WITHOUT CONTENT USE THE PASS STATEMENT 
TO AVOID GETTING ERROR
"""
print(" ")
#EXAMPLE 16: USE THE PASS STATEMENT TO EMPTY A FOR LOOP CONTENT IN PYTHON
for i in range(4):
    pass
print("The last iteration of the loop was : ",i)

for x in [0, 1, 2]:
  pass

print(" ")
print("The value of the x is : ",x," The type of the x is : ",type(x))



#EXAMPLE 17: FIND THE ODD AND EVEN NUMBERS USING MODULO OPERATOR IN PYTHON
"""One common use for the Modulo Operator is to find even or odd numbers. The code below uses the modulo operator to print 
all odd numbers between 0 and 10."""
print("\n")   
for i in range(1,10):
    if i % 2 != 0: 
        print(" the number is not divisible by 2 and is : ",i ,"the remainder is ",i%2)

print("\n")   
for i in range(1,10):
    if i % 2 == 0:
        print(" the number is divisible by 2 and is : ",i ,"the remainder is ",i%2)

