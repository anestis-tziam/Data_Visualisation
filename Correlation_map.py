##################################################################################################################################################
#################################################################################################################################################
##################################### Data Visualisation with Matplotlib ###################################################################
#############################################  Correlation Map  ##############################################################################
################################################################################################################################################

# Import the necessary libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


# The first thing to do is to upload the dataset that we will use for thsi session.
df = pd.read_csv('wheat.data', sep=',')


# Display necessary information for our dataset.
df.info()


# Display the first ten rows of the dataset.
df.head(10)


# Select the columns of interest.
# Our charts will be created from the new dataframes that we will create below.
df2 = df[['compactness','length','width','asymmetry','groove','wheat_type']]


# Create a correlation map
# Create a correlation table
df2.corr()


# Get a colormap with the correlation between the different parameters
plt.imshow(df2.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df2.columns))]
plt.xticks(tick_marks, df2.columns, rotation='vertical')
plt.yticks(tick_marks, df2.columns)

# Save your chart in a selected format
plt.savefig("Wheat_Correlation_Map.png", orientation = "landscape", dpi = 100)

plt.show()