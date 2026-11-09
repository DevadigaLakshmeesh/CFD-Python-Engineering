# Day 1: Python for Mechanical Engineers

import math

# Given parameters
mass = 1000          # kg
velocity = 30        # m/s
density = 1.225      # kg/m3
area = 2.2           # m2
drag_coefficient = 0.30

# Kinetic energy
kinetic_energy = 0.5 * mass * velocity**2

# Dynamic pressure
dynamic_pressure = 0.5 * density * velocity**2

# Aerodynamic drag
drag_force = dynamic_pressure * area * drag_coefficient

print("KINETIC ENERGY:", kinetic_energy, "J")
print("DYNAMIC PRESSURE:", dynamic_pressure, "Pa")
print("AERODYNAMIC DRAG:", drag_force, "N")