##################################################################################################################################################
#################################################################################################################################################
##################################### Data Visualisation with Matplotlib ###################################################################
######################################### Parallel coordinates plot ##############################################################################
########################################### Andrews curves chart #######################################################################


# Import the necessary libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


# Import the dataset
df = pd.read_csv('wheat.data')


# Display necessary information for our dataset.
df.info()


# Display the first ten rows of the dataset.
df.head(10)


# Select the columns of interest.
# Our charts will be created from the new dataframes that we will create below.
df2 = df[['compactness','length','width','asymmetry','groove','wheat_type']]


# Create the parallel coordinates chart
from pandas.plotting import parallel_coordinates
plt.figure(figsize = (8,8))
parallel_coordinates(df2, 'wheat_type', alpha = 0.8)

# Save your chart in a selected format
plt.savefig("Wheat_Parallel_Coordinates.png", orientation = "landscape", dpi = 100)

plt.show()


# Create an andrews curves chart
from pandas.tools.plotting import andrews_curves


plt.figure(figsize = (8,8))
andrews_curves(df2,"wheat_type",alpha = 0.8)

# Save your chart in a selected format
plt.savefig("Wheat_Andrews_Curve.png", orientation = "landscape", dpi = 100)

plt.show()

