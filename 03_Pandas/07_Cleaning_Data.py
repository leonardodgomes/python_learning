# Data Cleaning
# Data cleaning means fixing bad data in your data set.
#   Bad data could be:
#     » Empty cells
#     » Data in wrong format
#     » Wrong data
#     » Duplicates



# Cleaning Empty Cells**************************************************************************************************

# Empty cells can potentially give you a wrong result when you analyze data.

# Remove Rows ************************************
#   One way to deal with empty cells is to remove rows that contain empty cells.
#   This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

#   Example, Return a new Data Frame with no empty cells:
import pandas as pd

df = pd.read_csv('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\03_Pandas\\00_Files\\dirtydata.csv')

new_df = df.dropna()

print(new_df.to_string()) # Notice in the result that some rows have been removed (row 18, 22 and 28). These rows had cells with empty values.



# Replace Empty Values ***************************************

#   Another way of dealing with empty cells is to insert a new value instead.
#   This way you do not have to delete entire rows just because of some empty cells.
#   The fillna() method allows us to replace empty cells with a value:

#   Example, Replace NULL values with the number 130:

import pandas as pd

df = pd.read_csv('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\03_Pandas\\00_Files\\dirtydata.csv')

df.fillna(130, inplace = True)


# Replace Only For Specified Columns
#  The example above replaces all empty cells in the whole Data Frame.
#  To only replace empty values for one column, specify the column name for the DataFrame:

# Example, Replace NULL values in the "Calories" columns with the number 130:

import pandas as pd

df = pd.read_csv('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\03_Pandas\\00_Files\\dirtydata.csv')

df["Calories"].fillna(130, inplace = True) #Notice in the result: empty cells got the value 130 (in row 18, 22 and 28).



# Replace Using Mean, Median, or Mode ********************************

#  A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
#  Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

#     Example, Calculate the MEAN, and replace any empty values with it:
import pandas as pd

df = pd.read_csv('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\03_Pandas\\00_Files\\dirtydata.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True) # Mean = the average value (the sum of all values divided by number of values).
# As you can see in row 18 and 28, the empty values from "Calories" was replaced with the mean: 304.68


#     Example, Calculate the MEDIAN, and replace any empty values with it:

import pandas as pd

df = pd.read_csv('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\03_Pandas\\00_Files\\dirtydata.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True) # Median = the value in the middle, after you have sorted all values ascending.
#As you can see in row 18 and 28, the empty values from "Calories" was replaced with the median: 291.2


#     Example,  Calculate the MODE, and replace any empty values with it:

import pandas as pd

df = pd.read_csv('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\03_Pandas\\00_Files\\dirtydata.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True) # Mode = the value that appears most frequently.
#As you can see in row 18 and 28, the empty value from "Calories" was replaced with the mode: 300.





# Cleaning Data of Wrong Format **********************************************************************************************
#   Data of Wrong Format
#   Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
#   To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
print("Cleaning Data of Wrong Format***************************************************************")
# Example, Convert to date:

import pandas as pd

df = pd.read_csv('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\03_Pandas\\00_Files\\dirtydata.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())


#   Removing Rows******************************
#    The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.

# Example, Remove rows with a NULL value in the "Date" column:
import pandas as pd

df = pd.read_csv('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\03_Pandas\\00_Files\\dirtydata.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.dropna(subset=['Date'], inplace = True)

print(df.to_string())


# Removing Duplicates **************************************************************************************************

# Discovering Duplicates *******************************
#   Duplicate rows are rows that have been registered more than one time.
#   By taking a look at our test data set, we can assume that row 11 and 12 are duplicates.
#   To discover duplicates, we can use the duplicated() method.
#   The duplicated() method returns a Boolean values for each row:

# Example: Returns True for every row that is a duplicate, othwerwise False:
print('Removing Duplicates ************')
import pandas as pd

df = pd.read_csv('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\03_Pandas\\00_Files\\dirtydata.csv')
print(df.duplicated())


# Removing Duplicates *********************************
# To remove duplicates, use the drop_duplicates() method.

# Example: Remove all duplicates:

df.drop_duplicates(inplace = True)
print(df.to_string())