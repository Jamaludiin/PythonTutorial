# Change List Item
print("Example 0-------------------------------------------------------")

var_list = [10, 20, 30, 40, 50]

# Changing the third item
var_list[2] = 35
print(var_list)

# Changing the last item
var_list[-1] = 55
print(var_list)

# Output: [10, 20, 35, 40, 50]
# Output: [10, 20, 35, 40, 55]

print("Example 1-------------------------------------------------------")

# Change List Item using List Slicing
var_list = [10, 20, 30, 40, 50]

var_list[1:4] = [25, 35, 45]
print(var_list)

# Output: [10, 25, 35, 45, 50]
print("Example 2-------------------------------------------------------")


# Change List Item using List Methods
var_list = [10, 20, 30, 40, 50]

var_list.insert(2, 25)
print(var_list)

var_list.append(60)
print(var_list)

var_list.extend([70, 80, 90])
print(var_list)
print("Example 3-------------------------------------------------------")


# Add List Item Using Append List Method
var_list = [1, 2, 3]

var_list.append(4)

print(var_list)
print("Example 4-------------------------------------------------------")


# Add List Item Using Insert Method in Python
var_list = [1, 2, 3]

print(var_list)
var_list.insert(1, 5)

print(var_list)
print("Example 5-------------------------------------------------------")


# Add List Item Using Concatenation Operator (+) in Python
var_list = [1, 2, 3]
new_items = [4, 5]

print(var_list)
print(new_items)

var_list = var_list + new_items
print(var_list)
print("Example 6-------------------------------------------------------")


# Remove List Items Using Remove Method in Python
var_list = [1, 2, 3, 4, 5]

print(var_list)

var_list.remove(3)

print(var_list)
print("Example 7-------------------------------------------------------")


# Remove List Items Using Pop Method
var_list = [1, 2, 3, 4, 5]

print(var_list)

popped_item = var_list.pop(2)

print(var_list)
print(popped_item)
print("Example 7-------------------------------------------------------")


# Remove List Items Using del statement in Python
var_list = [1, 2, 3, 4, 5]

print(var_list)

del var_list[1]

print(var_list)
print("Example 8-------------------------------------------------------")


# iterate list items
var_list = [1, 2, 3, 4, 5]

# Iterate using a for loop
for item in var_list:
    print(item)

print("for loop stops here")
# Iterate using a while loop and index
index = 0
while index < len(var_list):
    print(var_list[index])
    index += 1
print("Example 9-------------------------------------------------------")
