"""
cover each section and sub section with simple easy to understand python codes and its output
Introduction to Python Tuples 
Characteristics of tuples Items
Data Types in tuples
    Check tuples Type
    Check tuples Length
The tuples() Constructor
Access tuples Items
    Positive Indexing
    Negative Indexing
    Positive Range Indexing
    Negative Range Indexing
    More Practice About Python tuples Slicing
Change tuples Items
    Change tuples Items Using tuples Slicing
    Change tuples Items Using tuples Methods
Add tuples Items
    Add tuples Item Using Append Method
    Add tuples Item Using Insert Method
    Add tuples Item Using Concatenation Operator (+)
Remove tuples Items
    Remove tuples Items Using Remove Method
    Remove tuples Items Using Pop Method
    Remove tuples Items Using Del Statement
Unpack Tuples
Loop tuples Items
tuples Comprehension
    tuples Comprehension Benefits and Usages
Tuple Methods
    Sort tuples Items
    Copy tuples Items
        Method 1: Using Slicing
        Method 2: Using the tuples() Constructor
        Method 3: Using the copy() Method:
        Other Method: Using the copy.deepcopy() Method
    Join tuples Items
Convert tuples to other data types
     int,float
     set
     dictionary
     list
perform operations in tuples
  join tuples
  multiply tuples
  compare tuples
  perform mathematical operation in tuples
  eliminate duplicates in tuples
Conclusion






--------------------
Characteristics of tuples Items
Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:"""

print("Example 0-------------------------------------------------------")

# Example of an ordered tuple
my_tuple = (3, 1, 4, 1, 5)
print(my_tuple)  # Output: (3, 1, 4, 1, 5)

print("\nExample 1-------------------------------------------------------")

# Example of an immutable tuple
my_tuple = (1, 2, 3)
# Attempting to modify the tuple will result in an error
# my_tuple[0] = 10  # Raises a TypeError: 'tuple' object does not support item assignment
print("Raises a TypeError: 'tuple' object does not support item assignment")

print("\nExample 2-------------------------------------------------------")

# Example of a tuple with duplicate elements
my_tuple = (1, 2, 3, 2, 4)
print(my_tuple)  # Output: (1, 2, 3, 2, 4)

print("\nExample 3-------------------------------------------------------")

my_tuple = (1, "Hello", 3.14, True)
print(my_tuple)  # Output: (1, "Hello", 3.14, True)

print("\nExample 4-------------------------------------------------------")

my_tuple = (1, 2, 3)
print(type(my_tuple))  # Output: <class 'tuple'>"""

print("\nExample 5-------------------------------------------------------")

my_tuple = (1, 2, 3)
print(len(my_tuple))  # Output: 3

print("\nExample 6-------------------------------------------------------")

# Using the tuple() constructor to create a tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

print("\nExample 7-------------------------------------------------------")

# Original tuple
my_tuple = (1, 2, 3)

# Value to be added
new_item = 4

# Create a new tuple with the added item
new_tuple = my_tuple + (new_item,)

print("Original tuple:", my_tuple)
print("New tuple:", new_tuple)

print("\nExample 8-------------------------------------------------------")

my_tuple = (1, 2, 3, 2)
value_to_remove = 2
new_tuple = (
    my_tuple[: my_tuple.index(value_to_remove)]
    + my_tuple[my_tuple.index(value_to_remove) + 1 :]
)
print(new_tuple)

print("\nExample 9-------------------------------------------------------")

my_tuple = (1, 2, 3, 2)  # Original tuple

my_list = list(my_tuple)
my_list.pop(2)

my_tuple = tuple(my_list)
print(my_tuple)

print("\nExample 10-------------------------------------------------------")

my_tuple = (1, 2, 3, 2)  # Original tuple

del my_tuple

# print(my_tuple)
print(
    "After you delete a tuple using del statement you cannot print again becos is gone"
)

print("\nExample 11-------------------------------------------------------")

# Unpacking a tuple into variables
tuple1 = (10, 20, 30)
x, y, z = tuple1
print("x:", x)
print("y:", y)
print("z:", z)

print("\nExample 12-------------------------------------------------------")

# Unpacking with an asterisk
tuple_1 = (40, 50, 60, 70, 80)
a, *b, c = tuple_1
print("a:", a)
print("b:", b)
print("c:", c)

print("\nExample 13-------------------------------------------------------")

# Example 2
tuple_2 = ("John", 37, "PhD", "+90875637389", "Sports")
(
    name,
    age,
    profession,
    tell,
    *others,
) = tuple_2
print("name:", name)
print("age:", age)
print("profession:", profession)
print("tell:", tell)
print("others:", others)

print("\nExample 14-------------------------------------------------------")

# Ignoring unwanted elements
tuple3 = (100, 200, 300, 400)
first, *_ = tuple3
print("first:", first)  # Output: first: 100

print("\nExample 15-------------------------------------------------------")

# Unpacking nested tuples
nested_tuple = ((1, 2), (3, 4))
(a, b), (c, d) = nested_tuple
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("\nExample 16-------------------------------------------------------")

a = 5
b = 10
a, b = b, a  # Swap the values of a and b
print("a:", a)
print("b:", b)

print("\nExample 17-------------------------------------------------------")

# =================================
# NEXT TALK ABOUT NESTED TUPLE, HOW TO ACCESS AND HOW TO DELETE IN THE ABOVE SECTIONS

# Creating a nested tuple
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# You can access nested tuples in this way
print(nested_tuple)

# Or You can access nested tuples in this way
element = nested_tuple[1][0]  # Accesses the element 3 from the second tuple
print(element)
element = nested_tuple[2][2]
print(element)


# Or you can access nested tuples in this way using for loop
# Printing the nested tuple
for inner_tuple in nested_tuple:
    print(inner_tuple)

print("\nExample 18-------------------------------------------------------")

my_tuple = (1, 2, 3, 4)

for item in my_tuple:
    print(item)

print("\nExample 19-------------------------------------------------------")

my_tuple = ("apple", "banana", "cherry")

for index, value in enumerate(my_tuple):
    print(f"Index {index}: {value}")

print("\nExample 20-------------------------------------------------------")

my_tuple = (5, 10, 15, 20)
index = 0

while index < len(my_tuple):
    print(my_tuple[index])
    index += 1

print("\nExample 21-------------------------------------------------------")

my_tuple = ("red", "green", "blue", "yellow", "blue")
index = 0

while index < len(my_tuple):
    if my_tuple[index] == "blue":
        break
    print(my_tuple[index])
    index += 1

print("\nExample 22-------------------------------------------------------")

# Create a tuple of even numbers from 1 to 10 using tuple comprehension
even_numbers = tuple(x for x in range(1, 11) if x % 2 == 0)

print(even_numbers)

print("\nExample 23-------------------------------------------------------")

# Tuple comprehension in Python
var_tuple_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Squaring each number in the tuple using tuple comprehension
# syntax: var_tuple = tuple(expression for item in iterable if condition)
var_squared_tuple_numbers = tuple(num**2 for num in var_tuple_numbers)

print(var_squared_tuple_numbers)

print("\nExample 24-------------------------------------------------------")

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)

# Compare tuples
if tuple1 == tuple2:
    print("Tuples are equal")
else:
    print("Tuples are not equal")  # Output: Tuples are not equal

print("\nExample 25-------------------------------------------------------")

tuple1 = (1, 2, 3)
sum_tuple = sum(tuple1)  # Calculate the sum of elements
average = sum_tuple / len(tuple1)  # Calculate the average
print("Sum:", sum_tuple)
print("Average:", average)

print("\nExample 26-------------------------------------------------------")

tuple_with_duplicates = (1, 2, 2, 3, 4, 4, 5)
tuple_without_duplicates = tuple(set(tuple_with_duplicates))
print(tuple_without_duplicates)

print("\nExample 27-------------------------------------------------------")

# Converting a single numeric value tuple to an integer
int_tuple = (42,)
integer_value = int(int_tuple[0])
print("Integer:", integer_value)

# Converting a single numeric value tuple to a float
float_tuple = (3.14,)
float_value = float(float_tuple[0])
print("Float:", float_value)

print("\nExample 28-------------------------------------------------------")

# Tuple with multiple numeric values
tuple_with_multiple_values = (10, 20, 30, 40, 50)

# Convert each value to integers
int_values = tuple(int(x) for x in tuple_with_multiple_values)

# Convert each value to floats
float_values = tuple(float(x) for x in tuple_with_multiple_values)

print("Original Tuple:", tuple_with_multiple_values)
print("Integers:", int_values)
print("Floats:", float_values)

print("\nExample 29-------------------------------------------------------")

tuple_with_duplicates = (1, 2, 2, 3, 4, 4, 5)
set_from_tuple = set(tuple_with_duplicates)
print(set_from_tuple)

print("\nExample 30-------------------------------------------------------")

tuple_of_pairs = (("Name", "John Murry"), ("Age", 55), ("Tell", +90866373893))
dict_from_tuple = dict(tuple_of_pairs)
print(dict_from_tuple)

print("\nExample 31-------------------------------------------------------")

tuple_to_list = (1, 2, 3)
list_from_tuple = list(tuple_to_list)
print(list_from_tuple)

print("\nExample 32-------------------------------------------------------")

my_tuple = (1, 2, 3, 2, 4, 2)
count_of_2 = my_tuple.count(2)
print(count_of_2)

print("\nExample 33-------------------------------------------------------")

my_tuple = ("apple", "banana", "cherry", "apple")
index_of_cherry = my_tuple.index("cherry")
print(index_of_cherry)

print("\nExample 34-------------------------------------------------------")

my_tuple = (5, 2, 8, 1, 9)
sorted_list = sorted(my_tuple)
print(sorted_list)
