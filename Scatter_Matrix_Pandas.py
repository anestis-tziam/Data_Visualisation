##################################################################################################################################################
#################################################################################################################################################
##################################### Data Visualisation with Pandas ###################################################################
######################################### Scatter Matrix Plot ##############################################################################
###############################################################################################################################


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


# We will use pandas to visualise the data.
from pandas.plotting import scatter_matrix


# Create and view the desired scatter matrix chart
scatter_matrix(df2, alpha = 0.2, figsize=(10, 10), diagonal='kde')

# By looking at the scatter matrix chart, it is evident that there are outliers present in 
# the dataset. Thus to make the scatter chart look nicer we can remove them and replot.


# Remove outliers from the data
q1 = df2['length'].quantile(0.25)
q3 = df2['length'].quantile(0.75)
iqr = q3 - q1
fence_low = q1 - 1.5*iqr
fence_high = q3 + 1.5*iqr
df_new = df2.loc [(df2['length'] > fence_low) & (df2['length'] < fence_high)]


# Let's see if there is a difference now!
scatter_matrix(df_new, alpha = 0.2, figsize=(10, 10), diagonal='kde')

# As we see, the scatter matrix looks much nicer now

# Save your chart in a selected format
plt.savefig("Wheat_Scatter_Matrix.png", orientation = "landscape", dpi = 100)