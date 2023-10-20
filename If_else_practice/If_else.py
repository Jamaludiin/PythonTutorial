"""
IF AND ELSE STATEMENTS ARE CONDITIONAL STATEMENTS USED TO CHECK AND EXECUTE A BLOCK OF CODE WHEN CERTAIN 
CONDITION BECOME TRUE.

Python supports the usual logical conditions from mathematics: [CITE: W3SCHOOLS]

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

WE USE THE IF STATEMENT TO CHECK THE FIRST CONDITION IF IT IS TRUE OR NOT
WE ALSO USE THE ELIF STATEMENT TO CHECK ANOTHER CONDITION SPECIALLY IF THE PREVIOUS CONDITION NOT TRUE
WE USE THE ELSE STATEMENT TO EXECUTE A BLOCK OF CODE WHEN ALL OF THE ABOVE CONDITIONS FAIL TO BE EXECUTED (FALSE)
"""

print("")
#EXAMPLE 1: CHECK IF THE AGE OF PERSON BELLOW 18 OR ABOVE OR EQUAL 18 USING IF STATEMENT IN PYTHON
age=18
if age >= 18:#if age is greater than or equal 18
    print("You are an adult person")

#THE ABOVE CODE YOU CAN ALSO WRITE LIKE THIS
print("")
if age > 18 or age == 18:#if age is greater than or equal 18
    print("You are an adult person")

#EXAMPLE 2: CHECK IF PLAYER ONE IS OLDER THAN PLAYER 2
#WE USE IF AND ELSE STATEMENT TO CHECK BOTH CONDITIONS
print("")
player1=19
player2=30
if player1>player2:
    print("Player one is older than player two")
else:
    print("Player one not older than player two")

#EXAMPLE 3: USE IF AND ELIF STATEMENT TO CHECK FOR MULTIPLE CONDITIONS IN PYTHON
print("")
if player1==player2:
    print("The age of Player one and player two is equal ")
elif player1>player2:
    print("The age of Player one is greater than the age of player two")
else:
    print("The age of Player one is less than the age of player two")


"""
SHORT HAND IF
YOU CAN SHORTEN THE CODE IF THE STATEMENT TO BE EXECUTED IS ONLY ONE WHILE USING IF STATEMENT
AND USE THE SAME LINE AS THE IF STATEMENT
"""
#EXAMPLE 4: SHORT HAND OF IF STATEMENT
print("")
if 20 < 30: print("The 20 is less than 30")

"""
SHORT HAND IF ... ELSE
YOU CAN ALSO SHORTEN THE CODE IF THE CODE TO BE EXECUTED IN IF AND ELSE STATEMENT IS ONE
AND PUT ALL THE CODE IN JUST ONE LINE AS FOLLOW

the template of such code
the one line to be executed when if condition becomes true follwed by the if and its condition followed by the 
else followed by the statement to be executed in the else.
NOTE: no collons should be used after the if statement and else statement
"""
print("")
a=5 
b=7
print("a id greater than b") if 5>7 else print("a is less than b")

print("")
#EXAMPLE 5: USE CONDITIONS AND PUT IN ONE LINE
#THIS IS 3 CONDITION, THE FIRST ONE IS IF 3> 4, SECOND IS IF 3==3, AND LAST ELSE
print("First condition of if") if 3 > 4 else print("The first else") if 3==3 else print("the last else")

#WE USE LOGICAL OPERATORS OF AND and OR TO CHECK MULTIPLE CONDITIONS
#EXAMPLE 6: USE AND OPERATOR DURING IF STATEMENT TO CHECK TWO CONDITIONS IN PYTHON
print("")
a=20
b=30
c=20
if a > b and b < c:
    print("This will be printed when both conditions become true.", end=" ")
    print("B is greater than or equal all")
elif a < b and b > c:
    print("This will be printed when both conditions in second elif become true.", end= " ")
    print("B is greater than or equal all")

#EXAMPLE 7: USE OR OPERATOR DURING IF STATEMENT TO CHECK TWO CONDITIONS IN PYTHON
print("")
if a == c or a < b: print("The or condition is partial true and can be executed this line")

#NESTED IF STATEMENT
#YOU CAN INSERT IF STATEMENT INSIDE ANOTHER IF STATEMENT
#EXAMPLE 8: USE NESTED IF STATEMENTS TO CHECK A CONDITION AFTER A CONDITION
print("")
if b > a:
    if b > c:
        print("B is the greatest")
    else:
        print("B is not the greates")

"""
USING THE PASS STATEMENT DURING IF..ELSE
IF STATEMENT CANNOT BE EMPTY AFTER ITS CONDITIONS EVALUATED THERE MUST BE SOMETHING TO BE EXECUTED OR NOT EXECUTED
BUT IF WE WANT THE IF STATEMENT TO BE EMPTY AFTER ITS CONDITIONS BEING EVALUATED WE USE PASS STATEMENT
USING PASS KEYWORD WILL AVOID YOU HAVING AN ERROR DUE TO EMPTY STATEMENT INSIDE THE IF CONDITIONS
"""

#EXAMPLE 9: USE THE PASS STATEMENT TO EMPTY THE CONTENT OF IF STATEMENT
print("")
if a < c:
    pass
else:
    print("A is not less than C") 

#EXAMPLE 10: USE THE PASS STATEMENT TO EMPTY THE CONTENT OF ELSE STATEMENT
print("")
if a < c:
    print("A is less than C") 
else:
    pass
