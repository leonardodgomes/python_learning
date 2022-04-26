# Plotting
#   Pandas uses the plot() method to create diagrams.
#   We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.

# Example: Import pyplot from Matplotlib and visualize our DataFrame:

#Three lines to make our compiler able to draw:
import sys
import matplotlib #pip install --upgrade Pillow if error:DLL load failed while importing _imaging:
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\03_Pandas\\00_Files\\data.csv')

df.plot()

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()



