



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate example trajectory data
time = np.linspace(0, 10, 1000)
altitude = 10000 * np.exp(-0.1 * time)
velocity = 1000 * np.exp(-0.05 * time)
angle_of_attack = np.deg2rad(5 * np.ones_like(time))

# Generate example aerodynamic forces data
lift = 0.5 * np.sin(angle_of_attack) * velocity**2
drag = 0.2 * velocity**2

# Generate example shockwave data
shockwave_intensity = 0.1 * np.exp(-0.05 * time)

# Generate example boundary layer transition data
boundary_layer_transition = np.random.rand(len(time))

# Generate example thermal effects data
temperature = 1000 - 50 * altitude / 10000 + 100 * np.sin(time)

# Generate example material deformation data
deformation = np.random.rand(len(time))

# Generate example pressure distribution data
pressure_distribution = 1000 - 5 * altitude / 10000 + np.random.normal(0, 10, len(time))

# Generate example Mach number data
mach_number = velocity / 343

# Visualization
fig = plt.figure(figsize=(24, 18))

# Subplot 1: Trajectory
ax_traj = fig.add_subplot(3, 3, 1, projection='3d')
ax_traj.plot(time, altitude, velocity, color='b')
ax_traj.set_xlabel('Time (s)')
ax_traj.set_ylabel('Altitude (m)')
ax_traj.set_zlabel('Velocity (m/s)')
ax_traj.set_title('Hypersonic Vehicle Trajectory')

# Subplot 2: Aerodynamic Forces
ax_aero = fig.add_subplot(3, 3, 2)
ax_aero.plot(time, lift, label='Lift')
ax_aero.plot(time, drag, label='Drag')
ax_aero.set_xlabel('Time (s)')
ax_aero.set_ylabel('Force (N)')
ax_aero.set_title('Aerodynamic Forces')
ax_aero.legend()

# Subplot 3: Shockwave Intensity
ax_shock = fig.add_subplot(3, 3, 3)
ax_shock.plot(time, shockwave_intensity, color='r')
ax_shock.set_xlabel('Time (s)')
ax_shock.set_ylabel('Intensity')
ax_shock.set_title('Shockwave Intensity')

# Subplot 4: Boundary Layer Transition
ax_boundary = fig.add_subplot(3, 3, 4)
ax_boundary.plot(time, boundary_layer_transition, color='g')
ax_boundary.set_xlabel('Time (s)')
ax_boundary.set_ylabel('Transition')
ax_boundary.set_title('Boundary Layer Transition')

# Subplot 5: Thermal Effects
ax_thermal = fig.add_subplot(3, 3, 5)
ax_thermal.plot(time, temperature, color='orange')
ax_thermal.set_xlabel('Time (s)')
ax_thermal.set_ylabel('Temperature (K)')
ax_thermal.set_title('Thermal Effects')

# Subplot 6: Material Deformation
ax_deform = fig.add_subplot(3, 3, 6)
ax_deform.plot(time, deformation, color='purple')
ax_deform.set_xlabel('Time (s)')
ax_deform.set_ylabel('Deformation')
ax_deform.set_title('Material Deformation')

# Subplot 7: Pressure Distribution
ax_pressure = fig.add_subplot(3, 3, 7)
ax_pressure.plot(time, pressure_distribution, color='m')
ax_pressure.set_xlabel('Time (s)')
ax_pressure.set_ylabel('Pressure (Pa)')
ax_pressure.set_title('Pressure Distribution')

# Subplot 8: Mach Number
ax_mach = fig.add_subplot(3, 3, 8)
ax_mach.plot(time, mach_number, color='brown')
ax_mach.set_xlabel('Time (s)')
ax_mach.set_ylabel('Mach Number')
ax_mach.set_title('Mach Number')

plt.tight_layout()
plt.show()
