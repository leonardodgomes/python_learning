# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".

#Assign String to a Variable *******************************************************************
print("Assign String to a Variable")
a = "a = Hello"
print(a)

#Multiline Strings *****************************************************************************
#"You can assign a multiline string to a variable by using three quotes:
print("Multiline Strings")
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)


#Slicing Strings *******************************************************************************
print("Slicing Strings")
b = "Hello, World!"
print(b[2:5]) #The first character has index 0.

c = "Hello, World!"
print(c[2:]) #Slice To the End


b = "Hello, World!"
print(b[-5:-2]) #Use negative indexes to start the slice from the end of the string


#Modify Strings *******************************************************************************
#Python has a set of built-in methods that you can use on strings.


print("Modify Strings - Upper Case")
d = "Hello, World!"
print(d.upper())

print("Modify Strings - Lower Case")
e = "Hello, World!"
print(e.lower())

print("Modify Strings - Remove Whitespace")
f = " Hello, World! "
print(f.strip()) # returns "Hello, World!"

print("Modify Strings - Replace String")
g = "Hello, World!"
print(g.replace("H", "J"))

print("Modify Strings - Split String")
h = "Hello, World!"
print(h.split(",")) # returns ['Hello', ' World!']


#String Concatenation **************************************************************************
#To concatenate, or combine, two strings you can use the + operator
name = "Leonardo"
last_name = "Gomes"
full_name = name + " " + last_name
print(full_name)


 #Format - Strings *****************************************************************************
 #As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
    #age = 36
    #txt = "My name is John, I am " + age
    #print(txt) # TypeError: must be str, not int

#Use the format() method to insert numbers into strings:  
print("Format - Strings")
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#Escape Character **********************************************************************************
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
txt2 = "We are the so-called \"Vikings\" from the north."
print(txt2)

#String Methods ***********************************************************************************
#  Python has a set of built-in methods that you can use on strings.
#  Note: All string methods returns new values. They do not change the original string.

# Method            | Description
# capitalize()      | Converts the first character to upper case
# casefold()        | Converts string into lower case
# center()          | Returns a centered string
# count()           | Returns the number of times a specified value occurs in a string
# encode()          | Returns an encoded version of the string
# endswith()        | Returns true if the string ends with the specified value
# expandtabs()      | Sets the tab size of the string
# find()            | Searches the string for a specified value and returns the position of where it was found
# format()          | Formats specified values in a string
# format_map()      | Formats specified values in a string
# index()           | Searches the string for a specified value and returns the position of where it was found
# isalnum()         | Returns True if all characters in the string are alphanumeric
# isalpha()         | Returns True if all characters in the string are in the alphabet
# isdecimal()       | Returns True if all characters in the string are decimals
# isdigit()         | Returns True if all characters in the string are digits
# isidentifier()    | Returns True if the string is an identifier
# islower()         | Returns True if all characters in the string are lower case
# isnumeric()       | Returns True if all characters in the string are numeric
# isprintable()     | Returns True if all characters in the string are printable
# isspace()         | Returns True if all characters in the string are whitespaces
# istitle()         | Returns True if the string follows the rules of a title
# isupper()         | Returns True if all characters in the string are upper case
# join()            | Joins the elements of an iterable to the end of the string
# ljust()           | Returns a left justified version of the string
# lower()           | Converts a string into lower case
# lstrip()          | Returns a left trim version of the string
# maketrans()       | Returns a translation table to be used in translations
# partition()       | Returns a tuple where the string is parted into three parts
# replace()         | Returns a string where a specified value is replaced with a specified value
# rfind()           | Searches the string for a specified value and returns the last position of where it was found
# rindex()          | Searches the string for a specified value and returns the last position of where it was found
# rjust()           | Returns a right justified version of the string
# rpartition()      | Returns a tuple where the string is parted into three parts
# rsplit()          | Splits the string at the specified separator, and returns a list
# rstrip()          | Returns a right trim version of the string
# split()           | Splits the string at the specified separator, and returns a list
# splitlines()      | Splits the string at line breaks and returns a list
# startswith()      | Returns true if the string starts with the specified value
# strip()           | Returns a trimmed version of the string
# swapcase()        | Swaps cases, lower case becomes upper case and vice versa
# title()           | Converts the first character of each word to upper case
# translate()       | Returns a translated string
# upper()           | Converts a string into upper case
# zfill()           | Fills the string with a specified number of 0 values at the beginning
