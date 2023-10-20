"""
Python Assignment Operators
Assignment operators are used to assign values to variables:

Operator	Example	    Same As	

=	        x = 5	    x = 5	
+=	        x += 3	    x = x + 3	
-=	        x -= 3	    x = x - 3	
*=	        x *= 3	    x = x * 3	
/=	        x /= 3	    x = x / 3	
%=	        x %= 3	    x = x % 3	
//=	        x //= 3	    x = x // 3	
**=	        x **= 3	    x = x ** 3	


&=	        x &= 3	    x = x & 3	
|=	        x |= 3	    x = x | 3	
^=	        x ^= 3	    x = x ^ 3	
>>=	        x >>= 3	    x = x >> 3	
<<=	        x <<= 3	    x = x << 3
"""
#THIS CONCEPT MEANS PERFORM OPERATION AND PUT BACK THE VALUE TO THE VARIABLE

#I THINK WE HAVE SEEN THE FIRST 8 OPERATORS PLUS THE ASSIGNMENT OPERATOR, THE LAST FIVE OPERATOR NOT SEEN

#EXAMPLE 1:  &= is and equals
""" EXPLANATION: a = a & b 
# & is bitwise and if a and b are either int or long.

        FURTHER EXPLANATION 
to put it in simple terms. Under the hood it does bit-wise binary operation.
for example 5 in binary is 0101 and 3 in binary is 0011
now do "And" operation between them (when both are 1 the result is one, 0 otherwise) 
and you will get binary 0001 which means 1 in decimal.

MEANING THE BITWISE AND OPERATOR CONVERTS THE FIRST AND SECOND OPERAND INTO THEIR RESPECTIVE BINARY
AND THEN COMPARES THE BOTH BINARY USING AND OPERATOR CONCEPTS (ONLY BECOMES TRUE WHEN BOTH COMPARED ELEMNT IS TRUE)
(OTHERWISE WILL BE ZERO)
"""

#EXAMPLE CONVERT THESE NUMBERS INTO BINARY AND PRINT IT e.g. 4 and 3
"""
In Python, you can simply use the bin() function to convert from a decimal value to its corresponding binary value.
And similarly, the int() function to convert a binary to its decimal value. The int() function takes as second argument 
the base of the number to be converted, which is 2 in case of binary numbers. [CITE: FROM https://www.datacamp.com/tutorial/python-data-type-conversion]
"""
print("\nThe binary value of 5 is ",bin(5))
print("\nThe binary value of 3 is ",bin(3))
#NOTE THE PYTHON PROVIDES THE OUTPUT using 0b AS PREFIX WHILE HE IGNORES THE ZERO DECIMALS IF THEY ARE PREFIC
#E.G. the decimal 5 converted to binary is 0101, BUT PYTHON DISPLAY 0b101 INSTEAD OF 0101

#PRACTICE IT USING BITWISE OPERATORS WITH ASSIGNMENT OPERATION
x = 5
x &= 3 # THIS IS SAME AS    x = x & 3
print("\nAfter using bitwise and the result is ",x)

#WHAT ABOUT THIS EXAMPLE AGAIN
x = 5
x &= 4 # THIS IS SAME AS    x = x & 4
print("\nAfter using bitwise and the result is ",x)

#WHAT ABOUT THIS EXAMPLE AGAIN
x = 5
x &= 7 # THIS IS SAME AS    x = x & 7
print("\nAfter using bitwise and the result is ",x)
"""
In Python, bitwise operators are used to performing bitwise calculations on integers. 
The integers are first converted into binary and then operations are performed on each bit 
or corresponding pair of bits, hence the name bitwise operators. The result is then returned in decimal format.
[CITE: https://www.geeksforgeeks.org/python-bitwise-operators/]
"""
#IF THE ABOVE IS CONFUSING LETS TRY THIS FOR UNDERSTANDING 
#they convert both operands (5 and 5) into decimal and compare using AND operator and convert the result back to decimal

#PRACTICE IT USING BITWISE OPERATORS WITHOUT ASSIGNMENT OPERATION
print("\n5 & 3 =", 5 & 3) 
print("\n5 & 4 =", 5 & 4)
print("\n5 & 7 =", 5 & 7)

#            SYMPOL: |	        NAME: Bitwise OR    SYNTAX: x | y
#EXAMPLE 1:  SYMPOL: |=	        EXAMPLE: x |= 3	    Same As: x = x | 3
#EXAMPLE CONVERT THESE NUMBERS INTO BINARY OR PRINT IT e.g. 4 and 3

#PRACTICE IT USING BITWISE OPERATORS WITH ASSIGNMENT OPERATION
x = 5
x |= 3 # THIS IS SAME AS    x = x | 3
print("\nAfter using bitwise OR the result is ",x)

#WHAT ABOUT THIS EXAMPLE AGAIN
x = 5
x |= 4 # THIS IS SAME AS    x = x | 4
print("\nAfter using bitwise OR the result is ",x)

#WHAT ABOUT THIS EXAMPLE AGAIN
x = 5
x |= 7 # THIS IS SAME AS    x = x | 7
print("\nAfter using bitwise OR the result is ",x)

