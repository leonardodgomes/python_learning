# RegEx
#  A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#  RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.
# Import the re module: import re


# RegEx in Python*********************************************************************************************

#Search the string to see if it starts with "The" and ends with "Spain":

import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


# RegEx Functions************************************************************************************************
# The re module offers a set of functions that allows us to search a string for a match:

#  Function	        Description
#  findall	        Returns a list containing all matches
#  search	        Returns a Match object if there is a match anywhere in the string
#  split	        Returns a list where the string has been split at each match
#  sub	            Replaces one or many matches with a string

# Metacharacters*************************************************************************************************
# Metacharacters are characters with a special meaning:

#  Character    - Description - Example
#  []           - A set of characters                           - "[a-m]"           |  Find all lower case characters alphabetically between "a" and "m":
#  \            - Signals a special sequence                     - "\d"             |  Find all digit characters:
#  .            - Any character (except newline character)      - "he..o"           |  Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
#  ^            - Starts with                                   - "^hello"          |  Check if the string starts with 'hello':
#  $            - Ends with                                     - "planet$"         |  Check if the string ends with 'planet':
#  *            - Zero or more occurrences                      - "he.*o"           |  Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
#  +            - One or more occurrences                       - "he.+o"           |  Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
#  ?            - Zero or one occurrences                       - "he.?o"           |  Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
#  {}           - Exactly the specified number of occurrences   - "he.{2}o"         |  Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
#  |            - Either or                                     - "falls|stays"     |  Check if the string contains either "falls" or "stays":
#  ()           - Capture and group


# Special Sequences*****************************************************************************************
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

#  Character    - Description                                                                                                                               - Example
#  \A           - Returns a match if the specified characters are at the beginning of the string                                                            - "\AThe"       | Check if the string starts with "The":
#  \b           - Returns a match where the specified characters are at the beginning or at the end of a word                                               - r"\bain"      | Check if "ain" is present at the beginning of a WORD:
#               - (the "r" in the beginning is making sure that the string is being treated as a "raw string")                                              - r"ain\b"      | Check if "ain" is present at the end of a WORD:
#  \B           - Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word                            - r"\Bain"      | Check if "ain" is present, but NOT at the beginning of a word:
#               - (the "r" in the beginning is making sure that the string is being treated as a "raw string")                                              - r"ain\B"      | Check if "ain" is present, but NOT at the end of a word:
#  \d           - Returns a match where the string contains digits (numbers from 0-9)                                                                       - "\d"          | Check if the string contains any digits (numbers from 0-9):
#  \D           - Returns a match where the string DOES NOT contain digits                                                                                  - "\D"          | Return a match at every no-digit character:
#  \s           - Returns a match where the string contains a white space character                                                                         - "\s"          | Return a match at every white-space character:
#  \S           - Returns a match where the string DOES NOT contain a white space character                                                                 - "\S"          | Return a match at every NON white-space character:
#  \w           - Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)   - "\w"          | Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
#  \W           - Returns a match where the string DOES NOT contain any word characters                                                                     - "\W"          | Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
#  \Z           - Returns a match if the specified characters are at the end of the string                                                                  - "Spain\Z"     | Check if the string ends with "Spain":


# Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning:

# Set	        Description	                                                                                | Example
# [arn]	        Returns a match where one of the specified characters (a, r, or n) are present	            | Check if the string has any a, r, or n characters:
# [a-n]	        Returns a match for any lower case character, alphabetically between a and n                | Check if the string has any characters between a and n:	
# [^arn]	    Returns a match for any character EXCEPT a, r, and n	                                    | Check if the string has other characters than a, r, or n
# [0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present	            | Check if the string has any 0, 1, 2, or 3 digits
# [0-9]	        Returns a match for any digit between 0 and 9	                                            | Check if the string has any digits
# [0-5][0-9]    Returns a match for any two-digit numbers from 00 and 59	                                | Check if the string has any two-digit numbers, from 00 to 59
# [a-zA-Z]	    Returns a match for any character alphabetically between a and z, lower case OR upper case	| Check if the string has any characters from a to z lower case, and A to Z upper case
# [+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string	| Check if the string has any + characters



# The findall() Function ************************************************************************************************
# The findall() function returns a list containing all matches.

#Print a list of all matches:

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#The list contains the matches in the order they are found.
# If no matches are found, an empty list is returned:
# Return an empty list if no match was found:

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


# The search() Function ********************************************************************************************
#  The search() function searches the string for a match, and returns a Match object if there is a match.
#  If there is more than one match, only the first occurrence of the match will be returned:

#Search for the first white-space character in the string:

import re

txt = "The rain in Spain"
x = re.search(r"\s", txt)

print("The first white-space character is located in position:", x.start())


#If no matches are found, the value None is returned:
# Make a search that returns no match:

txt1 = "The rain in Spain"
x = re.search("Portugal", txt1)
print(x)


# The split() Function *********************************************************************************
#  The split() function returns a list where the string has been split at each match:

#Split at each white-space character:

import re

txt2 = "The rain in Spain"
x2 = re.split(r"\s", txt2)
print(x2)

#You can control the number of occurrences by specifying the maxsplit parameter:
#Split the string only at the first occurrence:

txt3 = "The rain in Spain"
x3 = re.split(r"\s", txt3, 1)
print(x3)



# The sub() Function***************************************************************************************************
# The sub() function replaces the matches with the text of your choice:
# Replace every white-space character with the number 9:

import re

txt4 = "The rain in Spain"
x4 = re.sub(r"\s", "9", txt4)
print(x4)

# You can control the number of replacements by specifying the count parameter:

# Replace the first 2 occurrences:

txt5 = "The rain in Spain"
x5 = re.sub(r"\s", "9", txt5, 2)
print(x5)



# Match Object ******************************************************************************************************
#  A Match Object is an object containing information about the search and the result.
#  Note: If there is no match, the value None will be returned, instead of the Match Object.

# Example, Do a search that will return a Match Object:

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

#The Match object has properties and methods used to retrieve information about the search, and the result:
#  .span() returns a tuple containing the start-, and end positions of the match.
#  .string returns the string passed into the function
#  .group() returns the part of the string where there was a match


# Example
# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


# Example
# Print the string passed into the function:

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


# Example
# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())


#Note: If there is no match, the value None will be returned, instead of the Match Object.