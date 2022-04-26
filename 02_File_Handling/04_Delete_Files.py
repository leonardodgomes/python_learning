#Delete File
# To delete a file, you must import the OS module, and run its os.remove() function:

# Example, Remove the file "filetodelete.txt":****************************************************************

# Create a new file first:
fl = open("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\filetodelete.txt", "x")
fl.close()

import os
os.remove("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\filetodelete.txt")


# Check if File exist: ***************************************************************************************
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

# Example, Check if file exists, then delete it:

import os
if os.path.exists("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\filetodelete.txt"):
  os.remove("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\filetodelete.txt")
else:
  print("The file does not exist")


# CreateFolder **********************************************************************************************************
# Python program to explain os.mkdir() method

import os

directory = "foldertodelete" # Directory
parent_dir = "C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\" # Parent Directory path  
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print("Directory '% s' created" % directory)


# Delete  Folder **********************************************************************************************************
#  To delete an entire folder, use the os.rmdir() method:

import os
os.rmdir("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\02_File_Handling\\00_Files\\foldertodelete")
#Note: You can only remove empty folders.
print("Directory '% s' deleted" % directory)