# Decision Tree

# In this chapter we will show you how to make a "Decision Tree". A Decision Tree is a Flow Chart,
# and can help you make decisions based on previous experience.

# In the example, a person will try to decide if he/she should go to a comedy show or not.

# Luckily our example person has registered every time there was a comedy show in town, and registered
# some information about the comedian, and also registered if he/she went or not.

# Age	Experience	Rank	Nationality	    Go
# 36	10	        9	    UK	            NO
# 42	12	        4	    USA	            NO
# 23	4	        6	    N	            NO
# 52	4	        4	    USA	            NO
# 43	21	        8	    USA	            YES
# 44	14	        5	    UK	            NO
# 66	3	        7	    N	            YES
# 35	14	        9	    UK	            YES
# 52	13	        7	    N	            YES
# 35	5	        9	    N	            YES
# 24	3	        5	    USA	            NO
# 18	3	        7	    UK	            YES
# 45	9	        9	    UK	            YES

# Now, based on this data set, Python can create a decision tree that can be used to decide if any 
# new shows are worth attending to.


# How Does it Work? ********************************************************************************************

# First, import the modules you need, and read the dataset with pandas:

# Example: Read and print the data set:

import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Work\\Python\\05_Machine_Learning\\00_Files\\shows.csv", ";")

print(df)

# To make a decision tree, all data has to be numerical.

# We have to convert the non numerical columns 'Nationality' and 'Go' into numerical values.
#   {'UK': 0, 'USA': 1, 'N': 2}
#   Means convert the values 'UK' to 0, 'USA' to 1, and 'N' to 2.

#  Pandas has a map() method that takes a dictionary with information on how to convert the values.


# Example: Change string values into numerical values:

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

print(df)


# Then we have to separate the feature columns from the target column.

# The feature columns are the columns that we try to predict from, and the target column is the column
# with the values we try to predict.

# Example: X is the feature columns, y is the target column:

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

print(X)
print(y)

print("*********************************************************************************************************************************")
# Now we can create the actual decision tree, fit it with our details, and save a .png file on the computer:

# Example: Create a Decision Tree, save it as an image, and show the image:
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Work\\Python\\05_Machine_Learning\\00_Files\\shows.csv", ";")

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']
print(X)
print(y)
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Work\\Python\\05_Machine_Learning\\00_Decisions_Tree\\mydecisiontree.png")

img=pltimg.imread("C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Work\\Python\\05_Machine_Learning\\00_Decisions_Tree\\mydecisiontree.png")
imgplot = plt.imshow(img)
plt.show()