"""

Magnetic field B = u * I / (2pi*a)

u = permeability of free space 4*pi * 10^-7 Vs/Am

I = Current

a = distance between charge and wire

"""

 

import numpy as np

 

permeability = 4*np.pi*10e-7

 

###### INPUT ######

particle_charge = 1.602e-19 # Coulomb

particle_mass = 9.109e-31   # kg

particle_position = (1,1)   # x,y coordinates

particle_velocity = (1,2)   # x,y velocity

wire_current = 10e-3        # Ampere

 

a = np.sqrt(particle_position[0]**2 + particle_position[1]**2)

print(a)

 

def magnetic_field():

    """

    Calculates the magnetic field B

    """

    return permeability*wire_current / (2*np.pi*a)



def magnetic_force():

    """

    Calculates the magnetic force

    """

    return particle_charge*particle_velocity*magnetic_field()

 

print(magnetic_field())
