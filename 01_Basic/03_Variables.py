# Variables are containers for storing data values.

#Creating Variables

x = 5
v_name = "Leo"

print (x)
print (v_name)


#Output Variables
    #The Python print statement is often used to output variables.
    #To combine both text and a variable, Python uses the + character:

first_name = "Leonardo"
last_name = "Gomes"
full_name = first_name + " " + last_name
print(full_name)


a = 'Hamed'
b = 'Mark'
if(a!=b):
    print("Not equal")
else:
    print("Equal")



#Global Variables
    #Variables that are created outside of a function (as in all of the examples above) are known as global variables.
    #Global variables can be used by everyone, both inside of functions and outside.

n = 'n is a global variable'

def myfunction():
    h = ' h is a local variables'
    text = n + "|" + h
    print(text)

myfunction()
