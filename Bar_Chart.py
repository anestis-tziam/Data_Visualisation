######################################################################################################################################################
######################################################################################################################################################
##################################### Data Visualisation with Matplotlib ###################################################################
#############################################  Bar Chart  ##############################################################################
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

         
# Prepare the data       
Pokemon_attack = sum(attack)/len(attack)  
Pokemon_defense = sum(defense)/len(defense)
Pokemon_speed = sum(speed)/len(speed)
Pokemon_HP = sum(HP)/len(HP)         


# Create a bar plot
figure, (ax1) = plt.subplots(1,1, sharey = True)

ax1.bar(left = [1,2,3,4],
        height = [Pokemon_attack, Pokemon_defense, Pokemon_speed, Pokemon_HP],
        width = 0.35,
        align = "center",
        color = ["red","black","blue","green"])

plt.xticks([1,2,3,4],["Attack","Defense","Speed", "HP"])

#Create a title for the plot
ax1.set_title("Pokemon Bar Chart",fontdict = {"fontsize":15})

# Save your chart in a selected format
plt.savefig("Pokemon_Bar_Chart.png", orientation = "landscape", dpi = 100)

plt.show()

# Anything below plt.show() is not included in the chart

