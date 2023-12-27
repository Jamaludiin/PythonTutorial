# Local variable: can only be used in the methods that they are declared

def my_function():
    var_local = 20
    return var_local
print("The local variable inside this function holds value of",my_function())

# local variables can also be accessed from a function within the function:
print("\n")
def my_function_1():
    var_local = 22

    def my_nested_function():
        print("The local variable inside this function holds value of",var_local + 1)
    
    my_nested_function() # call the function inside its parent

my_function_1()
#print("The local variable inside this function holds value of",my_function_1())


#----------------===============================---------------------------------

# GLOBAL VARIABLES: are those created outside of any function or class or using the global keyword
print("\n")

var_global = 100
def my_fun_global_test():
    print("This is global var inside a function", var_global)

my_fun_global_test()


# This feature also must be keept in mind (Naming Variables)
print("\n")

var_named_global = 100
def my_fun_named_global_test():
    var_named_global = 50
    print("This is global var inside a function", var_named_global)

my_fun_named_global_test()

print(var_named_global) # prints 100


#-----------------------------------------------------------------------------------------
#The global keyword makes the variable global.
print("\n")

def my_global_test_func():
  global var_global_1
  var_global_1 = 450

my_global_test_func()

print(var_global_1) # can be accessed outside the function that was declared in it

# WHAT ABOUT THIS
#-----------------------------------------------------------------------------------------
#The global keyword makes the variable global.
print("\n")
var_global_1 = 900
print(var_global_1)

def my_global_test_func():
  global var_global_1
  var_global_1 = 800

my_global_test_func()

print(var_global_1) # IT WILL TAKE THE LAST DECLARED ONE USING SINCE BOTH ARE GLOBAL AND THE ONE IN THE FUNCTION USES THE GLOBAL KEYWORD
