#List
#  Lists are used to store multiple items in a single variable.
#  Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#  Lists are created using square brackets:

thislist = ["apple", "banana", "cherry"]
print(thislist)


#Allow Duplicates *********************************************************************************************
#   Since lists are indexed, lists can have items with the same value:
#   Example, Lists allow duplicate values:

thislistduplic = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislistduplic)



# List Length ************************************************************************************************
#   To determine how many items a list has, use the len() function:

thislistlen = ["apple", "banana", "cherry"]
print(len(thislistlen))


# Data Types ************************************************************************************************
#   List items can be of any data type:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#  A list can contain different data types:
list4 = ["abc", 34, True, 40, "male"]
print(list4)


#The list() Constructor  ***********************************************************************************
#   It is also possible to use the list() constructor when creating a new list.

thislistconst = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislistconst)


#Access Items **********************************************************************************************
#   List items are indexed and you can access them by referring to the index number:

thislistacc = ["apple", "banana", "cherry"]
print(thislistacc[1])

#   Negative indexing means start from the end
thislistaccneg = ["apple", "banana", "cherry"]
print(thislistaccneg[-1])

#   You can specify a range of indexes by specifying where to start and where to end the range.
thislistrng = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislistrng[2:5])


#Change List Items *******************************************************************************************

thislistcng = ["apple", "banana", "cherry"]
thislistcng[1] = "blackcurrant"
print(thislistcng)


#   To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
thislistcngrng = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislistcngrng[1:3] = ["blackcurrant", "watermelon"]
print(thislistcngrng)


#   Add List Items append()
thislistapp = ["apple", "banana", "cherry"]
thislistapp.append("orange")
print(thislistapp)

#   To insert a list item at a specified index, use the insert() method.
thislistins = ["apple", "banana", "cherry"]
thislistins.insert(1, "orange")
print(thislistins)

#   To append elements from another list to the current list, use the extend() method.
thislistext = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislistext.extend(tropical)
print(thislistext)

#   The remove() method removes the specified item.
thislistrem = ["apple", "banana", "cherry"]
thislistrem.remove("banana")
print(thislistrem)


#  The pop() method removes the specified index.
thislistremspec = ["apple", "banana", "cherry"]
thislistremspec.pop(1) # If you do not specify the index, the pop() method removes the last item.
print(thislistremspec)

# Clear the List
thislistcle = ["apple", "banana", "cherry"]
thislistcle.clear()
print(thislistcle)


#Loop Through a List *********************************************************************************************
#   You can loop through the list items by using a for loop:
thislistloop = ["apple", "banana", "cherry"]
for x in thislistloop:
  print(x)

#   You can also loop through the list items by referring to their index number.
#   Use the range() and len() functions to create a suitable iterable.
thislistrngloop = ["apple", "banana", "cherry"]
for i in range(len(thislistrngloop)):
  print(thislistrngloop[i])


#   You can loop through the list items by using a while loop.
#   Use the len() function to determine the length of the list, then start at 0 and loop your
#   way through the list items by refering to their indexes.
thislistw = ["apple", "banana", "cherry"]
i = 0
while i < len(thislistw):
  print(thislistw[i])
  i = i + 1


# Looping Using List Comprehension *******************************************************************************
# List Comprehension offers the shortest syntax for looping through lists:
thislistcomp = ["apple", "banana", "cherry"]
[print(x) for x in thislistcomp]


#   Condition - The condition is like a filter that only accepts the items that valuate to True.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#  Iterable  - The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10)]
print(newlist)

#   Expression - The expression is the current item in the iteration, but it is also the outcome, which 
#   you can manipulate before it ends up like a list item in the new list:
newlist = [x.upper() for x in fruits]
print(newlist)


# Sort List Alphanumerically ************************************************************************************
#   List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
sortlist = ["orange", "mango", "kiwi", "pineapple", "banana"]
sortlist.sort()
print(sortlist)

#  Sort Descending - To sort descending, use the keyword argument reverse = True:
sortlistreverse = [100, 50, 65, 82, 23]
sortlistreverse.sort(reverse = True)
print(sortlistreverse)


# Copy a List ***********************************************************************************************
#    You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1,
#    and changes made in list1 will automatically also be made in list2.

copythislist = ["apple", "banana", "cherry"]
tomylist = copythislist.copy()
print(tomylist)

#   Another way to make a copy is to use the built-in method list().
copythislist = ["apple", "banana", "cherry"]
tomylist = list(copythislist)
print(tomylist)


# Join Two Lists ************************************************************************************
#   There are several ways to join, or concatenate, two or more lists in Python.
#   One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#   Another way to join two lists is by appending all the items from list2 into list1, one by one:

for x in list2:
  list1.append(x)
print(list1)

#   Or you can use the extend() method, which purpose is to add elements from one list to another list:
list1.extend(list2)
print(list1)



# List Methods ***********************************************************************************************
#   Python has a set of built-in methods that you can use on lists.

# Method	|   Description
# append()	|   Adds an element at the end of the list
# clear()	|   Removes all the elements from the list
# copy()	|   Returns a copy of the list
# count()	|   Returns the number of elements with the specified value
# extend()	|   Add the elements of a list (or any iterable), to the end of the current list
# index()	|   Returns the index of the first element with the specified value
# insert()  |	Adds an element at the specified position
# pop()     |	Removes the element at the specified position
# remove()	|   Removes the item with the specified value
# reverse()	|   Reverses the order of the list
# sort()	|   Sorts the list