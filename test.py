import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize an empty scatter plot
scat = ax.scatter([], [], s=100)

# Initialization function: plot the background of each frame
def init():
    ax.set_xlim(0, 10)  # Set the x-axis limits
    ax.set_ylim(0, 10)  # Set the y-axis limits
    return scat,

# Animation function: called sequentially to update the plot elements
def update(frame):
    x = np.random.rand(10) * 10  # Generate random x-coordinates
    y = np.random.rand(10) * 10  # Generate random y-coordinates
    scat.set_offsets(np.column_stack((x, y)))  # Update the scatter plot
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

plt.show()