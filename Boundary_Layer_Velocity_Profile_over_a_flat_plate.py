#flow over flat plate

import numpy as np
import matplotlib.pyplot as plt

#constants

nu = 1.5e-5 #kinematic viscosity (m^2/s)
U_inf = 1   #Free stream velocity (m/s)
x = 1.0 # Distance from leading edge (m)

#Boundary layer thickness (delta)

Re_x = U_inf * x / nu #Reynolds number
def boundary_layer_thickness(Re_x):
    return 5.0 * x / np.sqrt(Re_x) #Approximation for laminar boundary layer

#Blasius similarity variable (eta)

def eta(y, x, U_inf, nu):
    return y * np.sqrt(U_inf / (nu * x))

#Velocity profile (approximation using Blasius solution)
def blasius_velocity_profile(eta):
    return np.tanh(eta)

#Generate data for visualiztion
y_vals = np.linspace(0, boundary_layer_thickness(Re_x), 100)
eta_vals = eta(y_vals, x, U_inf, nu)
u_vals =  blasius_velocity_profile(eta_vals)

#plotting
plt.figure(figsize=(10,8))
plt.plot(u_vals, y_vals, label="Velocity Profile", color="red")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(U_inf, color="Green", linestyle="--", label="Free Stream velocity")
plt.title("Boundary Layer Velocity Velocity Profile over a flat plate")
plt.xlabel("u/U_inf (Normalized Velocity)")
plt.ylabel("y (m)")
plt.grid(alpha=0.3)
plt.legend()
plt.show()