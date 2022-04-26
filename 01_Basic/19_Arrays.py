# An array is a special variable, which can hold more than one value at a time.
#  If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:
#     car1 = "Ford"
#     car2 = "Volvo"
#     car3 = "BMW"


#  Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]
print(cars)


# Access the Elements of an Array *************************************************************************************
#   You refer to an array element by referring to the index number.

#   Get the value of the first array item:
x = cars[0]
print(x)


#  The Length of an Array **********************************************************************************************
#  Use the len() method to return the length of an array (the number of elements in an array).

x = len(cars)
print(x)


# Looping Array Elements**********************************************************************************************
#   You can use the for in loop to loop through all the elements of an array.
for x in cars:
  print(x)

# Adding Array Elements *********************************************************************************************
#  You can use the append() method to add an element to an array.
cars.append("Honda")
print(cars)


# Removing Array Elements *******************************************************************************************
#   You can use the pop() method to remove an element from the array.
cars.pop(1)
print (cars)