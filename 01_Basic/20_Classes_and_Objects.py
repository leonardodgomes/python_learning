# Python Classes/Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# To create a class, use the keyword class:
class MyClass:
  x = 5


# Create Object ************************************************************************************

#Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)



# The __init__() Function *************************************************************************************
#  » The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
#  » To understand the meaning of classes we have to understand the built-in __init__() function.
#  » All classes have a function called __init__(), which is always executed when the class is being initiated.
#  » Use the __init__() function to assign values to object properties, or other operations that are necessary to
#    do when the object is being created:

# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# Object Methods **************************************************************************************************
# Objects can also contain methods. Methods in objects are functions that belong to the object.

#   Let us create a method in the Person class:
#   Insert a function that prints a greeting, and execute it on the p1 object:

class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc1(self):
    print("Hello my name is " + self.name)

p1 = Person1("John", 36)
p1.myfunc1()

# Modify Object Properties ************************************************************************************************
#  You can modify properties on objects like this:

#   Set the age of p1 to 40:
p1.age = 40
p1.myfunc3()


# Delete Object Properties***********************************************************************************************
#  You can delete properties on objects by using the del keyword:

#Delete the age property from the p1 object:
del p1.age


# Delete Objects ******************************************************************************************************
#  You can delete objects by using the del keyword:

#Delete the p1 object:
del p1