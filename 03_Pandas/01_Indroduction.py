# What is Pandas?
#    » Pandas is a Python library used for working with data sets.
#    » It has functions for analyzing, cleaning, exploring, and manipulating data.
#    » The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

# Why Use Pandas?
#    » Pandas allows us to analyze big data and make conclusions based on statistical theories.
#    » Pandas can clean messy data sets, and make them readable and relevant.
#    » Relevant data is very important in data science.

# What Can Pandas Do?
#    Pandas gives you answers about the data. Like:
#        » Is there a correlation between two or more columns?
#        » What is average value?
#        » Max value?
#        » Min value?
#    Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.

# Where is the Pandas Codebase?
#    » The source code for Pandas is located at this github repository https://github.com/pandas-dev/pandas



# Installation of Pandas****************************************************************************************************
#   If you have Python and PIP already installed on a system, then installation of Pandas is very easy.

# Install it using this command:
#     C:\Users\Your Name>pip install pandas
#     If this command fails, then use a python distribution that already has Pandas installed like, Anaconda, Spyder etc.

# Import Pandas ***********************************************************************************************************
# Once Pandas is installed, import it in your applications by adding the import keyword:

import pandas #Now Pandas is imported and ready to use.

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)



# Pandas as pd **********************************************************************************************************
#  Pandas is usually imported under the pd alias.
#    alias: In Python alias are an alternate name for referring to the same thing.

# Create an alias with the as keyword while importing:

import pandas as pd #Now the Pandas package can be referred to as pd instead of pandas.

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)


# Checking Pandas Version *************************************************************************************************
#  The version string is stored under __version__ attribute.

import pandas as pd

print(pd.__version__)