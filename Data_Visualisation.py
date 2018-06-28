######################################################################################################################################################
######################################################################################################################################################
##################################### Data Visualisation with Matplotlib ###################################################################
########################################################################################################################
######################################################################################################################################################


# Import the necessary libraries/packages that we need for data visualisation.

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt


# Certain types of plots require some special packages/tasks. These will be called just before the 
# specific chart-type is demonstrated.


# Import the dataset
data = pd.read_csv('pokemon.csv')


# Display necessary information for our dataset.
data.info()


# Display the first ten rows of the dataset.
data.head(10)


# Select the columns of interest from the dataframe.
attack = data['Attack'].values
defense = data['Defense'].values
speed = data['Speed'].values
speed_attack = data['Sp. Atk'].values 
speed_defense = data['Sp. Def'].values 
HP = data["HP"].values
    
         
# For the creation of most of the charts we will figure method instead of the plt option. By using the 
# figure package we can create either a single figure by using: 
# figure, (ax1) = plt.subplots(1, 1, sharey=True), or for creating a 2*2 grid of figures by using: 
# (ax1) = plt.subplots(2, 2, sharey=True)         
         


# Set the sttucture of the figure.
# You can create a single, or mupltiple figures in a grid formation.
figure, (ax1) = plt.subplots(1, 1, sharey=True) 


# Create the scatter.
ax1.scatter(attack, defense, marker = "*", color = "blue", alpha = 0.4, label = "Pokemons")


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

from matplotlib.ticker import MultipleLocator#,FormatStrFormatter
from matplotlib.ticker import FormatStrFormatter

# Set the interval for the major and minor ticks 
majorTickLocation = MultipleLocator(20)
minorTickLocation = MultipleLocator(10)

ax1.xaxis.set_major_locator(majorTickLocation)
ax1.xaxis.set_minor_locator(minorTickLocation)


ax1.xaxis.set_ticks_position("bottom")#top,bottom

ax1.spines["right"].set_visible(False)#bottom,right,top,left


# Add text annotations in your plot
ax1.text(40,200,"Attack & Defense",
         horizontalalignment = "center",#left,right,center
         verticalalignment = "center",#bottom,top,center
         rotation = 0,
         style = "italic",#italic
         weight = "bold")#0-1000,bold


# Save your plot in a selected format
plt.savefig("Pokenmon_Attack_vs_Defense.png",orientation = "landscape",dpi = 100)


# Make sure that everything you want to include in your chart is placed before the plt.show() command. 
# Any option after plt.show() will not be included in your plot.

plt.show()                         



# Creation of histograms. Below we will create two histograms. First a single histogram will be created 
# and then we will create two histograms plotted next to each other (i.e. row format) and also show how 
# histograms can be created into a column format. Finally, we will also create a 2D histogram.

#Set up a figure for a single histogram
figure, (ax2) = plt.subplots(1, 1)

ax2.hist(speed,bins = 12, align = 'mid', color = "blue",range = (0,175), cumulative = False)

#Set up a figure for two histograms plotted together
figure, axes = plt.subplots(1, 2, sharey=False)
ax3, ax4 = axes.flatten()

ax3.hist(speed,bins = 12, align = 'mid', color = "blue",range = (0,175), cumulative = False)

ax4.hist(x = [speed_attack, speed_defense],stacked = True, bins = 12, color = ("blue","red"), cumulative = False,label = ("sp.attack","sp.defense"))  

#Set up the aesthetic parameters
ax4.legend(loc = "best")

ax3.set_xlabel("Speed",labelpad = 2, fontdict = {"fontsize":10})
ax3.set_ylabel("Occurence", fontdict = {"fontsize":10})

ax4.set_xlabel("Speed_Attack and Speed Defense",labelpad = 1, fontdict = {"fontsize":10})
ax4.set_ylabel("Occurence", fontdict = {"fontsize":10})

figure.tight_layout()

#Set up a figure for a single histogram (2D in this case)
figure, (ax5) = plt.subplots(1, 1)

ax5.hist2d(attack, defense, bins=[20,10])#[xbins,ybins]
#plt.colorbar()

plt.show()


# Create a pie chart


fig, ax7 = plt.subplots(1,1)

labels = 'Attack', 'Defense', 'Speed', 'HP'
sizes = [attack2, defense2, speed2, HP2]
colors = ["yellow", "red", "blue", "green"]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Defense')

ax7.pie(sizes, explode=explode, labels=labels,colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
ax7.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

ax7.legend(loc=(-0.05,0.05),shadow=True) 
ax7.set_title("A pokemon pie")

figure.tight_layout()

plt.show()

# Create violin and box plots


# Create the figures
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

# Create a list with the parameter that you want to plot
all_data = [attack,defense,speed, HP]

# Create a box plot
axes[0].boxplot(all_data)
axes[0].set_title('Box plot')
axes[0].set_title('Pokemon Skills')
axes[0].set_xticklabels(['Attack','Defense','Speed','HP'],rotation = 45) #### NEEDS CORRECTIONS!!!!
axes[0].set_xlabel("Pokemon skills.")
axes[0].set_ylabel("Value")


# Create a violin plot
axes[1].violinplot(all_data, showmeans=False, showmedians=True)
axes[1].set_title('Violin plot')
axes[1].set_title('Pokemon Skills')
axes[1].set_xlabel("Pokemon skills.")
axes[1].set_ylabel("Value")

plt.show()


         