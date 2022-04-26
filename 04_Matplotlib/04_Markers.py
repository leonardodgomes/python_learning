# Markers *********************************************************************************************
#  You can use the keyword argument marker to emphasize each point with a specified marker:

# Example Mark each point with a circle:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()


# Marker Reference
# Marker      	Description
# 'o'	        Circle	
# '*'	        Star	
# '.'	        Point	
# ','	        Pixel	
# 'x'	        X	
# 'X'	        X (filled)	
# '+'	        Plus	
# 'P'	        Plus (filled)	
# 's'	        Square	
# 'D'	        Diamond	
# 'd'	        Diamond (thin)	
# 'p'	        Pentagon	
# 'H'	        Hexagon	
# 'h'	        Hexagon	
# 'v'	        Triangle Down	
# '^'	        Triangle Up	
# '<'	        Triangle Left	
# '>'	        Triangle Right	
# '1'	        Tri Down	
# '2'	        Tri Up	
# '3'	        Tri Left	
# '4'	        Tri Right	
# '|'	        Vline	
# '_'	        Hline


# Format Strings fmt ************************************************************************************
#  You can use also use the shortcut string notation parameter to specify the marker.
#  This parameter is also called fmt, and is written with this syntax:

# marker|line|color
# Example: Mark each point with a circle:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()

# Line Reference

# Line Syntax	    Description
# '-'	            Solid line	
# ':'	            Dotted line	
# '--'	            Dashed line	
# '-.'	        Dashed/dotted line	

# Note: If you leave out the line value in the fmt parameter, no line will be plotted.

# Color Reference

# Color Syntax	    Description
# 'r'	            Red	
# 'g'	            Green	
# 'b'	            Blue	
# 'c'	            Cyan	
# 'm'	            Magenta	
# 'y'	            Yellow	
# 'k'	            Black	
# 'w'	            White



# Marker Size *************************************************************************************************

# You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:
# Example: Set the size of the markers to 20:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()



# Marker Color ***********************************************************************************************

# You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:
# Example: Set the EDGE color to red:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()


# Use both the mec and mfc arguments to color of the entire marker:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()