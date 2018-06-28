######################################################################################################################################################
######################################################################################################################################################
##################################### Data Visualisation with Matplotlib ###################################################################
#############################################  Scatter-plot  ##############################################################################
######################################################################################################################################################


# Import the necessary libraries
import numpy as np                
import pandas as pd               
import matplotlib.pyplot as plt


# Import the dataset
data = pd.read_csv('pokemon.csv')


# Display the necessary information for the dataset.
data.info()


# Display the first ten rows of the dataset.
data.head(10)


# Select the columns of interest from the dataframe.
attack = data['Attack'].values
defense = data['Defense'].values

    
# Set the sttucture of the figure.
# You can create a single, or mupltiple figures in a grid formation.
figure, (ax1) = plt.subplots(1, 1, sharey = True) 


# Create the scatter plot
ax1.scatter(attack, defense, marker = "o", color = "blue", alpha = 0.4, label = "Pokemons")


#Create a title for the plot
ax1.set_title("Pokemon skills Defense vs. Attack",fontdict = {"fontsize":15})


# Add the names of the parameters you are plotting on the x&y axes.
ax1.set_xlabel("Defense",labelpad = 1, fontdict = {"fontsize":15})
ax1.set_ylabel("Attack", fontdict = {"fontsize":15})
ax1.legend(loc = "best")


# Set the value limits on both axes
ax1.set_xlim(0,200)#left,right
ax1.set_ylim(0,250)


# Set the location of the legend
ax1.legend(loc = "upper left")


# Set format on both axes
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter


# Set the interval for the major and minor ticks 
majorTickLocation = MultipleLocator(20)
minorTickLocation = MultipleLocator(10)
ax1.xaxis.set_major_locator(majorTickLocation)
ax1.xaxis.set_minor_locator(minorTickLocation)
ax1.xaxis.set_ticks_position("bottom") #top,bottom
ax1.spines["right"].set_visible(True)  #bottom,right,top,left

          
# Add text annotations in your plot
ax1.text(34,210,"Attack vs. Defense",
         horizontalalignment = "center",#left,right,center
         verticalalignment = "center",#bottom,top,center
         rotation = 0,
         style = "italic",
         weight = "bold")#0-1000,bold


# Save your plot in a selected format
plt.savefig("Pokemon_Attack_vs_Defense.png", orientation = "landscape", dpi = 100)

plt.show() 

# Anything below plt.show() is not included in the chart