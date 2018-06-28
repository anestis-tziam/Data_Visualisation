######################################################################################################################################################
######################################################################################################################################################
##################################### Data Visualisation with Matplotlib ###################################################################
#############################################  Pie Chart  ##############################################################################
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
     

# Create a pie chart    
fig, ax1 = plt.subplots(1,1)

labels = 'Attack', 'Defense', 'Speed', 'HP'
sizes = [Pokemon_attack, Pokemon_defense, Pokemon_speed, Pokemon_HP]
colors = ["yellow", "red", "blue", "green"]
explode = (0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Attack')

ax1.pie(sizes, explode = explode, labels = labels,colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

ax1.legend(loc = (-0.1,0.05),shadow = True) 
ax1.set_title("A pokemon pie")


# Save your chart in a selected format
plt.savefig("Pokemon_Pie_Chart.png", orientation = "landscape", dpi = 100)    

plt.show()

# Anything below plt.show() is not included in the chart   