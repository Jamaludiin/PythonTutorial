print(
    "lambda arguments : expression---- A lambda function can take any number of arguments, but can only have one expression"
)

result = lambda x: x + 5
print(result(10))

print(
    "This another example:----------------------------------------------------------------------------"
)
result = lambda x: x + 10
print(result(10))

print(
    "\nLmbda with Multiply argument and return the result:------------------------------------------------"
)
result = lambda a, b: a + b
print(result(5, 5))

print(
    "\nLmbda with Multiply argument and return string result:------------------------------------------------"
)

result = lambda str1, str2: str1 + str2
print(result("leyla", " Moha"))

print(
    "\nLmbda with three argument and return the result:------------------------------------------------------"
)

result = lambda a, b, c: print(a + b * c)
print(result(4, 5, 2))


# Main Purpose of Lmbda function is those bellow
def myFun(b):
    return lambda a: a + b


myaddition = myFun(5)

print(myaddition(5))
