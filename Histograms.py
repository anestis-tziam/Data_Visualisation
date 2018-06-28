######################################################################################################################################################
######################################################################################################################################################
##################################### Data Visualisation with Matplotlib ###################################################################
#############################################  Histograms  ##############################################################################
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

# Select the columns of interest.
attack = data['Attack'].values
defense = data['Defense'].values
speed = data['Speed'].values
speed_attack = data['Sp. Atk'].values 
speed_defense = data['Sp. Def'].values 
HP = data["HP"].values
         

#Set up a figure for a single histogram
figure, (ax2) = plt.subplots(1, 1)


# Create a single histogram
ax2.hist(speed, bins = 12, align = 'mid', color = "blue",range = (0,175), cumulative = False, label = "Pokemon speed")
ax2.set_xlabel("Speed",labelpad = 2, fontdict = {"fontsize":10})
ax2.set_ylabel("Occurrence", fontdict = {"fontsize":10})
ax2.legend(loc = "best")


#Create a title for the histograms
ax2.set_title("Pokemon speed",fontdict = {"fontsize":15})


#Set up a figure for two histograms plotted together
figure, axes = plt.subplots(1, 2, sharey = False)
ax3, ax4 = axes.flatten()


# Create the two histograms
ax3.hist(speed,bins = 12, align = 'mid', color = "blue",range = (0,175), cumulative = False, label = "Speed")
ax4.hist(x = [speed_attack, speed_defense],stacked = True, bins = 12, color = ("blue","red"), cumulative = False,label = ("sp.attack","sp.defense"))  


#Set up the aesthetic parameters
ax3.legend(loc = "best")
ax3.set_xlabel("Speed",labelpad = 2, fontdict = {"fontsize":10})
ax3.set_ylabel("Occurrence", fontdict = {"fontsize":10})

ax4.legend(loc = "best")
ax4.set_xlabel("Speed_Attack and Speed Defense",labelpad = 1, fontdict = {"fontsize":10})
ax4.set_ylabel("Occurrence", fontdict = {"fontsize":10})

figure.tight_layout()


# Save your histograms in a selected format
plt.savefig("Pokemon_Historgrams.png", orientation = "landscape", dpi = 100)

plt.show()

# Anything below plt.show() is not included in the chart