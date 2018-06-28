######################################################################################################################################################
######################################################################################################################################################
##################################### Data Visualisation with Matplotlib ###################################################################
###########################################$  Box & Violin Plots  ##############################################################################
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

         
#Create the box and the violin charts
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

# Create a list with the parameter that you want to plot
all_data = [attack, defense, speed, HP]

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


# Save your chart in a selected format
plt.savefig("Pokemon_Box_and_Violin_Charts.png", orientation = "landscape", dpi = 100)


plt.show()

# Anything below plt.show() is not included in the chart