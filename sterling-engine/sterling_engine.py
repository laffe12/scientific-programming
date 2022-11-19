"""
---------------------- The Stering Engine ---------------------- 

This program calculates the gas pressure of 0.1 mol helium inside a sterling
engine and plots the gas pressure as a function of gas volume.
It is useful to think of the one cycle of the engine process as consisting
of four parts, P1, P2, P3 and P4.
 
P1: Gas temperature increases as the gas expands => pressure decreases
P2: Temperature drastically decreases => instant pressure drop.
P3: Temperature decrease as the gas compresses => pressure increase 
P4: Addition of temperature => Instantaneous increase in pressure

Using the ideal gas law p*V = n*R*T it is possible to calculate the pressure 
for each process.

Written by Adam Rosén
"""
import numpy as np
import matplotlib.pyplot as plt

V1 = 0.001          # (m³) - min gas volume
V2 = 0.005          # (m³) - max gas volume
T1 = 650 + 273.15   # (K) - min gas temperature
T2 = 100 + 273.15   # (K) - max gas temperature
n = 0.1             # (mol) - amount of gas
R = 8.3145          # (J*K⁻¹*mol⁻¹) - Gas constant 
V = np.linspace(V1, V2, num=50) # discrete volume values used in P1 and P3
V_1 = [V1*1e3, V1*1e3] # (dm³) Volume for process 4 (only used for plotting)
V_2 = [V2*1e3, V2*1e3] # (dm³) Volume for process 2 (only used for plotting)

"""
Calculating the four processes of the sterling engine using the ideal gas law.
"""
P1 = n*R*T1 / V   
P2 = np.array([T2,T1]) * n * R / V2
P3 = n*R*T2 / V
P4 = np.array([T1, T2]) * n * R / V1

"""
Calculating the work for produced by process 1 (expansion) and 3 (compression)
This is done by integrating over p*dV in the interval V = 1-5 dm³

"""
We = np.trapz(P1, V) # integration between V=5-1 of p1*dV
Wc = np.trapz(P3, V) # integration between V=5-1 of p3*dV
W_tot = We - Wc      # Total work
print(f"Work produced from one engine cycle: {W_tot:.1f} Joule")

"""
The plot is showing how the gas pressure varies by the four processes 
of a sterling engine.The plot displays pressure in kPa and volume in dm³
"""

plt.plot(V*1e3, P1*1e-3, label="Heat increase (expansion)", linestyle="--")
plt.plot(V_2, P2*1e-3, label="Heat decrease (constant volume)", linestyle="--")
plt.plot(V*1e3, P3*1e-3, label="Heat decrease (compression)", linestyle="--")
plt.plot(V_1, P4*1e-3, label="Heat increase (constant volume)", linestyle="--")
plt.title("Sterling Engine")
plt.xlabel("Volume [dm³]")
plt.ylabel("Pressure [kPa]")
plt.legend()
plt.savefig('pV_sterling_engine.jpg')
plt.show()
