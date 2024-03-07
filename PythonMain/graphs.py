import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import pandas as pd
import os
import numpy as np
from matplotlib.animation import FuncAnimation

def best_fit(x,y):

   slope, y_intercept = np.polyfit(x, y, deg=1)
   slope = np.round(slope, 2)
   y_intercept = np.round(y_intercept, 2)

   # Calculate R Squared
   # 1 - RSS / TSS
   r_squared = 1 - (sum((y - (slope * x + y_intercept))**2) / ((len(y) - 1) * np.var(y, ddof=1)))
   r_squared = np.round(r_squared, 2)
   
   return slope, y_intercept, r_squared


# Load data. Needs data.csv to be in the same directory as file
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "data.csv"))

calories = [float(cal.replace(",", "")) for cal in df["calories"]]

#Changing the dates from a Year-Month-Day value to an interger matplotlib can understand
dates = (mdates.date2num(df["date"]))

debug = True
graph1 = False

if debug:
    if graph1:
        #Creating the white background
        fig = plt.figure()

        #Creating a 3d graph onto the background
        ax = fig.add_subplot(projection="3d")

        #Graph and labeling the X, Y, and Z lists
        ax.scatter(df["distance"], calories, dates)
        ax.set_xlabel('Distance')
        ax.set_ylabel('Calories')
        ax.set_zlabel('Dates')

        #Changing the date's format back into Year-Month-Day
        ax.zaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    fig2, ax2 = plt.subplots()
    slope1, y_int1 = best_fit(dates, calories)
    xseq = np.linspace(0, len(dates), num=len(dates))
    ax2.scatter(dates, calories)
    ax2.plt(xseq, y_int1 + slope1 * xseq)


plt.show()