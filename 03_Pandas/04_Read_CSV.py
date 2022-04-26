# Read CSV Files
# A simple way to store big data sets is to use CSV files (comma separated files).
# CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

# Example, Load a comma separated file (CSV file) into a DataFrame:
import pandas as pd
df = pd.read_csv('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\03_Pandas\\00_Files\\data.csv')
print(df) 
print(df.to_string())  # Tip: use to_string() to print the entire DataFrame.



# max_rows **********************************************************************************************************
# The number of rows returned is defined in Pandas option settings.
# You can check your system's maximum rows with the pd.options.display.max_rows statement.

#Example, Check the number of maximum returned rows:
import pandas as pd
print(pd.options.display.max_rows) 


# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
# You can change the maximum rows number with the same statement.

#  Example, Increase the maximum number of rows to display the entire DataFrame:
import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\03_Pandas\\00_Files\\data.csv')
print(df) 


# How to read a file with a semi colon separator in pandas
    # data = read_csv(csv_path, sep=';')