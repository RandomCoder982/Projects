import matplotlib.pyplot as plt

# Sample data
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]

# Plotting the data
plt.plot(x_values, y_values, label='Sample Line')

# Adding labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Simple Line Graph')

# Adding a legend
plt.legend()

# Display the plot
plt.show()
