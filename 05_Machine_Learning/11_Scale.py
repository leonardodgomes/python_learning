# Scale Features

#  When your data has different values, and even different measurement units, it can be difficult to compare them. What 
#  is kilograms compared to meters? Or altitude compared to time?

# The answer to this problem is scaling. We can scale data into new values that are easier to compare.

# Take a look at the table below, it is the same data set that we used in the multiple regression chapter, but this
# time the volume column contains values in liters instead of cm3 (1.0 instead of 1000).

# Car	        Model	    Volume	Weight	    CO2	
# Toyota	    Aygo	    1.0	    790	        99
# Mitsubishi	Space Star	1.2	    1160	    95
# Skoda	        Citigo	    1.0	    929	        95
# Fiat	        500	        0.9	    865	        90
# Mini	        Cooper	    1.5	    1140	    105
# VW	        Up!	        1.0	    929	        105
# Skoda	        Fabia	    1.4	    1109	    90
# Mercedes	    A-Class	    1.5	    1365	    92
# Ford	        Fiesta	    1.5	    1112	    98
# Audi	        A1	        1.6	    1150	    99
# Hyundai	    I20	        1.1	    980	        99
# Suzuki	    Swift	    1.3	    990	        101
# Ford	        Fiesta	    1.0	    1112	    99
# Honda	        Civic	    1.6	    1252	    94

# It can be difficult to compare the volume 1.0 with the weight 790, but if we
# scale them both into comparable values, we can easily see how much one value is compared to the other.

# There are different methods for scaling data, in this tutorial we will use a method called standardization.

# The standardization method uses this formula:
#    z = (x - u) / s
# Where z is the new value, x is the original value, u is the mean and s is the standard deviation.

# If you take the weight column from the data set above, the first value is 790, and the scaled value will be:
#    (790 - 1292.23) / 238.74 = -2.1

# If you take the volume column from the data set above, the first value is 1.0, and the scaled value will be:
#    (1.0 - 1.61) / 0.38 = -1.59

# Now you can compare -2.1 with -1.59 instead of comparing 790 with 1.0.

# You do not have to do this manually, the Python sklearn module has a method called StandardScaler() which returns 
# a Scaler object with methods for transforming data sets.

# Example: Scale all values in the Weight and Volume columns:

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Work\\Python\\05_Machine_Learning\\00_Files\\cars2.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)


# Predict CO2 Values ********************************************************************************************************

# The task in the Multiple Regression chapter was to predict the CO2 emission from a car when you only knew its weight and volume.

# When the data set is scaled, you will have to use the scale when you predict values:

# Example: Predict the CO2 emission from a 1.3 liter car that weighs 2300 kilograms:

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Work\\Python\\05_Machine_Learning\\00_Files\\cars2.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)