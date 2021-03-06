# Creating Scatter Plots

# With Pyplot, you can use the scatter() function to draw a scatter plot.

# The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:

# Example: A simple scatter plot:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()

# The observation in the example above is the result of 13 cars passing by.
# The X-axis shows how old the car is.
# The Y-axis shows the speed of the car when it passes.
# Are there any relationships between the observations?
# It seems that the newer the car, the faster it drives, but that could be a coincidence, after all we only registered 13 cars.



# Compare Plots ************************************************************************************************

# In the example above, there seems to be a relationship between speed and age, but what if we plot the observations
# from another day as well? Will the scatter plot tell us something else?

# Example: Draw two plots on the same figure:

import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()

# The two plots are plotted with two different colors, by default blue and orange, you will learn how to change colors later in this chapter.




# Colors

# You can set your own color for each scatter plot with the color or the c argument:

#Example: Set your own color of the markers:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()



# Color Each Dot **********************************************************************************************

# You can even set a specific color for each dot by using an array of colors as value for the c argument:

# Note: You cannot use the color argument for this, only the c argument.

# Example: Set your own color of the markers:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()



# ColorMap **********************************************************************************************************

# The Matplotlib module has a number of available colormaps.
#  A colormap is like a list of colors, where each color has a value that ranges from 0 to 100.

# Here is an example of a colormap:

#  This colormap is called 'viridis' and as you can see it ranges from 0, which is a purple color, and up to 100, which is a yellow color.

#  How to Use the ColorMap
#  You can specify the colormap with the keyword argument cmap with the value of the colormap, in this case 'viridis' which is one of the built-in colormaps available in Matplotlib.

#  In addition you have to create an array with values (from 0 to 100), one value for each of the point in the scatter plot:

#  Example: Create a color array, and specify a colormap in the scatter plot:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()

# You can include the colormap in the drawing by including the plt.colorbar() statement:

# Example: Include the actual colormap:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()

# Available ColorMaps cmap=

# cmap='Accent'     cmap='cubehelix'        cmap='hot'              cmap='prism'        cmap='summer'
# cmap='afmhot'     cmap='Dark2'            cmap='hsv'              cmap='PuBu'         cmap='tab10'
# cmap='autumn'     cmap='flag'             cmap='inferno'          cmap='PuBuGn'       cmap='tab20'
# cmap='binary'     cmap='gist_earth'       cmap='jet'              cmap='PuOr'         cmap='tab20b'
# cmap='Blues'      c map='gist_gray'       cmap='magma'            cmap='PuRd'         cmap='tab20c'
# cmap='bone'       cmap='gist_heat'        cmap='nipy_spectral'    cmap='Purples'      cmap='terrain'
# cmap='BrBG'       cmap='gist_ncar'        cmap='ocean'            cmap='rainbow'      cmap='twilight'
# cmap='brg'        cmap='gist_rainbow'     cmap='Oranges'          cmap='RdBu'         cmap='twilight_shifted'
# cmap='BuGn'       cmap='gist_stern'       cmap='OrRd'             cmap='RdGy'         cmap='viridis'
# cmap='BuPu'       cmap='gist_yarg'        cmap='Paired'           cmap='RdPu'         cmap='winter'
# cmap='bwr'        cmap='GnBu'             cmap='Pastel1'          cmap='RdYlBu'       cmap='Wistia'
# cmap='cividis'    cmap='gnuplot'          cmap='Pastel2'          cmap='RdYlGn'       cmap='YlGn'
# cmap='CMRmap'     cmap='gnuplot2'         cmap='pink'             cmap='Reds'         cmap='YlGnBu'
# cmap='cool'       cmap='gray'             cmap='PiYG'             cmap='seismic'      cmap='YlOrBr'
# cmap='coolwarm'   cmap='Greens'           cmap='plasma'           cmap='Spectral'     cmap='YlOrRd'
# cmap='copper'     cmap='Greys'            cmap='PRGn'             cmap='spring'
