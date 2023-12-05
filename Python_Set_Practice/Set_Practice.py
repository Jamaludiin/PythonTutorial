"""
cover each section and sub section with simple easy to understand python codes and its output
"Introduction to Python Sets 
Characteristics of Sets Items
Data Types in Sets
    Store diffrent data types in Sets
    Check Sets Type
    Check Sets Length
The Sets() Constructor
Access Sets Items
    Positive Indexing
    Negative Indexing
    Positive Range Indexing
    Negative Range Indexing
    More Practice About Python Sets Slicing
Change Sets Items
    Change Sets Items Using Sets Slicing
    Change Sets Items Using Sets Methods
Add Sets Items
    Add Sets Item Using Append Method
    Add Sets Item Using Insert Method
    Add Sets Item Using Concatenation Operator (+)
Remove Sets Items
    Remove Sets Items Using Remove Method
    Remove Sets Items Using Pop Method
    Remove Sets Items Using Del Statement
Unpack Sets
Loop Sets Items
Sets Comprehension
    Sets Comprehension Benefits and Usages
Sets Methods
    Sort Sets Items
    Copy Sets Items
        Method 1: Using Slicing
        Method 2: Using the Sets() Constructor
        Method 3: Using the copy() Method:
        Other Method: Using the copy.deepcopy() Method
    Join Sets Items
Convert Sets to other data types
     int,float
     Tuple
     dictionary
     list
perform operations in Sets
  join Sets
  multiply Sets
  compare Sets
  perform mathematical operation in Sets
  eliminate duplicates in Sets
Conclusion"
"""
print("Example 0-------------------------------------------------------\n")
# Creating a set using curly braces
my_set = {1, 2, 3, 4, 5}
print(my_set)

print("Example 1-------------------------------------------------------\n")

# Creating a set using the set() constructor
my_set1 = set([1, 2, 3, 4, 5])
my_set2 = set((1, 2, 3, 4, 5, 6))

print(my_set1)
print(my_set2)

print("Example 2-------------------------------------------------------\n")

# Creating an empty set using the set() constructor
empty_set1 = set()
print(empty_set1)

# Creating an empty set using the using empty curly braces {} would create an empty dictionary
empty_set2 = {}
print(empty_set2)
print(type(empty_set2))

print("Example 3-------------------------------------------------------\n")

my_set1 = {3, 1, 2, 4, 7, 8, 5, 6}
print(my_set1)

my_set2 = {"Yellow", 1, "Blue", "Green", 3, "Red", "Black", 4, "White"}
print(my_set2)

print("Example 4-------------------------------------------------------\n")

my_set = {1, 2, 2, 3, 3, 1, 4, 5, 5, 7, 8, 7}
print(my_set)

print("Example 5-------------------------------------------------------\n")

my_set = {1, 2, 3}
# Attempting to change the first element to 4
"""my_set[0] = 4  
print(my_set)"""

print("Example 6-------------------------------------------------------\n")

# Methods can be found here
my_set = {1, 2, 3, 7, 8, 9}
# Adding a duplicate element
my_set.add(2)
print(my_set)
# Adding a non-duplicate element
my_set.add(5)
print(my_set)

# Remove Sets Items Using remove Method
my_set.remove(3)
print(my_set)

print("Example 7-------------------------------------------------------\n")

# Add Sets Item Using update Method
my_set.update([3, 4, 5])
print(my_set)

print("Example 8-------------------------------------------------------\n")

# Remove Sets Items Using discard Method
my_set.discard(8)
print(my_set)

print("Example 9-------------------------------------------------------\n")

my_set = {1, "Akesh", 3.14, True, (4, 5), False}
print(type(my_set))

print("Example 10-------------------------------------------------------\n")

my_set1 = {1, 2, 3, 4, 5}
set_length = len(my_set1)
print(set_length)

my_set2 = {1, 2, 6, 33, 3, 4, 5, "Flash", True}
print(
    my_set2
)  # the True will not be displayed becouse 1 and True is same so it will considered duplicate
print(my_set2)
print(len(my_set2))

# Without Duplicate
my_set3 = {44, 2, 6, 33, 3, 4, 5, "Flash", True}
print(my_set3)
print(len(my_set3))

print("Example 11-------------------------------------------------------\n")

my_set = {1, 2, 3, 4, 5, 6, 7, 8}
if 7 in my_set:
    print("7 is in the set")
if 5 not in my_set:
    print("5 is not in the set")
if 10 not in my_set:
    print("10 is not in the set")

print("Example 12-------------------------------------------------------\n")

# Create a set
my_set = {44, 2, 6, 33, 3, 4, 5, "Flash", True}

# Access set items using a for loop
print("Accessing set items using a for loop:")
for item in my_set:
    print(item)

print("Example 13-------------------------------------------------------\n")

my_set = {44, 2, 6, 33, 3, 4, 5, "Flash", True}

"""my_set[4] = 55"""
print(my_set)

print("Example 14-------------------------------------------------------\n")

my_set = {1, 2, 3, 5, 7, 8}
my_set.add(4)  # Adding 4 to the set
print(my_set)

print("Example 15-------------------------------------------------------\n")

my_set = {1, 2, 3, 5, 7, 8}
my_set.update([4, 6, 9])  # Adding multiple items to the set
print(my_set)

print("Example 15-------------------------------------------------------\n")

my_set = {1, 2, 3, 5, 7, 8}
my_set.remove(3)  # Removing 3 from the set
print(my_set)

my_set.discard(5)  # Attempting to remove 6, which does not exist in the set
print(my_set)

popped_item = my_set.pop()  # Removing and returning an arbitrary item
print("Popped item:", popped_item)
print(my_set)

print("Example 16-------------------------------------------------------\n")

my_set = {1, 2, 3, 4, 5}
del my_set  # Deleting the entire set
# Now, my_set no longer exists
"""print(my_set)"""

print("Example 17-------------------------------------------------------\n")

my_set = {1, 9, 4, 5, "Flash"}
a, b, c, d, e = my_set
print(a, b, c, d, e)

print("Example 17-------------------------------------------------------\n")

my_set = {1, 9, 4, 5, "Flash"}
first, *rest = my_set
print("First:", first)
print("Rest:", rest)

print("Example 18-------------------------------------------------------\n")

my_set = {1, 9, 4, 5, "Flash"}
first, _, third, *remaining = my_set
print("First:", first)
print("Third:", third)
print("Remaining:", remaining)

print("Example 19-------------------------------------------------------\n")

my_set = {5, 1, 3, 2, 4, 7, 10, 89}
sorted_list = sorted(my_set)
sorted_set = set(sorted_list)

print("Original Set:", my_set)
print("Sorted Set:", sorted_set)

print("Example 20-------------------------------------------------------\n")

original_set = {5, 1, 3, 2, 4, 7, 10, 89}
copied_set = original_set.copy()

print("Original Set:", original_set)
print("Copied Set:", copied_set)

print("\nAfter using set constructor Method\n")

original_set = {5, 1, 3, 2, 4, 7, 10, 89}
copied_set = set(original_set)

print("Original Set:", original_set)
print("Copied Set:", copied_set)

print("Example 21-------------------------------------------------------\n")

set_1 = {1, 2, 3, 6, 8, 11}
set_2 = {3, 4, 5, 7, 13, 15}

print("Set one:", set_1)
print("Set two: ", set_2)

joined_set = set_1 | set_2
print("After sets joined: ", joined_set)

print("Example 22-------------------------------------------------------\n")

set_1 = {1, 2, 3, 6, 8, 11}
set_2 = {3, 4, 5, 7, 13, 15, 18, 20}

print("Set one:", set_1)
print("Set two: ", set_2)

set_1.update(set_2)
print("After sets joined: ", set_1)

print("Example 23-------------------------------------------------------\n")

set_1 = {1, 2, 3, 6, 8, 11}
set_2 = {3, 4, 5, 7, 13, 15, 18, 20}

print("Set one:", set_1)
print("Set two: ", set_2)

joined_set = {x for x in set_1} | {x for x in set_2}
print("After sets joined: ", joined_set)

print("Example 24-------------------------------------------------------\n")

my_set = {3, 4, 5, 7, 13, 15, 18, 20}

# Convert the set to an integer (e.g., try to find the sum of set)
int_value = sum(my_set)

# Convert the set to a float (e.g., try to find the average)
float_value = sum(my_set) / len(my_set)

print("Set value converted to Integer:", int_value)
print("Set value converted to Float:", float_value)

print("Example 25-------------------------------------------------------\n")

my_set = {3, 4, 5, 7, 13, 15, 18, 20}
set_to_tuple = tuple(my_set)
print("After sets converted to a tuple:", set_to_tuple)

print("Example 26-------------------------------------------------------\n")

my_set = {3, 4, 5, 7, 13, 15, 18, 20}
list_from_set = list(my_set)
print("After sets converted to a list:", list_from_set)

print("Example 27-------------------------------------------------------\n")

my_set = {"apple", "banana", "cherry"}
dictionary_from_set = {fruit: len(fruit) for fruit in my_set}
print("Dictionary from Set:", dictionary_from_set)

print("Example 28-------------------------------------------------------\n")

set_1 = {1, 2, 3}
set_2 = {3, 2, 1}
set_3 = {1, 2, 3, 4, 5}

# Check if two sets are equal
are_equal = set_1 == set_2

# Check if set1 is a subset of set3
is_subset = set_1.issubset(set_3)

# Check if set3 is a superset of set1
is_superset = set_3.issuperset(set_1)

print("Are Equal:", are_equal)
print("Is Subset:", is_subset)
print("Is Superset:", is_superset)

print("Example 29-------------------------------------------------------\n")

# Perform Mathematical Operations in Sets
my_set_1 = {3, 4, 5, 7}
my_set_2 = {10, 20, 30}


# Summ all items in a sets using sum() method
print("Sum of all set 1 values: ", sum(my_set_1))
print("Sum of all set 2 values :", sum(my_set_2))

Summation = sum(my_set_1) + sum(my_set_2)
print("Sum of all values in set 1 and set 2 : ", Summation)

# Perform divition
divition = sum(my_set_2) / sum(my_set_1)
print("Set value converted to Float:", divition)

# Multiplication
multipilication = divition * sum(my_set_1)
print("Multiplication performed :", multipilication)

print("Example 30-------------------------------------------------------\n")
print("Example 31-------------------------------------------------------\n")

# loop set items

my_set = {1, 2, 3, 4, 6, 8, 9}

for item in my_set:
    print("Item: ", item)

print("Example 32-------------------------------------------------------\n")

my_set = {1, 2, 3, 4, 6, 8, 9}
iterator = iter(my_set)
while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break

print("Example 33-------------------------------------------------------\n")

my_set = {1, 2, 3, 4, 6, 8, 9}

# Initialize i to the length of the set minus 1
i = len(my_set) - 1

# Use a while loop to iterate through the set
while i >= 0:
    print("The item at index", i, "is:", list(my_set)[i])
    i = i - 1

print("Example 34-------------------------------------------------------\n")

my_set = {1, 2, 3, 4, 6, 8, 9}

# Initialize i to 0 to start at the first index
i = 0

# Use a while loop to iterate through the set
while i < len(my_set):
    # Convert the set to a list to access elements by index
    item = list(my_set)[i]
    print("The item in the set is:", item)
    i = i + 1

print("Example 35-------------------------------------------------------\n")

my_set = {1, 2, 3, 4, 6, 8, 9}

# Initialize i to the length of the set minus 1
i = len(my_set) - 1

# Use a while loop to iterate through the set
while i >= 0:
    if list(my_set)[i] % 2:
        print("The item at index", i, "is:", list(my_set)[i])
    i = i - 1

print("Example 36-------------------------------------------------------\n")

my_set = {1, 2, 3, 4, 6, 8, 9}
i = 0

while i < len(my_set):
    if list(my_set)[i] % 2:
        print("The item at index", i, "is:", list(my_set)[i])
    i = i + 1

print("Example 37-------------------------------------------------------\n")

numbers = {1, 2, 3, 4, 5}
squared_numbers = {x**2 for x in numbers}
print("Squaroot values: ", squared_numbers)


numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
even_numbers = {x for x in numbers if x % 2 == 0}
print("Even numbers:", even_numbers)

print("Example 38-------------------------------------------------------\n")

words = {"Computer", "Super Computer", "Mini Computer"}
uppercase_words = {word.upper() for word in words}
print(uppercase_words)

print("Example 39-------------------------------------------------------\n")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = {x for x in set1} | {x for x in set2}
intersection_set = {x for x in set1} & {x for x in set2}
difference_set = {x for x in set1} - {x for x in set2}

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)

print("Example 40-------------------------------------------------------\n")

my_set_1 = {1, 2, 3, 4}
my_set_1.add(5)
print(my_set_1)

# Duplicate will not be uccepted
my_set_2 = {1, 2, 3, 4}
my_set_2.add(4)
print(my_set_2)

print("Example 41-------------------------------------------------------\n")

my_set_1 = {1, 2, 3, 4}
if 2 in my_set_1:
    removed_num = 2
    my_set_1.remove(2)
    print(
        "The reomved number is:", removed_num, "Thus the remained value is:", my_set_1
    )
else:
    removed_num = None

print("Example 42-------------------------------------------------------\n")

my_set_1 = {1, 2, 3, 4}
"""my_set_1.remove(5) #cannot be removed"""
print("Thus the remained value is:", my_set_1)

print("Example 43-------------------------------------------------------\n")

my_set = {1, 2, 3, 4, 5, 6}

# Discard and store the element 2
if 2 in my_set:
    discarded_num = 2
    my_set.discard(2)
else:
    discarded_num = None

print("The discarded number is:", discarded_num, "and the remaining set is:", my_set)

# Attempt to discard 10 (which is not in the set)
if 10 in my_set:
    discarded_num = 10
    my_set.discard(10)
else:
    discarded_num = None

print("The discarded number is:", discarded_num, "and the remaining set is:", my_set)

print("Example 44-------------------------------------------------------\n")

my_set = {1, 2, 3, 4}
popped_element = my_set.pop()
print("You have removed item:", popped_element, "and the rest is: ", my_set)

print("Example 45-------------------------------------------------------\n")

my_set = {1, 2, 3, 4}
my_set.clear()
print("The set is cleared:", my_set)

print("Example 46-------------------------------------------------------\n")

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)

# Combine more set items
set3 = {6, 7, 8}
union_set = set1.union(set2, set3)
print(union_set)


# -----------------------------------------------------------
# create this seperate post blog with only these
"""In Python, you can join (combine) the elements of multiple sets into a single set using various set methods and set operations. Here are several ways to join set items, along with examples for each method:

Using the union() Method:

The union() method returns a new set containing all unique elements from two or more sets.
python
Copy code"""
print("Example 47-------------------------------------------------------\n")

set1 = {1, 2, 3}
set2 = {3, 4, 5}
joined_set = set1.union(set2)
print(joined_set)

"""
Using the Pipe Operator (|):

You can use the | operator to perform a union operation between sets, which combines elements from multiple sets into a new set.
python
Copy code
"""
print("Example 48-------------------------------------------------------\n")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {8, 7, 6}

joined_set = set1 | set2 | set3
print(joined_set)
"""
Using the update() Method:

The update() method adds elements from one set to another, effectively joining the two sets.
python
Copy code"""
print("Example 49-------------------------------------------------------\n")

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)

"""
Using Set Comprehension:

You can use set comprehension to combine elements from multiple sets into a new set.
python
Copy code"""
print("Example 50-------------------------------------------------------\n")

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set2 = {8, 9, 6}

joined_set = {x for x in set1} | {x for x in set2} | {x for x in set3}
print(joined_set)

"""
Using the intersection() Method with Multiple Sets:

While not typically used for joining sets, you can use the intersection() method with multiple sets to achieve a similar result by finding the intersection of sets.
python
Copy code"""
print("Example 51-------------------------------------------------------\n")
# things that all the sets are similar with
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
set3 = {4, 5, 6, 3}
set4 = {4, 3, 6}

joined_set = set1.intersection(set2, set3, set4)
print(joined_set)

"""
Using Set Unions with * (Extended Unpacking):

You can use the * operator to unpack multiple sets and combine them into a new set.
python
Copy code"""
print("Example 52-------------------------------------------------------\n")

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}
joined_set = {*set1, *set2, *set3}
print(joined_set)

"""
These examples demonstrate different ways to join set items in Python, whether by using set methods, set operations, or set comprehensions, depending on your specific use case and preference."""


# Additional practices of the sets, just checing
print("Example 43-------------------------------------------------------\n")

set_test = set({})
print(set_test, type(set_test))

set_test = set(
    {
        1,
    }
)
print(set_test, type(set_test))
set_test = set({1, 2, 3})
print(set_test, type(set_test))
