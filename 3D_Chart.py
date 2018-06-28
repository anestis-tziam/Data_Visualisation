##################################################################################################################################################
#################################################################################################################################################
##################################### Data Visualisation with Matplotlib ###################################################################
###############################################  3D Chart  ##############################################################################
################################################################################################################################################


# Import the necessary libraries/packages that we need for data visualisation.
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


# Import the dataset
df = pd.read_csv('wheat.data', sep=',')


# Display necessary information for our dataset.
df.info()


# Display the first ten rows of the dataset.
df.head(10)


# Select the columns of interest.
# Our charts will be created from the new dataframes that we will create below.
df2 = df[['compactness','length','width','asymmetry','groove','wheat_type']]


# Create a 3D chart
# Import the necessary package for creating a 3D chart
from mpl_toolkits.mplot3d import Axes3D


# Set up the figure structure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create 3D scatter plot
ax.scatter(df.area, df.perimeter, df.asymmetry, c='black', marker='.', s = 50, alpha = 0.45)

# Add the axes names
ax.set_xlabel('Area')
ax.set_ylabel('Perimeter')
ax.set_zlabel('Asymmetry')

# Set the value limits on both axes
ax.set_xlim(9.5,20.5)#left,right
ax.set_ylim(13,18)
ax.set_zlim(0,8)

# Set the location of the legend
ax.legend(loc = "center left")

#Create a title for the plot
ax.set_title("Wheat Properties",fontdict = {"fontsize":10})


# Save your chart in a selected format
plt.savefig("Wheat_3D_Chart.png", orientation = "landscape", dpi = 100) 

plt.show()