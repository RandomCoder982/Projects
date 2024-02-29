from pyvis.network import Network
import networkx as nx

# nx_graph = nx.cycle_graph(10)
# nx_graph.nodes[1]["title"] = "Number 1"

# nt = Network()
# nt.from_nx(nx_graph)
# nt.show("nx.html")

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Sample data with dates
dates = ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']
values = [5, 7, 3, 8, 6]

# Convert string dates to datetime objects
date_objs = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

# Convert datetime objects to numeric values using date2num
x = mdates.date2num(date_objs)

# Create figure and axis objects
fig, ax = plt.subplots()

# Create scatter plot using fig.scatter
ax.scatter(x, values)

# Format x-axis as dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Show the plot
plt.show()

