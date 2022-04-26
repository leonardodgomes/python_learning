# Modules consider a module to be the same as a code library.
#   A file containing a set of functions you want to include in your application.


#Create a Module ***************************************************************************************************
# To create a module just save the code you want in a file with the file extension .py:

# 24_Mymodule.py


#Use a Module
# Now we can use the module we just created, by using the import statement:

# Import the module named mymodule, and call the greeting function:

import Mymodule

Mymodule.greeting("Leonardo")


# Variables in Module ******************************************************************************************************
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

#Save this code in the file mymodule.py

#person1 = {
#  "name": "John",
#  "age": 36,
#  "country": "Norway"
#}

#Import the module named mymodule, and access the person1 dictionary:

import Mymodule

a = Mymodule.person1["age"]
print(a)



# Naming a Module *******************************************************************************************
#  You can name the module file whatever you like, but it must have the file extension .py
# You can create an alias when you import a module, by using the as keyword:

#Create an alias for mymodule called mx:

import Mymodule as mx

a = mx.person1["age"]
print(a)


# Built-in Modules ***************************************************************************************************
#  There are several built-in modules in Python, which you can import whenever you like.

#Import and use the platform module:

import platform

x = platform.system()
print(x)


# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

#List all the defined names belonging to the platform module:

x = dir(platform) #The dir() function can be used on all modules, also the ones you create yourself.
print(x)


