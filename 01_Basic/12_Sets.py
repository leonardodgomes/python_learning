#Set
#  Sets are used to store multiple items in a single variable.
#  Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
#  A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)


# Access Items ***********************************************************************************************
#   You cannot access items in a set by referring to an index or a key.
#   But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


print("banana" in thisset) #Check if "banana" is present in the set


# Add Items***************************************************************************************************
#  Once a set is created, you cannot change its items, but you can add new items.


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


#   To add items from another set into the current set, use the update() method.
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

print(thisset)


# Remove Set Items *******************************************************************************************

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

print(thisset)  #Note: If the item to remove does not exist, remove() will raise an error.

#  Remove the last item by using the pop() method:

thisset = {"apple", "banana", "cherry"}
x = thisset.pop() #You can also use the pop() method to remove an item, but this method will remove the last item.
print(x)
print(thisset)

#  The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()

print(thisset)


#The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset


# Loop Sets ******************************************************************************************************

thissetloop = {"apple", "banana", "cherry"}

for x in thissetloop:
  print(x)


 # Join Sets *****************************************************************************************************

 # The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.

#Keep the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#  Keep All, But NOT the Duplicates
#  The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

#  Keep the items that are not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)



