"""
PYTHON ARITHMETIC OPERATORS
ARE SET OF OPERATOR OR MATHEMATICAL SYMBOLS THAT IS USED TO PERFORM MATHEMATICAL OPERATIONS
SUCH AS WHEN YOU WANT TO ADD TWO OR MULTIPLE VALUES YOU USE ADDITIONAL OPERATOR (+) ETC

Operator	Name	            Example
+	        Addition	        x + y	
-	        Subtraction	        x - y	
*	        Multiplication	    x * y	
/	        Division	        x / y	
%	        Modulus	            x % y	
**	        Exponentiation	    x ** y	
//	        Floor division	    x // y

"""
a=20
b=30
c=10

#EXAMPLE 1: USE ADDITIONAL OPERATOR TO COMBINE TWO VALUES IN PYTHON
print("")
print("Use additional operator to add the value of a and the value of b")
print("The value of a is : ",a," The value of b is : ",b," Thus a + b is : ",a+b)

#EXAMPLE 2: USE SUBTRACTION OPERATOR TO SUBTRACT TWO VALUES IN PYTHON
print("")
print("Use Subtraction operator to subtract the value of a and the value of b")
print("The value of a is : ",a," The value of b is : ",b," Thus a - b is : ",a-b)

#EXAMPLE 3: USE MULTIPLICATION OPERATOR TO MULTIPLY TWO VALUES IN PYTHON
print("")
print("Use Multiplication operator to Multiply the value of a and the value of b")
print("The value of a is : ",a," The value of b is : ",b," Thus a * b is : ",a*b)

#EXAMPLE 4: USE DIVISION OPERATOR TO DIVIDE TWO VALUES IN PYTHON
print("")
print("Use Division operator to divide the value of a and the value of b")
print("The value of a is : ",a," The value of b is : ",b," Thus a / b is : ",a/b)

#EXAMPLE 5: USE MODULUS OPERATOR TO RETURN THE REMINDER OF TWO VALUES AFTER BEING DIVIDED IN PYTHON
print("")
print("Use Modulus operator to return the remaining value after division of the value of a and the value of b")
print("The value of a is : ",a," The value of b is : ",b," Thus a % b is : ",a%b)
#the reminder of the above line is 20 becouse 30 does not go into 20 any times so the original three is still left over.
# Note, the modulo operator returns the remainder after performing division. The remainder is twenty. 
#the above example the right operand is greater, so lets see onother one were by the left operand is greater
print("\nThe value of : ", 5," divided by : ",2, " the reminder is : ",5%2)
#The result of the above line, means Two goes into five two times and there is one left over.


#EXAMPLE 6: FIND THE ODD AND EVEN NUMBERS USING MODULO OPERATOR IN PYTHON
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

#         **	Exponentiation	x ** y
#EXAMPLE 7: USE THE EXPONENTIATION OPERATOR IN PYTHON
"""
The ** operator in Python is used to raise the number on the left to the power of the exponent of the right. 
That is, in the expression 2 ** 4 , 2 is being raised to the 4rd power.
or Return the value of 2 to the power of 4 (same as 2 * 2 * 2 * 2):

this is also same as 
x = pow(4, 3) #using the power function in python
"""
x = 2
y = 4
print("\nThe Exponetiation of ",x," in ",y," times is : ",x ** y) #this is same as of doing    2*2*2*2

#       //	Floor division	x // y
#EXAMPLE 8: USE THE FLOOR DIVISION (also sometimes known as integer division) OPERATOR IN PYTHON
#WE USE THIS OPERATOR TO ROUND THE RESULT DOWN TO ITS NEAREST WHOLE NUMBER (this also same as math. floor() function.)
x = 5
y = 2
print("\nRounding after division of ",x," and ",y," "," and after rounding is ",x // y)

