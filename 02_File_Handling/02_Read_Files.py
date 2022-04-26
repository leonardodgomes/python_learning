# File Open
#  To open the file, use the built-in open() function.
#  The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\demofile.txt", "r")
print(f.read())


# Read Only Parts of the File ************************************************************************************************
#   By default the read() method returns the whole text, but you can also specify how many characters you want to return:

#   Example, return the 5 first characters of the file:

f = open("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\demofile.txt", "r")
print(f.read(5))


# Read Lines*****************************************************************************************************************
#  You can return one line by using the readline() method:
# Example, Read one line of the file:

f = open("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\demofile.txt", "r")
print(f.readline())

#  By calling readline() two times, you can read the two first lines:
f1 = open("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\demofile.txt", "r")
print(f1.readline())
print(f1.readline())


#  By looping through the lines of the file, you can read the whole file, line by line:
f = open("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\demofile.txt", "r")
for x in f:
  print(x)



# Close Files***************************************************************************************************
#  It is a good practice to always close the file when you are done with it.
#  Example, Close the file when you are finish with it:
f = open("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\demofile.txt", "r")
print(f.readline())
f.close()
#Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.