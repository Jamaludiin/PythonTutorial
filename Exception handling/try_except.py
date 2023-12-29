"""
The "try" block lets you test a block of code for errors.

The "except" block lets you handle the error.

The "else" block lets you execute code when there is no error.

The "finally" block lets you execute code, regardless of the result of the try- and except blocks.
"""

# simple example is like this
var_x =  10
try:
  print(var_x)
except:
  print("An exception occurred!")

#---------------------------------------------------------------------------------------------
# What about like this. You can run the code and message error in the except block will be displayed 
var_y =  10
try:
  print(var_z)
except:
  print("An exception occurred!")

#---------------------------------------------------------------------------------------------
# using multiple Exceptions.
# incase you want to check multiple blocks for error
print("\nSecond block test")

try:
  print(xs)
except NameError:
  print("Block 1 error")
except: 
  print("Block 2 error")


#---------------------------------------------------------------------------------------------
print("\nThird block test")

# What about if everything is ok use the Else to execute after checking errors
try:
  print("good")
except NameError:
  print("Block 1 error")
except: 
  print("Block 2 error")
else:
  print("No error exist")

#---------------------------------------------------------------------------------------------
print("\nFourth block test")

try:
  print("ok",rr)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") # this message will be printed regardless if the try block raises an error or not.


#---------------------------------------------------------------------------------------------
# example nested try 
print("\nFifth block test")
file_path = "/Users/jamalabdullahi/Python Tutorial/File Handling with Python/created_file.txt"

try:
  var_file = open(file_path)
  try:
    var_file.write("Try my writting")# the "w" parameter is missing so it must be error raised
  except:
    print("Error has happened when trying to write")
  finally:
    var_file.close()
    print("File is closed as well")
except:
  print("File opening has problem")


#---------------------------------------------------------------------------------------------
#Raise an exception
"""As a Python developer you can choose to throw an exception if a condition occurs.
To throw (or raise) an exception, use the raise keyword."""
print("\n")
x = 10

if x < 9:# if it is false exeception will be trigered
  raise Exception("Sorry, no numbers below zero")
else: # this will not be executed becouse the above condition must be false
    print("Number is below or equal 10")


#---------------------------------------------------------------------------------------------
# we can state what kind of error to be raised
x = "My name"
y = 10

if not type(x) is int: # if it is string this will be displayed "raise TypeError("Please use string in the condition")"
  raise TypeError("Please use string in the condition")