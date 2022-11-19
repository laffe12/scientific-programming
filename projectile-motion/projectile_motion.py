"""
This program calculates the x and y coordinates of the motion of two
object that is thrown in a projectile parabola.
The x and y coordinates are saved in numpy arrays respectively 
and is then plotted and saved using matplotlib

Written by Adam Rosén
"""

import matplotlib.pyplot as plt
import numpy as np


# Constants
g = 9.82
h = 0.002 # time step
y0 = 2
x0 = 0
v0 = 11
alpha = np.radians(30)

# Function for calculating x and y positions
def get_position(t, x0, y0, v0, alpha):
    x = x0 + v0 * np.cos(alpha) * t
    y = y0 + v0 * np.sin(alpha) * t - g*t**2 / 2
    
    return (x,y)    #returns tuple with coordinates

### Parabola 1 ###

# Initializing variables and arrays
y = 0
x_values = np.empty(0)
y_values = np.empty(0)

time = 0

# Do the calculation while the object is above ground (y>0)
while y >= 0:

    x = get_position(time, x0, y0, v0, alpha)[0] #get the x-coordinate 
    y = get_position(time, x0, y0, v0, alpha)[1] #get the y-coordinate 
    
    x_values = np.append(x_values, x)   # add x to array
    y_values = np.append(y_values, y)   # add y to array

    time += h   #update time

### Parabola 2 ### 

# Initializing variables and arrays
y2 = 0
x_values2 = np.empty(0)
y_values2 = np.empty(0)


time = 0
# Do the calculation while the object is above ground (y>0)
while y2 >= 0:

    x2 = get_position(time, 0, 1, 12, np.radians(45))[0]    #get the x-coordinate
    y2 = get_position(time, 0, 1, 12, np.radians(45))[1]    #get the y-coordinate
        
    x_values2 = np.append(x_values2, x2)    # add x to array
    y_values2 = np.append(y_values2, y2)    # add y to array
        
    time += h


# Plot the two parabolas
plt.plot(x_values, y_values, label="Starting point: $y$ = 2", linestyle="--")    #1st parabola
plt.plot(x_values2, y_values2, label="Starting point: $y$ = 1")  #2st parabola
plt.title("Projectile motion parabola")
plt.axhline(y=0, color='black', linestyle='-')
plt.xlabel("Distance [m]")
plt.ylabel("Height [m]")
plt.axis("equal")
plt.legend()

plt.savefig('parabola_plot.jpg')
print("Plot saved...")
