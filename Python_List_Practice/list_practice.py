#How to Find the Index of Items in a List in Python(cite: from codecamp)
#how to find the index value of a list item(s) in python

var_list =[1,20,20,3,4,5,4]
#we use index() method to return the index number of the item specified, if the items are duplicate the first item index is returned
#the index() method requires a parameter which the item you are searching his index.
#the value of the parameter can be any data type such as string, intiger, float even list
#the index() method has the follwoing format style list_var.index(item, start_index_of_sublist, end_index_of_sublist)
a=var_list.index(20)
print("This is the index number of the specified item: ", a) #output: This is the index number of item:  1

#if the item that you are looking is stored in the list as duplicate, the index() method only return the first item index
a=var_list.index(4)
print("This is the index number of the specified item: ", a) #output: This is the index number of item:  1

#Imagin we want to find if there is another 20 after the first 20
print("This is the index number of the specified item: ", var_list.index(20,2)) #output: This is the index number of the specified item:  2

#lets see one more example to find the index value of an item in a specied range
var_sublist=["A","B","C","D","B","C","B"]
#we search if there is an B after the third shelf e.g after the first C
print("The index of item B after the second self is: ",var_sublist.index("B", 2))

#we can also find the index value in a range, e.g find the index value of "B" after shelf number 2 and before shelf number 6, 
print("The index of item B after the 2 second self and before the 6 shelf: ",var_sublist.index("B", 2, 6))

#How to Find the Index of a List Item with Multiple Occurrences in Python (cite: from codecamp)
##How to Find all the Index value of a duplicate item in a List in Python
#assume we have list of items in a list while some items in the list is duplicate, how can you find all the index values of these items
#therefore using the index method cannot iterate all the indviduals and return their list, instead it can only return the index of first item
#we need some other technique or loop to perform such task as follows
#this example finds all the index value of the "B" items in the var_sublist variable 
b=[i for i in range(0, len(var_sublist)) if var_sublist[i]=="B"]
print("Option 1 The index values of 'B' items in the list is ",b)

# alternative loop example of the above solution is also written like this, but it prints in diffrent lines in each loop of 'B' item is found
i=0
for j in range (0,len(var_sublist)):
    if var_sublist[j]=="B":
        i=i+1
        print("Option 2 The index values of ",i,"th item 'B' in the list is ",j)

# alternative loop example of the above solution is also written like this, but the index values are stored in another list variable
k=[]
for j in range (0,len(var_sublist)):
    if var_sublist[j]=="B":
        k.append(j) #is better to use the extend() method but it cannot be iterated since the extend itself has iteration feature
print("Option 3 The index values of item 'B' items in the list is ",k)


#How to find the last index value of a duplicate item in a list in python
#this example you can print the last index value of a duplicate list item through iteration
#and it will stop the loop when reached the last item specified and store its index value in a variable
for j in range (0,len(var_sublist)):
    if var_sublist[j]=="B":
        h=j        
print("The index values of the last 'B' items in the list is ",h)
#ERROR CAN BE FOUND IF THE ITEM VALUE YOU PROVIDED IN THE index() method is not in the list
#a=var_list.index(2)#Error Output: ValueError: 2 is not in list

#How to find the number of times a list item is repeated in python
#for example how many times a 'B' item is found in a list variable. all what you need is to count the number of times the loop was executed and store in variable
k=0
for i in range(0,len(var_sublist)):
    if var_sublist[i]=='B':
        k=k+1
print("The number of times a 'B' item found in a list is =:", k) 

#How to know the number of items in a list in python
#OPTION 1: short route is to use the len() method and it return the lenght of the list is 
print("the leng of the list is: ", len(var_sublist))

#OPTION 2: long route to use is loop and count all the list items as follows;
#TODO

#How to print all the items in a list one by one using for loop in python
#OPTION 1: use for loop and iterate all the index value of the list variable as follows
#in this case you don not need to use the index() method instead use the list variable plus the [] brackets with target index e.g. var_sublist[i]
k=0
for i in range(0,len(var_sublist)):
    k=k+1
    print("The item ",k,"in the list is: ", var_sublist[i], "and has this index",i)

#How to print all the items in a list one by one using for loop in python
#OPTION 2: use for loop and iterate all the index value of the list variable as follows
#in this case you don not need to use the index() method instead use the list variable plus the [] brackets with target index e.g. var_sublist[i]
k=0
for x in var_sublist:
    k=k+1
    print("The item ",k,"in the list is: ", x)


#How to find the list items in a [odd] manner in python
#e.g. find and print item 1,3,5,7 etc or we can say find and print values which has index of 0,2,4,6 etc
k=0
m=len(var_sublist)
for i in range(0,len(var_sublist)):
  if k < m:
   print("The odd item in the list is: ", var_sublist[k], "and has this index value",k)
   k=k+2

#How to find the list items that has [odd] index in python
#e.g. find and print items in index 1,3,5 etc etc or we can say find and print list item 2,4,6 etc
k=1
m=len(var_sublist)
for i in range(0,len(var_sublist)):
  if k < m:
   print("The odd index item in the list is: ", var_sublist[k], "and has this index value",k)
   k=k+2

#how to find and print list items in reverse one by one in python
k=len(var_sublist)
m=len(var_sublist)
for i in range(0,len(var_sublist)):
    k=k-1
    print("The item ",m,"in the list is: ", var_sublist[k])
    m=m-1

#How to delete a duplicate list item from a list in python
#TODO


#if you re-assign new values to the previous var_list variable the new values are considered and deleted the previous one.
var_list=["jump",'run',1,"stop"]#you can use the single and double quatation at the same time in the list items but with diffrent items
print("This is a new value assigned the list var", var_list)



#HOW TO USE insert() method in a list variable in python
#The insert() method is used to add an item in a specified list position
#Syntax of insert() method is var_list.insert(position/index value, item/value). note the item can be any data type
# supose you have a list of favorite colors in a list so you want to add a new favorite color in a specific position, e.g. first position

var_color_list=["Green","Yellow","Red","Blue"]
print("The list color items before new insertion is : ", var_color_list)
var_color_list.insert(1,"White")
print("The list color items after new insertion is : ",var_color_list)

#List insert at index that is well out of range - behaves like append [cite: stackoverflow]
"""What happen if you specify a position/or index value more than the index range during insert() method. this means the list variable defined has 5 index/or positions
starting from 0 to 4. then you inserted a new value with a 7th position which does not exist.
in python this will not triger an error instead it will add the item at the last position. this is similar to append method. see the following example
"""
var_color_list.insert(7,"Maroon")
print("The list color items after new insertion at index that is well out of range - behaves like append: ",var_color_list)
"""as list was originally has a size of 5 (count from 0 to 4) and If we try to insert a new list item at index 7 while the last index of the declared variable is 4 , the insert() method will detect such range and behaves like append() method which means it will insert the inserted value at the last position and it will not throw any error at the runtime."""

#How to add set of items in a list at specified position one by one using python



#How to remove an item from a list at a specified position
#We use pop() method to remove item from a list at specified position or index
#the syntax is var_list.pop(position/index)
var_cars_list =["Tesla","Mazda","Toyota","BMW","Proton"]
print("the list of car before one is removed is :",var_cars_list)
#remove the second position which is 1 at index
var_cars_list.pop(1)
print("the list of car after one is removed is :",var_cars_list)

#Remove all the list items one by one using for loop and pop() method
print("length of cars is :", len(var_cars_list))

var_num_list=[1,2,3,4,5,6,7]

"""
k=0
for i in range(0,len(var_num_list)):
  var_num_list.pop(k)
  print("all the car list items was removed :", var_num_list)
  k=k+1
"""
#the problem of the above code is that the k is zero at the first round while the rest is always incremented by one 
# and removes the second value with 1 index number. note when you remove an item the index will be updated, therefore, 
# the k continue its incrementing and remove the second item from newly updated list items which have new index value. 
# the second item is removed during third iteration which is item 5, then 7 as iteration 3. this time the list has three
# items and k has made the fourth increment which is out of range in terms of index number pop() has .

#Alterative method of removing all list items one by is as folows. note keep the k=0 an not make any incrementation this procedure only deletes the first item always
#the items will be removed from left to right, the one which come the left are removed
k=0
for i in range(0,len(var_num_list)):
 var_num_list.pop(k)
 print("all the number list items was removed from left to right :", var_num_list)

#how to remove list items one by one and all the items to be removed from right to left, the one which stays the right are removed

var_dec_list=[1.1,2.2,3.3,4.4,5.5,6.6,7.7]
print("all the decimal number list before was removed :", var_dec_list)
k=len(var_dec_list)-1#you must deduct one becouse the length is 7 but the index is 6 so we target the index by deducting the 1 from the length value otherwise it will be trigering an error
for i in range(0,len(var_dec_list)):
 var_dec_list.pop(k)
 print("all the number list items was removed from right to left :", var_dec_list)
 k=k-1

"""
if k!=len(var_cars_list):
    for i in range(0,len(var_cars_list)):
     var_cars_list.pop(i)
     print("all the car list items was removed :", var_cars_list)"""

#List pop at index that is well out of range - throws an error
#this is not like the insert() method which can insert an item in list even if the specified location is out of range,
#while the pop() method removes a target item, so if you try to remove an item at a position that soes not exist is considered an error in python.
#what you want to remove must exist and you must define a position that is exist
"""var_cars_list.pop(4)
print("the list of car after one is removed is :",var_cars_list)"""

#How to remove a list item from a list
# we use remove() method to remove the first item of the element appeared that match the specified value.
#for example you have a list of names of people and you want to remove one from the list, note some of the names are duplicate or occur several times in the list
var_names_list =["Jack","Mike","Fatah","Owen","Lucas","Omar","Fatah"]#the Fatah has appeared two times, so lets remove one by specifying value
print("the list names is :",var_names_list)
var_names_list.remove("Fatah")#this removes the first apeared Fatah from the list
print("We removed the Fatah from the list and the current list is :",var_names_list)



#let me show you how we did it before using a loop
index_value=len(var_names_list)-1
size_value=len(var_names_list)
reversed_list_names =[]
for i in range(len(var_names_list)):
    print("the reveresed list names of names is:              ", var_names_list[index_value])
    reversed_list_names.append(var_names_list[index_value])
    #reversed_list_names.insert(index_value, var_names_list[index_value])
    index_value=index_value-1

print("before reversing all the names of the list items is:   ",var_names_list)
print("after reversed all the names wihtout using reverse is: ",reversed_list_names)
#the above process is long and complex to reverse a list items, the following can do as well in easy way


#how to reverse a list items using a list method called reverse()
#the reverse() method reverses the order of the list
var_names_list.reverse()
print("after reversed all the names using reverse method is:  ",var_names_list)

#what happens if you use the reverse() method inside the print() method: it prints none
print("after reversed all the names using reverse method is: ",var_names_list.reverse())
"""The list is being reversed. But list.reverse reverses in place, and does not return anything to the caller. You can verify this by printing the list after calling reverse on it: [source statckoveflow]"""

"""You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. This is a design principle for all mutable data structures in Python. source statckoveflow]"""
print(var_names_list.insert(2,"jamal"))# this is also same and it can not return to the caller, but the effect has done, which means the value was inserted
print(var_names_list)# check this to see whether the effect has done or not


#how to sort the list items in python
#we use sort() method to sort list items in a list
var_names_list.sort()
print("the sorted items in the list is :",var_names_list)# i noticed that if a list has string some starting small letter and some with capital letter the string starting from small letters are ranked at the end
"""The sort() method sorts the list ascending by default.
You can also make a function to decide the sorting criteria(s). [source w3schools]"""
"""the stntax of sort is 
list.sort(reverse=True|False, key=myFunc

Parameter	       Description
reverse	           Optional. reverse=True will sort the list descending. Default is reverse=False
key	               Optional. A function to specify the sorting criteria(s)
"""

var_names_list.sort(reverse=True)
print(var_names_list)

var_names_list.sort(reverse=False)# this is same as the      -----var_names_list.sort()-----
print(var_names_list)

#more practice of the sort() method is required


#can we use count method to count the number of times an item appears in a list
var_list_count=[1,2,3,4,44,55,44,33,44,33,2,2,8]
print("the item 44 appeared in the list ",var_list_count.count(44)," times")

#can we sort list with number items
var_list_count.sort()
print(var_list_count)#output: [1, 2, 2, 2, 3, 4, 8, 33, 33, 44, 44, 44, 55]