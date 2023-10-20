print("Example 0---------------------------------------")
a = 20
b = 40
c = 10

# USE ADDITIONAL OPERATOR TO COMBINE TWO VALUES IN PYTHON
print("a: ", a, "b: ", b, "c: ", c, "Result: a + b + c = ", a + b + c)

# Output: a:  20 b:  40 c:  10 Result: a + b + c =  70

print("Example 1---------------------------------------")

a = 20
b = 40
c = 10

# USE SUBTRACTION OPERATOR TO SUBTRACT TWO VALUES IN PYTHON
print("a: ", a, "b: ", b, "c: ", c, "Result: b - a - c = ", b - a - c)

# Output: a:  20 b:  40 c:  10 b - a - c =  10

print("Example 2---------------------------------------")

a = 2
b = 4
c = 3

# USE MULTIPLICATION OPERATOR TO MULTIPLY TWO VALUES IN PYTHON
print("a: ", a, "b: ", b, "c: ", c, "Result: b * a * c = ", b * a * c)

# Output: a:  2 b:  4 c:  3 Result: b * a * c =  24

print("Example 3---------------------------------------")

a = 5
b = 40
c = 2

# USE DIVISION OPERATOR TO DIVIDE TWO VALUES IN PYTHON
print("a: ", a, "b: ", b, "c: ", c, "Result: b / a / c = ", b / a / c)

# Output: a:  5 b:  40 c:  2 Result: b / a / c =  4.0

print("Example 4---------------------------------------")

a = 5
b = 40
c = 2.2

# USE FLOOR DIVISION OPERATOR TO DIVIDE TWO OR MORE VALUES IN PYTHON
print("a: ", a, "b: ", b, "Result: b // a = ", b // a)

# Output: a:  5 b:  40 Result: b // a =  8

print("a: ", a, "c: ", c, "Result: a // c = ", a // c)
# Output: a:  5 c:  2.2 Result: a // c =  2.0

print("Example 5---------------------------------------")

a = 5
b = 24

# USE MODULUS OPERATOR TO RETURN THE REMINDER OF TWO VALUES AFTER BEING DIVIDED IN PYTHON
print("a: ", a, "b: ", b, "Result: b % a = ", b % a)

# Output: a:  5 b:  24 Result: b % a =  4

# USE MODULUS OPERATOR TO CHECK IF THE NUMBER IS ODD OR EVEN IN PYTHON
c = 7

if c % 2 == 0:
    print("The Number is Even")
else:
    print("The Number is Odd")

# Output: The Number is Odd

print("Example 6---------------------------------------")

a = 2
b = 5

# USE THE EXPONENTIATION OPERATOR IN PYTHON
print("a: ", a, "b: ", b, "Result: b ** a = ", b**a)

# Output: a:  2 b:  5 Result: b ** a =  25

print("Example 7---------------------------------------")

# /-------------------------/

# Python Assignment Operators
a = 2
b = 5
c = 20

# USE THE ASSIGNMENT OPERATOR IN PYTHON
print("a: ", a, "b: ", b, "c:", c)

# Output: a:  2 b:  5 c: 20

print("Example 8---------------------------------------")

a = 5
a += 5  # equivalent to a = a + 4
b = 20
b += a  # equivalent to b = b + a
c = 2
c += a + b  # equivalent to c = c + a + b

# USE THE ASSIGNMENT OPERATOR IN PYTHON
print("a: ", a, "b: ", b, "c:", c)

# Output: a:  10 b:  30 c: 42

print("Example 9---------------------------------------")

a = 10
a -= 5  # equivalent to a = a - 5
b = 40
b -= a  # equivalent to b = b - a


# USE THE ASSIGNMENT OPERATOR IN PYTHON
print("a: ", a, "b: ", b)

# Output: a:  5 b:  35

print("Example 10---------------------------------------")

a = 6
a /= 2  # equivalent to a = a / 2
b = 3
b /= a  # equivalent to b = b / a

# USE THE ASSIGNMENT OPERATOR IN PYTHON
print("a: ", a, "b: ", b)

# Output: a:  3.0 b:  1.0

print("Example 11---------------------------------------")

a = 5
a %= 2  # equivalent to a = a % 2
b = 30
b %= 4  # equivalent to b = b % 3

# USE THE ASSIGNMENT OPERATOR IN PYTHON
print("a: ", a, "b: ", b)

# Output: a:  1 b:  2

print("Example 12---------------------------------------")

a = 15
a //= 3  # equivalent to a = a // 3
b = 30
b //= 4  # equivalent to b = b // 4

# USE THE ASSIGNMENT OPERATOR IN PYTHON
print("a: ", a, "b: ", b)

# Output: a:  5 b:  7

print("Example 13---------------------------------------")

a = 5
a **= 2  # equivalent to a = a ** 2
b = 2
b **= 2  # equivalent to b = b ** 2

# USE THE ASSIGNMENT OPERATOR IN PYTHON
print("a: ", a, "b: ", b)

# Output: a:  25 b:  4

print("Example 14---------------------------------------")

# BITWISE AND ASSIGNMENT OPERATOR
"""In Python, bitwise operators are used to performing bitwise calculations on integers. 
The integers are first converted into binary and then operations are performed on each bit 
or corresponding pair of bits, hence the name bitwise operators. The result is then returned in decimal format."""

a = 6
a &= 11  # equivalent to a = a & 11
b = 9
b &= 5  # equivalent to b = b & 5

# USE THE ASSIGNMENT OPERATOR IN PYTHON
print("a: ", a, "b: ", b)

# Output: a:  2 b:  1

print("Example 15---------------------------------------")

a = 6
a |= 11  # equivalent to a = a | 11
b = 9
b |= 5  # equivalent to b = b | 5

# USE THE ASSIGNMENT OPERATOR IN PYTHON
print("a: ", a, "b: ", b)

# Output: a:  15 b:  13

print("Example 16---------------------------------------")

a = 6
a ^= 11  # equivalent to a = a ^ 11
b = 9
b ^= 5  # equivalent to b = b ^ 5

# USE THE ASSIGNMENT OPERATOR IN PYTHON
print("a: ", a, "b: ", b)

# Output: a:  13 b:  12

print("Example 17---------------------------------------")

a = 2
a >>= 1  # equivalent to a = a >> 1
b = 4
b >>= 3  # equivalent to b = b >> 3

# USE THE ASSIGNMENT OPERATOR IN PYTHON
print("a: ", a, "b: ", b)

# Output: a:  1 b:  0

print("Example 18---------------------------------------")

a = 2
a <<= 1  # equivalent to a = a << 1
b = 4
b <<= 3  # equivalent to b = b << 3

# USE THE ASSIGNMENT OPERATOR IN PYTHON
print("a: ", a, "b: ", b)

# Output: a:  4 b:  32

print("Example 19---------------------------------------")

a = 5
b = ~a  # equivalent to a = a << 1

# USE THE ASSIGNMENT OPERATOR IN PYTHON
print("a: ", a, "b:", b)
a = ~a
print("a: ", a)

# Output: a:  5 b: -6
# Output: a:  -6
print("Example 20---------------------------------------")
