import pandas as pd
import sys
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("power_plants_CAN.csv")
pd.options.display.max_rows = 9999

df = pd.DataFrame(data)

# Top 10 Power Plants by Capacity in MW
# 1 megawatt (MW) of solar panels will generate 2,146 megawatt hours (MWh) of solar energy per year.
df_topPlant= np.array(df.nlargest(10,'capacity in MW')["capacity in MW"])
# Associated titles
df_topName = np.array(df.nlargest(10,'capacity in MW')["name of powerplant"])

x = df_topName
y = df_topPlant

plt.bar(x,y, color = "green")

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkblue','size':15}
font3 = {'family':'serif','color':'blue','size':8}

# Function to avoid overlapping
plt.xticks(rotation=45, ha="right")

# Title and Labels
plt.title("Top 10 Power Plants by Capacity", fontdict = font1)
plt.xlabel("Name of Power Plant", fontdict = font2)
plt.ylabel("Capacity in MW", fontdict = font2)

plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()