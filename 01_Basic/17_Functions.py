# Functions
#   A function is a block of code which only runs when it is called.
#   You can pass data, known as parameters, into a function.
#   A function can return data as a result.

# Creating a Function ******************************************************************************************
#  In Python a function is defined using the def keyword:

def my_function():
  print("Hello from a function")

# Calling a Function ********************************************************************************************
#  To call a function, use the function name followed by parenthesis:

def my_function2():
  print("Hello from a function")

my_function2()


# Arguments ***************************************************************************************************
#  » Information can be passed into functions as arguments.
#  » Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want,
#    just separate them with a comma.
#  » The following example has a function with one argument (fname). When the function is called, we pass along a first name,
#    which is used inside the function to print the full name:

def my_function3(fname):
  print(fname + " Refsnes")

my_function3("Emil")
my_function3("Tobias")
my_function3("Linus")

# note: The terms parameter and argument can be used for the same thing: information that are passed into a function.


# Number of Arguments *********************************************************************************************
#  » By default, a function must be called with the correct number of arguments. Meaning that if your function expects
#    2 arguments, you have to call the function with 2 arguments, not more, and not less.

# This function expects 2 arguments, and gets 2 arguments:

def my_function4(fname, lname):
  print(fname + " " + lname)

my_function4("Emil", "Refsnes")  #This function expects 2 arguments, but if gets only 1 you will get an error


# Arbitrary Arguments, *args *****************************************************************************************
#  » If you do not know how many arguments that will be passed into your function, add a * before the parameter
#    name in the function definition.
#  » This way the function will receive a tuple of arguments, and can access the items accordingly:

#If the number of arguments is unknown, add a * before the parameter name:

def my_function5(*kids):
  print("The youngest child is " + kids[2])

my_function5("Emil", "Tobias", "Linus")


# Keyword Arguments *********************************************************************************************
#  » You can also send arguments with the key = value syntax.
#  » This way the order of the arguments does not matter.

def my_function6(child3, child2, child1):
  print("The youngest child is " + child1)

my_function6(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



# Arbitrary Keyword Arguments, **kwargs *************************************************************************
#  » If you do not know how many keyword arguments that will be passed into your function,
#    add two asterisk: ** before the parameter name in the function definition.
#  » This way the function will receive a dictionary of arguments, and can access the items accordingly:

#  If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function7(**kid):
  print("His last name is " + kid["lname"])

my_function7(fname = "Tobias", lname = "Refsnes")



# Default Parameter Value *************************************************************************************
#  » The following example shows how to use a default parameter value.
#  » If we call the function without argument, it uses the default value:

def my_function8(country = "Norway"):
  print("I am from " + country)

my_function8("Sweden")
my_function8("India")
my_function8()
my_function8("Brazil")


# Passing a List as an Argument
#  » You can send any data types of argument to a function (string, number, list, dictionary etc.),
#    and it will be treated as the same data type inside the function.
#  » E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def my_function9(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function9(fruits)


# Return Values *********************************************************************************************
#  » To let a function return a value, use the return statement:

def my_function10(x):
  return 5 * x

print(my_function10(3))
print(my_function10(5))
print(my_function10(9))


# The pass Statement*****************************************************************************************
#  » function definitions cannot be empty, but if you for some reason have a function definition with no content,
#    put in the pass statement to avoid getting an error.

def myfunction():
  pass


# Recursion *******************************************************************************************************
#   » Python also accepts function recursion, which means a defined function can call itself.
#   » Recursion is a common mathematical and programming concept. It means that a function calls itself.
#     This has the benefit of meaning that you can loop through data to reach a result.
#   » The developer should be very careful with recursion as it can be quite easy to slip into writing a
#     function which never terminates, or one that uses excess amounts of memory or processor power.
#     However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
#   » In this example, tri_recursion() is a function that we have defined to call itself ("recurse").
#     We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when
#     the condition is not greater than 0 (i.e. when it is 0).

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(2)



# Program to print the fibonacci series upto n_terms
def recursive_fibonacci(n):
   if n <= 1:
       return n
   else:
       return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
   
n_terms = 10
   
# check if the number of terms is valid
if n_terms <= 0:
   print("Invalid input ! Please input a positive value")
else:
   print("Fibonacci series:")
   for i in range(n_terms):
       print(recursive_fibonacci(i))



