import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Løsning av ein enkel bølgjelikning ved bruk av eulers eksplisitte metode

# Krav: gamma = k/h^2 < 1/2 for stabilitet

# Parametre
c = 1.0 # bølgjehastigheit, for enkelhetsskyld
length_x = 10.0
length_y = 10.0
time_steps = 100
x_grid = 100
y_grid = 100

# Finne kvart enkelt steg i x, y og t "retning"
dx = length_x / (x_grid - 1)
dy = length_y / (y_grid - 1)
dt = 0.01

# Initialbetingelsar
u = np.zeros((x_grid, y_grid))
u[40:60, 40:60] = 1.0  # Initiell impulse

# Plot initialbetingelsar
fig = plt.figure()
ay = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(np.linspace(0, length_x, x_grid), np.linspace(0, length_y, x_grid))
ay.plot_surface(X, Y, u, cmap='plasma')
ay.set_xlabel('X-axis')
ay.set_ylabel('Y-axis')
ay.set_zlabel('Amplitude')
ay.set_title('Bølgjelikninga (Initialbetingelsar)')

# Eksplisitt Euler's metode
for t in range(1, time_steps):
    uxx = (u[2:, 1:-1] - 2*u[1:-1, 1:-1] + u[:-2, 1:-1]) / dx**2
    uyy = (u[1:-1, 2:] - 2*u[1:-1, 1:-1] + u[1:-1, :-2]) / dy**2

    u[1:-1, 1:-1] = u[1:-1, 1:-1] + dt * c**2 * (uxx + uyy)

# Plot den resulterende bølgja
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y = np.meshgrid(np.linspace(0, length_x, x_grid), np.linspace(0, length_y, y_grid))
ax.plot_surface(X, Y, u, cmap='inferno')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Amplitude')
ax.set_title('Bølgjelikninga (Etter %d tidssteg)' % time_steps)

plt.show()
