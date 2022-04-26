# Histogram
# A histogram is a graph showing frequency distributions.
# It is a graph showing the number of observations within each given interval.


# Create Histogram *******************************************************************************************
#  In Matplotlib, we use the hist() function to create histograms.
#  The hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.

#  For simplicity we use NumPy to randomly generate an array with 250 values, where the values will concentrate around 170, and the standard deviation is 10. Learn more about Normal Data Distribution in our Machine Learning Tutorial.

# Example: A Normal Data Distribution by NumPy:

import numpy as np

x = np.random.normal(170, 10, 250)

print(x)


# The hist() function will read the array and produce a histogram:

# Example: A simple histogram:

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 