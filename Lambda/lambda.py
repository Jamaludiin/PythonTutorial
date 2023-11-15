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


print(
    "\nLmbda with Multiply argument and return string result:------------------------------------------------"
)

result = lambda set1, set2: set1 + set2
print(result([1, 2, 3], [3, 4, 5]))
union_set = result([1, 2, 3], [3, 4, 5])

print(union_set)

"""print(union_set=set1.union(set2))
# Combine more set items
set3 = {6, 7, 8}
union_set = set1.union(set2, set3)
print(union_set)"""
