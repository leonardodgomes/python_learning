#Tuple
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.

thistuple = ("apple", "banana", "cherry")
print(thistuple)


#Access Tuple Items ***********************************************************************************************

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1])

# Negative Indexing 
print(thistuple[-1])

# Range of Indexes
print(thistuple[2:5])
print(thistuple[:4]) # By leaving out the start value, the range will start at the first item
print(thistuple[2:]) # By leaving out the end value, the range will go on to the end of the list
print(thistuple[-4:-1]) # Specify negative indexes if you want to start the search from the end of the tuple:


# Check if Item Exists
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


# Change Tuple Values ***********************************************************************************************
#  Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#  But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(y)

# Unpacking a Tuple
#  When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#  But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#  Using Asterisk*
#  If the number of variables is less than the number of values, you can add an * to the variable name and
#  the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


# Loop Through a Tuple *********************************************************************************************

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#  Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


# Join Two Tuples ***********************************************************************************************************

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#  Multiply Tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)