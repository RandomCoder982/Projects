import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import pandas as pd
import os
from datetime import datetime, timezone
import numpy as np
from scipy import stats
from matplotlib.animation import FuncAnimation

# Load data
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "data.csv"))

                
#Function to change epochs to a more readable time
def epoch2datetime(epoch):
    v1 = (datetime.fromtimestamp(epoch, timezone.utc))
    v2 = v1.strftime('%Y-%m-%d')
    return v2

#Applying that function to every value in epoch and creating a new columm containing those values
dates = df["epoch"].apply(epoch2datetime)
dates = (mdates.date2num(df["date"]))

debug = True

if debug:
    #df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.scatter(df["distance"], [*range(len(dates))], dates[::-1])
    ax.set_xlabel('Distance')
    ax.set_ylabel('Calories')
    ax.set_zlabel('Dates')
    ax.zaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    #plt.scatter(df["dates"], df["calories"])
    #plt.scatter(df["calories"], df["dates"])
    #plt.scatter([*range(len(df["dates"]))], df["calories"])
    #plt.plot(df["dates"], df["calories"])

plt.show()