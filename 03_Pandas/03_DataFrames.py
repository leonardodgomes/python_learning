# DataFrame
#  A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

#  Example, Create a simple Pandas DataFrame:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 



# Locate Row **********************************************************************************************************************
# As you can see from the result above, the DataFrame is like a table with rows and columns.
# Pandas use the loc attribute to return one or more specified row(s)

#Example, Return row 0:
#refer to the row index:
print(df.loc[0])

#Example, Return row 0 and 1:
#use a list of indexes:
print(df.loc[[0, 1]])



# Named Indexes ************************************************************************************************************
# With the index argument, you can name your own indexes.

#  Example, Add a list of names to give each row a name:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 


# Locate Named Indexes *******************************************************************************************************
# Use the named index in the loc attribute to return the specified row(s).
print("Locate Named Indexe")
#Example, Return "day2":
#refer to the named index:
print(df.loc["day2"])



# Load Files Into a DataFrame*************************************************************************************************
# If your data sets are stored in a file, Pandas can load them into a DataFrame.

# Example, Load a comma separated file (CSV file) into a DataFrame:
import pandas as pd
df = pd.read_csv('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\03_Pandas\\00_Files\\data.csv')
print(df) 