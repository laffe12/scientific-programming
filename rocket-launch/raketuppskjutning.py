#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This python program calculates the acceleration of a rocket driven by fuel 
that is propelled out from the rockets rear with force Fb. Fb is given by:
    
                        Fb = mb * vb / 1s. 
                    
Where mb is the fuels mass and vb is the velocity of which
the rocket fuel is expelled. Every second the rocket expells 1000 kg of fuel.

According to newtons third law an equally large opposite force, Fn = m*a,
acts on the rocket. Knowing the rocket mass m we can calculate the acceleration
of the rocket by. Also subtracting g (gravitational acceleration)

                        Fn = Fb => 
                        m*a = mb*vb =>
                        a = Fb/m - g
            

It is possible to change the time resolution of the calculation. For example:
Variable h = 0.01 makes to program calculate the acceleration for every 100th
of a second.

Created on Fri Oct  7 13:09:06 2022
@author: Adam Rosén
"""

import matplotlib.pyplot as plt
import numpy as np

# VARIABLE TO CHANGE TIME RESOLUTION
h = 0.01     # timestep

# Constants
g = 9.82     # m/s²
a = 0
seconds = 61 # preform calculation for # seconds
vb = 3000    # fuel velocity [m/s]
mb = 1000    # fuel mass [kg]
m = 90000    # rocket mass [kg]
v = 0        # v0 = 0
y = 0
a_list = []  # list of acceleration values
time = np.linspace(0, seconds, num=int(seconds/h)) # total time split into timesteps of size h
y_list = []

def Fb(mb, vb): # Fb = mb * vb/(1s)
    return mb * vb

# Calculate acceleration, rocket mass, velocity and y-position at every timestep t
for t in time:
    a = Fb(mb=mb, vb=vb)/m - g  # mb*vb = Fb = F = m*a => a = Fb/m
    m -= mb*h               # every timestep the rocket mass m decreases with mb*h
    v = v + a*h             # velocity
    y = y + v*h - a*h**2/2  # y-position (height)
    a_list.append(a)        # adds acceleration values to a list
    y_list.append(y)        # Saves the position in a list at every timestep

print(f"Final rocket acceleration: {a_list[-1]:.1f} m/s²")
print(f"Final rocket height {y_list[-1]:.1f} m")
print(f"Final rocket velocity {v:.1f} m/s")
print(f"Time step: {h} s")

# Plot the rockets acceleration vs time
plt.plot(time, a_list, label="Rocket acceleration", linestyle="-")
plt.title("Rocket Launch")
plt.xlabel("Time [s]")
plt.ylabel("Acceleration [m/s²]")
plt.legend()
plt.show()